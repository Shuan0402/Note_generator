import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
import jieba

try:
    from PIL import Image, ImageTk
except ImportError:
    import Image, ImageTk


# from generate import generate
from upload import upload
from editor import edit
from image_button import show_button


def txt_viewer(file_name, window):
    current_path = os.path.abspath(os.path.dirname(__file__))
    parent_path = os.path.abspath(os.path.join(current_path, os.pardir))
    target_txt = os.path.join(parent_path, 'txt', file_name)
    
    with open(target_txt) as f:
        content = f.read()

    # 預覽內文
    wrapped_content = wrap_text(content, line_length = 52)
    txt_Label = tk.Label(window, bg = 'white', fg = 'black', font = ('Arial', 12), text = wrapped_content)
    # txt_Label.grid(row = 0, column = 0, columnspan = 2)
    txt_Label.pack()
    


    # 確認內文按鍵
    yes_button = tk.Button(window, text = 'Yes', width = 15, height = 2, command = lambda: class_txt(window, content, file_name))
    # yes_button.grid(row = 1, column = 0)
    yes_button.pack()



# 關閉視窗
def close_window(root):
    root.destroy()

# 確認所需字符
def class_txt(window, content, file_name):
    # 建立顯示視窗
    txt_window = tk.Toplevel(window)  # 使用 Toplevel() 創建新的視窗，而不是 tk.Tk()
    txt_window.title('TXT')
    txt_window.geometry("500x600+200+200")

    hint_Label = tk.Label(txt_window, bg = 'white', fg = 'black', font = ('Arial', 12), text = 'All the words you need')
    hint_Label.grid(row = 0, column = 0, columnspan = 2)
    # 建立文字資料夾
    current_path = os.path.abspath(os.path.dirname(__file__))
    parent_path = os.path.abspath(os.path.join(current_path, os.pardir))
    target_folder = os.path.join(parent_path, 'Generated_txt', file_name)
    if not os.path.isdir(target_folder):
        os.mkdir(target_folder)

    # 統計文字符號
    txt = []
    for i in content:
        if i in txt or i == '\n':
            continue
        else:
            txt.append(i)
            txt_list = os.path.join(target_folder, i)
        if not os.path.isdir(txt_list):
            os.mkdir(txt_list)

    # 顯示需要的字符
    txt_list_len = len(txt) // 20   # 一行最多顯示 20 個字
    for i in range(txt_list_len):
        print_txt_list = tk.Label(txt_window, bg = 'white', fg = 'black', font = ('Arial', 12), text = txt[i * 20 : (i + 1) * 20])
        print_txt_list.pack()
    print_txt_list = tk.Label(txt_window, bg = 'white', fg = 'black', font = ('Arial', 12), text = txt[20 * txt_list_len : 20 * txt_list_len + len(txt) % 20])
    print_txt_list.grid(row = 2, column = 0, columnspan = 2)
    
    # generate的button
    # generate_button = os.path.join(parent_path, 'Resource\generate.png')
    # generate_img = Image.open(generate_button)
    # max_size = (75, 75)
    # generate_img.thumbnail(max_size, Image.ANTIALIAS)
    # tk_img = ImageTk.PhotoImage(generate_img)
    # button = tk.Button(txt_window, image=tk_img, command=lambda:edit(content, txt_window), compound="top", borderwidth=0, highlightthickness=0)
    # button.grid(row = 4, column = 0, columnspan = 2)
    # show_button.img = tk_img
    
    # 上傳圖片
    upload_button = tk.Button(txt_window, text = 'Upload', width = 15, height = 2, command = lambda: upload(file_name, txt_window))
    upload_button.grid(row = 3, column = 0, columnspan = 2)

    txt_window.mainloop()
    
def wrap_text(text, line_length=52):
    words = list(jieba.cut(text))
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) <= line_length:
            # 如果目前的行加上當前詞的長度不超過line_length，則將該詞加入目前行
            current_line += word
        else:
            # 超過line_length，換行並加入該詞到新行
            lines.append(current_line)
            current_line = word

    # 將最後一行加入結果
    lines.append(current_line)

    return "\n".join(lines)



# root = tk.Tk()
# root.title('oxxo.studio')
# root.geometry('300x300')

# show_button(root)

# root.mainloop()
