
import pandas as pd
import subprocess
import os
import sys
import io
import glob

# Ensure output UTF-8 for console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def get_video_summary(url):
    """Fetch description and simulate summary."""
    cmd = ["yt-dlp", "--get-description", "--no-warnings", url]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        desc = res.stdout.strip()
        if not desc:
            return "Không có mô tả video."
        # Short summary
        summary = f"Tóm tắt: {desc[:250]}..."
        return summary
    except:
        return "Lỗi lấy dữ liệu."

def process_file(excel_path):
    if not os.path.exists(excel_path):
        print(f"[!] Không tìm thấy file: {excel_path}")
        return

    print(f"\n--- Đang xử lý: {excel_path} ---")
    df = pd.read_excel(excel_path)
    
    count = 0
    total = len(df)
    needs_save = False
    
    for index, row in df.iterrows():
        if row.get('Summary') == '[NEED_AGENT_SUMMARY]':
            summary = get_video_summary(row['Video_URL'])
            df.at[index, 'Summary'] = summary
            print(f"✅ [{index+1}/{total}] Đã xong: {str(row['Title'])[:40]}...")
            count += 1
            needs_save = True
            
    if needs_save:
        df.to_excel(excel_path, index=False)
        print(f"--- Hoàn thành cập nhật {count} video! ---")
    else:
        print(f"--- Không có video nào cần tóm tắt trong file này. ---")

def main():
    base_dir = "Youtube_Master_Geting_Info"
    # Find all Summary Excel files
    files = glob.glob(os.path.join(base_dir, "*", "Youtube_Data_Summary_*.xlsx"))
    
    if not files:
        print("[!] Không tìm thấy file Excel nào để cập nhật.")
        return

    print(f"[*] Tìm thấy {len(files)} file cần kiểm tra.")
    for f in files:
        process_file(f)

if __name__ == "__main__":
    main()
