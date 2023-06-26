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
    upload_window = tk.Toplevel(txt_window)  # 使用 Toplevel() 創建新的視窗，而不是 tk.Tk()
    upload_window.title('upload')
    upload_window.geometry("500x600+200+200")

    current_path = os.path.abspath(os.path.dirname(__file__))
    target_folder = os.path.join(current_path, file_name)
    if os.getcwd() != target_folder:
        os.chdir(target_folder)

    all_file_names = os.listdir()
    all_file_names.remove('oxxostudio.jpg')
    upload_button = []
    time = 0

    file_list = {}
    for i in all_file_names:
        upload_button(i, upload_window, file_list)

        

def upload_button(file_name, upload_window):
    txt_upload = tk.Label(upload_window, bg = 'white', fg = 'black', font = ('Arial', 12), width = 10, text = i)
    txt_upload.pack()

    upload_button = tk.Button(upload_window, text = i, width = 15, height = 2, command = lambda: show(name, upload_window))
    upload_button.pack()
    