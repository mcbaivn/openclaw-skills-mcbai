import sys, json

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\PCM\.openclaw\workspace\srt_parsed.json', encoding='utf-8') as f:
    data = json.load(f)

# Print as JSON to stdout so it can be captured properly
texts = [{"id": item["id"], "text": item["text"]} for item in data]
print(json.dumps(texts, ensure_ascii=False, indent=2))
