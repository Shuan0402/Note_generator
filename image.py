import tkinter as tk
from PIL import Image, ImageTk
import os

def photo(file_name):
    # 圖像顯示視窗
    # txt_photo = tk.Tk()
    # txt_photo.title('txt_generate_photo')
    # txt_photo.geometry('500x500')

    # 獲得當前與目的文件位置
    current_path = os.path.abspath(os.path.dirname(__file__))
    target_folder = os.path.join(current_path, file_name)   # 目標文件字符資料夾位置
    txt_file = os.path.join(current_path, 'txt', file_name)   # 目標文件位置
    
    # 獲得完整文件
    with open(txt_file) as f:
        content = f.read()

    # 確保程式在運行時正確處於指定的目錄
    if os.getcwd() != target_folder:
        os.chdir(target_folder)

    # 儲存資料夾內所有字符與其位置
    file_key = os.listdir()
    file_image = {}
    for i in file_key:
        if i == 'oxxostudio.jpg':
            continue
        file_image[i] = os.path.join(current_path, file_name, i, 'test.jpg')

    # 創建畫布
    bg = Image.new('RGB',(1200, 800), '#000000') 

    # 拼貼圖片
    x = 0
    y = 0
    for i in content:
        if i == '\n':
            x = 0
            y += 100
        else:
            img = Image.open(file_image[i])  # 開啟圖片
            img = img.resize((100, 100))   # 調整為固定尺寸 100*100
            bg.paste(img,(x, y))
            x += 100

    bg.save('oxxostudio.jpg')

    

    # txt_photo.mainloop()

photo('test1.txt')
