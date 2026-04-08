import sys
import json
import subprocess
import os
import re
from datetime import datetime
import pandas as pd

def get_channel_name(channel_url):
    name = None
    try:
        cmd = ["yt-dlp", "--print", "uploader", "--flat-playlist", "--playlist-items", "1", channel_url]
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
        name = res.stdout.strip()
    except:
        pass
    
    if not name or name == "NA" or name == "null":
        try:
            if '@' in channel_url:
                name = channel_url.split('@')[-1].split('/')[0]
            else:
                name = channel_url.split('/')[-1]
        except:
            name = "Unknown_Channel"
            
    return re.sub(r'[\\/*?:"<>|]', "", name)

def main():
    if len(sys.argv) < 3:
        print("Usage: python master_info.py <count> <url>")
        return

    requested_count = int(sys.argv[1])
    channel_url = sys.argv[2]
    
    base_dir = "Youtube_Master_Geting_Info"
    channel_name = get_channel_name(channel_url)
    channel_dir = os.path.join(base_dir, channel_name)
    os.makedirs(channel_dir, exist_ok=True)

    history_file = os.path.join(channel_dir, "history_urls.txt")
    
    print(f"--- ─Éang qu├⌐t {channel_name} (Sß╗¡ dß╗Ñng Flat-Playlist) ─æß╗â lß║Ñy {requested_count} video ---")
    
    # Sß╗¡ dß╗Ñng flat-playlist ─æß╗â lß║Ñy th├┤ng tin cß╗▒c nhanh m├á kh├┤ng bß╗ï YouTube chß║╖n
    cmd_list = [
        "yt-dlp", 
        "--flat-playlist", 
        "-j",
        "--playlist-items", f"1:{requested_count}", 
        channel_url
    ]
    
    new_videos = []
    try:
        res = subprocess.run(cmd_list, capture_output=True, text=True, encoding='utf-8', errors='replace')
        for line in res.stdout.strip().split('\n'):
            if not line: continue
            v = json.loads(line)
            v_url = v.get('webpage_url') or v.get('url') or f"https://www.youtube.com/watch?v={v.get('id')}"
            
            # Lß║Ñy th├┤ng tin tß╗½ flat playlist (nhanh, kh├┤ng cß║ºn fetch tß╗½ng video)
            new_videos.append({
                'Video_URL': v_url,
                'Title': v.get('title', 'N/A'),
                'Description': 'N/A (Flat-Playlist)', # Flat playlist kh├┤ng c├│ description
                'Thumbnail': v.get('thumbnails', [{}])[0].get('url', 'N/A'),
                'Channel_URL': channel_url
            })
            print(f"Γ£à ─É├ú bß╗æc: {v.get('title')[:40]}...")
    except Exception as e:
        print(f"Γ¥î Lß╗ùi: {str(e)}")

    now = datetime.now()
    date_str = f"{now.day}_{now.month}_{now.year}"
    excel_file = f"Youtube_Data_{date_str}.xlsx"
    
    idx = 1
    while os.path.exists(os.path.join(channel_dir, excel_file)):
        excel_file = f"Youtube_Data_{date_str}_{idx}.xlsx"
        idx += 1

    if new_videos:
        df = pd.DataFrame(new_videos)
        df.to_excel(os.path.join(channel_dir, excel_file), index=False)
        
        with open(history_file, "w", encoding="utf-8") as f_hist:
            for v in new_videos:
                f_hist.write(f"{v['Video_URL']}\n")

    print(f"\nΓ£à Channel: {channel_name}")
    print(f"≡ƒôè Requested: {requested_count} videos")
    print(f"≡ƒåò New videos collected: {len(new_videos)}")
    print(f"\n≡ƒôü Saved to Excel:")
    print(f"Youtube_Master_Geting_Info/{channel_name}/{excel_file}")

if __name__ == "__main__":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    main()
