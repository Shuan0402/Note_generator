import tkinter as tk
from PIL import ImageTk, Image
import os
# def on_button_click():
#     print("generate")

# root = tk.Tk()

# def button(button_name, window, function):
#     global photo  # 將 photo 設為全域變數
#     path = "generate.jpg"
#     img = Image.open(path)
#     img = img.resize((100, 100), Image.LANCZOS)
#     photo = ImageTk.PhotoImage(img)

#     button = tk.Button(window, image=photo, compound="top", command = lambda:function, borderwidth=0, highlightthickness=0)
#     button.pack()
    
# button('generate.jpg', root, on_button_click())
# root.mainloop()

def button_click():
    # 按钮点击事件处理函数
    print("Button clicked")

def show_button(root, function):
    current_path = os.path.abspath(os.path.dirname(__file__))
    target_folder = os.path.join(current_path, r'Resource\generate.png')
    img = Image.open(target_folder)
    
    # 调整图像大小以适应按钮
    max_size = (200, 200)  # 设置按钮的最大尺寸
    img.thumbnail(max_size, Image.ANTIALIAS)

    
    show_button.tk_img = ImageTk.PhotoImage(img)

    button = tk.Button(root, image=tk_img, command=function)
    button.pack()

    # 保持对图像对象的引用，以防止被垃圾回收
    show_button.img = tk_img