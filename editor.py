from email.policy import default
import tkinter as tk
import os
try:
    from PIL import Image, ImageTk
except ImportError:
    import Image, ImageTk

# 定義顯示函式，注意一定要有一個參數
def show(e):
    temp = scale_h.get()
    font_size.set(temp)
    scale_test.config(font=('Arial', font_size.get()))  # 更新Label的字體大小


def edit(content, txt_window):
    editor_window = tk.Toplevel(txt_window)
    editor_window.title('edit')
    editor_window.geometry('300x300')

    # 字型大小
    global font_size, scale_test, scale_h
    font_size = tk.IntVar()
    scale_test = tk.Label(editor_window, text = content, font = ('Arial', font_size.get()))
    scale_h = tk.Scale(editor_window, from_ = 1, to = 72, orient='horizontal',variable = font_size, command = show)  # 改變時執行 show
    
    scale_label = tk.Label(editor_window, text = 'font size', font = ('Arial', 12))
    scale_label.pack()
    scale_h.pack()
    scale_test.pack()

    # 版面邊界
    bound_Label = tk.Label(editor_window, bg = 'white', fg = 'black', font = ('Arial', 12), text = "bound size")
    bound_Label.pack()
    bound_list = ['標準', '窄', '中等', '寬']
    bound = tk.StringVar()
    listbox = tk.Listbox(editor_window)    
    for item in bound_list:
        listbox.insert('end', item)  
    listbox.pack()




    editor_window.mainloop()


# edit()
    
