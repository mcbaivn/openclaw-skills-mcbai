
import sys
import os

# Đường dẫn đến skill
skill_path = r"C:\Users\PCM\.claude\skills\notebooklm"
scripts_path = os.path.join(skill_path, "scripts")
sys.path.append(scripts_path)

# Mock cái print để nó không bị lỗi Unicode
import builtins
def safe_print(*args, **kwargs):
    try:
        builtins._original_print(*args, **kwargs)
    except UnicodeEncodeError:
        new_args = [str(arg).encode('ascii', 'ignore').decode('ascii') for arg in args]
        builtins._original_print(*new_args, **kwargs)

builtins._original_print = print
builtins.print = safe_print

# Chạy ask_question
from ask_question import main as ask_main
import argparse

# Giả lập tham số dòng lệnh cho ask_question
sys.argv = [
    "ask_question.py",
    "--notebook-id", "phim-trọng-sinh-báo-thù",
    "--question", "Hãy tóm tắt chi tiết bộ phim này bằng tiếng Việt"
]

try:
    ask_main()
except SystemExit:
    pass
except Exception as e:
    print(f"Lỗi: {e}")
