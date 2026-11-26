import copy
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CAPTURE = load("capture")
AUDIT = load("audit")
CHROMIUM = os.environ.get("CAPTURE_CHROMIUM_EXECUTABLE")
if not CHROMIUM:
    candidates = list(
        (Path.home() / "Library/Caches/ms-playwright").glob(
            "chromium-*/chrome-mac-*/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"
        )
    )
    CHROMIUM = (
        str(max(candidates))
        if candidates
        else shutil.which("chromium")
        or shutil.which("chromium-browser")
        or shutil.which("google-chrome")
    )
try:
    import playwright.sync_api  # noqa: F401
except ImportError:
    CHROMIUM = None


class LocalJourney:
    def __init__(self):
        self.records, self.submits, self.ready = {}, [], {}
        self.readback_delays = {}
        fixture = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *_args):
                pass

            def respond(self, status, data, html=False):
                body = data.encode() if html else json.dumps(data).encode()
                self.send_response(status)
                self.send_header(
                    "Content-Type", "text/html" if html else "application/json"
                )
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                try:
                    self.wfile.write(body)
                except (BrokenPipeError, ConnectionResetError):
                    pass

            def do_GET(self):
                parts = urlsplit(self.path)
                query = parse_qs(parts.query)
                identity = query.get("test_id", [""])[0]
                if parts.path == "/api/records":
                    if identity in fixture.readback_delays:
                        time.sleep(fixture.readback_delays[identity])
                    if (
                        identity in fixture.ready
                        and time.monotonic() >= fixture.ready[identity][0]
                    ):
                        fixture.records[identity] = [fixture.ready.pop(identity)[1]]
                    self.respond(
                        200,
                        {
                            "test_id": identity,
                            "records": fixture.records.get(identity, []),
                        },
                    )
                    return
                if parts.path == "/analytics":
                    self.respond(200, {"purchase": True})
                    return
                kind = query.get("kind", ["purchase"])[0]
                payload = json.dumps(
                    {
                        "test_id": identity,
                        "mode": query.get("mode", ["confirmed"])[0],
                        "kind": kind,
                    }
                )
                button = "Pay test amount" if kind == "purchase" else "Book test slot"
                page = f"""<!doctype html><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Local synthetic journey</title><style>body{{font:18px system-ui;padding:24px;color:#14243b}}input,select,button{{display:block;font:inherit;margin:16px 0;padding:10px;max-width:290px}}button{{background:#194dd3;color:white}}[role=status]{{margin-top:24px}}</style>
<h1>Synthetic {kind}</h1><p>No real payment or reservation</p>
<form><label>Email<input type="email" required></label><label>Slot<select><option value="2030-01-01T10:00:00Z">10:00</option></select></label><button>{button}</button></form><p role="status"></p>
<script>document.querySelector('form').onsubmit=async event=>{{event.preventDefault();
const response=await fetch('/api/submit',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({payload})}});
const data=await response.json();document.querySelector('[role=status]').textContent=data.text;
fetch('/analytics?token=do-not-export');
if ({payload}.mode==='ui_changes') setTimeout(()=>{{document.querySelector('[role=status]').textContent='Declined';}},100);}};</script>"""
                self.respond(200, page, html=True)

            def do_POST(self):
                payload = json.loads(
                    self.rfile.read(int(self.headers["Content-Length"]))
                )
                fixture.submits.append(payload)
                identity, mode = payload["test_id"], payload["mode"]
                if mode == "slow_readback":
                    fixture.readback_delays[identity] = 0.35
                row = {
                    "test_id": identity,
                    "status": "confirmed",
                    "amount": 1250,
                    "currency": "EUR",
                    "slot": "2030-01-01T10:00:00Z",
                    "private_token": "must-not-export",
                }
                if mode == "confirmed":
                    fixture.records[identity] = [row]
                elif mode in (
                    "wrong_status",
                    "wrong_amount",
                    "wrong_slot",
                    "wrong_identity",
                ):
                    field, value = {
                        "wrong_status": ("status", "pending"),
                        "wrong_amount": ("amount", 999),
                        "wrong_slot": ("slot", "2030-01-02T10:00:00Z"),
                        "wrong_identity": ("test_id", "another-test"),
                    }[mode]
                    row[field] = value
                    fixture.records[identity] = [row]
                elif mode in ("delayed", "ui_changes"):
                    fixture.ready[identity] = (time.monotonic() + 0.6, row)
                text = (
                    "Pending confirmation"
                    if mode in ("pending", "delayed")
                    else "Declined"
                    if mode == "declined"
                    else "Confirmed. Thank you!"
                )
                self.respond(
                    402 if mode == "declined" else 202 if mode == "pending" else 200,
                    {"text": text},
                )

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.origin = f"http://127.0.0.1:{self.server.server_port}"

    def close(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()


class ConfigTests(unittest.TestCase):
    def setUp(self):
        self.config = json.loads((ROOT / "fixtures/capture-purchase.json").read_text())

    def test_help_does_not_require_playwright_or_launch_a_browser(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/capture.py"), "--help"],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("--executable-path", result.stdout)

    def test_external_origin_requires_explicit_configuration(self):
        self.config["browser"]["url"] = "https://example.invalid/checkout"
        with self.assertRaisesRegex(CAPTURE.CaptureError, "origin"):
            CAPTURE.validate(self.config)

    def test_no_secret_field_or_unbounded_processing_window(self):
        for change in ("secret", "bound"):
            config = copy.deepcopy(self.config)
            if change == "secret":
                config["readback"]["expected"]["access_token"] = "test"
            else:
                config["readback"]["processing_bound_ms"] = 100000
            with self.assertRaises(CAPTURE.CaptureError):
                CAPTURE.validate(config)

    def test_malformed_nested_config_has_a_clear_error(self):
        for field in ("journey", "browser", "ui", "submission", "readback"):
            with self.subTest(field=field):
                config = copy.deepcopy(self.config)
                config[field] = []
                with self.assertRaisesRegex(CAPTURE.CaptureError, "must be an object"):
                    CAPTURE.validate(config)

    def test_missing_optional_dependency_is_explicit(self):
        result = subprocess.run(
            [
                sys.executable,
                "-S",
                str(ROOT / "scripts/capture.py"),
                str(ROOT / "fixtures/capture-purchase.json"),
                "/unused-output",
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("Playwright Python is optional and unavailable", result.stdout)


@unittest.skipUnless(
    CHROMIUM,
    "Optional Playwright and existing Chromium required; set CAPTURE_CHROMIUM_EXECUTABLE",
)
class BrowserCaptureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = LocalJourney()

    @classmethod
    def tearDownClass(cls):
        cls.fixture.close()

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.config = json.loads((ROOT / "fixtures/capture-purchase.json").read_text())
        self.config["base_url"] = self.fixture.origin
        self.identity = self.id().split(".")[-1]

    def run_case(self, mode, kind="purchase"):
        config = self.config
        config["journey"].update(id=self.identity, kind=kind)
        config["browser"]["url"] = f"/?kind={kind}&mode={mode}&test_id={self.identity}"
        config["steps"][-1]["target"]["name"] = (
            "Pay test amount" if kind == "purchase" else "Book test slot"
        )
        config["readback"]["url"] = f"/api/records?test_id={self.identity}"
        config["readback"]["identity"]["value"] = self.identity
        if kind == "booking":
            config["readback"]["expected"]["slot"] = "2030-01-01T10:00:00Z"
        evidence = CAPTURE.capture(config, Path(self.temp.name), CHROMIUM)
        result = AUDIT.audit(evidence)
        self.assertEqual(result["status"], "audited_supplied_evidence", result)
        return evidence, result

    def test_confirmed_purchase_has_matching_persisted_fields_and_real_pixels(self):
        evidence, result = self.run_case("confirmed")
        self.assertEqual(evidence["observations"][0]["result"], "pass")
        self.assertEqual(evidence["capture"]["backend_semantics"], "matched")
        self.assertEqual(result["outcome_checks"][0]["status"], "verified_present")
        self.assertEqual(result["findings"], [])
        screen = Path(self.temp.name) / "final.png"
        self.assertTrue(screen.read_bytes().startswith(b"\x89PNG"))
        self.assertEqual(
            evidence["capture"]["screenshots"][-1]["viewport"],
            {"width": 390, "height": 844},
        )
        network = json.loads((Path(self.temp.name) / "network.json").read_text())
        self.assertTrue(
            any(
                row["method"] == "POST" and row["status"] == 200
                for row in network["requests"]
            )
        )
        exported = " ".join(
            path.read_text() for path in Path(self.temp.name).glob("*.json")
        )
        for secret in (
            "must-not-export",
            "do-not-export",
            "capture@example.invalid",
            "private_token",
        ):
            self.assertNotIn(secret, exported)

    def test_false_success_purchase_and_booking_are_reproduced_defects(self):
        for kind in ("purchase", "booking"):
            with self.subTest(kind=kind):
                if kind == "booking":
                    self.identity += "-booking"
                    self.temp.cleanup()
                    self.temp = tempfile.TemporaryDirectory()
                    self.addCleanup(self.temp.cleanup)
                evidence, result = self.run_case("false_success", kind)
                self.assertEqual(evidence["capture"]["backend_semantics"], "absent")
                self.assertEqual(evidence["observations"][0]["result"], "fail")
                self.assertEqual(
                    result["outcome_checks"][0]["status"], "verified_absent"
                )
                self.assertIn(
                    "observed_reproducible_defect",
                    [row["classification"] for row in result["findings"]],
                )

    def test_pending_booking_before_processing_bound_stays_unknown(self):
        self.config["readback"].update(processing_bound_ms=10000, max_wait_ms=250)
        evidence, result = self.run_case("pending", "booking")
        self.assertEqual(evidence["observations"][0]["result"], "unknown")
        self.assertFalse(
            evidence["observations"][0]["outcome"]["verification"]["settled"]
        )
        self.assertEqual(result["outcome_checks"][0]["status"], "pending_verification")
        self.assertEqual(result["findings"], [])

    def test_delayed_backend_record_is_polled_without_repeated_submission(self):
        self.config["readback"].update(processing_bound_ms=1500, max_wait_ms=1500)
        evidence, result = self.run_case("delayed")
        self.assertEqual(evidence["capture"]["backend_semantics"], "matched")
        readback = json.loads((Path(self.temp.name) / "readback.json").read_text())
        self.assertGreater(len(readback["attempts"]), 1)
        self.assertEqual(result["outcome_checks"][0]["status"], "verified_present")
        self.assertEqual(
            len(
                [row for row in self.fixture.submits if row["test_id"] == self.identity]
            ),
            1,
        )

    def test_wrong_status_amount_and_slot_do_not_become_success(self):
        for mode in ("wrong_status", "wrong_amount", "wrong_slot"):
            with self.subTest(mode=mode):
                self.identity += f"-{mode}"
                if mode != "wrong_status":
                    self.temp.cleanup()
                    self.temp = tempfile.TemporaryDirectory()
                    self.addCleanup(self.temp.cleanup)
                evidence, result = self.run_case(mode, "booking")
                self.assertEqual(
                    evidence["capture"]["backend_semantics"], "field_mismatch"
                )
                self.assertEqual(evidence["observations"][0]["result"], "fail")
                self.assertEqual(
                    result["outcome_checks"][0]["status"], "verified_present"
                )
                self.assertIn(
                    "observed_reproducible_defect",
                    [row["classification"] for row in result["findings"]],
                )

    def test_final_ui_is_resampled_after_backend_polling(self):
        self.config["readback"].update(processing_bound_ms=1500, max_wait_ms=1500)
        evidence, result = self.run_case("ui_changes")
        self.assertEqual(evidence["capture"]["backend_semantics"], "matched")
        self.assertEqual(evidence["capture"]["ui"]["state"], "failure")
        self.assertIn(
            evidence["capture"]["ui"]["initial_observation"]["state"],
            ("unknown", "success"),
        )
        self.assertEqual(evidence["observations"][0]["result"], "fail")
        self.assertIn(
            "observed_reproducible_defect",
            [row["classification"] for row in result["findings"]],
        )

    def test_slow_readback_cannot_turn_short_observation_into_settled_failure(self):
        self.config["readback"].update(processing_bound_ms=1000, max_wait_ms=60)
        evidence, result = self.run_case("slow_readback")
        readback = json.loads((Path(self.temp.name) / "readback.json").read_text())
        self.assertLess(readback["final"]["elapsed_after_actions_ms"], 200)
        self.assertFalse(readback["final"]["settled"])
        self.assertEqual(evidence["observations"][0]["result"], "unknown")
        self.assertEqual(result["outcome_checks"][0]["status"], "unverified")

    def test_zero_followup_budget_does_not_start_an_unbounded_probe(self):
        self.config["readback"]["max_wait_ms"] = 0
        evidence, result = self.run_case("confirmed")
        readback = json.loads((Path(self.temp.name) / "readback.json").read_text())
        self.assertEqual(readback["attempts"], [])
        self.assertEqual(evidence["observations"][0]["result"], "unknown")
        self.assertEqual(result["outcome_checks"][0]["status"], "unverified")

    def test_wrong_record_identity_is_unverified_instead_of_absent_or_success(self):
        evidence, result = self.run_case("wrong_identity")
        self.assertEqual(evidence["observations"][0]["result"], "unknown")
        self.assertEqual(
            evidence["observations"][0]["outcome"]["persisted_record"], "unchecked"
        )
        self.assertEqual(result["outcome_checks"][0]["status"], "unverified")

    def test_declined_negative_control_is_not_a_false_success(self):
        self.config["ui"]["expected"] = "failure"
        evidence, result = self.run_case("declined")
        self.assertEqual(evidence["observations"][0]["result"], "pass")
        self.assertEqual(evidence["observations"][0]["outcome"]["http_status"], 402)
        self.assertEqual(result["findings"], [])

    def test_preexisting_record_blocks_actions_instead_of_crediting_old_success(self):
        self.fixture.records[self.identity] = [
            {"test_id": self.identity, "status": "confirmed"}
        ]
        before = len(self.fixture.submits)
        evidence, result = self.run_case("confirmed")
        self.assertEqual(evidence["capture"]["status"], "blocked_baseline")
        self.assertEqual(evidence["observations"][0]["result"], "unknown")
        self.assertEqual(len(self.fixture.submits), before)
        self.assertEqual(result["outcome_checks"][0]["status"], "unverified")


if __name__ == "__main__":
    unittest.main()
