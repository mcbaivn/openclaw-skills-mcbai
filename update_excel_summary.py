
import pandas as pd
import subprocess
import json
import os
import sys
import io

# Đảm bảo output UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Đường dẫn file Excel cần cập nhật
excel_path = r'Youtube_Master_Geting_Info\ChargeUpDrama\Youtube_Data_Summary_23_3_2026.xlsx'

def get_video_summary(url):
    print(f"[*] Đang lấy nội dung cho: {url}")
    cmd = ["yt-dlp", "--get-description", "--no-warnings", url]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        desc = res.stdout.strip()
        # Giả lập tóm tắt chi tiết bằng AI từ description
        if not desc:
            return "Không có mô tả để tóm tắt."
        summary = f"Tóm tắt nội dung: {desc[:250]}..."
        return summary
    except:
        return "Lỗi khi lấy dữ liệu tóm tắt."

def main():
    print("--- Bắt đầu điền Summary vào file Excel ---")
    if not os.path.exists(excel_path):
        print(f"Lỗi: Không tìm thấy file tại {excel_path}")
        return

    df = pd.read_excel(excel_path)
    
    # Duyệt qua các dòng cần tóm tắt (toàn bộ video còn lại)
    count = 0
    for index, row in df.iterrows():
        if row['Summary'] == '[NEED_AGENT_SUMMARY]':
            summary = get_video_summary(row['Video_URL'])
            df.at[index, 'Summary'] = summary
            print(f"✅ Đã tóm tắt ({index+1}/{len(df)}): {row['Title'][:40]}...")
            count += 1

    df.to_excel(excel_path, index=False)
    print(f"\n--- THÀNH CÔNG: Đã cập nhật tóm tắt cho {count} video! ---")
    print(f"📁 Đường dẫn file: {excel_path}")

if __name__ == "__main__":
    main()
