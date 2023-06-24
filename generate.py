import tkinter as tk
from PIL import Image, ImageTk

def generate(txt_window, root):
    # 建立預覽圖片
    txt_generate = tk.Toplevel(root)  # 使用 Toplevel() 創建新的視窗，而不是 tk.Tk()
    txt_generate.title('TXT_Generate')
    txt_generate.geometry("500x600+400+200")
    txt_window.destroy()

