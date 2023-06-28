# coding=utf-8
import tkinter as tk
import os
from generate import generate
from upload import upload

def txt_viewer(file_name, window):
    txt_window = tk.Toplevel(window)  # 使用 Toplevel() 創建新的視窗，而不是 tk.Tk()
    txt_window.title('TXT')
    txt_window.geometry("500x600+200+200")

    current_path = os.path.abspath(os.path.dirname(__file__))
    target_txt = os.path.join(current_path, 'txt', file_name)
    
    with open(target_txt) as f:
        content = f.read()

    txt_Label = tk.Label(txt_window, bg = 'white', fg = 'black', font = ('Arial', 12), text = content)
    txt_Label.pack()

    yes_button = tk.Button(txt_window, text = 'Yes', width = 15, height = 2, command = lambda: class_txt(txt_window, file_name, txt_window, window, content))
    no_button = tk.Button(txt_window, text = 'No', width = 15, height = 2, command = lambda: close_window(txt_window))
    yes_button.pack()
    no_button.pack()

def close_window(root):
    root.destroy()

def class_txt(root, file_name, txt_window, window, content):
    # 建立文字資料夾
    current_path = os.path.abspath(os.path.dirname(__file__))
    target_folder = os.path.join(current_path, file_name)
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
    print_txt_list = tk.Label(txt_window, bg = 'white', fg = 'black', font = ('Arial', 12), text = txt[20 * txt_list_len : 20 * txt_list_len + txt_list_len % 5])
    print_txt_list.pack()
    
    # 生成圖片
    generate_button = tk.Button(txt_window, text = 'Generate', width = 15, height = 2, command = lambda: generate(txt_window, window, file_name))
    generate_button.pack()

    # 上傳圖片
    # 此功能不完全，之後再優化
    upload_Label = tk.Label(txt_window, bg = 'white', fg = 'black', font = ('Arial', 12), text = 'upload hasn\'t completed, dont touch')
    upload_Label.pack()
    upload_button = tk.Button(txt_window, text = 'Upload', width = 15, height = 2, command = lambda: upload(file_name, txt_window))
    upload_button.pack()
    

