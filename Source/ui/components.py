# ui/components.py
import tkinter as tk
from tkinter import Scrollbar
from PIL import ImageTk, Image
from config import RESOURCE_DIR

# def show_image_button(tag, root, frame, function, location, button_data):
    # 在開頭加一行測試
    # btn = tk.Button(frame, text=button_data[0], command=function)
    # btn.pack(side='left', padx=10)
    # return btn
def show_image_button(tag, root, frame, function, location, button_data):
    """
    button_data: [圖片檔名, 寬, 高]
    """
    # 使用 config.py 提供的路徑，解決反斜線問題
    target_path = RESOURCE_DIR / f"{button_data[0]}.png"
    
    try:
        img = Image.open(target_path)
    except FileNotFoundError:
        print(f"錯誤：找不到圖片 {target_path}")
        # 如果找不到圖片，建立一個純文字按鈕代替，防止程式崩潰
        button = tk.Button(frame, text=button_data[0], command=function)
        button.pack()
        return button

    # 調整圖像大小 (相容新舊 Pillow 版本)
    max_size = (button_data[1], button_data[2])
    resample_mode = getattr(Image, 'LANCZOS', getattr(Image, 'ANTIALIAS', Image.BICUBIC))
    img.thumbnail(max_size, resample_mode)

    tk_img = ImageTk.PhotoImage(img)

    button = tk.Button(frame, image=tk_img, command=function, borderwidth=0, highlightthickness=0)
    button.image = tk_img  # 強制保持引用，防止圖片變空白

    # 排版邏輯
    if tag == 'window_class':
        button.pack(side='right', padx=1, pady=1)
    elif tag in ['txt_viewer content', 'upload next_back']:
        side_val = location[2] if len(location) > 2 else 'left'
        button.pack(side=side_val)
    else:
        button.pack()
        
    return button

def scroll_component(tag, root, size, content):
    """
    tag: 'text' 或 'image'
    size: [寬, 高]
    content: 文本內容 或 圖片路徑 (Path 對象)
    """
    if tag == 'text':
        frame = tk.Frame(root)
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        text_widget = tk.Text(frame, wrap=tk.WORD, width=size[0], height=size[1])
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = Scrollbar(frame, command=text_widget.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_widget.config(yscrollcommand=scrollbar.set)
        text_widget.insert(tk.END, content)
        
        # 綁定滾輪
        text_widget.bind("<MouseWheel>", lambda e: text_widget.yview_scroll(-1*(e.delta//120), "units"))
        return text_widget

    elif tag == 'image':
        canvas_width, canvas_height = 620, 530
        image_frame = tk.Frame(root)
        image_frame.pack(pady=20, side='left')

        scrollbar = tk.Scrollbar(image_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        canvas = tk.Canvas(image_frame, width=canvas_width, height=canvas_height, yscrollcommand=scrollbar.set)
        canvas.pack()
        scrollbar.config(command=canvas.yview)

        img = Image.open(content) # content 應為 Path 物件
        img.thumbnail((canvas_width, 10000)) # 高度比例縮放

        tk_img = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor='nw', image=tk_img)
        canvas.image = tk_img # 保持引用
        canvas.configure(scrollregion=canvas.bbox("all"))
        
        canvas.bind("<MouseWheel>", lambda e: canvas.yview_scroll(-1*(e.delta//120), "units"))
        return canvas