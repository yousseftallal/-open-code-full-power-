# Joe Skills - OpenCode Bundle

**Joe Skills** is a complete OpenCode setup with 14 specialist agents, 50+ skills, 13 MCP servers, and a cross-platform installer (GUI + PowerShell). It provides multi-model orchestration, parallel execution, and persistent memory.

---

## Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Direct Download Links](#direct-download-links)
- [Agents](#agents)
- [MCP Servers](#mcp-servers)
- [Skills](#skills)
- [Multi-Agent Collaboration](#multi-agent-collaboration)
- [Goal Management](#goal-management)
- [Environment Variables](#environment-variables)
- [Notes](#notes)
- [License](#license)

---

## Features

- **Multi-Agent Harness** - Orchestrator + 13 specialists (UI, UX, Frontend, Backend, Security, MCP, Media, Research, SkillScout, Reviewer, Coder, Planner, Pentest).
- **50+ Skills** - Video editing, accessibility, code-review, testing, performance, and more.
- **13 MCP Servers** - Pexels, Playwright, Semgrep, Snyk, MagicUI, Claude-Mem, Artemis, Context7, Sentry, GitHub (OAuth), Filesystem, Exa, Brave.
- **Installer GUI** - Python/Tkinter with Components, Install, Log, and Model Map tabs.
- **Cross-Platform** - Windows, macOS, Linux (auto-detects OS).
- **Direct Download Links** - Python, Node, Bun, uv, ffmpeg, scrcpy, Docker.
- **Docker Support** - Strix + Artemis containers.
- **Goal Management** - Big goals + small goals + auto-review before close.
- **Memory (claude-mem)** - Persistent notes across sessions.
- **Free & Paid Models** - Uses free OpenCode models; supports paid (GPT-5.5, Claude Opus, Gemini Pro).

---

## Quick Start

### Option 1: GUI Installer (Recommended)
1. Download `opencode-share-bundle.zip` from [Releases](https://github.com/yousseftallal/-open-code-full-power-/releases).
2. Extract and run `install.bat` (Windows) or `python installer.py`.
3. Select components, click **Start Install**.
4. Restart OpenCode.

### Option 2: PowerShell Installer
```powershell
.\install.ps1
```

### Option 3: Docker
```bash
docker-compose up --build
```

### Option 4: Manual
1. Copy `agents/` to `~/.config/opencode/agents/`
2. Copy `skills/` to `~/.config/opencode/skills/`
3. Merge `opencode.jsonc` into `~/.config/opencode/opencode.jsonc`
4. Set environment variables
5. Restart OpenCode

---

## Installation

### Windows
1. Install Python 3.11+ (https://www.python.org/downloads/)
2. Install Node.js >=20 (https://nodejs.org/)
3. Run `install.bat` or `python installer.py`
4. Installer auto-installs deps via winget/pip/npm
5. Restart OpenCode

### macOS
1. Install Homebrew: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. Run `python3 installer.py`
3. Installer auto-installs deps via brew/pip/npm
4. Restart OpenCode

### Linux
1. Install Python 3.11+: `sudo apt install python3 python3-pip`
2. Install Node.js >=20: `sudo apt install nodejs npm`
3. Run `python3 installer.py`
4. Installer auto-installs deps via apt/pip/npm
5. Restart OpenCode

---

## Dependencies

| Dependency | Purpose | Auto-Install |
|---|---|---|
| Python 3.12 | Strix, Artemis | winget/brew/apt |
| Python 3.11 | agent-reach, video skills | winget/brew/apt |
| Node.js >=20 | MCP servers, claude-mem | winget/brew/apt |
| Bun | claude-mem worker | winget/brew |
| uv | Artemis | pip |
| ffmpeg | Video processing | winget/brew/apt |
| scrcpy | Artemis video recording | winget/brew/apt |
| Docker | Strix, GitHub MCP OAuth | winget/brew/apt |
| Playwright | Browser testing | pip |
| faster-whisper | Video transcription | pip |
| mediapipe | Face tracking | pip |
| semgrep | Security scanning | pip |
| snyk | Dependency scanning | npm |
| strix-agent | Penetration testing | pip (Python 3.12) |
| claude-mem | Persistent memory | npm |
| agent-reach | Web scraping | pip (git) |

---

## Direct Download Links

| Dependency | Link |
|---|---|
| Python 3.12 | https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe |
| Node.js 24.16.0 | https://nodejs.org/dist/v24.16.0/node-v24.16.0-x64.msi |
| Bun | https://github.com/oven-sh/bun/releases/latest/download/bun-windows-x64.zip |
| uv | https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-pc-windows-msvc.zip |
| ffmpeg 9.0.2 | https://github.com/GyanD/codexffmpeg/releases/download/9.0.2/ffmpeg-9.0.2-full_build.zip |
| scrcpy 5.0.1 | https://github.com/Genymobile/scrcpy/releases/download/v5.0.1/scrcpy-win64-v5.0.1.zip |
| Docker Desktop | https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe |

Run `download_deps.ps1` to download all automatically.

---

## Agents

| Agent | Model | Role |
|---|---|---|
| orchestrator | opencode/beam-free | Router / coordinator |
| planner | opencode/deepseek-v4.1-flash-free | Planning / analysis |
| ui-designer | opencode/glm-5.3-flash-free | UI / visual design |
| ux-researcher | opencode/deepseek-v4.1-flash-free | UX / research |
| frontend-dev | opencode/glm-5.3-flash-free | Frontend code |
| backend-dev | opencode/minimax-m3.1-flash-free | Backend / auth |
| security-auditor | opencode/minimax-m3.1-flash-free | Security audit |
| mcp-integrator | opencode/longcat-2.5-free | MCP / connectivity |
| media-analyst | opencode/gemini-3.5-flash | Images/text/video (vision) |
| web-researcher | opencode/longcat-2.5-free | Web search / assets |
| skill-scout | opencode/deepseek-v4.1-flash-free | Find skills/MCPs |
| reviewer | opencode/mimo-v2.6-flash-free | Code review |
| coder | opencode/glm-5.3-flash-free | Implementation |
| pentest-agent | opencode/minimax-m3.1-flash-free | Strix pentesting |

---

## MCP Servers (13)

| Server | Type | Status |
|---|---|---|
| pexels | local (npx) | Configured |
| playwright | local (npx) | Configured |
| filesystem | local (npx) | Configured |
| context7 | remote | Configured |
| sentry | remote (OAuth) | Configured |
| github | docker (OAuth) | Configured |
| brave-search | local (npx) | Disabled (no key) |
| semgrep | local (CLI) | Configured |
| snyk | local (CLI) | Configured |
| exa | local (npx) | Disabled (no key) |
| magicui | local (npx) | Configured |
| claude-mem | local (CLI) | Configured |
| artemis | local (uv) | Configured |

---

## Skills (50+)

### Built-in (OpenCode)
accessibility, browser, build-dashboard, code-review, data-visualization, diagnosing-bugs, frontend-design, performance-optimization, playwright-best-practices, report, universal-erp-flow, verification-before-completion, web-design-guidelines, xlsx-manipulation.

### Joe Skills (custom)
- multi-agent-harness — parallel/context persistence
- multi-agent-collaboration — collaborative execution
- opencode-models-guide — free/paid models
- goal-management — big/small goals + auto-review
- auto-review — review before closing goal
- agent-reach — web/social scraping CLI
- free-llm-apis — free LLM providers list
- artemis-mobile — Android automation MCP

### Anthropic Skills
academy-guide, algorithmic-art, brand-guidelines, canvas-design, claude-api, discernment-nudge, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing, xlsx.

### Video Skills (8)
business-short-form-reels, depth-ui-reel, educational-youtube-editor, personal-broll-library, personal-short-form-reels, ranking-format, tutorial-videos, youtube-clips.

---

## Multi-Agent Collaboration

### Patterns
1. **Parallel Review** — 2-3 agents on same task (reviewer + security + ui).
2. **Discuss → Refine → Execute** — planner + frontend + backend discuss, then coder implements.
3. **Divide & Conquer** — frontend UI + backend API + security review in parallel.
4. **Review Loop** — coder → reviewer → coder → reviewer until clean.

### Usage Examples
> "Run reviewer + security-auditor + ui-designer in parallel on this change, then synthesize."

> "Have planner, frontend-dev, backend-dev discuss and implement a login page together."

---

## Goal Management

### Workflow
1. **Set big goal:** `work_state_write(list="project", fields={"goal": "Build login page", "status": "active"})`
2. **Add sub-goals:** `work_state_write(list="project", fields={"sub1": {"task": "Design UI", "agent": "ui-designer", "status": "todo"}})`
3. **Agents update:** `work_state_write(list="project", fields={"sub1": {"status": "done"}})`
4. **Auto-review:** Run reviewer + security-auditor before marking done.
5. **Mark complete:** Only when all reviews pass.

---

## Environment Variables

- `PEXELS_API_KEY` (Pexels)
- `GITHUB_PERSONAL_ACCESS_TOKEN` (GitHub MCP) — or OAuth
- `BRAVE_API_KEY` (Brave Search) — optional
- `EXA_API_KEY` (Exa) — optional
- `LLM_API_KEY` (Strix)
- `STRIX_LLM` (Strix model)
- `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Artemis)
- `OPEN_ROUTER_API_KEY` (Artemis/OpenRouter)

---

## Notes

- `media-analyst` uses `opencode/gemini-3.5-flash` (may be paid). Change to `nemotron-3.5-super-vl-free` for free vision.
- `brave-search`/`exa` disabled until API keys set.
- Strix requires Docker + LLM_API_KEY.
- Artemis requires Android device/emulator + Gemini key.
- Skills (video) require Python+ffmpeg+packages.

---

## License

MIT (for Joe Skills bundle). Individual tools have their own licenses.