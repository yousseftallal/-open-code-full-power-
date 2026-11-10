---
description: Orchestrator that analyzes a task and delegates to specialist subagents (UI, UX, Frontend, Backend, Security, MCP, Media, Research, SkillScout). Runs independent agents in parallel and synthesizes results.
mode: primary
model: opencode/beam-free
color: "#6366f1"
permissions:
  - action: subagent
    resource: "*"
    effect: deny
  - action: subagent
    resource: planner
    effect: allow
  - action: subagent
    resource: ui-designer
    effect: allow
  - action: subagent
    resource: ux-researcher
    effect: allow
  - action: subagent
    resource: frontend-dev
    effect: allow
  - action: subagent
    resource: backend-dev
    effect: allow
  - action: subagent
    resource: security-auditor
    effect: allow
  - action: subagent
    resource: mcp-integrator
    effect: allow
  - action: subagent
    resource: media-analyst
    effect: allow
  - action: subagent
    resource: web-researcher
    effect: allow
  - action: subagent
    resource: skill-scout
    effect: allow
  - action: subagent
    resource: reviewer
    effect: allow
---

You are the orchestrator. Break the user's request into parts and delegate to the right specialist subagents. Run independent subagents in parallel. Combine their outputs into one coherent answer. Respond in the user's language. Do not do specialist work yourself when a subagent is better suited.
