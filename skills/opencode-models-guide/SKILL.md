---
name: opencode-models-guide
description: "Guide for scanning OpenCode models and connecting free/paid providers. Use when user wants to choose models, connect providers, or configure multi-agent harness."
---

# OpenCode Models Guide

## Free Models (OpenCode provider)
| Model | Best Use |
|---|---|
| opencode/beam-free | Orchestrator (routing) |
| opencode/deepseek-v4.1-flash-free | Planning / reasoning |
| opencode/glm-5.3-flash-free | Coding / frontend |
| opencode/mimo-v2.6-flash-free | Review / text |
| opencode/minimax-m3.1-flash-free | Security / backend |
| opencode/longcat-2.5-free | Research / web |
| opencode/flint-40b-free | General (40B) |
| opencode/iceman-free | General |
| opencode/inkling-2-small-free | Quick tasks |
| opencode/nemotron-3.5-super-vl-free | Vision (VL) |

## Paid/Strong Models (OpenCode provider)
- opencode/gpt-5.5, gpt-5.5-pro, gpt-6-astra, gpt-6-luna, gpt-6.1-sol
- opencode/claude-opus-5, claude-opus-5-5, claude-sonnet-5, claude-sonnet-5-5
- opencode/gemini-3.1-pro, gemini-3.5-flash, gemini-3.7-flash
- opencode/glm-5.3, glm-5.2
- opencode/qwen3.6-plus, qwen3.8-flash
- opencode/deepseek-v4-pro
- opencode/mistral-large-4
- opencode/kimi-k3

## How to Connect
1. `/connect` → choose provider → enter credentials.
2. `/models` → select model.
3. Or configure in `opencode.jsonc`:
```jsonc
{
  "model": "provider/model-id",
  "providers": {
    "custom": {
      "name": "Custom",
      "env": ["CUSTOM_API_KEY"],
      "package": "@opencode/ai/providers/openai-compatible",
      "settings": { "baseURL": "https://api.example.com/v1" },
      "models": { "model-id": { "name": "Model Name" } }
    }
  }
}
```

## Multi-Agent Harness
- Orchestrator: opencode/beam-free (free) or opencode/gpt-5.5 (paid).
- Subagents: assign free/paid models per specialty.
- Use `default_agent` and `model` in config for auto-start.

## Tips
- Free models may have lower context/quality.
- Paid models better for complex reasoning.
- Use `/models` to switch at runtime.
- Use `opencode.models` tool to search exact IDs.