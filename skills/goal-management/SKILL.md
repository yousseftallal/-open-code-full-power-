---
name: goal-management
description: "Manage goals (big + small) for multi-agent tasks. Distribute sub-goals to agents, track progress, and ensure alignment. Use for complex projects with multiple steps."
---

# Goal Management (OpenCode)

## Overview
Use **claude-mem work_state** to track goals and sub-goals across agents.

## Big Goal
Define the overall objective (e.g., "Build a login page with auth").

## Small Goals (Sub-goals)
Break into tasks:
- Design UI (ui-designer)
- Implement frontend (frontend-dev)
- Implement backend (backend-dev)
- Security review (security-auditor)
- Final review (reviewer)

## Distribution
- Orchestrator assigns sub-goals to agents.
- Each agent reports progress via `work_state_write`.
- Orchestrator tracks completion.

## Workflow
1. **Set big goal:** `work_state_write(list="project", fields={"goal": "Build login page", "status": "active"})`
2. **Add sub-goals:** `work_state_write(list="project", fields={"sub1": {"task": "Design UI", "agent": "ui-designer", "status": "todo"}})`
3. **Agents update:** `work_state_write(list="project", fields={"sub1": {"status": "done"}})`
4. **Check progress:** `work_state_read(includeClosed=true)`

## Best Practices
- Keep sub-goals small and focused.
- Use claude-mem to persist goal state.
- Review before marking big goal done.