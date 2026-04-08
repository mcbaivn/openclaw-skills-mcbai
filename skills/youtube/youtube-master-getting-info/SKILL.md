---
name: youtube-master-getting-info
clawhub_id: mcbaivn-youtube-master-getting-info
description: Access a YouTube channel, fetch latest X videos, auto-filter duplicates from previous runs based on saved file history. Export data to 2 separate files (video_url and metadata) using standard folder structure. Use when user asks "Get X videos from @Channel" or "Qu├⌐t th├┤ng tin k├¬nh".
---

# ≡ƒÄ» Youtube Master Getting Info

Skill n├áy gi├║p ─Éß║íi ca Bß║▒ng thu thß║¡p th├┤ng tin video tß╗½ YouTube mß╗Öt c├ích chuy├¬n nghiß╗çp, c├│ bß╗Ö lß╗ìc chß╗æng tr├╣ng lß║╖p th├┤ng minh.

> ≡ƒôª **Install:** `npx clawhub@latest install mcbaivn-youtube-master-getting-info`

## C├ái ─æß║╖t

### C├ích 1 - Qua ClawHub (khuyß║┐n nghß╗ï)
```bash
npx clawhub@latest install mcbaivn-youtube-master-getting-info
```

### C├ích 2 - Clone repo

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

## ≡ƒôè ─Éß╗ïnh dß║íng Output (Excel)
- **File Excel**: `Youtube_Data_D_M_Y.xlsx`
- **C├íc cß╗Öt dß╗» liß╗çu**:
  - `Video_URL`
  - `Title`
  - `Description`
  - `Thumbnail`
  - `Channel_URL`

## ≡ƒÜÇ C├ích sß╗¡ dß╗Ñng
Khi nhß║¡n ─æ╞░ß╗úc y├¬u cß║ºu "Get 30 videos from @Channel", ─æß╗ç sß║╜ tß╗▒ ─æß╗Öng qu├⌐t v├á xuß║Ñt file Excel.

### C├║ ph├íp lß╗çnh:
`python scripts/master_info.py <sß╗æ_l╞░ß╗úng> <url_k├¬nh>`

**V├¡ dß╗Ñ:**
- `Get 30 videos from https://www.youtube.com/@EvernovaDrama`:
  `python scripts/master_info.py 30 https://www.youtube.com/@EvernovaDrama`

## ≡ƒôü Cß║Ñu tr├║c Th╞░ mß╗Ñc
```
Youtube_Master_Geting_Info/
ΓööΓöÇΓöÇ [T├¬n_K├¬nh]/
    Γö£ΓöÇΓöÇ video_url_22_3_2026.txt
    ΓööΓöÇΓöÇ metadata_22_3_2026.txt
```

---
**L╞░u ├╜ cho ─Éß╗ç:** Kh├┤ng bao giß╗¥ ghi ─æ├¿ (overwrite) file c┼⌐. Nß║┐u chß║íy nhiß╗üu lß║ºn trong ng├áy, h├úy th├¬m sß╗æ thß╗⌐ tß╗▒ v├áo t├¬n file (v├¡ dß╗Ñ: `_1`, `_2`).
