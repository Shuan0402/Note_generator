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
    print(target_folder)
    img = Image.open(target_folder)        # 開啟圖片
    tk_img = ImageTk.PhotoImage(img)    # 轉換為 tk 圖片物件

    txt_image = tk.Label(txt_generate, image = tk_img)
    txt_image.pack()


