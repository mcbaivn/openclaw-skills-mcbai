---
name: youtube-trending-pro
clawhub_id: mcbaivn-youtube-trending-pro
description: Automate the full workflow of scanning trending videos, generating metadata, and downloading from YouTube. Manages the Checking-trending-youtube folder structure, calculates advanced Trending Score ((Views*0.6)+(Likes*0.3)+(Comments*0.1)), creates data.txt before downloading, saves videos as .webm. Use when user asks "Trending X Video @Channel" or needs to scan a list of channels.
---

# ≡ƒöÑ Youtube Trending Pro (OpenClaw)

Skill n├áy gi├║p ─Éß║íi ca Bß║▒ng tß╗▒ ─æß╗Öng h├│a to├án bß╗Ö quy tr├¼nh tß╗½ qu├⌐t k├¬nh ─æß║┐n tß║úi video v├á tß╗ò chß╗⌐c file khoa hß╗ìc.

> ≡ƒôª **Install:** `npx clawhub@latest install mcbaivn-youtube-trending-pro`

## C├ái ─æß║╖t

### C├ích 1 - Qua ClawHub (khuyß║┐n nghß╗ï)
```bash
npx clawhub@latest install mcbaivn-youtube-trending-pro
```

### C├ích 2 - Clone repo

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

## ≡ƒôä File metadata (data.txt)
ΓÜá∩╕Å Tß║ío file n├áy TR╞»ß╗ÜC khi tß║úi video.
Format mß╗ùi d├▓ng:
`Video_URL | Title | Description | Link thumbnail | Views | Likes | Comments | Trending_Score | Channel_url`
- **Trending_Score**: Chuß║⌐n h├│a theo thang ─æiß╗âm tß╗½ **1 ─æß║┐n 100**.

## ≡ƒôÑ Download video
- **Format**: `.webm`
- **Y├¬u cß║ºu**: Chß║Ñt l╞░ß╗úng tß╗æt (>= 720p), ╞░u ti├¬n nhß║╣ dung l╞░ß╗úng.
- **Tool**: `yt-dlp`

## ≡ƒôè B├ío c├ío & Cron (Tß╗▒ ─æß╗Öng)
- **Tß╗▒ ─æß╗Öng b├ío c├ío**: Mß╗ùi 3 ph├║t, ─æß╗ç sß║╜ gß╗¡i b├ío c├ío tiß║┐n ─æß╗Ö qua Telegram cho ─Éß║íi ca.
- **Tß╗▒ ─æß╗Öng tß║»t**: Sau khi gß╗¡i b├ío c├ío "HO├ÇN TH├ÇNH TO├ÇN Bß╗ÿ C├öNG VIß╗åC" duy nhß║Ñt mß╗Öt lß║ºn, hß╗ç thß╗æng sß║╜ tß╗▒ ─æß╗Öng x├│a lß╗çnh Cron job v├á dß╗½ng b├ío c├ío v─⌐nh viß╗àn ─æß╗â kh├┤ng l├ám phiß╗ün sß║┐p.
- **Nß╗Öi dung b├ío c├ío**:
  - T├¬n k├¬nh hiß╗çn tß║íi & sß╗æ thß╗⌐ tß╗▒ k├¬nh ─æang xß╗¡ l├╜.
  - Sß╗æ video ─æ├ú tß║úi xong / Tß╗òng sß╗æ.
  - Sß╗æ video c├▓n lß║íi.
  - Tß╗╖ lß╗ç ho├án th├ánh (%).
  - Video ─æang xß╗¡ l├╜ hiß╗çn tß║íi.
  - Tß╗▒ ─æß╗Öng tß║úi lß║íi nß║┐u gß║╖p lß╗ùi (Retry 3 lß║ºn).

## ≡ƒÜÇ C├ích sß╗¡ dß╗Ñng
Khi nhß║¡n ─æ╞░ß╗úc y├¬u cß║ºu "Trending X Video @Channel", h├úy sß╗¡ dß╗Ñng script `upgrade_scan.py` trong folder `Checking-trending-youtube`.

### C├║ ph├íp lß╗çnh:
`python Checking-trending-youtube/upgrade_scan.py <sß╗æ_l╞░ß╗úng> <url_k├¬nh1> [url_k├¬nh2] ...`

**V├¡ dß╗Ñ:**
- `Trending 10 Video @MrBeast`:
  `python Checking-trending-youtube/upgrade_scan.py 10 https://www.youtube.com/@MrBeast`
- `Trending 5 Video [ChannelA, ChannelB]`:
  `python Checking-trending-youtube/upgrade_scan.py 5 URL_A URL_B`

---
**L╞░u ├╜ cho ─Éß╗ç:** Lu├┤n ─æß║úm bß║úo `data.txt` ─æ╞░ß╗úc tß║ío tr╞░ß╗¢c khi bß║»t ─æß║ºu tß║úi video. Nß║┐u qu├í tr├¼nh tß║úi lß╗ùi, tß╗▒ ─æß╗Öng retry tß╗æi ─æa 3 lß║ºn tr╞░ß╗¢c khi ─æ├ính dß║Ñu l├á lß╗ùi trong b├ío c├ío.
