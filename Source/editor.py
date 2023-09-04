from email.policy import default
import tkinter as tk
import os
try:
    from PIL import Image, ImageTk
except ImportError:
    import Image, ImageTk
from tkinter import ttk
import tkinter.colorchooser
from editor_viewer import editor_preview

# 定義顯示函式，注意一定要有一個參數
def show(e):
    temp = scale_h.get()
    font_size.set(temp)
    view_Label.config(font=('Arial', font_size.get()))  # 更新Label的字體大小


def edit(content, upload_window, window, save_path):
    upload_window.destroy()
    editor_window = tk.Toplevel(window)
    editor_window.title('edit')
    editor_window.geometry('500x500')

    # 字型大小
    global font_size, scale_test, scale_h
    font_size = tk.IntVar()
    scale_h = tk.Scale(editor_window, from_ = 1, to = 72, orient = 'horizontal', variable = font_size, command = show)
    scale_label = tk.Label(editor_window, text = 'font size', font = ('Arial', 12))
    scale_label.grid(row = 0, column = 0, columnspan = 4)
    scale_h.grid(row = 1, column = 0, columnspan = 4)

    # 版面邊界
    bound_Label = tk.Label(editor_window, bg = 'white', fg = 'black', font = ('Arial', 12), text = "bound size")
    bound_Label.grid(row = 3, column = 0, columnspan = 4)

    bound_list = ['標準', '窄', '中等', '寬']
    bound = tk.StringVar()
    bound.set(bound_list[0])
    dropdown = ttk.Combobox(editor_window, textvariable=bound, values=bound_list, state="readonly")
    dropdown.grid(row = 4, column = 0, columnspan = 4)
    dropdown.bind("<<ComboboxSelected>>", lambda event: on_selection_changed(bound.get()))


    # 字體粗細
    # 建立按鍵1
    button1 = tk.Button(editor_window, text = "正常", command = button1_click)
    button1.grid(row = 5, column = 1)
    # 建立按鍵2
    button2 = tk.Button(editor_window, text = "粗體", command = button2_click)
    button2.grid(row = 5, column = 2)

    # 背景顏色
    def open_color_chooser():
        color = tk.colorchooser.askcolor(title="Choose a color")
        if color[1]:
            selected_color_label.config(text="Selected Color: " + color[1])
            selected_color_label.config(bg=color[1])

    open_button = tk.Button(editor_window, text = "Open Color Chooser", command = open_color_chooser)
    open_button.grid(row = 6, column = 0, columnspan = 4)

    selected_color_label = tk.Label(editor_window, text = "Selected Color: ", bg = "white")
    selected_color_label.grid(row = 7, column = 0, columnspan = 4)

    image_path = os.path.join("..", "Resource", "editor_image.png")
    img = Image.open(image_path)
    img = img.resize((100, 100))  # 调整图像大小
    img_tk = ImageTk.PhotoImage(img)

    view_Label = tk.Label(editor_window, image = img_tk)
    view_Label.grid(row = 0, column = 4, columnspan = 4, rowspan = 7)
    # print(target_folder)

    editor_window.mainloop()

def button1_click():
    print("Button 1 clicked")

def button2_click():
    print("Button 2 clicked")

def on_selection_changed(selection):
    print("Selected:", selection)


def open_color_chooser():
    color = tk.colorchooser.askcolor(title="Choose a color")
    if color[1]:
        selected_color_label.config(text="Selected Color: " + color[1])
        selected_color_label.config(bg=color[1])

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Color Chooser")

    content = 'test'

    upload_window = tk.Toplevel(root)
    upload_window.title("Color Chooser")
    
    
    save_path = os.path.join("test.png")
    
    edit(content, upload_window, root, save_path)

    root.mainloop()
