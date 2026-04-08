---
name: content-writer
clawhub_id: mcbaivn-content-writer
description: |
  Tạo bài đăng mạng xã hội chất lượng cao từ bài viết nghiên cứu và dữ liệu nguồn.
  Hỗ trợ nhiều nền tảng (LinkedIn, Facebook, Twitter/X, TikTok, Threads),
  6 định dạng nội dung (Toplist, POV, Case Study, How-to, Story, Hook-List-CTA),
  nhiều tone giọng (mặc định, mạnh mẽ, giáo dục, kể chuyện, phân tích, viral, đồng cảm, tùy chỉnh),
  3 độ dài (ngắn/vừa/dài), 2 ngôn ngữ (Anh/Việt).
  Dùng khi user muốn viết bài, tạo nội dung mạng xã hội, soạn content từ dữ liệu nghiên cứu,
  hoặc yêu cầu "viết bài", "tạo nội dung", "draft a post", "viết post từ bài này".
---

# ✍️ Content Writer Skill

> 📦 **Install:** `npx clawhub@latest install mcbaivn-content-writer`

Generate professional social media posts from research articles. Supports LinkedIn, Facebook, Twitter/X, TikTok caption, Threads — taking source material and producing polished, platform-optimized posts.

## When to Use

- User has articles/data and wants to create social media posts
- User wants to write a post in a specific format
- User needs content for any platform: LinkedIn, Facebook, Twitter/X, TikTok, Threads
- Works best after using the `content-research` skill to gather sources

## Core Workflow

### Step 1: Gather Inputs

Collect from the user (ask if not provided):

1. **Source material** (required) — article, URL, summary, or raw data
2. **Platform** (default: LinkedIn) — LinkedIn / Facebook / Twitter/X / TikTok / Threads
3. **Content format** (default: toplist) — see 6 formats below
4. **Tone** (default: default) — see Tone Presets
5. **Length** (default: medium) — short/medium/long
6. **Language** (default: Vietnamese) — English or Vietnamese

### Step 2: Select Format

| Format | File | Best For |
|--------|------|----------|
| 📋 Toplist | `references/format-toplist.md` | Numbered lists with data |
| 💡 POV | `references/format-pov.md` | Bold opinions backed by data |
| 🔍 Case Study | `references/format-case-study.md` | Deep-dive one story |
| 🛠️ How-to | `references/format-how-to.md` | Step-by-step guides |
| 📖 Story | `references/format-story.md` | Narrative, emotional journey |
| 🔥 Hook-List-CTA | `references/format-hook-list-cta.md` | Facebook viral format |

### Step 3: Apply Platform Rules

Read `references/platform-rules.md` for platform-specific constraints:

| Platform | Max length | Style | Hashtag |
|----------|-----------|-------|---------|
| LinkedIn | 3,000 chars | Professional, data-driven | 3-5 tags |
| Facebook | 63,206 chars | Conversational, emotional | 0-3 tags |
| Twitter/X | 280 chars | Punchy, hook-heavy | 1-2 tags |
| TikTok | 2,200 chars | Casual, trendy, FOMO | 5-10 tags |
| Threads | 500 chars | Conversational, casual | 0-2 tags |

### Step 4: Generate Content

Output rules (non-negotiable):
- **Plain text only** — no markdown on social platforms
- **ZERO asterisks** — no `*`, no `**`
- **No em dashes** — use `-` or comma
- **No source URLs** in post body
- **Short paragraphs** — 1-2 sentences max
- **Data-driven** — every claim backed by numbers

## Reference Files

- `references/brand-context.md` — MCB AI brand identity + writing rules
- `references/format-*.md` — Format instructions for each type
- `references/tone-presets.md` — All tone details
- `references/platform-rules.md` — Platform-specific constraints
- `references/formatting-rules.md` — Critical formatting rules (MUST read)

## Critical Rules (Non-Negotiable)

1. ABSOLUTELY NO asterisks (*) anywhere
2. ABSOLUTELY NO markdown formatting
3. ABSOLUTELY NO em dashes
4. ABSOLUTELY NO source URLs in post
5. Output MUST be plain text only
6. Emphasis = CAPS on 1-2 words max
7. Lists = numbers or → arrows only
8. Emoji = natural, platform-appropriate
