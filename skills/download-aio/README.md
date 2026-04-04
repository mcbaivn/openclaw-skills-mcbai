# Tải video từ 1000+ nền tảng — YouTube, TikTok, Facebook, Instagram và hơn thế nữa

Skill **download-aio** cho [OpenClaw](https://openclaw.mcbai.vn/) sử dụng `yt-dlp` để tải video, audio, playlist, subtitle từ hầu hết các nền tảng video trên internet. Sau khi tải xong, tự động gửi file về Telegram nếu dung lượng <= 50MB.

## Tính năng

- Tải video (best quality hoặc chọn 1080p/720p/480p/360p)
- Tải audio only (mp3/m4a)
- Tải toàn bộ playlist
- Tải subtitle/phụ đề (tự động + chính thức)
- Tải thumbnail
- Auto gửi file về Telegram sau khi tải
- Script cài đặt tự động (Python, yt-dlp, ffmpeg)
- Hỗ trợ 1000+ nền tảng

## Nền tảng phổ biến

YouTube · TikTok · Facebook · Instagram · Twitter/X · Twitch · Vimeo · SoundCloud · Reddit · Bilibili · Dailymotion · và hơn 1000 trang khác

## Cài đặt

```powershell
# 1. Copy skill vào OpenClaw
Copy-Item -Recurse download-aio $env:USERPROFILE\.agents\skills\

# 2. Chạy script cài đặt tự động
powershell -ExecutionPolicy Bypass -File $env:USERPROFILE\.agents\skills\download-aio\scripts\install.ps1
```

## Cách dùng

Chỉ cần paste URL vào chat với OpenClaw agent:

```
https://www.youtube.com/watch?v=...
https://www.tiktok.com/@user/video/...
https://www.facebook.com/reel/...
```

Agent sẽ tự tải về + gửi file về Telegram.

---

**By [MCB AI](https://mcbai.vn)** · [OpenClaw Cheatsheet](https://openclaw.mcbai.vn/) · [Khoá học OpenClaw 101](https://openclaw.mcbai.vn/openclaw101)
