
from patchright.sync_api import sync_playwright as sync_patchright
import os
import time

DATA_DIR = r"C:\Users\PCM\.claude\skills\notebooklm\data"
STATE_PATH = os.path.join(DATA_DIR, "browser_state")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def setup_auth():
    print("[*] Starting Chrome for Authentication...")
    with sync_patchright() as p:
        # Dùng Chrome thực thay vì Chromium
        browser = p.chromium.launch_persistent_context(
            user_data_dir=STATE_PATH,
            channel="chrome",
            headless=False, # Hiện cửa sổ cho sếp
            viewport={"width": 1280, "height": 800}
        )
        
        page = browser.new_page()
        page.goto("https://notebooklm.google.com/")
        
        print("[!] PLEASE LOG IN TO GOOGLE ON THE OPENED BROWSER.")
        print("[!] AFTER LOGGING IN, CLOSE THE BROWSER WINDOW TO FINISH.")
        
        # Đợi sếp đăng nhập (đợi đến khi sếp đóng trình duyệt)
        try:
            while True:
                if browser.pages == []:
                    break
                time.sleep(1)
        except:
            pass
            
        browser.close()
        print("[+] Authentication State Saved!")

if __name__ == "__main__":
    setup_auth()
