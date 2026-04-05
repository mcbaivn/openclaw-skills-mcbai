
from patchright.sync_api import sync_playwright
import os

# Đường dẫn mới của Skill
STATE_PATH = r"C:\Users\PCM\.claude\skills\notebooklm\data\browser_state"

def test_auth():
    print(f"[*] Testing Authenticated State in Skill directory...")
    with sync_playwright() as p:
        try:
            # Dùng chính cái state vừa copy
            browser = p.chromium.launch_persistent_context(
                user_data_dir=STATE_PATH,
                channel="chrome",
                headless=True,
                extra_http_headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"},
                args=["--no-sandbox"]
            )
            
            page = browser.new_page()
            page.goto("https://notebooklm.google.com/")
            
            # Đợi load
            page.wait_for_timeout(5000)
            url = page.url
            print(f"[+] Final URL: {url}")
            
            if "google.com/accounts" in url:
                print("[!] Error: Redirected to Login. Cookie transfer might have failed.")
            else:
                print("[✨] SUCCESS! You are LOGGED IN as your Human in the Skill environment!")
                
            browser.close()
        except Exception as e:
            print(f"[!] Error: {e}")

if __name__ == "__main__":
    test_auth()
