# content-writer — Viết LinkedIn post chuyên nghiệp từ nguồn bài

> Skill OpenClaw tạo LinkedIn post chất lượng cao từ bài nghiên cứu. Hỗ trợ **4 format, 6 tone, 2 ngôn ngữ**. Output plain text chuẩn LinkedIn — không markdown, không asterisk. Thường dùng sau `content-research`.

---

## Skill này dùng để làm gì?

Bạn có bài viết hay, data thú vị — nhưng không biết viết thành LinkedIn post thế nào cho cuốn? Skill này giúp bạn:
- Biến bất kỳ bài nghiên cứu nào thành LinkedIn post chuyên nghiệp
- Chọn format phù hợp: Toplist, POV, Case Study, How-to
- Điều chỉnh tone: mạnh bạo, giáo dục, kể chuyện, phân tích...
- Viết bằng tiếng Anh hoặc tiếng Việt
- Output chuẩn ngay — không cần chỉnh sửa thêm

---

## Tính năng

| Tính năng | Chi tiết |
|-----------|---------|
| 📋 4 Format | Toplist / POV / Case Study / How-to |
| 🎭 6 Tone | Default / Bold / Educational / Storytelling / Analytical / Custom |
| 📏 3 Độ dài | Short (80-150 từ) / Medium (150-300 từ) / Long (400-700 từ) |
| 🌐 2 Ngôn ngữ | Tiếng Anh / Tiếng Việt |
| ✅ Plain text | Output chuẩn LinkedIn — không markdown, không asterisk |
| 🔗 Tích hợp | Nhận nguồn bài trực tiếp từ `content-research` |

---

## Cài đặt

```powershell
# Windows
Copy-Item -Recurse content-writer $env:USERPROFILE\.agents\skills\

# macOS / Linux
cp -r content-writer ~/.agents/skills/
```

---

## Cách dùng

### Đơn giản nhất — paste bài và yêu cầu
```
Viết LinkedIn post từ bài này: [paste nội dung bài]
```

### Chỉ định format
```
Viết post format Toplist từ bài này: [URL hoặc nội dung]

Viết POV post bằng tiếng Việt, tone Bold, medium length
```

### Sau khi research xong
```
Dùng bài 1 và 3 để viết Case Study post, tiếng Việt, dài
```

---

## 4 Format có sẵn

### 📋 Toplist
Danh sách có số thứ tự với data points. Phù hợp khi có nhiều điểm muốn trình bày.
```
HOOK: Bold claim + số cụ thể
CONTEXT: Tại sao quan trọng
LIST: Mỗi item → chi tiết + metric
TAKEAWAY: Pattern rút ra
CTA: Câu hỏi engagement
```

### 💡 POV
Quan điểm táo bạo có data hỗ trợ. Phù hợp khi muốn tạo tranh luận.
```
HOOK: Contrarian opening
DATA: Bằng chứng với số liệu
ANALYSIS: Ý nghĩa
PREDICTION: Dự đoán rõ ràng
CTA: Câu hỏi kích comment
```

### 🏢 Case Study
Deep-dive một công ty/dự án cụ thể. Phù hợp khi có câu chuyện thực tế.
```
HOOK: Metric/outcome ấn tượng nhất
CONTEXT: Vấn đề ban đầu
WHAT THEY DID: Chiến lược + số liệu
RESULTS: Kết quả cụ thể
LESSON: Bài học không ai nói
CTA: Câu hỏi hoặc MCB AI mention
```

### 🛠️ How-to
Hướng dẫn từng bước có thể làm ngay. Phù hợp khi muốn giáo dục.
```
HOOK: Hứa hẹn kết quả rõ ràng
WHY: Tại sao quan trọng
STEPS: 3-7 bước có thể hành động
PRO TIP: Shortcut không ai biết
RESULT: Họ sẽ đạt được gì
CTA: "Thử bước 1 ngay hôm nay"
```

---

## 6 Tone có sẵn

| Tone | Phong cách |
|------|-----------|
| Default | Data-driven, tự tin, dễ tiếp cận |
| Bold | Táo bạo, contrarian, lập trường mạnh |
| Educational | Dạy học, dùng ví dụ, giải thích rõ |
| Storytelling | Kể chuyện, có cảm xúc, narrative arc |
| Analytical | Phân tích, so sánh, pattern recognition |
| Custom | Bạn tự mô tả tone muốn dùng |

---

## Quy tắc output (Critical)

Output luôn là plain text chuẩn LinkedIn:
- Không asterisk (`*`) — không bao giờ
- Không markdown (`**`, `#`, `[]`)
- Không em dash (`—`) — dùng `-` hoặc dấu phẩy
- Không URL trong bài
- Nhấn mạnh bằng CAPS: `"Đây là CƠ HỘI thực sự"`
- List dùng số (`1. 2. 3.`) hoặc mũi tên (`→`)
- Emoji tối đa 2-3 cái, chỉ để ngắt đoạn

---

## Cấu trúc files

```
content-writer/
├── README.md                    ← Bạn đang đọc
├── SKILL.md                     ← Điều khiển agent
└── references/
    ├── brand-context.md         ← Brand identity MCB AI
    ├── format-toplist.md        ← Hướng dẫn format Toplist
    ├── format-pov.md            ← Hướng dẫn format POV
    ├── format-case-study.md     ← Hướng dẫn format Case Study
    ├── format-how-to.md         ← Hướng dẫn format How-to
    ├── tone-presets.md          ← Chi tiết các tone preset
    └── formatting-rules.md     ← Quy tắc formatting bắt buộc
```

---

<p align="center">
  <a href="https://www.mcbai.vn">MCB AI</a> &nbsp;·&nbsp;
  <a href="https://www.youtube.com/@mcbaivn">YouTube</a> &nbsp;·&nbsp;
  <a href="https://openclaw.mcbai.vn">OpenClaw Cheatsheet</a> &nbsp;·&nbsp;
  <a href="https://openclaw.mcbai.vn/openclaw101">Khoá học OpenClaw 101</a> &nbsp;·&nbsp;
  <a href="https://www.facebook.com/groups/openclawxvn">Cộng đồng Facebook</a> &nbsp;·&nbsp;
  <a href="https://zalo.me/g/mmqkhi259">MCB AI Academy (Zalo)</a>
</p>
