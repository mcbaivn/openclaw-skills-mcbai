---
name: youtube-scheduler
clawhub_id: mcbaivn-youtube-scheduler
description: |
  Phân tích lịch đăng video của kênh YouTube để tìm "khung giờ vàng" —
  thời điểm đăng có nhiều view và engagement nhất.
  Dùng khi user yêu cầu "Tìm giờ vàng đăng video @Channel",
  "Best time to post for @Channel", "Kênh này hay đăng lúc mấy giờ",
  hoặc muốn tối ưu lịch đăng nội dung.
---

# ⏰ YouTube Scheduler Analyzer

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-scheduler`

Phân tích lịch đăng của kênh → tìm ngày và giờ có hiệu suất cao nhất.

## Cài đặt

```bash
npx clawhub@latest install mcbaivn-youtube-scheduler
```

## Sử dụng

```
python scripts/analyze_schedule.py <channel_url> [--limit N] [--tz Asia/Ho_Chi_Minh]
```

**Ví dụ:**
- `Tìm giờ vàng @MrBeast` → `python scripts/analyze_schedule.py https://youtube.com/@MrBeast --limit 50`
- Đổi timezone → thêm `--tz Asia/Ho_Chi_Minh` (mặc định UTC)

## Output

```
Youtube_Schedule/
└── [Channel]_schedule_DD_MM_YYYY.txt
```

**Báo cáo gồm:**
- 📅 Ngày trong tuần tốt nhất (sắp xếp theo avg views)
- ⏰ Khung giờ vàng (0-23h, theo avg views)
- 🗓️ Heatmap Ngày × Giờ (ASCII)
- 🏆 Top 5 video views cao nhất với ngày/giờ đăng
- 💡 Khuyến nghị lịch đăng tối ưu

## Lưu ý
- Phân tích dựa trên `--limit` video gần nhất (khuyến nghị 30-100 video).
- Mặc định timezone UTC, dùng `--tz` để chuyển sang giờ địa phương.
- Kết quả là ước tính thống kê từ dữ liệu lịch sử, không phải đảm bảo tuyệt đối.
