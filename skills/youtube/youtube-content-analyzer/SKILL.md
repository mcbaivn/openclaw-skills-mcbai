---
name: youtube-content-analyzer
clawhub_id: mcbaivn-youtube-content-analyzer
description: Phân tích nội dung video YouTube từ file SRT/VTT/TXT hoặc URL trực tiếp. Tóm tắt nội dung, extract key points, phân tích chủ đề chính, tạo báo cáo. Dùng khi user yêu cầu "Tóm tắt video X", "Analyze content từ SRT", "Key points từ [URL]", "Đọc nội dung video mà không cần xem", hoặc cần hiểu nhanh nội dung hàng loạt video.
---

# 🤖 YouTube Content Analyzer

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-content-analyzer`

Đọc phụ đề → tóm tắt nội dung, key points, phân tích chủ đề. Không cần xem video.

## Cài đặt

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-content-analyzer`

### Cách 1 — Tải skill thẳng từ GitHub (khuyến nghị)

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-content-analyzer`

```powershell
# Windows

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-content-analyzer`
$skillDir = "$env:USERPROFILE\.agents\skills\youtube-content-analyzer"
New-Item -ItemType Directory -Force $skillDir | Out-Null
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai/main/skills/youtube/youtube-content-analyzer/SKILL.md" -OutFile "$skillDir\SKILL.md"
New-Item -ItemType Directory -Force "$skillDir\scripts" | Out-Null
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai/main/skills/youtube/youtube-content-analyzer/scripts/analyze_content.py" -OutFile "$skillDir\scripts\analyze_content.py"
```

```bash
# macOS / Linux

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-content-analyzer`
mkdir -p ~/.agents/skills/youtube-content-analyzer/scripts
curl -o ~/.agents/skills/youtube-content-analyzer/SKILL.md \
  https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai/main/skills/youtube/youtube-content-analyzer/SKILL.md
curl -o ~/.agents/skills/youtube-content-analyzer/scripts/analyze_content.py \
  https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai/main/skills/youtube/youtube-content-analyzer/scripts/analyze_content.py
```

### Cách 2 — Clone toàn bộ repo

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-content-analyzer`

```powershell
# Windows

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-content-analyzer`
git clone https://github.com/mcbaivn/openclaw-skills-mcbai.git
Copy-Item -Recurse openclaw-skills-mcbai\skills\youtube\youtube-content-analyzer $env:USERPROFILE\.agents\skills\
```

```bash
# macOS / Linux

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-content-analyzer`
git clone https://github.com/mcbaivn/openclaw-skills-mcbai.git
cp -r openclaw-skills-mcbai/skills/youtube/youtube-content-analyzer ~/.agents/skills/
```

## Workflow

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-content-analyzer`

**Cách 1 - Từ file SRT/TXT có sẵn:**
```
python scripts/analyze_content.py --file path/to/subtitle.srt
```

**Cách 2 - Từ URL (tự tải subtitle rồi phân tích):**
```
python scripts/analyze_content.py --url https://youtu.be/xxxx [--lang vi]
```

**Cách 3 - Phân tích hàng loạt:**
```
python scripts/analyze_content.py --folder Youtube_Subtitles/ChannelName/
```

## Output

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-content-analyzer`

```
Youtube_Analysis/
└── [Video_Title]_analysis_DD_MM_YYYY.txt
```

**Mỗi file analysis gồm:**
- 📝 **Tóm tắt** (3-5 câu)
- 🔑 **Key Points** (bullet list)
- 🏷️ **Chủ đề chính** (tags)
- 💬 **Quotes đáng chú ý**
- 📊 **Thống kê**: độ dài, ngôn ngữ, mật độ thông tin

## Lưu ý

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-content-analyzer`
- Với video dài (>30 phút), script chia nhỏ thành chunks trước khi phân tích.
- Kết hợp với `youtube-subtitle-extractor` để có pipeline đầy đủ.
