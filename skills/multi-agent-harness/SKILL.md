---
name: multi-agent-harness
description: "Guide for using OpenCode multi-agent orchestration: parallel subagents, context persistence, and task distribution. Use when setting up or troubleshooting multi-agent workflows."
---

# Multi-Agent Harness (OpenCode)

## Overview
OpenCode supports **primary** (orchestrator) and **subagent** (specialists) agents.  
Subagents run in **child sessions** with fresh context. They can run **foreground** (blocking) or **background** (parallel).

## Best Practices
1. **Use foreground for dependent tasks** — waits for result, keeps in parent context.
2. **Use background for independent tasks** — launches all at once, collects results later.
3. **Persist intermediate results** — write to `work/plan.md`, `work/findings.md`, `work/done.md`.
4. **Use claude-mem** — save durable notes (`save_memory` / `observation_add`).
5. **Keep tasks small** — avoid context compaction.
6. **Preload context** — use `instructions` in `opencode.jsonc`.

## Agents (Joe Skills bundle)
- orchestrator (primary) — router
- planner, ui-designer, ux-researcher, frontend-dev, backend-dev, security-auditor, mcp-integrator, media-analyst, web-researcher, skill-scout, reviewer, coder, pentest-agent (subagents)

## Parallel Execution
Ask orchestrator:
> "Run ui-designer and frontend-dev in parallel to design+implement a navbar"

Orchestrator will use `subagent` with `background=true`.

## Context Persistence
- Write plans to `work/plan.md`.
- Agents read `work/plan.md` instead of re-scanning.
- Use claude-mem for cross-session memory.

## Troubleshooting
- **Re-reading files:** Use foreground + intermediate files.
- **Lost context:** Use claude-mem `save_memory`.
- **Slow sequential:** Ask for parallel execution explicitly.