# Setup by client

Server URL: `https://mcp.sogood.ai/mcp`. Sign-in is OAuth in the browser; there is no key. The founder picks which businesses the connection can use.

## Claude Code

```bash
claude plugin marketplace add sogoodai/ai-business-plugin
claude plugin install sogood@sogood
```

Then in Claude Code: `/mcp`, select `plugin:sogood:sogood`, sign in.

MCP only, without the plugin:

```bash
claude mcp add --transport http sogood https://mcp.sogood.ai/mcp
```

## Codex

```bash
codex plugin marketplace add sogoodai/ai-business-plugin
codex plugin add sogood@sogood
```

Approve the SoGood sign-in when Codex asks (or `codex mcp login sogood`). MCP only, in `~/.codex/config.toml`:

```toml
[mcp_servers.sogood]
url = "https://mcp.sogood.ai/mcp"
```

then `codex mcp login sogood`. Keep `call_sensitive_action` on approval (the default).

Skills only: copy `skills/*` into `~/.agents/skills/` (or `~/.codex/skills/`).

## Claude.ai and Claude Desktop

Settings, Connectors, Add custom connector, URL `https://mcp.sogood.ai/mcp`.

## Cursor

`~/.cursor/mcp.json`:

```json
{ "mcpServers": { "sogood": { "url": "https://mcp.sogood.ai/mcp" } } }
```

## Gemini CLI

```bash
gemini extensions install https://github.com/sogoodai/ai-business-plugin
```

## VS Code (Copilot agent mode)

`.vscode/mcp.json`:

```json
{ "servers": { "sogood": { "type": "http", "url": "https://mcp.sogood.ai/mcp" } } }
```

## Any other client

Use [`mcp.json`](../../../mcp.json) at the repository root, or point the client at the URL as a remote Streamable HTTP server. Clients that only speak stdio can bridge with `npx mcp-remote https://mcp.sogood.ai/mcp`.
