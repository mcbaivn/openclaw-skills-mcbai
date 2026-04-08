import sys
import json
import subprocess
import os
import re
from datetime import datetime, timedelta

def get_video_info(url):
    cmd = ["yt-dlp", "-j", "--no-download", url]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        return json.loads(res.stdout)
    except:
        return None

def get_channel_videos(channel_url, count=10):
    # Lß║Ñy video trong 6 th├íng qua
    six_months_ago = (datetime.now() - timedelta(days=180)).strftime('%Y%m%d')
    # Flat playlist ─æß╗â lß║Ñy meta nhanh
    cmd = ["yt-dlp", "-j", "--flat-playlist", "--playlist-items", f"1:50", channel_url]
    
    videos = []
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        for line in res.stdout.strip().split('\n'):
            if not line: continue
            v = json.loads(line)
            videos.append(v)
    except:
        pass
    
    # Sß║»p xß║┐p theo view ─æß╗â lß║Ñy top
    videos.sort(key=lambda x: x.get('view_count') or 0, reverse=True)
    return videos[:count]

def calculate_score(views, comments, upload_date_str, coeff=10):
    try:
        upload_date = datetime.strptime(upload_date_str, '%Y%m%d')
        days = (datetime.now() - upload_date).days
        if days <= 0: days = 1
    except:
        days = 30 # Default
        
    score = (views / days) + (comments * coeff)
    return score, days

def main():
    if len(sys.argv) < 2:
        print("Usage: python scan_pro.py <channel_url> [count] [coeff]")
        return

    channel_url = sys.argv[1]
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    coeff = int(sys.argv[3]) if len(sys.argv) > 3 else 10

    print(f"--- ─Éang qu├⌐t k├¬nh: {channel_url} ---")
    videos = get_channel_videos(channel_url, count)
    
    report = []
    uploader = "Unknown"
    
    for v in videos:
        v_url = v.get('url') or f"https://www.youtube.com/watch?v={v.get('id')}"
        # Lß║Ñy meta chi tiß║┐t (comments)
        meta = get_video_info(v_url)
        if not meta: continue
        
        uploader = meta.get('uploader', uploader)
        views = meta.get('view_count') or 0
        comments = meta.get('comment_count') or 0
        upload_date = meta.get('upload_date')
        
        score, days = calculate_score(views, comments, upload_date, coeff)
        
        report.append({
            'title': meta.get('title'),
            'url': v_url,
            'views': views,
            'comments': comments,
            'days': days,
            'score': score
        })

    # Sort report by score
    report.sort(key=lambda x: x['score'], reverse=True)

    print(f"# ≡ƒôè TRENDING REPORT ΓÇô {uploader}")
    print("\n## ≡ƒÑç TOP VIDEOS\n")
    for i, item in enumerate(report):
        print(f"### {i+1}. {item['title']}")
        print(f"- ≡ƒöù Link: {item['url']}")
        print(f"- ≡ƒæü Views: {item['views']:,}")
        print(f"- ≡ƒÆ¼ Comments: {item['comments']:,}")
        print(f"- ≡ƒôà Days since publish: {item['days']}")
        print(f"- ≡ƒÜÇ Trending Score: {item['score']:,.0f}")
        print("\n---\n")

if __name__ == "__main__":
    main()
