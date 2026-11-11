---
name: multi-agent-collaboration
description: "Guide for running multiple OpenCode agents (2-3) on the same task: parallel execution, discussion, and collaborative implementation. Use when a task needs multiple perspectives or collaborative work."
---

# Multi-Agent Collaboration (OpenCode)

## Overview
OpenCode allows running **multiple agents on the same task** (not just one per specialty).  
Use this for complex tasks needing **discussion, review, and collaborative execution**.

## Patterns

### 1. Parallel Review (2-3 agents same task)
- Launch `reviewer`, `security-auditor`, `ui-designer` in parallel on the same change.
- Each provides independent feedback.
- Orchestrator synthesizes findings.

### 2. Discuss → Refine → Execute
- Launch `planner` + `ui-designer` + `frontend-dev` in parallel.
- Each proposes an approach.
- Orchestrator compares, picks best, then delegates implementation to `coder`.

### 3. Divide & Conquer (same task, split work)
- `frontend-dev` handles UI, `backend-dev` handles API, `security-auditor` reviews both.
- Run in parallel, then integrate.

### 4. Review Loop
- `coder` implements → `reviewer` reviews → `coder` fixes → `reviewer` re-reviews.

## How to request
> "Run reviewer + security-auditor + ui-designer in parallel on this change, then synthesize."

> "Have planner, frontend-dev, backend-dev discuss and implement a login page together."

## Best Practices
- Use **foreground** for dependent steps.
- Use **background** for independent parallel work.
- Persist intermediate results to `work/` files.
- Use claude-mem for durable notes.
- Keep tasks small to avoid context loss.

## Available Agents
orchestrator, planner, ui-designer, ux-researcher, frontend-dev, backend-dev, security-auditor, mcp-integrator, media-analyst, web-researcher, skill-scout, reviewer, coder, pentest-agent.

## Available Skills
accessibility, code-review, diagnosing-bugs, frontend-design, performance-optimization, playwright-best-practices, web-design-guidelines, multi-agent-harness, opencode-models-guide, etc.