---
name: youtube-trending-pro
clawhub_id: mcbaivn-youtube-trending-pro
description: Automate the full workflow of scanning trending videos, generating metadata, and downloading from YouTube. Manages the Checking-trending-youtube folder structure, calculates advanced Trending Score ((Views*0.6)+(Likes*0.3)+(Comments*0.1)), creates data.txt before downloading, saves videos as .webm. Use when user asks "Trending X Video @Channel" or needs to scan a list of channels.
---

# 🔥 Youtube Trending Pro (OpenClaw)

Skill này giúp Đại ca Bằng tự động hóa toàn bộ quy trình từ quét kênh đến tải video và tổ chức file khoa học.

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-trending-pro`

## Cài đặt

### Cách 1 - Qua ClawHub (khuyến nghị)
```bash
npx clawhub@latest install mcbaivn-youtube-trending-pro
```

### Cách 2 - Clone repo

```powershell
# Windows
git clone https://github.com/mcbaivn/openclaw-skills-mcbai.git
Copy-Item -Recurse openclaw-skills-mcbai\skills\youtube\youtube-trending-pro $env:USERPROFILE\.agents\skills\
```

```bash
# macOS / Linux
git clone https://github.com/mcbaivn/openclaw-skills-mcbai.git
cp -r openclaw-skills-mcbai/skills/youtube/youtube-trending-pro ~/.agents/skills/
```

## 📄 File metadata (data.txt)
⚠️ Tạo file này TRƯỚC khi tải video.
Format mỗi dòng:
`Video_URL | Title | Description | Link thumbnail | Views | Likes | Comments | Trending_Score | Channel_url`
- **Trending_Score**: Chuẩn hóa theo thang điểm từ **1 đến 100**.

## 📥 Download video
- **Format**: `.webm`
- **Yêu cầu**: Chất lượng tốt (>= 720p), ưu tiên nhẹ dung lượng.
- **Tool**: `yt-dlp`

## 📊 Báo cáo & Cron (Tự động)
- **Tự động báo cáo**: Mỗi 3 phút, đệ sẽ gửi báo cáo tiến độ qua Telegram cho Đại ca.
- **Tự động tắt**: Sau khi gửi báo cáo "HOÀN THÀNH TOÀN BỘ CÔNG VIỆC" duy nhất một lần, hệ thống sẽ tự động xóa lệnh Cron job và dừng báo cáo vĩnh viễn để không làm phiền sếp.
- **Nội dung báo cáo**:
  - Tên kênh hiện tại & số thứ tự kênh đang xử lý.
  - Số video đã tải xong / Tổng số.
  - Số video còn lại.
  - Tỷ lệ hoàn thành (%).
  - Video đang xử lý hiện tại.
  - Tự động tải lại nếu gặp lỗi (Retry 3 lần).

## 🚀 Cách sử dụng
Khi nhận được yêu cầu "Trending X Video @Channel", hãy sử dụng script `upgrade_scan.py` trong folder `Checking-trending-youtube`.

### Cú pháp lệnh:
`python Checking-trending-youtube/upgrade_scan.py <số_lượng> <url_kênh1> [url_kênh2] ...`

**Ví dụ:**
- `Trending 10 Video @MrBeast`:
  `python Checking-trending-youtube/upgrade_scan.py 10 https://www.youtube.com/@MrBeast`
- `Trending 5 Video [ChannelA, ChannelB]`:
  `python Checking-trending-youtube/upgrade_scan.py 5 URL_A URL_B`

---
**Lưu ý cho Đệ:** Luôn đảm bảo `data.txt` được tạo trước khi bắt đầu tải video. Nếu quá trình tải lỗi, tự động retry tối đa 3 lần trước khi đánh dấu là lỗi trong báo cáo.
