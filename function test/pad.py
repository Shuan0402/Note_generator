import tkinter as tk

root = tk.Tk()
root.title("Padding Example")

# 創建Frame並使用padx和pady外部填充
frame_pad = tk.Frame(root, padx=10, pady=10)
frame_pad.pack()

# 在Frame中創建Entry
entry = tk.Entry(frame_pad, width=20)
entry.pack(ipadx=100, ipady=100)

root.mainloop()
