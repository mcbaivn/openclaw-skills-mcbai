import sys, json
sys.stdout.reconfigure(encoding='utf-8')
with open(r'C:\Users\PCM\.openclaw\workspace\srt_parsed.json', encoding='utf-8') as f:
    data = json.load(f)

# Write to a new file with proper encoding
with open(r'C:\Users\PCM\.openclaw\workspace\srt_texts.txt', 'w', encoding='utf-8') as f:
    for item in data:
        f.write(str(item["id"]) + "|" + item["text"] + "\n")

print("Done:", len(data), "lines")
