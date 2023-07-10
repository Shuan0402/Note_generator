import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
from copy_img import copy_image
import shutil
# 上傳字符的視窗
def upload(file_name, txt_window):
    # 創建上傳的視窗
    upload_window = tk.Toplevel(txt_window)
    upload_window.title('upload')
    upload_window.geometry("500x600+200+200")

    # 確認所須字符
    current_path = os.path.abspath(os.path.dirname(__file__))
    target_folder = os.path.join(current_path, file_name)
    if os.getcwd() != target_folder:
        os.chdir(target_folder)
    all_file_names = os.listdir()
    all_file_names.remove('oxxostudio.jpg')

    # 逐一上傳字符與 next 鍵
    global current_txt
    current_txt = tk.StringVar()
    current_txt.set(all_file_names[0])
    current_txt_Label = tk.Label(upload_window, bg = 'white', fg = 'black', font = ('Arial', 12), textvariable = current_txt)
    current_txt_Label.pack()
    
    global txt_path
    txt_path = []
    upload_button = tk.Button(upload_window, text = 'upload', width = 15, height = 2, command = lambda:upload_image(current_txt, upload_window, file_name))
    upload_button.pack()
    next_button = tk.Button(upload_window, text = 'next', width = 15, height = 2, command = lambda:next_txt(current_txt, all_file_names, upload_window, file_name))
    next_button.pack()
    

# 上傳字符
def upload_image(txt, upload_window, file_name):
    file_path = filedialog.askopenfilename()
    txt_path.append(file_path)
    if os.path.exists(file_path):
        # 顯示選取的路徑
        upload_path_Label = tk.Label(upload_window, bg = 'white', fg = 'black', font = ('Arial', 12), text = file_path)
        upload_path_Label.pack()
        
        # 刪除路徑
        del_button = tk.Button(upload_window, text = 'delete', command = lambda: delete(file_path, upload_path_Label, del_button))
        del_button.pack()

        
    else:
        print('no')

# 下一個字符
def next_txt(current_element, all_file_names, upload_window, file_name):
    current_element = current_element.get()  # 獲取當前的字符
    copy_txt(file_name, current_txt)
    if current_element == all_file_names[-1]:   # 如果此字符位最後一個字符，則直接結束
        clear_window(upload_window)
        complete_Label = tk.Label(upload_window, bg = 'white', fg = 'black', font = ('Arial', 12), text = 'complete')
        complete_Label.pack()
    else:
        current_index = all_file_names.index(current_element) + 1   # 獲得當前字符的順序位置，並往後移到下一位
        current_txt.set(all_file_names[current_index])  # 將下一個字符設為當前字符
        clear_path(upload_window)

    print(txt_path)


# 清除螢幕
def clear_window(window):
    for widget in window.winfo_children():
        widget.pack_forget()  # 或者使用 grid_forget() 或 place_forget()

# 清除前一個字符的路徑
def clear_path(window):
    time = 0
    for widget in window.winfo_children():
        if time < 3:
            time += 1
        else:
            widget.pack_forget()

def delete(path, Label, Button):
    if os.path.exists(path):
        os.remove(path)
        Label.pack_forget()
        Button.pack_forget()
        print("yes")
    else:
        print("no")

def copy_txt(file_name, current_txt):
    # 將選取的圖片複製到當前字符的資料夾
    current_path = os.path.abspath(os.path.dirname(__file__))
    target_folder = os.path.join(current_path, file_name, current_txt.get())
    for i in txt_path:
        txt_name = os.path.basename(i)  # 取得檔案名稱
        target_path = os.path.join(target_folder, txt_name) # 組合目標資料夾路徑與檔案名稱
        print(target_path)
        if os.path.exists(target_path):
            print("has existed")
        else:
            shutil.copy(i, target_path) # 複製檔案到目標資料夾
    
    txt_path.clear()

