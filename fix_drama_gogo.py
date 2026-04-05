
import pandas as pd
import subprocess
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def get_video_summary(url):
    cmd = ["yt-dlp", "--get-description", "--no-warnings", url]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        desc = res.stdout.strip()
        return f"Tóm tắt: {desc[:250]}..." if desc else "Không có mô tả."
    except:
        return "Lỗi lấy dữ liệu."

def main():
    target = r'Youtube_Master_Geting_Info\DramaGo-Go\Youtube_Data_Summary_23_3_2026.xlsx'
    if not os.path.exists(target): return
    
    print(f"[*] Xử lý nốt DramaGo-Go...")
    df = pd.read_excel(target)
    for index, row in df.iterrows():
        if row.get('Summary') == '[NEED_AGENT_SUMMARY]':
            df.at[index, 'Summary'] = get_video_summary(row['Video_URL'])
            if (index + 1) % 10 == 0: print(f"✅ Đã xong {index+1}/100")
            
    df.to_excel(target, index=False)
    print("--- HOÀN THÀNH DRAMAGO-GO ---")

if __name__ == "__main__":
    main()
