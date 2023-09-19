import tkinter as tk
from tkinter import Canvas, Scrollbar
from PIL import Image, ImageTk
import os

# 声明全局变量
text_widget = None

def scroll_text(event):
    global text_widget
    if text_widget:
        text_widget.yview_scroll(-1*(event.delta//120), "units")

def on_mousewheel(event):
    scroll_canvas.yview_scroll(-1*(event.delta//120), "units")

global scroll_canvas
canvas_width = 620
canvas_height = 530

def scroll(tag, root, size, file_comment):
    global text_widget, scroll_canvas
    if tag == 'text':
        # 创建一个文本框
        text_widget = tk.Text(root, wrap = tk.WORD, width = size[0], height = size[1])
        text_widget.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)

        # 创建一个滚动条并与文本框关联
        scrollbar = Scrollbar(root, command = text_widget.yview)
        scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        text_widget.config(yscrollcommand = scrollbar.set)

        # 添加一些示例文本
        text_widget.insert(tk.END, file_comment)

        # 绑定鼠标滚轮事件以实现滚动
        text_widget.bind("<MouseWheel>", scroll_text)
    
    
    elif tag == 'image':
        def on_canvas_configure(event):
            scroll_canvas.configure(scrollregion=scroll_canvas.bbox("all"))

        # 创建 Canvas 和 Frame
        image_frame = tk.Frame(root)
        image_frame.pack(pady=20, side = 'left')

        image_frame = tk.Frame(image_frame)
        image_frame.pack()

        # 创建垂直滚动条
        scrollbar = tk.Scrollbar(image_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        # 创建 Canvas，并将滚动条与 Canvas 链接

        scroll_canvas = tk.Canvas(image_frame, width=canvas_width, height=canvas_height, yscrollcommand=scrollbar.set)
        scroll_canvas.pack()

        scrollbar.config(command=scroll_canvas.yview)

        # 打开图像文件并调整大小以适应 Canvas
        img = Image.open(file_comment)
        img.thumbnail((canvas_width, img.height))

        # 将图像转换为 PhotoImage 对象并在 Canvas 上显示
        global tk_img
        tk_img = ImageTk.PhotoImage(img)
        scroll_canvas.create_image(0, 0, anchor='nw', image=tk_img)

        # 监听 Canvas 大小的变化以更新滚动区域
        scroll_canvas.bind("<Configure>", on_canvas_configure)
    
def change_image():
    global tk_img, scroll_canvas

    # 关闭之前的图像
    scroll_canvas.delete("all")

    # 打开新图像文件并调整大小以适应 Canvas
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    image_path = os.path.join(parent_dir, "Resource", "editor_image.png")  # 假設txt資料夾的名稱是'txt資料夾'
    
    new_img = Image.open(image_path)
    new_img.thumbnail((canvas_width, new_img.height))

    # 将新图像转换为 PhotoImage 对象并在 Canvas 上显示
    tk_img = ImageTk.PhotoImage(new_img)
    scroll_canvas.create_image(0, 0, anchor='nw', image=tk_img)

    # 更新 Canvas 的滚动区域
    scroll_canvas.configure(scrollregion=scroll_canvas.bbox("all"))




if __name__ == "__main__":
    # 创建主窗口
    root = tk.Tk()
    root.title("Text Viewer")

    file_comment = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Praesent in libero id libero hendrerit accumsan. Vivamus facilisis purus 
    eget congue sodales. Integer id metus quis erat sollicitudin fermentum. 
    Fusce at lectus ut elit aliquet congue. Donec scelerisque dui id lectus 
    eleifend, a efficitur lectus egestas. Quisque non urna eget quam dictum 
    cursus. Nam at metus ut nunc facilisis luctus vel a urna. Duis tincidunt 
    justo id eros bibendum interdum. Etiam eget leo sed neque porttitor 
    venenatis. Vivamus eget dolor in metus eleifend hendrerit."""

    # scroll('text', root, [40, 10], file_comment)
    scroll('image', root, [1000, 1000], "editor_image.png")
    # 创建一个按钮来切换图像
    change_image_button = tk.Button(root, text = "切换图像", command = change_image)
    change_image_button.pack()

    # 启动主循环
    root.mainloop()
