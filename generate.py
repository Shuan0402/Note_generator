import tkinter as tk
from PIL import Image, ImageTk
from image import photo
import os

def generate(txt_window, root, file_name):
    # 建立預覽圖片視窗
    txt_generate = tk.Toplevel(root)  # 使用 Toplevel() 創建新的視窗，而不是 tk.Tk()
    txt_generate.title('TXT_Generate')
    txt_generate.geometry("500x600+400+200")
    txt_window.destroy()
    
    # 生成圖片
    photo(file_name)

    # 取得圖片位置
    current_path = os.path.abspath(os.path.dirname(__file__))
    target_folder = os.path.join(current_path, file_name, 'oxxostudio.jpg')   # 目標文件字符資料夾位置
    # print(target_folder)
    if os.path.exists(target_folder):
        print("yes")
    else:
        print("no")

    # # 讀取圖片
    # img = Image.open(target_folder)

    # # 創建圖像物件
    # img_obj = ImageTk.PhotoImage(img)

    # # 創建Label元件並顯示圖像
    # label = tk.Label(txt_generate, image=img_obj)
    # label.pack()

    selection_buttom = tk.Button(txt_generate, text = 'test', width = 15, height = 2, command = test)
    selection_buttom.pack()

def test():
    print('test')


