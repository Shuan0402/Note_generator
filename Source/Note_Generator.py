# -*- coding: utf8 -*-
import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import ttk

# 函式庫
from txt_viewer import txt_viewer   # txt 預覽視窗
from window_class import DraggableWindow

# 宣告主視窗
window = tk.Tk()
screen_width = window.winfo_screenwidth()   # 獲得螢幕的長
screen_height = window.winfo_screenheight() # 獲得螢幕的高
window.geometry("845x590+" + str((screen_width - 845)//2) + "+" + str((screen_height - 590)//2))    # 宣告視窗大小且視窗置中
draggable = DraggableWindow(window, [845, 590]) # 使視窗標準化



# 當前選取的資料
file_name = None
def print_selection():
    # 清空螢幕
    time = 0
    for widget in window.winfo_children():
        if time < 1:
            time += 1
        else:
            widget.pack_forget()
            
    if file_name == None:
        txt_viewer('README.txt', window)
    else:
        txt_viewer(file_name, window)

# 點選下拉式清單
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
selected_option.set('README.txt')
dropdown = ttk.OptionMenu(window, selected_option, 'README.txt', *all_file_names, command = on_selection_changed)
dropdown.pack()

# 選取的確認鍵
selection_button = tk.Button(window, text = 'select', width = 15, height = 2, command = print_selection)
selection_button.pack()

# 主迴圈
window.mainloop()

