# OpenClaw Skills - MCBAI

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

> **Bộ sưu tập Skills mở rộng cho OpenClaw** - được tuyển chọn và phát triển bởi [MCB AI](https://www.mcbai.vn)

> 🌍 **Phiên bản khác:** [🇺🇸 English Version](https://github.com/mcbaivn/openclaw-skills-mcbai-en)

---

## ⚡ Cài đặt Skills

### Cài từng skill (nhanh nhất, không cần git)

```bash
npx clawhub@latest install mcbaivn-download-aio
npx clawhub@latest install mcbaivn-subtitle-translator
npx clawhub@latest install mcbaivn-youtube-subtitle-extractor
npx clawhub@latest install mcbaivn-youtube-content-analyzer
npx clawhub@latest install mcbaivn-youtube-channel-compare
npx clawhub@latest install mcbaivn-youtube-scheduler
npx clawhub@latest install mcbaivn-facebook-page-manager
```

> Skills tự động tải vào `~/.agents/skills/` — không cần biết git hay cấu trúc repo.

### Cài tất cả cùng lúc

```bash
# macOS / Linux
git clone https://github.com/mcbaivn/openclaw-skills-mcbai.git && \
cp -r openclaw-skills-mcbai/skills/*/* ~/.agents/skills/
```

```powershell
# Windows
git clone https://github.com/mcbaivn/openclaw-skills-mcbai.git
Copy-Item -Recurse openclaw-skills-mcbai\skills\*\* $env:USERPROFILE\.agents\skills\
```

---

## Danh sách tất cả Skills

| Skill | Mô tả | Cài đặt | Category |
|-------|-------|---------|----------|
| [download-aio](skills/tien-ich/download-aio/) | Tải video/audio từ 1000+ nền tảng | `npx clawhub@latest install mcbaivn-download-aio` | 🔧 Tiện Ích |
| [subtitle-translator](skills/tien-ich/subtitle-translator/) | Dịch file SRT sang bất kỳ ngôn ngữ nào | `npx clawhub@latest install mcbaivn-subtitle-translator` | 🔧 Tiện Ích |
| [youtube-subtitle-extractor](skills/youtube/youtube-subtitle-extractor/) | Tải phụ đề SRT/VTT từ YouTube | `npx clawhub@latest install mcbaivn-youtube-subtitle-extractor` | 🎬 YouTube |
| [youtube-content-analyzer](skills/youtube/youtube-content-analyzer/) | Đọc SRT/TXT → tóm tắt, key points, tags, quotes | `npx clawhub@latest install mcbaivn-youtube-content-analyzer` | 🎬 YouTube |
| [youtube-channel-compare](skills/youtube/youtube-channel-compare/) | So sánh 2-5 kênh: views, engagement, trending score | `npx clawhub@latest install mcbaivn-youtube-channel-compare` | 🎬 YouTube |
| [youtube-scheduler](skills/youtube/youtube-scheduler/) | Tìm ngày/giờ vàng đăng video, heatmap ASCII | `npx clawhub@latest install mcbaivn-youtube-scheduler` | 🎬 YouTube |
| [facebook-page-manager](skills/social-media/facebook-page-manager/) | Đăng & quản lý nội dung Facebook Page tự động | `npx clawhub@latest install mcbaivn-facebook-page-manager` | 📱 Social Media |

> 🔄 Cập nhật thêm thường xuyên. **Star repo** để không bỏ lỡ!

---

## Skills theo Category

### 🔧 Tiện Ích

| Skill | Mô tả | Cài đặt |
|-------|-------|---------|
| [download-aio](skills/tien-ich/download-aio/) | Tải video/audio từ 1000+ nền tảng (YouTube, TikTok, Facebook...) | `npx clawhub@latest install mcbaivn-download-aio` |
| [subtitle-translator](skills/tien-ich/subtitle-translator/) | Dịch file SRT phụ đề, tự detect encoding, hỗ trợ mọi ngôn ngữ | `npx clawhub@latest install mcbaivn-subtitle-translator` |
| [youtube-subtitle-extractor](skills/youtube/youtube-subtitle-extractor/) | Tải phụ đề SRT/VTT/TXT từ YouTube (auto-generated + manual) | `npx clawhub@latest install mcbaivn-youtube-subtitle-extractor` |

---

### ✍️ Content

| Skill | Mô tả | Cài đặt |
|-------|-------|---------|
| [youtube-content-analyzer](skills/youtube/youtube-content-analyzer/) | Phân tích SRT/TXT → tóm tắt, key points, tags, quotes hay | `npx clawhub@latest install mcbaivn-youtube-content-analyzer` |

---

### 🎬 YouTube

> [→ Xem hướng dẫn chi tiết category YouTube](skills/youtube/README.md)

| Skill | Mô tả | Dùng khi nào | Cài đặt |
|-------|-------|--------------|---------|
| [youtube-subtitle-extractor](skills/youtube/youtube-subtitle-extractor/) | Tải phụ đề SRT/VTT từ YouTube | Cần file phụ đề để dịch hoặc phân tích | `npx clawhub@latest install mcbaivn-youtube-subtitle-extractor` |
| [youtube-content-analyzer](skills/youtube/youtube-content-analyzer/) | Đọc SRT/TXT → tóm tắt, key points, tags, quotes | Muốn hiểu nhanh nội dung video không cần xem | `npx clawhub@latest install mcbaivn-youtube-content-analyzer` |
| [youtube-channel-compare](skills/youtube/youtube-channel-compare/) | So sánh 2-5 kênh theo views, engagement, trending score | Nghiên cứu đối thủ, tìm kênh mạnh trong niche | `npx clawhub@latest install mcbaivn-youtube-channel-compare` |
| [youtube-scheduler](skills/youtube/youtube-scheduler/) | Phân tích lịch đăng → tìm khung giờ vàng + heatmap ASCII | Muốn tối ưu thời điểm đăng video | `npx clawhub@latest install mcbaivn-youtube-scheduler` |

**Pipeline gợi ý:**
```
youtube-subtitle-extractor → youtube-content-analyzer
youtube-channel-compare + youtube-scheduler → tối ưu lịch đăng
```

---

### 📊 Phân Tích

| Skill | Mô tả | Cài đặt |
|-------|-------|---------|
| [youtube-channel-compare](skills/youtube/youtube-channel-compare/) | So sánh metrics 2-5 kênh: views, likes, comments, trending score | `npx clawhub@latest install mcbaivn-youtube-channel-compare` |
| [youtube-scheduler](skills/youtube/youtube-scheduler/) | Heatmap ngày/giờ đăng video tối ưu dựa trên 50 video gần nhất | `npx clawhub@latest install mcbaivn-youtube-scheduler` |

---

### 📱 Social Media

| Skill | Mô tả | Cài đặt |
|-------|-------|---------|
| [facebook-page-manager](skills/social-media/facebook-page-manager/) | Đăng text/ảnh/video/Reels/Story, hẹn giờ, quản lý comment trên Facebook Page | `npx clawhub@latest install mcbaivn-facebook-page-manager` |

**Pipeline gợi ý:**
```
youtube-content-analyzer → facebook-page-manager (đăng + hẹn giờ)
```

---

## Cấu trúc repo

```
openclaw-skills-mcbai/
├── README.md
└── skills/
    ├── tien-ich/          🔧 Tiện Ích
    │   ├── download-aio/
    │   └── subtitle-translator/
    ├── youtube/           🎬 YouTube
    │   ├── README.md
    │   ├── youtube-subtitle-extractor/
    │   ├── youtube-content-analyzer/
    │   ├── youtube-channel-compare/
    │   └── youtube-scheduler/
    └── social-media/      📱 Social Media
        └── facebook-page-manager/
```

---

## Về MCB AI

| | |
|--|--|
| 🌐 Website | [mcbai.vn](https://www.mcbai.vn/) |
| 📘 Fanpage | [facebook.com/mcb.ai.vn](https://www.facebook.com/mcb.ai.vn/) |
| 🎬 YouTube | [youtube.com/@mcbaivn](https://www.youtube.com/@mcbaivn) |
| 🗒️ OpenClaw Cheatsheet | [openclaw.mcbai.vn](https://openclaw.mcbai.vn/) |
| 📚 Khóa học OpenClaw 101 | [openclaw.mcbai.vn/openclaw101](https://openclaw.mcbai.vn/openclaw101) |
| 💬 Cộng đồng Facebook | [OpenClaw AI Kiếm Cơm](https://www.facebook.com/groups/openclawxvn) |
| 🎓 MCB AI Academy (Zalo) | [zalo.me/g/mmqkhi259](https://zalo.me/g/mmqkhi259) |

---

## Đóng góp

Có skill hay muốn chia sẻ? Tạo Pull Request hoặc liên hệ qua Fanpage MCB AI.

---

<p align="center">Made with ❤️ by <a href="https://www.mcbai.vn">MCB AI</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/@mcbaivn">YouTube</a> &nbsp;·&nbsp; <a href="https://openclaw.mcbai.vn/openclaw101">Học OpenClaw 101</a> &nbsp;·&nbsp; <a href="https://zalo.me/g/mmqkhi259">MCB AI Academy</a></p>
