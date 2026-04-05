import sys, json
sys.stdout.reconfigure(encoding='utf-8')
with open(r'C:\Users\PCM\.openclaw\workspace\srt_parsed.json', encoding='utf-8') as f:
    data = json.load(f)
for item in data:
    print(str(item["id"]) + "|" + item["text"])
