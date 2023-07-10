import shutil
import os

def copy_image(source_path, destination_folder):
    # 拼接目标路径
    destination_path = destination_folder + '/' + source_path.split('/')[-1]
    
    try:
        shutil.copyfile(source_path, destination_path)
        print("yes")
    except IOError:
        print("no")

# 调用函数进行复制
# current_path = os.path.abspath(os.path.dirname(__file__))
# source_path = os.path.join(current_path, 'test.jpg') # 替換為實際的絕對路徑和圖片名稱
# destination_folder = '\image'  # 替換為實際的目標資料夾路徑
# copy_image(source_path, current_path)
