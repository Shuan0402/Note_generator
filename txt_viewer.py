import tkinter as tk
import os

def txt_viewer(file_name, window):
    txt_window = tk.Toplevel(window)  # 使用 Toplevel() 創建新的視窗，而不是 tk.Tk()
    txt_window.title('TXT')
    txt_window.geometry("500x600+200+200")
    
    with open(file_name) as f:
        content = f.read()

    txt_Label = tk.Label(txt_window, bg = 'white', fg = 'black', font = ('Arial', 12), width = 10, text = content)
    txt_Label.pack()

    yes_button = tk.Button(txt_window, text = 'Yes', width = 15, height = 2, command = lambda: class_txt(txt_window, file_name))
    no_button = tk.Button(txt_window, text = 'No', width = 15, height = 2, command = lambda: close_window(txt_window))
    yes_button.place(x = 130, y = 50)
    no_button.place(x = 260, y = 50)

def close_window(root):
    root.destroy()

def class_txt(root, file_name):
    # 建立文字資料夾
    current_path = os.path.abspath(os.path.dirname(__file__))
    target_folder = os.path.join(current_path, file_name)
    if not os.path.isdir(target_folder):
        os.mkdir(target_folder)

    # 統計文字符號
    txt = []
    with open(file_name) as f:
        content = f.read()
    for i in content:
        if i in txt or i == '\n':
            continue
        else:
            txt.append(i)
            txt_list = os.path.join(target_folder, i)
        if not os.path.isdir(txt_list):
            os.mkdir(txt_list)
            
    
    root.destroy()