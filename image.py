import tkinter as tk
from PIL import Image, ImageTk
import os

def photo(file_name):
    txt_photo = tk.Tk()
    txt_photo.title('txt_generate_photo.studio')
    txt_photo.geometry('500x500')

    current_path = os.path.abspath(os.path.dirname(__file__))
    target_folder = os.path.join(current_path, file_name)

    if os.getcwd() != target_folder:
        os.chdir(target_folder)
    print(target_folder)

    all_file_names = os.listdir()

    bg = Image.new('RGB',(1200, 800), '#000000') 
    time = 1
    for i in all_file_names:
        if i == 'oxxostudio.jpg':
            continue
        current_path = os.path.abspath(os.path.dirname(__file__))
        target_folder = os.path.join(current_path, 'test1.txt', i, 'test.jpg')
        print(target_folder)
        img = Image.open(target_folder)  # 開啟圖片
        img = img.resize((300, 400))   # 縮小尺寸為 300x400
        x = time                    # 根據開啟的順序，決定 x 座標
        y = 1                   # 根據開啟的順序，決定 y 座標 ( // 為快速取整數 )
        bg.paste(img,(x*300, y*400))   # 貼上圖片
        time += 1

    bg.save('oxxostudio.jpg')

    img = Image.open('oxxostudio.jpg')        # 開啟圖片
    tk_img = ImageTk.PhotoImage(img)    # 轉換為 tk 圖片物件

    photo = tk.Label(txt_photo, width = 100, height= 100, image = tk_img)
    photo.pack()

    txt_photo.mainloop()

photo('test1.txt')
