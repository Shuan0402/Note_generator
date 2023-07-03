import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
from copy_img import copy_image
import shutil

def path_list(file_list, file_name, file_path):
    file_list[file_name] = file_path



def show(txt, upload_window):
    file_path = filedialog.askopenfilename()
    if os.path.exists(file_path):
        upload_path_Label = tk.Label(upload_window, bg = 'white', fg = 'black', font = ('Arial', 12), width = 10, text = file_path)
        upload_path_Label.pack()
        path_list(file_list, txt, file_path)
        print(file_list)
    else:
        print('no')
    
    
        
    
    # f = open(file_path,'r')      # 根據檔案路徑開啟檔案
    # a = f.read()                 # 讀取檔案內容
    # text = tk.StringVar()   # 設定 text 為文字變數
    # text.set(a)                  # 設定變數為檔案內容
    # f.close()                    # 關閉檔案
    # mylabel = tk.Label(txt_window, textvariable=text, font=('Arial',20))  # 放入標籤，使用 textvariable=text
    # mylabel.pack()


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

    global current_txt
    current_txt = tk.StringVar()
    current_txt.set(all_file_names[0])
    current_txt_Label = tk.Label(upload_window, bg = 'white', fg = 'black', font = ('Arial', 12), textvariable = current_txt)
    current_txt_Label.pack()
    upload_button = tk.Button(upload_window, text = 'upload', width = 15, height = 2, command = lambda:upload_image(current_txt, upload_window))
    upload_button.pack()
    next_button = tk.Button(upload_window, text = 'next', width = 15, height = 2, command = lambda:next_txt(current_txt, all_file_names, upload_window))
    next_button.pack()
    

def upload_image(txt, upload_window):
    print("Upload")
    file_path = filedialog.askopenfilename()
    if os.path.exists(file_path):
        upload_path_Label = tk.Label(upload_window, bg = 'white', fg = 'black', font = ('Arial', 12), text = file_path)
        upload_path_Label.pack()
        path_list(file_list, txt, file_path)
        print(file_list)
    else:
        print('no')

def next_txt(current_element, all_file_names, upload_window):
    current_element = current_element.get()  # 获取 StringVar 对象的值
    if current_element == all_file_names[-1]:
        print(current_element)
        clear_window(upload_window)
        complete_Label = tk.Label(upload_window, bg = 'white', fg = 'black', font = ('Arial', 12), text = 'complete')
        complete_Label.pack()
    else:
        current_index = all_file_names.index(current_element) + 1
        current_txt.set(all_file_names[current_index])
        print(current_element)
    

        

def clear_window(window):
    for widget in window.winfo_children():
        widget.pack_forget()  # 或者使用 grid_forget() 或 place_forget()


# def upload_button(file_name, upload_window):
#     txt_upload = tk.Label(upload_window, bg = 'white', fg = 'black', font = ('Arial', 12), width = 10, text = i)
#     txt_upload.pack()

#     upload_button = tk.Button(upload_window, text = i, width = 15, height = 2, command = lambda: show(name, upload_window))
#     upload_button.pack()
    