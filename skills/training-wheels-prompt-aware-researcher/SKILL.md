---
name: training-wheels-prompt-aware-researcher
description: Use when you need to extract specific information from one or more URLs using the web_fetch tool. This skill ensures surgical, token-efficient extraction by crafting precise prompts.
---

# Prompt-Aware Researcher

## Overview
The `web_fetch` tool is most powerful when used with a specific `prompt`. Instead of fetching a full page and then processing it, providing a `prompt` allows the underlying system (or the tool's implementation) to extract and summarize only the relevant data. This saves significant context/tokens and provides a cleaner result.

## When to Use
- You need specific data from a webpage (e.g., "What is the latest version of Raylib?").
- You are researching a topic across multiple URLs.
- You have a strict token budget.
- You want a summarized or structured response directly from the tool.

## Core Pattern
Always use the `prompt` parameter in `web_fetch` to define exactly what you want to extract.

### Example: Surgical Extraction
**Task:** Get the latest Raylib version features.

**Surgical Approach:**
```json
{
  "prompt": "Extract a bulleted list of the new features in Raylib 5.5 from this page. Focus on API changes and new platforms."
}
```

**VS Vague Approach (Inefficient):**
```json
{
  "prompt": "Summarize this page."
}
```

## Implementation Checklist
1. **Identify the Target:** What specific piece of information do you need?
2. **Craft the Extraction Prompt:** Be explicit about the format (bullets, JSON, table) and the focus areas.
3. **Use multiple URLs:** If the tool supports it, pass several URLs with the same prompt to gather consolidated data.
4. **Verify the Output:** Check if the tool's summary meets your needs before requesting more context.

## Common Mistakes
- **Vague Prompts:** Asking for a "summary" when you want a "list of version numbers."
- **Fetching the whole page:** Thinking you need to see everything to find one thing.
- **Ignoring Tool Constraints:** Not specifying a format when a structured one is needed.

## Real-World Impact
- **Token Efficiency:** Reduces context usage by up to 90% by skipping navigation, ads, and irrelevant sections.
- **Speed:** Faster turns since the model receives a pre-processed summary.
