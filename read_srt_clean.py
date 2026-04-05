import sys, json, re

# Force UTF-8 output
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

src = r'C:\Users\PCM\.openclaw\media\inbound\transcribe_video_1---4192f9a6-6ee7-4a06-9103-7ddee39a60fd'

with open(src, 'rb') as f:
    raw = f.read()

content = raw.decode('utf-8')
blocks = re.split(r'\n\s*\n', content.strip())

subtitles = []
for block in blocks:
    lines = block.strip().split('\n')
    if len(lines) < 3:
        continue
    try:
        sub_id = int(lines[0].strip())
        timecode = lines[1].strip()
        text = ' '.join(l.strip() for l in lines[2:] if l.strip())
        subtitles.append({"id": sub_id, "timecode": timecode, "text": text})
    except:
        pass

out = r'C:\Users\PCM\.openclaw\workspace\srt_clean.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(subtitles, f, ensure_ascii=False, indent=2)

print(f"Saved {len(subtitles)} subtitles to {out}")
for s in subtitles:
    print(f"{s['id']}. {s['text']}")
