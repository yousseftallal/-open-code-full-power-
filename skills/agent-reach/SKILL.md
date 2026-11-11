---
name: agent-reach
description: "Give AI agents eyes to see the internet: search/read Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu, V2EX, Xueqiu, and more via CLI. Use when user asks to search/read social platforms, get transcripts, or gather web data."
---

# Agent Reach

CLI tool for searching and reading social platforms and web content.

## Setup
- Installed via: `pip install git+https://github.com/Panniantong/Agent-Reach.git`
- Run: `agent-reach channels` to see available channels.
- Run: `agent-reach <channel> <action> [args]` (e.g., `agent-reach bilibili search "大模型"`).
- Read by URL: `agent-reach read <url>`.

## Channels
bilibili, v2ex, github, youtube, web, xiaohongshu, xueqiu, boss, xiaoyuzhou, linkedin, reddit, twitter, facebook, instagram.

## Notes
- Read-only (no posting).
- Some channels require login (optional).
- Groq/OpenAI key needed for YouTube transcription (optional).
