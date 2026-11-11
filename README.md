# OpenCode Bundle — Agents + Skills + MCPs

This bundle contains:
- **Agents** (multi-model harness: orchestrator + specialists)
- **Skills** (8 video-editing skills)
- **MCP config template** (11 MCP servers)
- **Dependencies list**

## 1) Install OpenCode
Download from https://opencode.ai/v2/docs/ (Desktop or CLI).

## 2) Copy Agents (global)
Copy `agents/` to:
- Windows: `%USERPROFILE%\.config\opencode\agents\`
- macOS/Linux: `~/.config/opencode/agents/`

## 3) Copy Skills (global)
Copy `skills/` to:
- Windows: `%USERPROFILE%\.config\opencode\skills\`
- macOS/Linux: `~/.config/opencode/skills/`

(Or put in project `.opencode/skills/` for project-only.)

## 4) Merge Config
Merge `opencode.jsonc` into your global config:
- Windows: `%USERPROFILE%\.config\opencode\opencode.jsonc`
- macOS/Linux: `~/.config/opencode/opencode.jsonc`

If you already have a config, merge the `mcp.servers`, `default_agent`, and `model` fields.

## 5) Set Environment Variables (for MCPs)
Set these in your OS environment (or use `{env:...}` substitution):
- `PEXELS_API_KEY` (Pexels)
- `GITHUB_PERSONAL_ACCESS_TOKEN` (GitHub MCP)
- `BRAVE_API_KEY` (Brave Search) — optional, disabled by default
- `EXA_API_KEY` (Exa) — optional, disabled by default

## 6) Install Dependencies

### Python + Video skills
- Python 3.11+
- ffmpeg (modern build)
- pip install faster-whisper mediapipe playwright
- playwright install chromium

### Security/Testing tools
- semgrep: `pip install semgrep`
- snyk: `npm install -g snyk` then `snyk auth`

### Node
- Node.js >= 20

## 7) Restart OpenCode
Restart OpenCode Desktop/CLI to load agents, skills, and MCPs.

## 8) Verify
- `/mcps` → check connected servers
- Ask: "List available agents and their models"
- Try: "Use ui-designer + frontend-dev + backend-dev to build a login page"

## Notes
- `media-analyst` uses `opencode/gemini-3.5-flash` (may be paid).  
  Change to `nemotron-3.5-super-vl-free` for free vision.
- `semgrep`/`snyk` MCPs require CLI installed.
- `brave-search`/`exa` are disabled until API keys are set.
- Skills (video) require Python+ffmpeg+packages.

## Direct Download Links (Dependencies)

| Dependency | Direct Link |
|---|---|
| Python 3.12 | https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe |
| Node.js 24.16.0 | https://nodejs.org/dist/v24.16.0/node-v24.16.0-x64.msi |
| Bun | https://github.com/oven-sh/bun/releases/latest/download/bun-windows-x64.zip |
| uv | https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-pc-windows-msvc.zip |
| ffmpeg 9.0.2 | https://github.com/GyanD/codexffmpeg/releases/download/9.0.2/ffmpeg-9.0.2-full_build.zip |
| scrcpy 5.0.1 | https://github.com/Genymobile/scrcpy/releases/download/v5.0.1/scrcpy-win64-v5.0.1.zip |
| Docker Desktop | https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe |

Run `download_deps.ps1` to download all automatically.

## Model Assignment (who does what)

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

Free models: beam-free, deepseek-v4.1-flash-free, glm-5.3-flash-free, mimo-v2.6-flash-free, minimax-m3.1-flash-free, longcat-2.5-free, nemotron-3.5-super-vl-free (vision).

## Contents
- `agents/` — 14 specialist agents
- `skills/` — 8 video-editing skills
- `opencode.jsonc` — MCP + default agent/model config
- `README.md` — this file
- `installer.py` + `install.bat` — GUI installer
- `install.ps1` — PowerShell installer
- `download_deps.ps1` — direct download links


## Multi-Agent Collaboration (How to Use)

### 1) Parallel Review (2-3 agents on same task)
**Request:** "Run reviewer + security-auditor + ui-designer in parallel on this change, then synthesize."
**What happens:** All three run in background, then Orchestrator combines findings.

### 2) Discuss → Refine → Execute
**Request:** "Have planner, frontend-dev, backend-dev discuss and implement a login page together."
**What happens:** All propose approaches → Orchestrator picks best → coder implements.

### 3) Divide & Conquer (same task, split work)
**Request:** "Run frontend-dev (UI) + backend-dev (API) + security-auditor (review) in parallel, then integrate."
**What happens:** Each handles their part → Orchestrator integrates.

### 4) Review Loop
**Request:** "Implement X, then review, then fix, then re-review."
**What happens:** coder → reviewer → coder → reviewer until clean.

### Available Agents
orchestrator, planner, ui-designer, ux-researcher, frontend-dev, backend-dev, security-auditor, mcp-integrator, media-analyst, web-researcher, skill-scout, reviewer, coder, pentest-agent.

### Available Skills
accessibility, code-review, diagnosing-bugs, frontend-design, performance-optimization, playwright-best-practices, web-design-guidelines, multi-agent-harness, multi-agent-collaboration, opencode-models-guide, agent-reach, free-llm-apis, artemis-mobile, and 8 video skills.

### Best Practices
- Use **foreground** for dependent steps.
- Use **background** for independent parallel work.
- Persist intermediate results to `work/` files.
- Use claude-mem for durable notes.
- Keep tasks small to avoid context loss.
