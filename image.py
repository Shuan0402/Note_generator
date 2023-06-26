import tkinter as tk
from PIL import Image, ImageTk
import os
import random

def photo(file_name):

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
    
    # 初始化字符字典 list
    for i in file_key:
        if i == 'oxxostudio.jpg':
            continue
        file_image[i] = []

    # 將所有字跡儲存在相應的字典中
    for i in file_key:
        if i == 'oxxostudio.jpg':
            continue
        txt_folder = os.path.join(target_folder, i)   # 目標文件字符資料夾位置
        all_file_name = os.listdir(txt_folder)
        for j in all_file_name:
            file_image[i].append(os.path.join(current_path, file_name, i, j))

    # 創建畫布
    bg = Image.new('RGB',(1200, 800), '#FFFFFF') 

    # 拼貼圖片
    x = 0
    y = 0
    for i in content:
        if i == '\n':
            x = 0
            y += 30
        elif i == ' ':
            x += 10
        else:
            txt_len = len(file_image[i])
            txt_random = random.randint(0, txt_len - 1) 
            img = Image.open(file_image[i][txt_random])  # 開啟圖片
            img = img.resize((30, 30))   # 調整為固定尺寸 100*100
            bg.paste(img,(x, y))
            x += 30

    bg.save('oxxostudio.jpg')


def test():
    import os
    #↑載入OS模組

    dir_path = os.path.dirname(os.path.realpath(__file__))
    #↑獲取當前資料夾名稱然後存成dir_path變數

    all_file_name = os.listdir(dir_path)
    #↑讀取資料夾內所有檔案名稱然後放進all_file_name這個list裡

    print(all_file_name)

photo('test1.txt')
# test()