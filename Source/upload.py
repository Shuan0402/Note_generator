import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
from copy_img import copy_image
from editor import edit
import shutil
# 上傳字符的視窗
def upload(file_name, txt_window):
    # 創建上傳的視窗
    upload_window = tk.Toplevel(txt_window)
    upload_window.title('upload')
    upload_window.geometry("500x600+200+200")

    # 確認所須字符
    current_path = os.path.abspath(os.path.dirname(__file__))
    parent_path = os.path.abspath(os.path.join(current_path, os.pardir))
    target_folder = os.path.join(parent_path, 'Generated_txt', file_name)
    if os.getcwd() != target_folder:
        os.chdir(target_folder)
    all_file_names = os.listdir()
    all_file_names.remove('oxxostudio.jpg')

    # 建立所有字符的路徑資料夾
    global txt_path_folder
    txt_path_folder = {}
    for i in all_file_names:
        txt_folder = os.path.join(target_folder, i)
        all_txt_file = os.listdir(txt_folder)
        txt_path_folder[i] = []
        for j in all_txt_file:
            ori_txt_path = os.path.join(txt_folder, j)
            txt_path_folder[i].append(ori_txt_path)

    # 建立當前字符的全域變數
    global current_txt
    current_txt = tk.StringVar()
    current_txt.set(all_file_names[0])  # 預設為第一個字符
    
    # 宣告常駐內容
    global current_txt_Label, upload_button, next_button, back_button

    # 顯示目前字符
    current_txt_Label = tk.Label(upload_window, bg = 'white', fg = 'black', font = ('Arial', 12), textvariable = current_txt)
    current_txt_Label.grid(row = 0, column = 0, columnspan = 2)
    
    # 上傳圖片按鍵
    upload_button = tk.Button(upload_window, text = 'upload', width = 15, height = 2, command = lambda:upload_image(current_txt, upload_window, file_name))
    upload_button.grid(row = 1, column = 0, columnspan = 2)
    
    # 下一個字符按鍵
    next_button = tk.Button(upload_window, text = 'next', width = 15, height = 2, command = lambda:change_txt(current_txt, all_file_names, upload_window, file_name, 'next'))
    next_button.grid(row = 2, column = 1)
    
    # 上一個字符按鍵
    back_button = tk.Button(upload_window, text = 'back', width = 15, height = 2, command = lambda:change_txt(current_txt, all_file_names, upload_window, file_name, 'back'))
    back_button.grid(row = 2, column = 0)
    
    # 顯示當前字符的所有筆跡
    show_path(upload_window, file_name, current_txt.get())

    


# 上傳字符
def upload_image(txt, upload_window, file_name):
    file_path = filedialog.askopenfilename()

    # 選取相同路徑
    if file_path in txt_path_folder[current_txt.get()]:
        print("same file")
        return

    # 路徑是否存在
    elif os.path.exists(file_path):
        txt_path_folder[current_txt.get()].append(file_path)
        print(txt_path_folder[current_txt.get()])
    else:
        print('file path doesn\'t exist')

# 變換字符
def change_txt(current_element, all_file_names, upload_window, file_name, tag):
    current_element = current_element.get()  # 獲取當前的字符
    # copy_txt(file_name, current_txt)
    
    
    # 上一個字符
    if tag == 'back':
        if current_element == all_file_names[0]:
            print("already the first txt")
        else:
            current_index = all_file_names.index(current_element) - 1   # 獲得當前字符的順序位置，並往後移到上一位
            current_txt.set(all_file_names[current_index])  # 將上一個字符設為當前字符
        show_path(upload_window, file_name, current_txt.get())
    
    # 下一個字符
    elif tag == 'next':
        # 最後一個字符
        if current_element == all_file_names[-1]:   # 如果此字符位最後一個字符，則直接結束
        # 清理視窗
            clear_window(upload_window)
            complete_Label = tk.Label(upload_window, bg = 'white', fg = 'black', font = ('Arial', 12), text = 'complete')
            complete_Label.grid(row = 0, column = 0, columnspan = 2)

        else:
            current_index = all_file_names.index(current_element) + 1   # 獲得當前字符的順序位置，並往後移到下一位
            current_txt.set(all_file_names[current_index])  # 將下一個字符設為當前字符
            show_path(upload_window, file_name, current_txt.get())

def complete(content, upload_window):
    edit_button = tk.Button(upload_window, text = 'edit', width = 15, height = 2, command=lambda:edit(content, upload_window))
    edit_button.grid(row = 5, column = 0,columnspan = 2)

# 清除螢幕
def clear_window(window):
    for widget in window.winfo_children():
        widget.grid_forget()  # 或者使用 grid_forget() 或 place_forget()

# 清除前一個字符的路徑
def clear_path(window):
    time = 0
    non_resident = [current_txt_Label, upload_button, next_button, back_button]

    # 遍历窗口中的子部件
    for widget in window.winfo_children():
        if widget in non_resident:
            continue  # 跳过常驻内容部件
        else:
            widget.grid_forget()  # 隐藏非常驻内容部件


# 刪除路徑
def delete(path, Label, Button):
    if os.path.exists(path):
        os.remove(path)
        Label.grid_forget()
        Button.grid_forget()
        print("has deleted")
    else:
        print("path doesn\'t exist")

# 將選取的圖片複製到當前字符的資料夾
def copy_txt(file_name, current_txt):
    # 跳到正確位置
    current_path = os.path.abspath(os.path.dirname(__file__))
    parent_path = os.path.abspath(os.path.join(current_path, os.pardir))
    target_folder = os.path.join(parent_path, 'Generated_txt', file_name, current_txt.get())
    
    # 將所有選取檔案複製到指定資料夾
    for i in txt_path:
        txt_name = os.path.basename(i)  # 取得檔案名稱
        target_path = os.path.join(target_folder, txt_name) # 組合目標資料夾路徑與檔案名稱
        if os.path.exists(target_path):
            print("has existed")
        else:
            shutil.copy(i, target_path) # 複製檔案到目標資料夾
    
    # 初始化位址資料夾
    txt_path.clear()

# 用於換頁的字跡顯示
def show_path(upload_window, file_name, txt):
    clear_path(upload_window)
    

    # 獲得該字符的所有字跡之路徑
    current_path = os.path.abspath(os.path.dirname(__file__))   # 此檔案位置
    parent_path = os.path.abspath(os.path.join(current_path, os.pardir))    # 回上層資料夾
    target_folder = os.path.join(parent_path, 'Generated_txt', file_name, txt)  # 到指定字符資料夾
    image_files = [f for f in os.listdir(target_folder) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]   # 獲得指定字符所有字跡的檔案名稱

    # 创建一个列表来存储Label和图像对象的引用
    labels = []

    for i in image_files:
        image_path = os.path.join(target_folder, i)
        img = Image.open(image_path)
        img = img.resize((100, 100))  # 调整图像大小
        img_tk = ImageTk.PhotoImage(img)

        label = tk.Label(upload_window, image = img_tk)
        label.grid(row = 3 + len(labels), column = 0)
        del_button = tk.Button(upload_window, text = 'delete', command = lambda: delete(image_path, label, del_button))
        del_button.grid(row = 3 + len(labels), column = 1)
        

        # 将Label和图像对象的引用添加到列表中
        labels.append((label, img_tk))

    # 将Label和图像对象的引用存储在窗口属性中，以便后续访问
    upload_window.image_labels = labels



# window = tk.Tk()
# window.title('upload_window')
# window.geometry("845x590")

# show_path(window, 'test3.txt', 't')

# window.mainloop()