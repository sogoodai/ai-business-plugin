# SoGood AI

This extension connects the SoGood MCP (`https://mcp.sogood.ai/mcp`) and ships business playbooks in `skills/`.

- For a SoGood business: read `skills/sogood/SKILL.md` first. Run reads freely. Before `call_sensitive_action` (sends, publishes, deletes, spend), state exactly what will happen and get the user's yes. Finish with `call_action handBackToTeam` after any write.
- For business advice: open the matching `skills/<type>/SKILL.md` (for example `home-services`, `ecommerce-brand`, `boring-businesses`) and follow it.
