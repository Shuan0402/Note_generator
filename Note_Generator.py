# -*- coding: utf8 -*-
import tkinter as tk
import os
from PIL import Image, ImageTk

# 函式庫
from txt_viewer import txt_viewer   # txt 預覽視窗

window = tk.Tk()
window.title('Note Generator')
window.geometry("500x500+500+150")


# 當前選取的資料
file_name = None
def print_selection():
    global file_name
    file_name = listbox.get(listbox.curselection())   # 獲取當前選中的文字
    current_file.set(file_name)  # 為label設定值
    txt_viewer(file_name, window)    # 預覽選取文件

# 顯示當前選取的資料名稱
current_file = tk.StringVar()
current_file_label = tk.Label(window, bg = 'white', fg = 'black', font = ('Arial', 12), width = 10, textvariable = current_file)
current_file_label.pack()

# 開啟 txt 資料夾獲得 txt 選項
current_path = os.path.abspath(os.path.dirname(__file__))
target_folder = os.path.join(current_path, 'txt')

# 如果位置不對則跳到指定位置
if os.getcwd() != target_folder:
    os.chdir(target_folder)

# 建立 txt 選項清單
all_file_names = os.listdir()
listbox = tk.Listbox(window)    
for item in all_file_names:
    listbox.insert('end', item)  
listbox.pack()

# 選取的確認鍵
selection_buttom = tk.Button(window, text = 'print selection', width = 15, height = 2, command = print_selection)
selection_buttom.pack()

# 主迴圈
window.mainloop()

print("hello")
