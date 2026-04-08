---
name: subtitle-translator-mcbai
clawhub_id: mcbaivn-subtitle-translator
description: |
  Dịch file phụ đề SRT sang bất kỳ ngôn ngữ nào bằng AI.
  Xử lý phụ đề theo lô để xử lý file lớn hiệu quả, giữ nguyên định dạng SRT và timing,
  xuất ra file SRT mới đã dịch.
  Dùng khi user muốn dịch phụ đề, dịch file SRT, dịch phụ đề phim,
  hoặc yêu cầu chuyển đổi phụ đề sang ngôn ngữ khác.
  Kích hoạt với "dịch phụ đề", "translate subtitles", "dịch file srt",
  "translate srt", "dịch sang tiếng Việt", hoặc khi user tải lên/paste file SRT và yêu cầu dịch.
---

# 🌐 Subtitle Translator - MCB AI

> 📦 **Install:** `npx clawhub@latest install mcbaivn-subtitle-translator`

Dịch file SRT sang bất kỳ ngôn ngữ nào. Xử lý theo lô (batch), giữ nguyên format và timing SRT, xuất file SRT mới.

## Cài đặt

```bash
npx clawhub@latest install mcbaivn-subtitle-translator
```

## Cách dùng

```
Dịch file phụ đề này sang tiếng Việt: [đường dẫn file .srt]
Translate this subtitle to English: [path/to/file.srt]
```

Hoặc paste nội dung SRT trực tiếp vào chat và yêu cầu dịch.

## Tùy chọn

| Tham số | Mặc định | Mô tả |
|---------|---------|-------|
| Ngôn ngữ dịch | Vietnamese | Bất kỳ ngôn ngữ nào |
| Batch size | 50 dòng | Số dòng mỗi lần gọi AI |
| Output | Cùng thư mục + `_vi` | Tên file output |

## Workflow

1. **Parse** file SRT (tự detect encoding: UTF-8, GBK, Shift-JIS, v.v.)
2. **Chia batch** - mỗi batch 50 dòng, dịch tuần tự
3. **Build** - ghép lại thành file SRT chuẩn với timecode gốc
4. **Xuất** file `[tên gốc]_[lang].srt`

## Lưu ý
- Giữ nguyên toàn bộ timecode gốc
- HTML tags (`<i>`, `<b>`) được giữ nguyên, chỉ dịch text bên trong
- File lớn (>500 dòng): báo ước tính thời gian trước khi chạy
