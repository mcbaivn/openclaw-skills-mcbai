---
name: youtube-channel-compare
clawhub_id: mcbaivn-youtube-channel-compare
description: |
  So sánh 2-5 kênh YouTube theo views, engagement rate, trending score và tần suất đăng bài.
  Dùng khi user hỏi "So sánh @KênhA vs @KênhB", "Kênh nào mạnh hơn trong niche X",
  hoặc cần dữ liệu phân tích cạnh tranh.
---

# 📊 YouTube Channel Compare

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-channel-compare`

So sánh hiệu suất của nhiều kênh YouTube và tạo báo cáo benchmark.

## Cài đặt

```bash
npx clawhub@latest install mcbaivn-youtube-channel-compare
```

## Sử dụng

```bash
python scripts/compare_channels.py <url1> <url2> [url3...] [--limit N]
```

**Ví dụ:**
- `So sánh @MrBeast vs @PewDiePie`
  → `python scripts/compare_channels.py https://youtube.com/@MrBeast https://youtube.com/@PewDiePie --limit 20`

## Output

```
Youtube_Compare/
└── compare_[Kênh1]_vs_[Kênh2]_DD_MM_YYYY.txt
```

**Báo cáo gồm:**

| Chỉ số | Kênh A | Kênh B |
|--------|--------|--------|
| Avg Views | ... | ... |
| Avg Likes | ... | ... |
| Avg Comments | ... | ... |
| Trending Score | ... | ... |
| Tần suất đăng | ... | ... |
| Engagement Rate | ... | ... |

**Trending Score**: `(Views × 0.6) + (Likes × 0.3) + (Comments × 0.1)` chuẩn hóa 1-100

## Lưu ý
- Mặc định lấy 20 video gần nhất mỗi kênh (dùng `--limit` để thay đổi).
- Kênh không có stats công khai sẽ hiển thị N/A.
