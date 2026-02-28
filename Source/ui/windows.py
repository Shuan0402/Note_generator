# ui/windows.py
import tkinter as tk
from ui.components import show_image_button

class DraggableWindow:
    def __init__(self, root, window_size):
        self.root = root
        self.root.overrideredirect(True)  # 移除標題欄
        self.root.resizable(False, False) # 禁用調整大小

        # 視窗拖動綁定
        self.root.bind("<ButtonPress-1>", self.start_move)
        self.root.bind("<ButtonRelease-1>", self.stop_move)
        self.root.bind("<B1-Motion>", self.do_move)

        self.root.columnconfigure(0, weight=1)

        # 頂部自定義工具列框架
        self.title_frame = tk.Frame(self.root)
        self.title_frame.pack(side='top', fill=tk.X)

        # 關閉按鈕
        show_image_button('window_class', self.root, self.title_frame, 
                         self.root.destroy, [window_size[0] - 50, 0, ""], ["X", 25, 25])
        
        # 最小化按鈕
        show_image_button('window_class', self.root, self.title_frame, 
                         self.minimize_action, [window_size[0] - 101, 0, ""], ["_", 25, 25])

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        if self.x is not None and self.y is not None:
            deltax = event.x - self.x
            deltay = event.y - self.y
            new_x = self.root.winfo_x() + deltax
            new_y = self.root.winfo_y() + deltay
            self.root.geometry(f"+{new_x}+{new_y}")
            
    def minimize_action(self):
        self.min_window = tk.Toplevel()
        self.min_window.overrideredirect(True)
        self.min_window.geometry("300x50")
        
        # 使最小化的小視窗也能拖動 (可選)
        restore_button = tk.Button(self.min_window, text="恢復視窗 (Restore)", 
                                 command=self.restore_window, bg="#333", fg="white")
        restore_button.pack(fill=tk.BOTH, expand=True)
        self.root.withdraw()
        
    def restore_window(self):
        if hasattr(self, 'min_window'):
            self.min_window.destroy()
        self.root.deiconify()