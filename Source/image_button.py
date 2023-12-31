import tkinter as tk
from PIL import ImageTk, Image
import os

def button_click():
    print("Button clicked")

def show_image_button(tag, root, frame , function, location, button_data):
    current_path = os.path.abspath(os.path.dirname(__file__))
    parent_path = os.path.abspath(os.path.join(current_path, os.pardir))
    target_folder = os.path.join(parent_path, r'Resource' + "\\" + button_data[0] + ".png")
    img = Image.open(target_folder)
    
    # 调整图像大小以适应按钮
    max_size = (button_data[1], button_data[2])  # 设置按钮的最大尺寸
    img.thumbnail(max_size, Image.ANTIALIAS)

    tk_img = ImageTk.PhotoImage(img)

    
    button = tk.Button(frame, image = tk_img, command = function, borderwidth = 0, highlightthickness = 0)
    button.image = tk_img  # 将 tk_img 对象附加到按钮对象

    if tag == 'window_class':
        button.pack(side = 'right', padx = 1, pady = 1)
    elif tag == 'txt_viewer content' or tag == 'upload next_back':    # next_back_frame
        button.pack(side = location[2])
    else:
        button.pack()




if __name__ == "__main__":
    root = tk.Tk()
    frame = tk.Frame(root)                  # 加入 Frame 框架
    frame.pack(side = 'top', fill = tk.X)
    show_image_button(root, frame, button_click, [0, 1, "ne"], ["X", 50, 50])
    show_image_button(root, frame, button_click, [0, 0, "ne"],  ["_", 50, 50])  # 使用不同的按钮名
    root.mainloop()
