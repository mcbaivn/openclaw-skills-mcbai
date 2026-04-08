---
name: youtube-subtitle-extractor
clawhub_id: mcbaivn-youtube-subtitle-extractor
description: Download subtitles (SRT/VTT/TXT) from YouTube videos using yt-dlp. Supports auto-generated and manual subtitles, multi-language. Use when user asks "Tải phụ đề video X", "Get subtitles from [URL]", "Extract SRT from @Channel", or needs subtitle files for content analysis.
---

# 📥 YouTube Subtitle Extractor

Tải phụ đề từ video hoặc kênh YouTube, xuất ra file `.srt` sạch.

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-subtitle-extractor`

## Cài đặt

### Cách 1 - Qua ClawHub (khuyến nghị)
```bash
npx clawhub@latest install mcbaivn-youtube-subtitle-extractor
```

### Cách 2 - Tải thẳng từ GitHub

```powershell
# Windows
$skillDir = "$env:USERPROFILE\.agents\skills\youtube-subtitle-extractor"
New-Item -ItemType Directory -Force "$skillDir\scripts" | Out-Null
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai/main/skills/youtube/youtube-subtitle-extractor/SKILL.md" -OutFile "$skillDir\SKILL.md"
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai/main/skills/youtube/youtube-subtitle-extractor/scripts/extract_subtitles.py" -OutFile "$skillDir\scripts\extract_subtitles.py"
```

```bash
# macOS / Linux
mkdir -p ~/.agents/skills/youtube-subtitle-extractor/scripts
curl -o ~/.agents/skills/youtube-subtitle-extractor/SKILL.md \
  https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai/main/skills/youtube/youtube-subtitle-extractor/SKILL.md
curl -o ~/.agents/skills/youtube-subtitle-extractor/scripts/extract_subtitles.py \
  https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai/main/skills/youtube/youtube-subtitle-extractor/scripts/extract_subtitles.py
```

### Cách 3 - Clone toàn bộ repo

```powershell
# Windows
git clone https://github.com/mcbaivn/openclaw-skills-mcbai.git
Copy-Item -Recurse openclaw-skills-mcbai\skills\youtube\youtube-subtitle-extractor $env:USERPROFILE\.agents\skills\
```

```bash
# macOS / Linux
git clone https://github.com/mcbaivn/openclaw-skills-mcbai.git
cp -r openclaw-skills-mcbai/skills/youtube/youtube-subtitle-extractor ~/.agents/skills/
```

## Sử dụng

```
python scripts/extract_subtitles.py <video_or_channel_url> [--lang vi,en] [--format srt] [--auto]
```

**Ví dụ:**
- `Tải phụ đề từ https://youtu.be/xxxx` → `python scripts/extract_subtitles.py https://youtu.be/xxxx`
- `Tải phụ đề tiếng Việt` → thêm `--lang vi`
- Chỉ lấy auto-generated → thêm `--auto`

## Output

```
Youtube_Subtitles/
└── [Video_Title]/
    ├── [title].vi.srt
    ├── [title].en.srt
    └── [title]_plain.txt    (plain text không có timestamp)
```

## Lưu ý
- Ưu tiên manual subtitles trước, fallback sang auto-generated nếu không có.
- File `_plain.txt` dùng để đưa vào `youtube-content-analyzer`.
- Nếu URL là kênh, tải phụ đề tất cả video trong kênh (giới hạn với `--limit N`).
