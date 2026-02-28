# config.py 修正版
from pathlib import Path
import sys

# 根據 main.py 的位置（假設 main.py 在 Source/ 內）
# 我們要抓到 Source 的上一層作為 BASE_DIR
current_file = Path(__file__).resolve()
SOURCE_DIR = current_file.parent
BASE_DIR = SOURCE_DIR.parent  # 這才是 Note_generator/ 根目錄

# 定義各子資料夾路徑
RESOURCE_DIR = BASE_DIR / "Resource"
TXT_DIR = BASE_DIR / "txt"
CORE_DIR = SOURCE_DIR / "core" # core 現在在 Source/ 下
UI_DIR = SOURCE_DIR / "ui"     # ui 現在在 Source/ 下
OUTPUT_DIR = BASE_DIR / "Generated_txt"

# 將路徑加入系統，確保 import 正常
if str(SOURCE_DIR) not in sys.path:
    sys.path.append(str(SOURCE_DIR))

# 打印路徑以便除錯 (執行時如果還有錯，請看這幾行輸出)
print(f"--- Path Diagnostic ---")
print(f"Base Directory: {BASE_DIR}")
print(f"Resource Directory: {RESOURCE_DIR}")
print(f"Checking for X.png: {RESOURCE_DIR / 'X.png'}")
print(f"-----------------------")