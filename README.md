# 🚀 Joe Skills — OpenCode Bundle

![Joe Skills](https://img.shields.io/badge/Joe%20Skills-OpenCode%20Bundle-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=for-the-badge)

> **Joe Skills** is a complete OpenCode setup with **14 specialist agents**, **12+ skills**, **13 MCP servers**, and an **installer GUI** — all configured for multi-model orchestration and parallel execution.

---

## 📸 Preview

![Installer Preview](docs/installer-preview.png)

> *The installer GUI (Python/Tkinter) with Components, Install, Log, and Model Map tabs.*

---

## ✨ Features

- **Multi-Agent Harness** — Orchestrator + 13 specialists (UI, UX, Frontend, Backend, Security, MCP, Media, Research, SkillScout, Reviewer, Coder, Planner, Pentest).
- **12+ Skills** — Video editing, accessibility, code-review, testing, performance, etc.
- **13 MCP Servers** — Pexels, Playwright, Semgrep, Snyk, MagicUI, Claude-Mem, Artemis, Context7, Sentry, GitHub (OAuth), Filesystem, Exa, Brave.
- **Installer GUI** — Select components, check installed status, auto-install deps.
- **Direct Download Links** — Python, Node, Bun, uv, ffmpeg, scrcpy, Docker.
- **Docker Support** — Strix + Artemis containers.
- **Goal Management** — Big goals + small goals + auto-review before close.
- **Memory (claude-mem)** — Persistent notes across sessions.
- **Free & Paid Models** — Uses free OpenCode models; supports paid (GPT-5.5, Claude Opus, Gemini Pro).

---

## 🚀 Quick Start

### Option 1: GUI Installer (Recommended)
1. Download `JoeSkillsInstaller.exe` from [Releases](https://github.com/yousseftallal/-open-code-full-power-/releases).
2. Run `JoeSkillsInstaller.exe`.
3. Select components → **Start Install**.
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
1. Copy `agents/` → `~/.config/opencode/agents/`
2. Copy `skills/` → `~/.config/opencode/skills/`
3. Merge `opencode.jsonc` into `~/.config/opencode/opencode.jsonc`
4. Set environment variables (see below)
5. Restart OpenCode

---

## 📋 Installation Guide

### Step 1: Install OpenCode
Download from https://opencode.ai/v2/docs/ (Desktop or CLI).

### Step 2: Install Dependencies
| Dependency | Direct Link |
|---|---|
| Python 3.12 | https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe |
| Node.js 24.16.0 | https://nodejs.org/dist/v24.16.0/node-v24.16.0-x64.msi |
| Bun | https://github.com/oven-sh/bun/releases/latest/download/bun-windows-x64.zip |
| uv | https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-pc-windows-msvc.zip |
| ffmpeg 9.0.2 | https://github.com/GyanD/codexffmpeg/releases/download/9.0.2/ffmpeg-9.0.2-full_build.zip |
| scrcpy 5.0.1 | https://github.com/Genymobile/scrcpy/releases/download/v5.0.1/scrcpy-win64-v5.0.1.zip |
| Docker Desktop | https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe |

Or run `download_deps.ps1` to download all automatically.

### Step 3: Copy Files
- `agents/` → `~/.config/opencode/agents/`
- `skills/` → `~/.config/opencode/skills/`

### Step 4: Merge Config
Merge `opencode.jsonc` into your global config.

### Step 5: Set Environment Variables
- `PEXELS_API_KEY` (Pexels)
- `GITHUB_PERSONAL_ACCESS_TOKEN` (GitHub MCP) — or use OAuth/Docker
- `BRAVE_API_KEY` (Brave Search) — optional
- `EXA_API_KEY` (Exa) — optional
- `LLM_API_KEY` (Strix)
- `STRIX_LLM` (Strix model)
- `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Artemis)
- `OPEN_ROUTER_API_KEY` (Artemis/OpenRouter)

### Step 6: Restart OpenCode
Restart OpenCode Desktop/CLI to load agents, skills, and MCPs.

### Step 7: Verify
- `/mcps` → check connected servers
- Ask: "List available agents and their models"
- Try: "Use ui-designer + frontend-dev + backend-dev to build a login page"

---

## 🤖 Agents (Multi-Model Harness)

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

## 🔌 MCP Servers (13)

| Server | Type | Status |
|---|---|---|
| pexels | local (npx) | ✅ configured |
| playwright | local (npx) | ✅ configured |
| filesystem | local (npx) | ✅ configured |
| context7 | remote | ✅ configured |
| sentry | remote (OAuth) | ✅ configured |
| github | docker (OAuth) | ✅ configured |
| brave-search | local (npx) | ⚠️ disabled (no key) |
| semgrep | local (CLI) | ✅ configured |
| snyk | local (CLI) | ✅ configured |
| exa | local (npx) | ⚠️ disabled (no key) |
| magicui | local (npx) | ✅ configured |
| claude-mem | local (CLI) | ✅ configured |
| artemis | local (uv) | ✅ configured |

---

## 📹 Skills (12+)

### Built-in (OpenCode)
accessibility, browser, build-dashboard, code-review, data-visualization, diagnosing-bugs, frontend-design, performance-optimization, playwright-best-practices, report, universal-erp-flow, verification-before-completion, web-design-guidelines, xlsx-manipulation.

### Joe Skills (custom)
- **multi-agent-harness** — parallel/context persistence guide
- **multi-agent-collaboration** — collaborative execution patterns
- **opencode-models-guide** — free/paid models + connection
- **goal-management** — big/small goals + auto-review
- **auto-review** — review before closing goal
- **agent-reach** — web/social scraping CLI
- **free-llm-apis** — free LLM providers list
- **artemis-mobile** — Android automation MCP

### Video Skills (8)
business-short-form-reels, depth-ui-reel, educational-youtube-editor, personal-broll-library, personal-short-form-reels, ranking-format, tutorial-videos, youtube-clips.

---

## 🎯 Multi-Agent Collaboration

### Patterns
1. **Parallel Review** — 2-3 agents on same task (reviewer + security + ui).
2. **Discuss → Refine → Execute** — planner + frontend + backend discuss, then coder implements.
3. **Divide & Conquer** — frontend UI + backend API + security review in parallel.
4. **Review Loop** — coder → reviewer → coder → reviewer until clean.

### Usage Examples
> "Run reviewer + security-auditor + ui-designer in parallel on this change, then synthesize."

> "Have planner, frontend-dev, backend-dev discuss and implement a login page together."

---

## 🔮 Future Skills (to add)
- **Security:** OWASP checklist, SAST rules, dependency scanning.
- **Testing:** Jest, Vitest, Cypress, Playwright advanced.
- **DevOps:** Docker, CI/CD, Kubernetes, Terraform.
- **Data:** SQL, analytics, ETL, dbt.
- **Docs:** API docs, README, changelog, OpenAPI.
- **Mobile:** iOS testing, Flutter, React Native.
- **Design:** Figma, shadcn, Tailwind, design tokens.
- **AI/ML:** RAG, embeddings, fine-tuning.

---

## 🔐 Environment Variables
- `PEXELS_API_KEY` (Pexels)
- `GITHUB_PERSONAL_ACCESS_TOKEN` (GitHub MCP) — or OAuth
- `BRAVE_API_KEY` (Brave Search) — optional
- `EXA_API_KEY` (Exa) — optional
- `LLM_API_KEY` (Strix)
- `STRIX_LLM` (Strix model)
- `GEMINI_API_KEY` / `GOOGLE_API_KEY` (Artemis)
- `OPEN_ROUTER_API_KEY` (Artemis/OpenRouter)

---

## 🛠️ Dependencies
- Python 3.12 (Strix, Artemis)
- Python 3.11 (agent-reach, video skills)
- Node.js >=20
- Bun (claude-mem)
- uv (Artemis)
- ffmpeg (video)
- scrcpy (Artemis video recording)
- Docker (Strix, GitHub MCP OAuth)
- Android device/emulator (Artemis)

---

## 📝 Notes
- `media-analyst` uses `opencode/gemini-3.5-flash` (may be paid). Change to `nemotron-3.5-super-vl-free` for free vision.
- `brave-search`/`exa` disabled until API keys set.
- Strix requires Docker + LLM_API_KEY.
- Artemis requires Android device/emulator + Gemini key.

---

## 📄 License
MIT (for Joe Skills bundle). Individual tools have their own licenses.