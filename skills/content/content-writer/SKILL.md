---
name: content-writer
description: Generate high-quality LinkedIn posts from research articles and source data. Supports 4 content formats (Toplist, POV, Case Study, How-to), multiple tones (default, bold, educational, storytelling, analytical, custom), 3 lengths (short/medium/long), and 2 languages (English/Vietnamese). Use this skill whenever the user wants to write LinkedIn content, create social media posts, draft professional content from research data, generate content in toplist/POV/case-study/how-to format, or asks to "write a post", "create content", "draft a LinkedIn post", "generate a post from this article", or any content writing from source material.
---

# Content Writer Skill

Generate professional LinkedIn posts from research articles. This skill replicates a complete content writing pipeline — taking source articles and producing polished, data-driven LinkedIn posts in multiple formats.

## When to Use

- User has research articles and wants to create LinkedIn posts
- User wants to write a post in a specific format (toplist, POV, case study, how-to)
- User needs content generated from news/data sources
- User asks to "write a post" or "create content" from source material
- Works best after using the `content-research` skill to gather sources

## Core Workflow

### Step 1: Gather Inputs

Collect from the user (ask if not provided):

1. **Source articles** (required) — at minimum: title, source, date, summary
2. **Content format** (default: toplist) — one of 4 formats below
3. **Tone** (default: default) — see Tone Presets
4. **Length** (default: medium) — short/medium/long
5. **Language** (default: en) — English or Vietnamese
6. **Number of posts** (default: 1) — how many posts to generate (max = number of articles)

### Step 2: Select Format

Read the appropriate format reference file for detailed prompt instructions:

| Format | File | Best For |
|--------|------|----------|
| 📋 Toplist | `references/format-toplist.md` | Numbered lists with data points |
| 💡 POV | `references/format-pov.md` | Bold opinions backed by data |
| 🏢 Case Study | `references/format-case-study.md` | Deep-dive on one company |
| 🛠️ How-to | `references/format-how-to.md` | Step-by-step actionable guides |

### Step 3: Build the Prompt

Combine these components (read `references/brand-context.md` for the full brand context):

1. **Brand context** — MCB AI (mcbai.vn) writing style and rules
2. **Task description** — format-specific instructions
3. **Source articles** — all selected articles as context, with one primary
4. **Tone instructions** — from tone preset or custom
5. **Language instructions** — English or Vietnamese
6. **Length constraints** — word count targets
7. **Multi-post note** — if generating multiple posts, each must have unique angle

### Step 4: Generate Content

Write the post following the format structure exactly. The output must be:
- **Plain text only** — LinkedIn does not render markdown
- **ZERO asterisks** — no `*`, no `**`, no markdown bold/italic
- **No em dashes** (—) — use hyphens (-) or commas instead
- **No source URLs** in the post body
- **No markdown formatting** of any kind (#, [], (), etc.)
- **Short paragraphs** — 1-2 sentences max per paragraph
- **Data-driven** — every claim backed by specific numbers

### Step 5: Present and Refine

Present the generated post(s) and offer:
- Copy as plain text
- Regenerate with different format/tone/length
- Edit specific sections
- Generate additional posts from remaining articles

## Format Structures

### Toplist Format
```
HOOK (1-2 lines): Bold claim + specific number
CONTEXT (2-3 lines): Why this matters now
NUMBERED LIST: Each item → key detail + metric
TAKEAWAY (2-3 lines): Pattern that emerges
CTA: Engagement question or soft MCB AI mention
```

### POV Format
```
HOOK (1-2 lines): Contrarian bold opening
DATA (3-5 lines): Evidence with numbers, companies, dollars
ANALYSIS (3-5 lines): What this means, connect dots
PREDICTION (2-3 lines): Clear position, don't hedge
CTA: Provocative question to drive comments
```

### Case Study Format
```
HOOK (1-2 lines): Most impressive metric/outcome
CONTEXT (2-3 lines): Problem that existed
WHAT THEY DID (3-5 lines): Specific strategy, names, numbers
RESULTS (2-3 lines): Concrete outcomes
LESSON (2-3 lines): Non-obvious takeaway
CTA: Engagement question or soft MCB AI mention
```

### How-to Format
```
HOOK (1-2 lines): Promise clear outcome
WHY (2-3 lines): Why it matters, what people get wrong
STEPS (3-7 numbered): Action verb + why it works + tool/example
PRO TIP (1-2 lines): Non-obvious shortcut
RESULT (1-2 lines): What they'll achieve
CTA: "Try step 1 today" or engagement question
```

## Length Guidelines

| Length | Word Count | Character Count | Description |
|--------|-----------|----------------|-------------|
| Short | 80-150 words | ~500-800 chars | Concise, punchy. Every word earns its place. |
| Medium | 150-300 words | ~800-1800 chars | Standard LinkedIn post with substance. |
| Long | 400-700 words | ~2500-4500 chars | Article-length deep dive. Mini-article. |

## Tone Presets

Read `references/tone-presets.md` for full details. Quick reference:

| Tone | Style |
|------|-------|
| Default | Data-driven, confident, accessible |
| Bold | Provocative, contrarian, strong positions |
| Educational | Teacher mode, analogies, "here's why" |
| Storytelling | Narrative arc, scenes, emotional |
| Analytical | Research analyst, patterns, comparisons |
| Custom | User provides their own tone description |

## Reference Files

- `references/brand-context.md` — Full brand identity, writing rules, design system
- `references/format-toplist.md` — Toplist format detailed instructions
- `references/format-pov.md` — POV format detailed instructions
- `references/format-case-study.md` — Case Study format detailed instructions
- `references/format-how-to.md` — How-to format detailed instructions
- `references/tone-presets.md` — All tone preset details and custom tone handling
- `references/formatting-rules.md` — Critical formatting constraints (MUST read)

## Critical Rules (Non-Negotiable)

These formatting rules are absolute and will cause output to be rejected if violated:

1. ABSOLUTELY NO asterisks (*) anywhere — not for bold, not for lists
2. ABSOLUTELY NO markdown formatting — no **, no *, no #, no [], no ()
3. ABSOLUTELY NO em dashes (—) — use hyphens or commas
4. ABSOLUTELY NO source citations or URLs in post text
5. Output MUST be plain text only
6. For emphasis, use CAPS for 1-2 key words: "This is the REAL opportunity."
7. For list items, use numbers (1. 2. 3.) or → arrows. Never asterisk bullets.
8. Emoji sparingly — max 2-3 per post, only for visual section breaks

