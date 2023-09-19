import tkinter as tk

class DraggableWindow:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)  # 移除標題欄和窗口邊框
        self.root.bind("<ButtonPress-1>", self.start_move)
        self.root.bind("<ButtonRelease-1>", self.stop_move)
        self.root.bind("<B1-Motion>", self.do_move)

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

# root = tk.Tk()
# root.geometry("300x200")

# draggable = DraggableWindow(root)

# exit_button = tk.Button(root, text="Exit", command=root.destroy)
# exit_button.pack()

# root.mainloop()
