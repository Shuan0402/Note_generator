import tkinter as tk
from image_button import show_image_button

class DraggableWindow:
    
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)  # 移除标题栏和窗口边框

        # 移动窗口时的动作
        self.root.bind("<ButtonPress-1>", self.start_move)
        self.root.bind("<ButtonRelease-1>", self.stop_move)
        self.root.bind("<B1-Motion>", self.do_move)

        # 设置列权重，让标签所在的列能够填充剩余空间
        self.root.columnconfigure(0, weight=1)

        # 關閉視窗
        show_image_button(root, root.destroy, [0, 1, "ne"], ["X", 25, 25])
        
        #最小化視窗
        show_image_button(root, self.minimize_action, [0, 0, "ne"], ["_", 25, 25])

        self.hidden = False  # 记录窗口的隐藏状态

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry("+{}+{}".format(x, y))

    def minimize_action(self):
        global min_window
        min_window = tk.Toplevel()  # 创建新窗口
        min_window.overrideredirect(True)
        min_window.geometry("300x100")
        restore_button = tk.Button(min_window, text="恢复窗口", command = self.restore_window)
        restore_button.pack()

        self.root.withdraw()
        
    def restore_window(self):
        min_window.destroy()
        self.root.deiconify()  # 恢复原始窗口

if __name__ == "__main__":
    root = tk.Tk()
    draggable = DraggableWindow(root)
    root.mainloop()
