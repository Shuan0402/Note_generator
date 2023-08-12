# -*- coding: utf8 -*-
import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import ttk

# 函式庫
from txt_viewer import txt_viewer   # txt 預覽視窗

window = tk.Tk()
window.title('Note Generator')
window.geometry("845x590")


# 當前選取的資料
file_name = None
def print_selection():
    time = 0
    for widget in window.winfo_children():
        if time < 2:
            time += 1
        else:
            widget.pack_forget()
    txt_viewer(file_name, window)

def on_selection_changed(selection):
    global file_name
    file_name = selection
    selected_option.set(selection)

# 開啟 txt 資料夾獲得 txt 選項
current_path = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.abspath(os.path.join(current_path, os.pardir))
target_folder = os.path.join(parent_path, 'txt')

# 如果位置不對則跳到指定位置
if os.getcwd() != target_folder:
    os.chdir(target_folder)

# 建立 txt 下拉選單
all_file_names = os.listdir()
selected_option = tk.StringVar()
selected_option.set(all_file_names[0])
dropdown = ttk.OptionMenu(window, selected_option, all_file_names[0], *all_file_names, command = on_selection_changed)
dropdown.pack()

# 選取的確認鍵
selection_button = tk.Button(window, text = 'select', width = 15, height = 2, command = print_selection)
selection_button.pack()

# 主迴圈
window.mainloop()

