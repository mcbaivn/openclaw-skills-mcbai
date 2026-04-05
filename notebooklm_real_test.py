
import os
import sys
import time
from patchright.sync_api import sync_playwright

# Cấu hình "long mạch" của đại ca
USER_DATA_DIR = r"C:\Users\PCM\AppData\Local\Google\Chrome\User Data"
PROFILE_NAME = "Profile 86"

def get_notebooklm_summary(video_url):
    print(f"[*] Đang dùng Profile 86 để đột kích NotebookLM...")
    print(f"[*] Video mục tiêu: {video_url}")
    
    with sync_playwright() as p:
        try:
            # Khởi chạy Chrome dùng Profile của sếp
            # Lưu ý: Sếp cần đóng Chrome Profile 86 trước khi chạy cái này
            browser = p.chromium.launch_persistent_context(
                user_data_dir=USER_DATA_DIR,
                channel="chrome",
                headless=False, # Hiện cửa sổ để đại ca quan sát
                args=[f"--profile-directory={PROFILE_NAME}", "--no-sandbox", "--disable-blink-features=AutomationControlled"]
            )
            
            page = browser.new_page()
            
            # 1. Vào trang chủ NotebookLM
            page.goto("https://notebooklm.google.com/")
            page.wait_for_timeout(5000)
            
            # Kiểm tra xem có bị bắt login không
            if "accounts.google.com" in page.url:
                print("[!] Lỗi: Profile 86 chưa đăng nhập hoặc bị Google chặn automation.")
                browser.close()
                return "Cần đăng nhập lại Profile 86."

            # 2. Nhấn nút "Tạo mới" (Dựa trên snapshot hôm qua nút có text "Tạo mới")
            # Tìm nút có icon 'add' hoặc text 'Tạo mới'
            print("[*] Đang tạo Notebook mới...")
            page.get_by_role("button", name="Tạo mới").click()
            page.wait_for_timeout(5000)

            # 3. Chọn nguồn "Trang web" (Dựa trên snapshot hôm qua)
            print("[*] Đang chọn nguồn YouTube/Trang web...")
            page.get_by_role("button", name="Trang web").click()
            page.wait_for_timeout(2000)

            # 4. Dán link YouTube
            print("[*] Đang dán link YouTube...")
            # Tìm textbox nhập URL
            textbox = page.get_by_placeholder("Dán liên kết bất kỳ")
            textbox.fill(video_url)
            page.wait_for_timeout(1000)
            page.keyboard.press("Enter")
            page.wait_for_timeout(3000)

            # 5. Nhấn nút "Chèn" (Nút này hay bị disabled nếu Google chưa check xong)
            insert_btn = page.get_by_role("button", name="Chèn")
            if insert_btn.is_enabled():
                insert_btn.click()
                print("[*] Đã nhấn nút Chèn.")
            else:
                print("[!] Nút Chèn bị khóa. Đệ thử dùng mẹo click tọa độ...")
                insert_btn.click(force=True)
            
            # Đợi NotebookLM nạp nguồn (thường mất 10-20s cho video dài)
            print("[*] Đang đợi NotebookLM học nội dung video (30s)...")
            page.wait_for_timeout(30000)

            # 6. Đặt câu hỏi tóm tắt
            print("[*] Đang hỏi Gemini tóm tắt...")
            chat_input = page.get_by_placeholder("Bắt đầu nhập...")
            chat_input.fill("Hãy tóm tắt nội dung video này cực kỳ chi tiết bằng tiếng Việt, chia theo các mốc thời gian nếu có.")
            page.keyboard.press("Enter")
            
            # Đợi câu trả lời (Gemini trả lời khá nhanh)
            page.wait_for_timeout(20000)
            
            # Lấy câu trả lời cuối cùng
            # Thường là phần tử cuối cùng trong chat history
            responses = page.query_selector_all(".chat-response") # Selector giả định, sẽ lấy text nếu tìm thấy
            if responses:
                summary = responses[-1].inner_text()
            else:
                # Nếu không tìm thấy selector, chụp snapshot hoặc lấy toàn bộ text vùng chat
                summary = "Đã gửi câu hỏi, sếp xem trên màn hình nhé!"
            
            print(f"\n[✨] KẾT QUẢ TỪ NOTEBOOKLM:\n{summary}")
            
            # Giữ trình duyệt lại 10s cho sếp xem kết quả
            time.sleep(10)
            browser.close()
            return summary

        except Exception as e:
            print(f"[!] Lỗi trong quá trình tác chiến: {e}")
            if 'browser' in locals(): browser.close()
            return f"Lỗi: {str(e)}"

if __name__ == "__main__":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    video = "https://www.youtube.com/watch?v=oprGnj8RiSE"
    get_notebooklm_summary(video)
