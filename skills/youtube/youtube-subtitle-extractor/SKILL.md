---
name: youtube-subtitle-extractor
clawhub_id: mcbaivn-youtube-subtitle-extractor
description: |
  Tải phụ đề (SRT/VTT/TXT) từ video YouTube bằng yt-dlp.
  Hỗ trợ auto-generated và manual subtitles, đa ngôn ngữ.
  Dùng khi user yêu cầu "Tải phụ đề video X", "Get subtitles from [URL]",
  "Extract SRT from @Channel", hoặc cần file phụ đề để phân tích nội dung.
---

# 📥 YouTube Subtitle Extractor

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-subtitle-extractor`

Tải phụ đề từ video hoặc kênh YouTube, xuất ra file `.srt` sạch.

## Cài đặt

```bash
npx clawhub@latest install mcbaivn-youtube-subtitle-extractor
```

## Sử dụng

```bash
python scripts/extract_subtitles.py <video_or_channel_url> [--lang vi,en] [--format srt] [--auto]
```

**Ví dụ:**
- `Tải phụ đề từ https://youtu.be/xxxx`
  → `python scripts/extract_subtitles.py https://youtu.be/xxxx`
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
