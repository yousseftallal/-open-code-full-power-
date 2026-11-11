---
name: artemis-mobile
description: "Android automation via Google Artemis MCP: natural language instructions to real Android devices, logcat, screenshots, testing. Use when user needs mobile testing/automation."
---

# Artemis (Android Automation)

GitHub: https://github.com/google/artemis

## What it does
- Turns natural language into Android UI automation.
- MCP server for IDEs (Antigravity, Claude Code, Windsurf, OpenCode).
- Captures logs, screenshots, replays.

## Prerequisites
- Python 3.12+
- uv (Python package manager)
- Android device/emulator with USB debugging
- Docker (for Strix, not Artemis)

## Setup
```bash
git clone https://github.com/google/artemis.git
cd artemis
# macOS/Linux
./start.sh
# Windows
.\start.bat
```
Opens http://localhost:8000 and configures MCP.

## MCP
Artemis runs an MCP server. Connect via OpenCode MCP config:
```jsonc
{
  "mcp": {
    "servers": {
      "artemis": {
        "type": "local",
        "command": ["uv", "run", "artemis", "mcp"]
      }
    }
  }
}
```
(Requires artemis repo cloned and uv installed.)

## Notes
- First run installs accessibility helper on device.
- Supports Flash/Pro profiles.
- 99%+ success on AndroidWorld benchmark.
