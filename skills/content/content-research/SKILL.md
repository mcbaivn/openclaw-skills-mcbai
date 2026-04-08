---
name: content-research
clawhub_id: mcbaivn-content-research
description: |
  Tìm kiếm và khám phá nguồn nội dung trending cho bất kỳ chủ đề nào bằng web search.
  Dùng khi user muốn tìm bài viết, tin tức, blog, hoặc nội dung trending về một chủ đề
  cụ thể để tạo content, viết bài LinkedIn, mạng xã hội, hoặc tổng hợp nội dung.
  Kích hoạt khi user đề cập "research chủ đề", "tìm bài viết về", "tin tức trending",
  "nguồn nội dung", "tìm kiếm content", hoặc muốn thu thập dữ liệu/nguồn trước khi viết bài.
---

# 🔍 Content Research Skill

> 📦 **Install:** `npx clawhub@latest install mcbaivn-content-research`

Search the web for trending articles, news, and content sources on any topic. This skill powers the MCB AI content research pipeline — finding, filtering, scoring, and organizing source material for content creation.

## Search Strategy: Brave + Tavily Dual-Engine

This skill uses TWO search providers in parallel for maximum coverage:

- **Brave Search** — via `web_search` tool (built-in OpenClaw tool)
- **Tavily** — via direct API call using `TAVILY_API_KEY` from `~/.openclaw/.env`

### Tavily API Call

```
POST https://api.tavily.com/search
Headers: Content-Type: application/json
Body:
{
  "api_key": "<TAVILY_API_KEY>",
  "query": "<query>",
  "search_depth": "advanced",
  "include_answer": false,
  "include_raw_content": false,
  "max_results": 10,
  "topic": "news"
}
```

Run Tavily via `exec` with PowerShell:
```powershell
$body = @{
  api_key = $env:TAVILY_API_KEY
  query = "<query>"
  search_depth = "advanced"
  include_answer = $false
  include_raw_content = $false
  max_results = 10
  topic = "news"
} | ConvertTo-Json

Invoke-RestMethod -Uri "https://api.tavily.com/search" -Method Post -ContentType "application/json" -Body $body
```

### Fallback Logic

- Run Brave (`web_search`) and Tavily in parallel
- If Brave fails → use Tavily results only
- If Tavily fails → use Brave results only
- If both succeed → merge and deduplicate by URL

## When to Use

- User wants to research a topic before writing content
- User needs to find recent articles, news, or data about a subject
- User wants to discover trending content sources for LinkedIn/social media
- User needs to curate sources for a toplist, POV, case study, or how-to post

## Core Workflow

### Step 1: Understand the Research Request

Extract from the user's message:
1. **Topic** — the subject to research (required)
2. **Source filter** — where to search (default: all sources)
3. **Freshness** — how recent (default: past month for web, past week for news)
4. **Count** — how many results to return (default: 10-15)

### Step 2: Execute Dual Search (Brave + Tavily)

Run BOTH providers. Each provider runs TWO queries when possible.

### Step 3: Merge and Deduplicate

1. Collect all results from Brave (web + news) and Tavily (general + news)
2. **Deduplicate** by URL — keep one copy per URL
3. **Sort** by relevance (news first, then by freshness)
4. **Limit** to requested count (default 15)
5. **Label source engine** in metadata

### Step 4: Process and Organize Results

For each result, extract and structure:
- Title, Source, URL, Date, Summary, Type, Tag, Engine

### Step 5: Present Results

Present organized results in a clear, scannable format. Then ask the user which articles they want to use for content creation.

## Integration with Content Writer

After research, pass selected articles to the content-writer skill.

See `references/source-filters.md` for detailed source filter configurations.
