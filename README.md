# Joe Skills — OpenCode Bundle

**Joe Skills** is a packaged OpenCode setup with:
- **14 specialist agents** (multi-model harness)
- **8 video-editing skills**
- **13 MCP servers** (Pexels, Playwright, Semgrep, Snyk, MagicUI, Claude-Mem, Artemis, etc.)
- **Installer** (GUI + PowerShell + Docker)

---

## 🚀 Quick Start

### Option 1: GUI Installer
1. Run `install.bat` (requires Python).
2. Select components → Start Install.
3. Restart OpenCode.

### Option 2: PowerShell Installer
```powershell
.\install.ps1
```

### Option 3: Docker
```bash
docker-compose up --build
```

---

## 📁 Contents
- `agents/` — 14 specialist agents
- `skills/` — 8 video-editing skills
- `opencode.jsonc` — MCP + default agent/model config
- `installer.py` — GUI installer
- `install.bat` — launcher
- `install.ps1` — PowerShell installer
- `download_deps.ps1` — download all deps
- `Dockerfile.strix` — Strix container
- `Dockerfile.artemis` — Artemis container
- `docker-compose.yml` — orchestration
- `README.md` — this file

---

## 🔗 Direct Download Links (Dependencies)
| Dependency | Link |
|---|---|
| Python 3.12 | https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe |
| Node.js 24.16.0 | https://nodejs.org/dist/v24.16.0/node-v24.16.0-x64.msi |
| Bun | https://github.com/oven-sh/bun/releases/latest/download/bun-windows-x64.zip |
| uv | https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-pc-windows-msvc.zip |
| ffmpeg 9.0.2 | https://github.com/GyanD/codexffmpeg/releases/download/9.0.2/ffmpeg-9.0.2-full_build.zip |
| scrcpy 5.0.1 | https://github.com/Genymobile/scrcpy/releases/download/v5.0.1/scrcpy-win64-v5.0.1.zip |
| Docker Desktop | https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe |

Run `download_deps.ps1` to download all.

---

## 🤖 Agents (Multi-Model Harness)
| Agent | Model | Role |
|---|---|---|
| orchestrator | opencode/beam-free | Router |
| planner | opencode/deepseek-v4.1-flash-free | Planning |
| ui-designer | opencode/glm-5.3-flash-free | UI/visual |
| ux-researcher | opencode/deepseek-v4.1-flash-free | UX/research |
| frontend-dev | opencode/glm-5.3-flash-free | Frontend |
| backend-dev | opencode/minimax-m3.1-flash-free | Backend |
| security-auditor | opencode/minimax-m3.1-flash-free | Security |
| mcp-integrator | opencode/longcat-2.5-free | MCP/connectivity |
| media-analyst | opencode/gemini-3.5-flash | Images/text/video |
| web-researcher | opencode/longcat-2.5-free | Web search/images |
| skill-scout | opencode/deepseek-v4.1-flash-free | Find skills |
| reviewer | opencode/mimo-v2.6-flash-free | Review |
| coder | opencode/glm-5.3-flash-free | Implementation |
| pentest-agent | opencode/minimax-m3.1-flash-free | Strix pentesting |

---

## 🔌 MCP Servers
- pexels, playwright, filesystem, context7, sentry, github, brave-search (disabled), semgrep, snyk, exa (disabled), magicui, claude-mem, artemis.

---

## 📹 Skills (Video)
- business-short-form-reels, depth-ui-reel, educational-youtube-editor, personal-broll-library, personal-short-form-reels, ranking-format, tutorial-videos, youtube-clips.

---

## 🔐 API Keys (Environment Variables)
- `PEXELS_API_KEY` (Pexels)
- `GITHUB_PERSONAL_ACCESS_TOKEN` (GitHub)
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
- Docker (Strix)
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