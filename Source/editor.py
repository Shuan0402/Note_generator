from email.policy import default
import tkinter as tk
import os
try:
    from PIL import Image, ImageTk
except ImportError:
    import Image, ImageTk
from tkinter import ttk
import tkinter.colorchooser
from editor_viewer import EditorPreview
from window_class import DraggableWindow
from scroll import scroll, change_image

# 定義顯示函式，注意一定要有一個參數
def show(e):
    temp = scale_h.get()
    font_size.set(temp)
    view_Label.config(font=('Arial', font_size.get()))  # 更新Label的字體大小

editor_viewer = EditorPreview()

def edit(file_name, upload_window, window):
    upload_window.destroy()
    editor_window = tk.Toplevel(window)
    screen_width = window.winfo_screenwidth()   # 獲得螢幕的長
    screen_height = window.winfo_screenheight() # 獲得螢幕的高
    editor_window.geometry("845x590+" + str((screen_width - 845)//2) + "+" + str((screen_height - 590)//2))    # 宣告視窗大小且視窗置中
    draggable = DraggableWindow(editor_window, [845, 590]) 

    viewer_frame = tk.Frame(editor_window)
    viewer_frame.pack()
    

    button_frame = tk.Frame(viewer_frame)
    button_frame.pack(side = 'left', padx = 20)

    # 字型大小
    global font_size, scale_label
    font_size = tk.IntVar(value = 12)
    font_label = tk.Label(button_frame, text = 'font size', font = ('Arial', 12))
    font_label.pack(pady = 5)

    font_frame = tk.Frame(button_frame)
    font_frame.pack(pady = 5)
    scale_label = tk.Label(font_frame, text = str(font_size.get()), font = ('Arial', 12))
    scale_label.grid(row = 0, column = 1)
    font_smaller_button = tk.Button(font_frame, text = "-", command = lambda: set_font_size(editor_viewer, 'small'))
    font_smaller_button.grid(row = 0, column = 0)
    font_bigger_button = tk.Button(font_frame, text = "+", command = lambda: set_font_size(editor_viewer, 'big'))
    font_bigger_button.grid(row = 0, column = 2)
    


    # 版面邊界
    bound_Label = tk.Label(button_frame, fg = 'black', font = ('Arial', 12), text = "bound size")
    bound_Label.pack(pady = 5)

    bound_list = {'normal':'標準', 'narrow':'窄', 'medium':'中等', 'width':'寬'}
    bound = tk.StringVar()
    bound.set(bound_list['normal'])
    dropdown = ttk.Combobox(button_frame, textvariable=bound, values=list(bound_list.values()), state="readonly")
    dropdown.pack(pady = 5)
    dropdown.bind("<<ComboboxSelected>>", lambda event: on_selection_changed(bound.get()))


    # 字體粗細
    global font_weight
    font_weight_list = ['正常', '粗體']
    font_weight = tk.StringVar(value = '正常')
    weight_frame = tk.Frame(button_frame)
    weight_frame.pack(pady = 5)
    bound_button = tk.Button(weight_frame, text = "正常", command = lambda: set_font_weight('normal'))
    bound_button.pack(side = 'left')
    bold_button = tk.Button(weight_frame, text = "粗體", command = lambda: set_font_weight('bold'))
    bold_button.pack(side = 'left')

    # 背景顏色
    viewer_bg = 'white'
    viewer_fg = 'black'
    def open_color_chooser(tag):
        color = tk.colorchooser.askcolor(title = "Choose a color")
        if color[1]:
            if tag == 'bg':
                color_label.config(bg = color[1])
                viewer_bg = color[1]
            elif tag == 'fg':
                color_label.config(fg = color[1])
                viewer_fg = color[1]

    # 創建顏色預覽標籤
    color_label = tk.Label(button_frame, text = "文本預覽", bg = "white")
    color_label.pack(pady = 5)
    color_frame = tk.Frame(button_frame)
    color_frame.pack(pady = 5)
    # 创建背景颜色按钮
    bg_color_button = tk.Button(color_frame, text = "背景顏色", command = lambda: open_color_chooser('bg'))
    bg_color_button.pack(side = 'left')
    # 创建文本颜色按钮
    text_color_button = tk.Button(color_frame, text="文本顏色", command = lambda: open_color_chooser('fg'))
    text_color_button.pack(side = 'left')

    # 預覽圖片
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    image_path = os.path.join(parent_dir, "Resource", "editor_image.png")  # 假設txt資料夾的名稱是'txt資料夾'
    scroll('image', viewer_frame, [620, 530], image_path)

    test_button = tk.Button(color_frame, text="test", command = lambda: set_image('bg', 'black'))
    test_button.pack(side = 'left')

    editor_window.mainloop()
def set_font_weight(tag):
    if tag == 'normal':
        font_weight.set('正常')
    elif tag == 'bold':
        font_weight.set('粗體')
    print(font_weight.get())

def set_font_size(root, tag):
    if tag == 'big' and font_size.get() < 72:
        font_size.set(font_size.get() + 1)
    elif tag == 'small' and font_size.get() > 1:
        font_size.set(font_size.get() - 1)
    scale_label.config(text = str(font_size.get()))
    set_image('font_size', font_size.get())

def set_image(ope, value):
    # root.update_image_property(key, value)
    editor_viewer.config(ope = value)
    editor_viewer.editor_preview("test3.txt")
    change_image()
    

def on_selection_changed(selection):
    print("Selected:", selection)


def open_color_chooser():
    color = tk.colorchooser.askcolor(title="Choose a color")
    if color[1]:
        selected_color_label.config(text="Selected Color: " + color[1])
        selected_color_label.config(bg=color[1])



if __name__ == "__main__":
    root = tk.Tk()
    
    upload_window = tk.Toplevel(root)

    edit('test3.txt', upload_window, root)

    root.mainloop()
