# Source/core/generator.py
from PIL import Image
from config import TXT_DIR, OUTPUT_DIR, RESOURCE_DIR
import random

def generate_preview(file_name):
    print(f"正在生成 {file_name} 的預覽圖...")
    
    # 1. 讀取原始文本內容
    txt_path = TXT_DIR / file_name
    with open(txt_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 2. 定義字元圖片來源資料夾
    char_base_dir = OUTPUT_DIR / file_name.replace('.txt', '')
    
    # 3. 建立畫布 (假設 A4 大小預設為白色)
    canvas = Image.new('RGB', (1200, 1600), (255, 255, 255))
    x_offset, y_offset = 50, 50
    line_height = 100
    char_size = 80

    for char in content:
        if char == '\n':
            y_offset += line_height
            x_offset = 50
            continue
        
        # 尋找該字元的圖片
        char_folder = char_base_dir / char
        img_files = list(char_folder.glob("*.png")) + list(char_folder.glob("*.jpg"))
        
        if img_files:
            # 隨機選一張該字元的筆跡
            char_img = Image.open(random.choice(img_files)).resize((char_size, char_size))
            # 這裡可以加一點隨機位移，讓它更像手寫
            canvas.paste(char_img, (x_offset + random.randint(-3, 3), y_offset + random.randint(-3, 3)))
        else:
            # 如果沒上傳該字，可以用預設字體或跳過 (這裡我們印出偵錯)
            print(f"提示：字元 '{char}' 尚未上傳圖片，跳過中...")
        
        x_offset += char_size
        if x_offset > 1100: # 自動換行
            x_offset = 50
            y_offset += line_height

    # 4. 【關鍵】儲存產出檔案
    save_path = char_base_dir / "preview.png"
    canvas.save(save_path)
    print(f"--- 偵錯：預覽圖已成功儲存至 {save_path} ---")