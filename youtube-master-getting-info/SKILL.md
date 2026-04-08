---
name: youtube-master-getting-info
clawhub_id: mcbaivn-youtube-master-getting-info
description: Access a YouTube channel, fetch latest X videos, auto-filter duplicates from previous runs based on saved file history. Export data to 2 separate files (video_url and metadata) using standard folder structure. Use when user asks "Get X videos from @Channel" or "Quét thông tin kênh".
---

# 🎯 Youtube Master Getting Info

Skill này giúp Đại ca Bằng thu thập thông tin video từ YouTube một cách chuyên nghiệp, có bộ lọc chống trùng lặp thông minh.

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-master-getting-info`

## Cài đặt

### Cách 1 - Qua ClawHub (khuyến nghị)
```bash
npx clawhub@latest install mcbaivn-youtube-master-getting-info
```

### Cách 2 - Clone repo

```powershell
# Windows
git clone https://github.com/mcbaivn/openclaw-skills-mcbai.git
Copy-Item -Recurse openclaw-skills-mcbai\skills\youtube\youtube-master-getting-info $env:USERPROFILE\.agents\skills\
```

```bash
# macOS / Linux
git clone https://github.com/mcbaivn/openclaw-skills-mcbai.git
cp -r openclaw-skills-mcbai/skills/youtube/youtube-master-getting-info ~/.agents/skills/
```

## 📊 Định dạng Output (Excel)
- **File Excel**: `Youtube_Data_D_M_Y.xlsx`
- **Các cột dữ liệu**:
  - `Video_URL`
  - `Title`
  - `Description`
  - `Thumbnail`
  - `Channel_URL`

## 🚀 Cách sử dụng
Khi nhận được yêu cầu "Get 30 videos from @Channel", đệ sẽ tự động quét và xuất file Excel.

### Cú pháp lệnh:
`python scripts/master_info.py <số_lượng> <url_kênh>`

**Ví dụ:**
- `Get 30 videos from https://www.youtube.com/@EvernovaDrama`:
  `python scripts/master_info.py 30 https://www.youtube.com/@EvernovaDrama`

## 📁 Cấu trúc Thư mục
```
Youtube_Master_Geting_Info/
└── [Tên_Kênh]/
    ├── video_url_22_3_2026.txt
    └── metadata_22_3_2026.txt
```

---
**Lưu ý cho Đệ:** Không bao giờ ghi đè (overwrite) file cũ. Nếu chạy nhiều lần trong ngày, hãy thêm số thứ tự vào tên file (ví dụ: `_1`, `_2`).
