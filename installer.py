import os, json, shutil, subprocess, threading, sys
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

HOME = Path.home()
CONFIG = HOME / ".config" / "opencode"
AGENTS_DIR = CONFIG / "agents"
SKILLS_DIR = CONFIG / "skills"
import sys
if getattr(sys, "frozen", False):
    BUNDLE = Path(sys.executable).resolve().parent
else:
    BUNDLE = Path(__file__).resolve().parent
SKILLS_SRC = BUNDLE / "skills"
AGENTS_SRC = BUNDLE / "agents"
CONFIG_SRC = BUNDLE / "opencode.jsonc"

SKILL_NAMES = ["business-short-form-reels","depth-ui-reel","educational-youtube-editor","personal-broll-library","personal-short-form-reels","ranking-format","tutorial-videos","youtube-clips"]
AGENT_NAMES = ["orchestrator","planner","ui-designer","ux-researcher","frontend-dev","backend-dev","security-auditor","mcp-integrator","media-analyst","web-researcher","skill-scout","reviewer","coder","pentest-agent"]

def run_cmd(cmd, log):
    log(f"$ {' '.join(cmd)}")
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if r.stdout: log(r.stdout.strip())
        if r.stderr: log(r.stderr.strip())
        return r.returncode == 0
    except Exception as e:
        log(f"ERROR: {e}")
        return False

def is_installed_skill(name):
    return (SKILLS_DIR / name / "SKILL.md").exists()

def is_installed_agent(name):
    return (AGENTS_DIR / f"{name}.md").exists()

def is_installed_cmd(cmd):
    try:
        r = subprocess.run(["where", cmd], capture_output=True, text=True)
        return r.returncode == 0
    except Exception:
        return False

def is_installed_py(pkg):
    try:
        r = subprocess.run([sys.executable, "-c", f"import {pkg}"], capture_output=True, text=True)
        return r.returncode == 0
    except Exception:
        return False

class InstallerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OpenCode Bundle Installer")
        self.root.geometry("700x500")
        self.log_text = None
        self.vars = {}
        self.build_ui()

    def build_ui(self):
        nb = ttk.Notebook(self.root)
        nb.pack(fill="both", expand=True, padx=10, pady=10)

        # Components tab
        comp_frame = ttk.Frame(nb)
        nb.add(comp_frame, text="Components")
        self.build_components(comp_frame)

        # Install tab
        inst_frame = ttk.Frame(nb)
        nb.add(inst_frame, text="Install")
        self.build_install(inst_frame)

        # Models tab
        models_frame = ttk.Frame(nb)
        nb.add(models_frame, text="Model Map")
        self.build_models(models_frame)

        # Log tab
        log_frame = ttk.Frame(nb)
        nb.add(log_frame, text="Log")
        self.build_log(log_frame)

    def build_components(self, frame):
        canvas = tk.Canvas(frame)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scroll_frame = ttk.Frame(canvas)
        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0,0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Skills
        ttk.Label(scroll_frame, text="Skills (Video)", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(5,2))
        for name in SKILL_NAMES:
            var = tk.BooleanVar(value=not is_installed_skill(name))
            self.vars[f"skill:{name}"] = var
            cb = ttk.Checkbutton(scroll_frame, text=f"{name} {'(installed)' if is_installed_skill(name) else ''}", variable=var)
            cb.pack(anchor="w")

        # Agents
        ttk.Label(scroll_frame, text="Agents (Multi-Model)", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(10,2))
        for name in AGENT_NAMES:
            var = tk.BooleanVar(value=not is_installed_agent(name))
            self.vars[f"agent:{name}"] = var
            cb = ttk.Checkbutton(scroll_frame, text=f"{name} {'(installed)' if is_installed_agent(name) else ''}", variable=var)
            cb.pack(anchor="w")

        # MCP Config
        ttk.Label(scroll_frame, text="MCP Config", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(10,2))
        var = tk.BooleanVar(value=True)
        self.vars["config:mcp"] = var
        ttk.Checkbutton(scroll_frame, text="Merge opencode.jsonc (MCPs + default_agent + model)", variable=var).pack(anchor="w")

        # Dependencies
        ttk.Label(scroll_frame, text="Dependencies", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(10,2))
        deps = [
            ("python312", "Python 3.12", is_installed_cmd("python3.12") or is_installed_cmd("py")),
            ("node", "Node.js >=20", is_installed_cmd("node")),
            ("bun", "Bun runtime", is_installed_cmd("bun")),
            ("uv", "uv (Python package manager)", is_installed_cmd("uv")),
            ("ffmpeg", "ffmpeg (modern)", is_installed_cmd("ffmpeg")),
            ("scrcpy", "scrcpy (video recording)", is_installed_cmd("scrcpy")),
            ("playwright", "Playwright + Chromium", is_installed_py("playwright")),
            ("faster-whisper", "faster-whisper", is_installed_py("faster_whisper")),
            ("mediapipe", "mediapipe", is_installed_py("mediapipe")),
            ("semgrep", "semgrep", is_installed_cmd("semgrep")),
            ("snyk", "snyk", is_installed_cmd("snyk")),
            ("strix", "strix (security)", is_installed_cmd("strix")),
            ("claude-mem", "claude-mem (memory)", is_installed_cmd("claude-mem")),
            ("agent-reach", "agent-reach (web)", is_installed_cmd("agent-reach")),
        ]
        for key, label, installed in deps:
            var = tk.BooleanVar(value=not installed)
            self.vars[f"dep:{key}"] = var
            ttk.Checkbutton(scroll_frame, text=f"{label} {'(installed)' if installed else ''}", variable=var).pack(anchor="w")

    def build_install(self, frame):
        ttk.Label(frame, text="Install selected components", font=("Segoe UI", 11, "bold")).pack(pady=10)
        self.progress = ttk.Progressbar(frame, mode="indeterminate")
        self.progress.pack(fill="x", padx=20, pady=5)
        btn = ttk.Button(frame, text="Start Install", command=self.start_install)
        btn.pack(pady=10)
        ttk.Label(frame, text="Log will appear in 'Log' tab.", font=("Segoe UI", 9)).pack()

    def build_models(self, frame):
        ttk.Label(frame, text="Model Assignment (who does what)", font=("Segoe UI", 11, "bold")).pack(pady=10)
        cols = ("Agent", "Model", "Role")
        tree = ttk.Treeview(frame, columns=cols, show="headings", height=15)
        for c in cols:
            tree.heading(c, text=c)
            tree.column(c, width=200)
        rows = [
            ("orchestrator", "opencode/beam-free", "Router / coordinator"),
            ("planner", "opencode/deepseek-v4.1-flash-free", "Planning / analysis"),
            ("ui-designer", "opencode/glm-5.3-flash-free", "UI / visual design"),
            ("ux-researcher", "opencode/deepseek-v4.1-flash-free", "UX / research"),
            ("frontend-dev", "opencode/glm-5.3-flash-free", "Frontend code"),
            ("backend-dev", "opencode/minimax-m3.1-flash-free", "Backend / auth"),
            ("security-auditor", "opencode/minimax-m3.1-flash-free", "Security audit"),
            ("mcp-integrator", "opencode/longcat-2.5-free", "MCP / connectivity"),
            ("media-analyst", "opencode/gemini-3.5-flash", "Images/text/video (vision)"),
            ("web-researcher", "opencode/longcat-2.5-free", "Web search / assets"),
            ("skill-scout", "opencode/deepseek-v4.1-flash-free", "Find skills/MCPs"),
            ("reviewer", "opencode/mimo-v2.6-flash-free", "Code review"),
            ("coder", "opencode/glm-5.3-flash-free", "Implementation"),
            ("pentest-agent", "opencode/minimax-m3.1-flash-free", "Strix pentesting"),
        ]
        for r in rows:
            tree.insert("", "end", values=r)
        tree.pack(fill="both", expand=True, padx=10, pady=5)
        ttk.Label(frame, text="Free models: beam-free, deepseek-v4.1-flash-free, glm-5.3-flash-free, mimo-v2.6-flash-free, minimax-m3.1-flash-free, longcat-2.5-free, nemotron-3.5-super-vl-free (vision).", font=("Segoe UI", 9)).pack(pady=5)

    def build_log(self, frame):
        self.log_text = scrolledtext.ScrolledText(frame, height=20, state="disabled")
        self.log_text.pack(fill="both", expand=True, padx=5, pady=5)

    def log(self, msg):
        self.log_text.configure(state="normal")
        self.log_text.insert("end", msg + "\n")
        self.log_text.see("end")
        self.log_text.configure(state="disabled")

    def start_install(self):
        self.progress.start()
        threading.Thread(target=self.install_worker, daemon=True).start()

    def install_worker(self):
        self.log("=== Starting installation ===")
        # Skills
        for name in SKILL_NAMES:
            if self.vars.get(f"skill:{name}", tk.BooleanVar(value=False)).get():
                self.log(f"Installing skill: {name}")
                src = SKILLS_SRC / name
                dst = SKILLS_DIR / name
                try:
                    if dst.exists():
                        shutil.rmtree(dst)
                    shutil.copytree(src, dst)
                    self.log(f"  -> OK")
                except Exception as e:
                    self.log(f"  -> ERROR: {e}")
        # Agents
        for name in AGENT_NAMES:
            if self.vars.get(f"agent:{name}", tk.BooleanVar(value=False)).get():
                self.log(f"Installing agent: {name}")
                src = AGENTS_SRC / f"{name}.md"
                dst = AGENTS_DIR / f"{name}.md"
                try:
                    AGENTS_DIR.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dst)
                    self.log(f"  -> OK")
                except Exception as e:
                    self.log(f"  -> ERROR: {e}")
        # Config
        if self.vars.get("config:mcp", tk.BooleanVar(value=False)).get():
            self.log("Merging opencode.jsonc (MCPs + default_agent + model)")
            try:
                CONFIG.mkdir(parents=True, exist_ok=True)
                if (CONFIG / "opencode.jsonc").exists():
                    cur = json.loads((CONFIG / "opencode.jsonc").read_text(encoding="utf-8"))
                else:
                    cur = {}
                src_cfg = json.loads(CONFIG_SRC.read_text(encoding="utf-8"))
                # merge mcp.servers
                cur.setdefault("mcp", {}).setdefault("servers", {}).update(src_cfg.get("mcp", {}).get("servers", {}))
                if "default_agent" in src_cfg:
                    cur["default_agent"] = src_cfg["default_agent"]
                if "model" in src_cfg:
                    cur["model"] = src_cfg["model"]
                (CONFIG / "opencode.jsonc").write_text(json.dumps(cur, indent=2, ensure_ascii=False), encoding="utf-8")
                self.log("  -> OK")
            except Exception as e:
                self.log(f"  -> ERROR: {e}")
        # Dependencies (basic)
        if self.vars.get("dep:python312", tk.BooleanVar(value=False)).get():
            self.log("Python 3.12: please install via winget if missing")
        if self.vars.get("dep:node", tk.BooleanVar(value=False)).get():
            self.log("Node.js: please install via winget if missing")
        if self.vars.get("dep:bun", tk.BooleanVar(value=False)).get():
            self.log("Bun: please install via winget if missing")
        if self.vars.get("dep:uv", tk.BooleanVar(value=False)).get():
            self.log("uv: pip install uv")
            run_cmd([sys.executable, "-m", "pip", "install", "uv"], self.log)
        if self.vars.get("dep:ffmpeg", tk.BooleanVar(value=False)).get():
            self.log("ffmpeg: winget install Gyan.FFmpeg")
        if self.vars.get("dep:scrcpy", tk.BooleanVar(value=False)).get():
            self.log("scrcpy: winget install Genymobile.scrcpy")
        if self.vars.get("dep:playwright", tk.BooleanVar(value=False)).get():
            self.log("Installing playwright + chromium")
            run_cmd([sys.executable, "-m", "pip", "install", "playwright"], self.log)
            run_cmd([sys.executable, "-m", "playwright", "install", "chromium"], self.log)
        if self.vars.get("dep:faster-whisper", tk.BooleanVar(value=False)).get():
            self.log("Installing faster-whisper")
            run_cmd([sys.executable, "-m", "pip", "install", "faster-whisper"], self.log)
        if self.vars.get("dep:mediapipe", tk.BooleanVar(value=False)).get():
            self.log("Installing mediapipe")
            run_cmd([sys.executable, "-m", "pip", "install", "mediapipe"], self.log)
        if self.vars.get("dep:semgrep", tk.BooleanVar(value=False)).get():
            self.log("Installing semgrep (Python 3.12)")
            run_cmd(["py", "-3.12", "-m", "pip", "install", "semgrep"], self.log)
        if self.vars.get("dep:snyk", tk.BooleanVar(value=False)).get():
            self.log("Installing snyk (npm)")
            run_cmd(["npm", "install", "-g", "snyk"], self.log)
        if self.vars.get("dep:strix", tk.BooleanVar(value=False)).get():
            self.log("Installing strix (Python 3.12)")
            run_cmd(["py", "-3.12", "-m", "pip", "install", "strix-agent"], self.log)
        if self.vars.get("dep:claude-mem", tk.BooleanVar(value=False)).get():
            self.log("Installing claude-mem (npm)")
            run_cmd(["npm", "install", "-g", "claude-mem"], self.log)
        if self.vars.get("dep:agent-reach", tk.BooleanVar(value=False)).get():
            self.log("Installing agent-reach (git)")
            run_cmd([sys.executable, "-m", "pip", "install", "git+https://github.com/Panniantong/Agent-Reach.git"], self.log)

        self.log("=== Installation complete ===")
        self.progress.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = InstallerApp(root)
    root.mainloop()
