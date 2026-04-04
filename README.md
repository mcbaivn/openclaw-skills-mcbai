# OpenClaw Skills — MCBAI

> **Bộ sưu tập Skills mở rộng cho OpenClaw** — được tuyển chọn và phát triển bởi [MCB AI](https://mcbai.vn)

Tất cả skills trong repo này đều plug-and-play: tải về, copy vào `~/.agents/skills/`, dùng ngay.

---

## Skills hiện có

| Skill | Mô tả | Nền tảng |
|-------|-------|----------|
| [download-aio](skills/download-aio/) | Tải video/audio từ 1000+ nền tảng (YouTube, TikTok, Facebook...) | Windows |

> Sẽ cập nhật thêm thường xuyên. Star repo để không bỏ lỡ 🌟

---

## Cách cài đặt

### Cài 1 skill cụ thể

```bash
# Clone repo
git clone https://github.com/mcb0809/openclaw-skills-mcbai.git

# Copy skill muốn dùng vào thư mục skills của OpenClaw
cp -r openclaw-skills-mcbai/skills/download-aio ~/.agents/skills/
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/mcb0809/openclaw-skills-mcbai.git
Copy-Item -Recurse openclaw-skills-mcbai\skills\download-aio $env:USERPROFILE\.agents\skills\
```

### Cài toàn bộ skills

```bash
git clone https://github.com/mcb0809/openclaw-skills-mcbai.git
cp -r openclaw-skills-mcbai/skills/* ~/.agents/skills/
```

---

## Cấu trúc repo

```
openclaw-skills-mcbai/
├── README.md
└── skills/
    ├── download-aio/          # Tải video từ 1000+ nền tảng
    │   ├── SKILL.md
    │   ├── scripts/
    │   │   ├── install.ps1    # Cài đặt tự động
    │   │   ├── check.ps1      # Kiểm tra dependencies
    │   │   └── find-python.ps1
    │   └── references/
    │       ├── commands.md    # Lệnh chi tiết
    │       ├── platforms.md   # Danh sách nền tảng
    │       └── troubleshooting.md
    └── (skills tiếp theo...)
```

---

## Về MCB AI

MCB AI là nền tảng AI content & marketing automation của người Việt, dành cho người Việt.

| | |
|--|--|
| 🌐 Website | [mcbai.vn](https://mcbai.vn) |
| 📘 Fanpage | [facebook.com/mcb.ai.vn](https://www.facebook.com/mcb.ai.vn/) |
| 🛠️ OpenClaw Cheatsheet | [openclaw.mcbai.vn](https://openclaw.mcbai.vn/) |
| 🎓 Khoá học OpenClaw 101 | [openclaw.mcbai.vn/openclaw101](https://openclaw.mcbai.vn/openclaw101) |
| 👥 Cộng đồng Facebook | [OpenClaw AI Kiếm Cơm](https://www.facebook.com/groups/openclawxvn) |

---

## Đóng góp

Có skill hay muốn chia sẻ? Tạo Pull Request hoặc liên hệ qua Fanpage MCB AI.

---

<p align="center">Made with ❤️ by <a href="https://mcbai.vn">MCB AI</a> · <a href="https://openclaw.mcbai.vn/openclaw101">Học OpenClaw 101</a></p>
