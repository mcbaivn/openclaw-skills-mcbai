
from patchright.sync_api import sync_playwright
import os

USER_DATA_DIR = r"C:\Users\PCM\AppData\Local\Google\Chrome\User Data"
PROFILE_NAME = "Profile 86"

def test_auth():
    print(f"[*] Attempting to use existing Chrome Profile: {PROFILE_NAME}")
    with sync_playwright() as p:
        try:
            # Kết nối thẳng vào Profile của sếp
            browser = p.chromium.launch_persistent_context(
                user_data_dir=USER_DATA_DIR,
                channel="chrome",
                headless=True, # Chạy ngầm cho sếp đỡ phiền
                extra_http_headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"},
                args=[f"--profile-directory={PROFILE_NAME}", "--no-sandbox"]
            )
            
            page = browser.new_page()
            page.goto("https://notebooklm.google.com/")
            
            # Đợi xem có thấy tên sếp không (check login)
            page.wait_for_timeout(5000)
            title = page.title()
            url = page.url
            
            print(f"[+] Connected! Page Title: {title}")
            print(f"[+] Current URL: {url}")
            
            if "google.com/accounts" in url:
                print("[!] Error: Still redirected to Login page. Please ensure Profile 86 is logged in.")
            else:
                print("[✨] SUCCESS: Authenticated using your Chrome Profile!")
                
            browser.close()
        except Exception as e:
            print(f"[!] Error: {e}")

if __name__ == "__main__":
    test_auth()
