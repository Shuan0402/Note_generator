import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
from copy_img import copy_image
from editor import edit
from window_class import DraggableWindow
import shutil
from image_button import show_image_button

# 上傳字符的視窗
def goto_upload(file_name, txt_window, window):
    # 創建上傳的視窗
    txt_window.destroy()
    upload_window = tk.Toplevel(window)
    screen_width = upload_window.winfo_screenwidth()   # 獲得螢幕的長
    screen_height = upload_window.winfo_screenheight() # 獲得螢幕的高
    upload_window.geometry("845x590+" + str((screen_width - 845)//2) + "+" + str((screen_height - 590)//2-10))    # 宣告視窗大小且視窗置中
    draggable = DraggableWindow(upload_window, [845, 590])
    
    # 確認所須字符
    current_path = os.path.abspath(os.path.dirname(__file__))
    parent_path = os.path.abspath(os.path.join(current_path, os.pardir))
    target_folder = os.path.join(parent_path, 'Generated_txt', file_name)
    if os.getcwd() != target_folder:
        os.chdir(target_folder)
    all_file_names = os.listdir()
    if 'oxxostudio.jpg' in all_file_names:
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
    current_txt_Label.pack()
    
    global upload_frame
    upload_frame = tk.Frame(upload_window)  # 加入 Frame 框架
    upload_frame.pack()
    show_image_button('upload', upload_window, upload_frame, lambda: upload_image(current_txt, upload_window, file_name, target_folder), [4, 0, ""], ["Upload", 100, 100])

    
    # 上下一個字符按鍵
    global next_back_frame
    next_back_frame = tk.Frame(upload_window)  # 加入 Frame 框架
    next_back_frame.pack()
    show_image_button('upload next_back', upload_window, next_back_frame, lambda: change_txt(current_txt, all_file_names, upload_window, file_name, 'next', window), [4, 0, "right"], ["Next", 100, 100])
    show_image_button('upload next_back', upload_window, next_back_frame, lambda: change_txt(current_txt, all_file_names, upload_window, file_name, 'back', window), [4, 0, "right"], ["Back", 100, 100])
    
    # 顯示當前字符的所有筆跡
    show_path(upload_window, file_name, current_txt.get())

# 上傳字符
def upload_image(txt, upload_window, file_name, current_path):
    file_path = filedialog.askopenfilename()

    # 選取相同路徑
    if file_path in txt_path_folder[current_txt.get()]:
        print("same file")
        return
    # 路徑是否存在
    elif os.path.exists(file_path):
        txt_path_folder[current_txt.get()].append(file_path)    # 在當前上傳字符的資料夾新增選取的檔案路徑
        target_folder = os.path.join(current_path, current_txt.get())   # 獲得當前上傳字符的資料夾位置
        # 替新圖片路徑取名
        txt_name = os.path.basename(file_path)  # 取得檔案名稱
        target_path = os.path.join(target_folder, txt_name) # 組合目標資料夾路徑與檔案名稱
        if os.path.exists(target_path):
            print("has existed")
        else:
            shutil.copy(file_path, target_path) # 複製檔案到目標資料夾
            show_path(upload_window, file_name, current_txt.get())  # 預覽上傳的圖片

        print(txt_path_folder[current_txt.get()])

    else:
        print('file path doesn\'t exist')

# 變換字符
def change_txt(current_element, all_file_names, upload_window, file_name, tag, window):
    # 上一個字符
    if tag == 'back':
        if current_element.get() == all_file_names[0]:
            print("already the first txt")
        else:
            if current_element.get() == all_file_names[-1]:
                upload_button.pack()
                next_button.pack()
            current_index = all_file_names.index(current_element.get()) - 1   # 獲得當前字符的順序位置，並往後移到上一位
            current_txt.set(all_file_names[current_index])  # 將上一個字符設為當前字符
        show_path(upload_window, file_name, current_txt.get())
    
    # 下一個字符
    elif tag == 'next':
        # 最後一個字符
        if current_element.get() == all_file_names[-1]:   # 如果此字符位最後一個字符，則直接結束
        # 清理視窗
            clear_path(upload_window, False)
            next_back_frame.pack_forget()
            complete_Label = tk.Label(upload_window, bg = 'white', fg = 'black', font = ('Arial', 12), text = 'complete')
            complete_Label.pack()
            content = 'test'
            
            edit_frame = tk.Frame(upload_window)  # 加入 Frame 框架
            edit_frame.pack()
            show_image_button('upload', upload_window, edit_frame, lambda: edit(file_name, upload_window, window), [4, 0, "right"], ["Edit", 100, 100])
    

        else:
            current_index = all_file_names.index(current_element.get()) + 1   # 獲得當前字符的順序位置，並往後移到下一位
            current_txt.set(all_file_names[current_index])  # 將下一個字符設為當前字符
            show_path(upload_window, file_name, current_txt.get())


# 清除螢幕
def clear_window(window):
    time = 0
    for widget in window.winfo_children():
        if time <= 2:
            time += 1
        else:
            widget.pack_forget()  # 或者使用 pack_forget() 或 place_forget()

# 清除前一個字符的路徑
def clear_path(window, tag):

    time = 0
    non_resident = [current_txt_Label, upload_frame, next_back_frame]

    # 遍历窗口中的子部件
    for widget in window.winfo_children():
        if time < 1:
            time +=1
        elif widget in non_resident and tag:
            continue  # 跳过常驻内容部件
        else:
            widget.pack_forget()  # 隐藏非常驻内容部件

# 刪除路徑
def delete(path, Label, Button, upload_window, file_name):
    if os.path.exists(path):
        os.remove(path)
        Label.pack_forget()
        Button.pack_forget()
        show_path(upload_window, file_name, current_txt.get())
        print("has deleted")
    else:
        print("path doesn\'t exist")

# 用於換頁的字跡顯示
def show_path(upload_window, file_name, txt):
    clear_path(upload_window, True)

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
        label.pack()
        del_button = tk.Button(upload_window, text = 'delete', command = lambda: delete(image_path, label, del_button, upload_window, file_name))
        del_button.pack()
        

        # 将Label和图像对象的引用添加到列表中
        labels.append((label, img_tk))

    # 将Label和图像对象的引用存储在窗口属性中，以便后续访问
    upload_window.image_labels = labels

if __name__ == "__main__":
    root = tk.Tk()
    pass_window = tk.Toplevel(root)
    goto_upload('test3.txt', pass_window, root)
    root.mainloop()