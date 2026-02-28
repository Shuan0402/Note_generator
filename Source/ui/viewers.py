from curses import window
import tkinter as tk
from pathlib import Path
import shutil
import traceback
from tkinter import filedialog, ttk, colorchooser
from PIL import Image, ImageTk
import os
import subprocess

# 從你的專案架構匯入
from config import TXT_DIR, OUTPUT_DIR, RESOURCE_DIR
from ui.components import show_image_button, scroll_component
from ui.windows import DraggableWindow
from core.generator import generate_preview

def format_text(file_name, text_width):
    """將文字依照指定寬度換行"""
    file_path = TXT_DIR / file_name
    if not file_path.exists():
        return "檔案不存在"

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    lines = []
    line = ''
    for char in content:
        if len(line) < text_width:
            line += char
        else:
            lines.append(line.strip())
            line = char
    if line: lines.append(line.strip())
    return '\n'.join(lines)

def txt_viewer(file_name, window):
    """文本預覽介面"""
    target_txt = TXT_DIR / file_name
    
    with open(target_txt, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- 介面佈局 ---
    
    # 1. 底部按鈕區 (最先 pack，確保不會被擠掉)
    btn_frame = tk.Frame(window, height=100) 
    btn_frame.pack(side='bottom', fill='x', pady=20)
    btn_frame.pack_propagate(False) 

    # 點擊 Next 會進入 class_txt 分析字符介面
    show_image_button('txt_viewer content', window, btn_frame, 
                     lambda: class_txt(window, content, file_name), 
                     [2, 0, "right"], ["Next", 80, 80])
    
    show_image_button('txt_viewer content', window, btn_frame, 
                     lambda: back_to_select(window), 
                     [2, 1, "right"], ["Back", 80, 80])

    # 2. 中間文字預覽區 (填滿剩餘空間)
    text_frame = tk.Frame(window)
    text_frame.pack(side='top', fill='both', expand=True)
    
    wrapped_content = format_text(file_name, 52)
    scroll_component('text', text_frame, [115, 30], wrapped_content)

def class_txt(window, content, file_name):
    """分析文字並顯示需要的字符清單"""
    # 建立新視窗
    txt_window = tk.Toplevel(window)
    DraggableWindow(txt_window, [845, 590])

    tk.Label(txt_window, bg='mediumvioletred', fg='white', 
             font=('Arial', 12), text='All unique characters needed:').pack(fill='x', pady=5)

    # 建立輸出資料夾
    target_folder = OUTPUT_DIR / file_name.replace('.txt', '')
    target_folder.mkdir(parents=True, exist_ok=True)

    # 統計字元
    unique_chars = []
    for char in content:
        if char not in unique_chars and not char.isspace():
            unique_chars.append(char)
            (target_folder / char).mkdir(exist_ok=True)

    # 顯示字符滾動區
    display_frame = tk.Frame(txt_window, bg='white')
    display_frame.pack(fill='both', expand=True, padx=20, pady=10)
    
    char_text = "  ".join(unique_chars)
    scroll_component('text', display_frame, [80, 20], char_text)

    # 下方按鈕
    up_btn_frame = tk.Frame(txt_window)
    up_btn_frame.pack(side='bottom', pady=20)
    
    show_image_button('', txt_window, up_btn_frame, 
                     lambda: goto_upload(file_name, txt_window, window), 
                     [0, 0, ""], ["Upload", 100, 100])

def back_to_select(window):
    """清除元件回到主選單"""
    for widget in window.winfo_children():
        if not hasattr(widget, 'is_title_bar'): # 假設標題列有標記
            widget.destroy()
    print("已返回主選單")

def change_char(current_char_var, all_chars, window, base_path, direction, preview_container):
    """
    確保這裡的參數順序與 lambda 調用一致：
    1. current_char_var
    2. all_chars
    3. window (即 upload_window)
    4. base_path (即 char_base_folder)
    5. direction ('next' 或 'back')
    6. preview_container (即 preview_area)
    """
    current_val = current_char_var.get()
    current_index = all_chars.index(current_val)
    
    if direction == 'next':
        new_index = (current_index + 1) % len(all_chars)
    else:
        new_index = (current_index - 1) % len(all_chars)
    
    new_char = all_chars[new_index]
    current_char_var.set(new_char)
    
    # 切換字元後，刷新該字元的圖片預覽
    refresh_char_previews(preview_container, base_path, new_char)

def goto_upload(file_name, prev_window, root_window):
    """進入圖片上傳與管理介面"""
    prev_window.destroy()
    upload_window = tk.Toplevel(root_window)
    # 這裡我們用 upload_window 而不是 window，避免與系統保留字衝突
    DraggableWindow(upload_window, [845, 590])
    
    char_base_folder = OUTPUT_DIR / file_name.replace('.txt', '')
    all_chars = [f.name for f in char_base_folder.iterdir() if f.is_dir()]
    
    if not all_chars:
        print("沒有需要上傳的字符")
        return

    current_char_var = tk.StringVar(value=all_chars[0])

    # --- UI 佈局 ---
    tk.Label(upload_window, textvariable=current_char_var, font=('Arial', 24, 'bold')).pack(pady=10)
    
    # 建立一個容器專門放預覽圖
    preview_area = tk.Frame(upload_window, bg='#f0f0f0', height=150)
    preview_area.pack(fill='x', padx=20, pady=10)
    preview_area.pack_propagate(False) 

    # --- 按鈕區域 ---
    up_frame = tk.Frame(upload_window)
    up_frame.pack(pady=10)
    show_image_button('upload', upload_window, up_frame, 
                     lambda: upload_logic(current_char_var, upload_window, char_base_folder, preview_area), 
                     [0, 0, ""], ["Upload", 80, 80])

    nav_frame = tk.Frame(upload_window)
    nav_frame.pack(side='bottom', pady=20)
    # --- 在導航按鈕下方，增加一個大的「完成生成」按鈕 ---
    finish_frame = tk.Frame(upload_window)
    finish_frame.pack(side='bottom', pady=10)

    # 這裡的 lambda 會帶領使用者進入最後的編輯/生成畫面
    show_image_button('generate_btn', upload_window, finish_frame, 
                     lambda: edit_screen(file_name, upload_window, root_window), 
                     [0, 0, ""], ["Edit", 120, 120]) 
    
    # 你可以把圖片名稱換成 "Start" 或 "Generate" (如果 Resource 裡有對應 PNG)
    # 暫時先用 Next.png 代替，或加個 Label 提示
    tk.Label(finish_frame, text="Generate Note", font=('Arial', 10, 'bold')).pack()
    
    # 修正：將 preview_area 傳入 change_char
    show_image_button('upload next_back', upload_window, nav_frame, 
                     lambda: change_char(current_char_var, all_chars, upload_window, char_base_folder, 'next', preview_area), 
                     [0, 0, "right"], ["Next", 80, 80])
    
    show_image_button('upload next_back', upload_window, nav_frame, 
                     lambda: change_char(current_char_var, all_chars, upload_window, char_base_folder, 'back', preview_area), 
                     [0, 0, "right"], ["Back", 80, 80])

    # 初始刷新
    refresh_char_previews(preview_area, char_base_folder, current_char_var.get())

# Source/ui/viewers.py
def upload_logic(char_var, window, base_path, preview_container):
    # 使用簡化的過濾器
    ftypes = [
        ("Image files", "*.png;*.jpg;*.jpeg;*.PNG;*.JPG;*.JPEG"),
        ("PNG files", "*.png"),
        ("JPEG files", "*.jpg;*.jpeg"),
        ("All files", "*.*")
    ]
    
    file_path = filedialog.askopenfilename(
        parent=window,
        title=f"選擇 '{char_var.get()}' 的圖片",
        filetypes=ftypes,
        # 在 PowerShell/Windows 執行時，initialdir 要用 Windows 路徑格式
        initialdir=str(RESOURCE_DIR) 
    )
    
    if not file_path:
        return

    # 這裡加入除錯印出，確認你有選到檔案
    print(f"--- 偵錯：已選擇檔案 {file_path} ---")

    src_path = Path(file_path)
    dest_folder = base_path / char_var.get()
    dest_folder.mkdir(parents=True, exist_ok=True)
    dest_path = dest_folder / src_path.name
    
    try:
        shutil.copy(src_path, dest_path)
        print(f"--- 偵錯：檔案已成功複製到 {dest_path} ---")
        refresh_char_previews(preview_container, base_path, char_var.get())
    except Exception as e:
        print(f"複製出錯: {e}")
      
def refresh_char_previews(window, base_path, char):
    """刷新當前字符的所有筆跡預覽"""
    # 清除舊的預覽 (邏輯與原本 clear_path 相似)
    for widget in window.winfo_children():
        if isinstance(widget, tk.Label) and hasattr(widget, 'is_preview'):
            widget.destroy()
        if isinstance(widget, tk.Button) and getattr(widget, 'is_del_btn', False):
            widget.destroy()

    char_folder = base_path / char
    img_list = list(char_folder.glob("*.png")) + list(char_folder.glob("*.jpg"))

    for img_path in img_list:
        img = Image.open(img_path).resize((80, 80))
        tk_img = ImageTk.PhotoImage(img)
        
        lbl = tk.Label(window, image=tk_img)
        lbl.is_preview = True # 標記以便清除
        lbl.image = tk_img
        lbl.pack(side='left', padx=5)
        
        # 刪除按鈕
        del_btn = tk.Button(window, text="X", command=lambda p=img_path: delete_img(p, window, base_path, char))
        del_btn.is_del_btn = True
        del_btn.pack(side='left')

def delete_img(path, window, base_path, char):
    if path.exists():
        path.unlink()
        refresh_char_previews(window, base_path, char)

def refresh_editor_preview(container, file_name):
    """將生成的筆記預覽圖顯示在右側區域"""
    # 1. 徹底清除舊組件
    for widget in container.winfo_children():
        widget.destroy()

    # 2. 定義產出的圖片路徑
    # 確保與 generator.py 的儲存路徑完全一致
    preview_path = OUTPUT_DIR / file_name.replace('.txt', '') / "preview.png"

    if preview_path.exists():
        try:
            # 使用 PIL 開啟圖片
            raw_img = Image.open(preview_path)
            
            # --- 縮放邏輯：讓圖片符合視窗寬度 (約 600px) ---
            target_width = 600
            ratio = target_width / float(raw_img.width)
            target_height = int(float(raw_img.height) * float(ratio))

            resample_mode = getattr(Image, 'Resampling', Image).LANCZOS
            resized_img = raw_img.resize((target_width, target_height), resample_mode)
            
            # 轉換為 Tkinter 可讀格式
            tk_img = ImageTk.PhotoImage(resized_img)
            
            # 3. 放入 Label 並「固定」引用
            # 注意：在 Tkinter 中，如果沒有把 PhotoImage 掛在一個變數上，它會被回收導致圖變透明
            img_label = tk.Label(container, image=tk_img, bg='white')
            img_label.image = tk_img  # <--- 這行是關鍵！防止圖片消失
            img_label.pack(expand=True, fill='both', padx=10, pady=10)
            
            print(f"--- 介面偵錯：已成功渲染預覽圖 ---")
            
        except Exception as e:
            tk.Label(container, text=f"圖片渲染失敗: {e}", fg='red').pack()
            print(f"圖片渲染報錯: {e}")
    else:
        tk.Label(container, text="找不到預覽檔，請點擊 Apply 生成", bg='white').pack(pady=20)

def edit_screen(file_name, prev_window, root_window):
    """進入最終編輯與預覽介面"""
    prev_window.destroy()
    editor_window = tk.Toplevel(root_window)
    DraggableWindow(editor_window, [845, 590])

    # --- 左側控制台 ---
    ctrl_frame = tk.Frame(editor_window, width=220, bg='#eeeeee')
    ctrl_frame.pack(side='left', fill='y', padx=10, pady=10)

    tk.Label(ctrl_frame, text="Note Settings", font=('Arial', 14, 'bold'), bg='#eeeeee').pack(pady=10)

    # 【功能 1】定義打開資料夾的邏輯
    def open_result_folder():
        path = OUTPUT_DIR / file_name.replace('.txt', '')
        # 針對 WSL 環境將路徑轉換為 Windows 格式並開啟 explorer
        try:
            win_path = str(path).replace('/mnt/c/', 'C:/').replace('/', '\\')
            subprocess.run(['explorer.exe', win_path])
        except Exception as e:
            print(f"無法開啟資料夾: {e}")

    # 生成按鈕
    def run_generation():
        print("--- 偵錯：開始生成筆記圖片 ---")
        try:
            generate_preview(file_name) 
            refresh_editor_preview(preview_frame, file_name)
        except Exception as e:
            print(f"生成失敗: {e}")
            traceback.print_exc()

    # 【按鈕 1】Apply 按鈕
    tk.Button(ctrl_frame, text="Apply & Preview", command=run_generation, 
              bg='mediumvioletred', fg='white', width=15).pack(pady=20)

    # 【按鈕 2】加入 Open Folder 按鈕
    tk.Button(ctrl_frame, text="Open Folder", command=open_result_folder, 
              bg='gray', fg='white', width=15).pack(pady=5)

    # --- 右側預覽區 ---
    preview_frame = tk.Frame(editor_window, bg='white')
    preview_frame.pack(side='right', fill='both', expand=True, padx=10, pady=10)
    
    tk.Label(preview_frame, text="Click 'Apply' to see your handwritten note", bg='white').pack(expand=True)