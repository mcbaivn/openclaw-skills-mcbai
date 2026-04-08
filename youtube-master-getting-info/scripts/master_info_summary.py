import sys
import json
import subprocess
import os
import re
from datetime import datetime
import pandas as pd

# Giả lập việc Agent gọi tool tóm tắt nội dung
def get_summary_from_agent(video_url, title):
    """
    Hàm này được thiết kế để Agent (đệ) can thiệp và cung cấp tóm tắt.
    Trong kịch bản thực tế, Agent sẽ thấy yêu cầu tóm tắt và thực hiện 
    qua browser hoặc các công cụ AI khác trước khi điền vào đây.
    """
    print(f"[*] Đang yêu cầu AI tóm tắt cho video: {title}...")
    # Vì script này chạy trong subprocess, nó không thể gọi trực tiếp tool của Agent.
    # Agent sẽ đọc file Excel sau khi tạo xong và điền nốt cột Summary
    # HOẶC script này sẽ để trống cột Summary để Agent xử lý sau.
    return "[ĐANG CHỜ AI TÓM TẮT]"

def get_channel_name(channel_url):
    name = None
    try:
        cmd = ["yt-dlp", "--print", "uploader", "--flat-playlist", "--playlist-items", "1", channel_url]
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
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

def get_video_meta(url):
    cmd = ["yt-dlp", "-j", "--no-download", url]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        return json.loads(res.stdout)
    except:
        return None

def main():
    if len(sys.argv) < 3:
        print("Usage: python master_info_summary.py <count> <url> [exclude_urls...]")
        return

    requested_count = int(sys.argv[1])
    channel_url = sys.argv[2]
    exclude_list = sys.argv[3:]
    
    base_dir = "Youtube_Master_Geting_Info"
    channel_name = get_channel_name(channel_url)
    channel_dir = os.path.join(base_dir, channel_name)
    os.makedirs(channel_dir, exist_ok=True)

    history_file = os.path.join(channel_dir, "history_urls.txt")
    existing_urls = set()
    if os.path.exists(history_file):
        with open(history_file, "r", encoding="utf-8") as f:
            for line in f:
                existing_urls.add(line.strip())
    
    for url in exclude_list:
        existing_urls.add(url.strip())

    print(f"--- Đang quét {channel_name} kèm TÓM TẮT NỘI DUNG (Xuất Excel) ---")
    cmd_list = ["yt-dlp", "-j", "--flat-playlist", "--playlist-items", "1:150", channel_url]
    raw_videos = []
    try:
        res = subprocess.run(cmd_list, capture_output=True, text=True, encoding='utf-8')
        for line in res.stdout.strip().split('\n'):
            if not line: continue
            raw_videos.append(json.loads(line))
    except:
        pass

    new_videos = []
    skipped_count = 0
    
    for v in raw_videos:
        v_url = v.get('webpage_url') or v.get('url') or f"https://www.youtube.com/watch?v={v.get('id')}"
        
        is_excluded = False
        for ex_url in existing_urls:
            if v.get('id') in ex_url or ex_url in v_url:
                is_excluded = True
                break
        
        if is_excluded:
            skipped_count += 1
            continue
        
        meta = get_video_meta(v_url)
        if not meta: continue
        
        # Thêm bước tóm tắt - Agent sẽ xử lý phần này sau khi script tạo file
        new_videos.append({
            'Video_URL': v_url,
            'Title': meta.get('title', 'N/A'),
            'Description': meta.get('description', 'N/A').replace('\n', ' ')[:500],
            'Summary': '[NEED_AGENT_SUMMARY]', # Placeholder cho Agent điền vào
            'Thumbnail': meta.get('thumbnail', 'N/A'),
            'Channel_URL': channel_url
        })
        
        print(f"✅ Đã bốc & Chuẩn bị tóm tắt: {meta.get('title')[:40]}...")
        
        if len(new_videos) >= requested_count:
            break

    now = datetime.now()
    date_str = f"{now.day}_{now.month}_{now.year}"
    excel_file = f"Youtube_Data_Summary_{date_str}.xlsx"
    
    idx = 1
    while os.path.exists(os.path.join(channel_dir, excel_file)):
        excel_file = f"Youtube_Data_Summary_{date_str}_{idx}.xlsx"
        idx += 1

    output_path = os.path.join(channel_dir, excel_file)
    if new_videos:
        df = pd.DataFrame(new_videos)
        df.to_excel(output_path, index=False)
        
        with open(history_file, "a", encoding="utf-8") as f_hist:
            for v in new_videos:
                f_hist.write(f"{v['Video_URL']}\n")

    print(f"\n✅ Channel: {channel_name}")
    print(f"🆕 Collected: {len(new_videos)}")
    print(f"\n📁 File Excel (Chờ Agent điền Summary):")
    print(f"{output_path}")

if __name__ == "__main__":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    main()
