---
name: free-llm-apis
description: "Curated list of free LLM APIs (OpenAI-compatible) with rate limits, providers, and setup guides. Use when user needs free LLM endpoints or wants to add free models to OpenCode."
---

# Free LLM APIs

Reference: https://github.com/mnfst/awesome-free-llm-apis

## Popular free providers
- Google Gemini (free tier)
- NVIDIA NIM (free models)
- Groq (free tier)
- OpenRouter (free models)
- DeepSeek (free credits)
- Mistral (free tier)

## How to add to OpenCode
Add a custom provider in `opencode.jsonc`:
```jsonc
{
  "providers": {
    "free-llm": {
      "name": "Free LLM",
      "env": ["FREE_LLM_API_KEY"],
      "package": "@opencode/ai/providers/openai-compatible",
      "settings": { "baseURL": "https://api.example.com/v1" },
      "models": { "model-id": { "name": "Model Name" } }
    }
  }
}
```

## Notes
- Rate limits apply.
- Some require API key (free signup).
- Check provider docs for model IDs.
