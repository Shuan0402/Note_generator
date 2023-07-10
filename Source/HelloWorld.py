import tkinter as tk

import tkinter.messagebox

def hello():
    print("hello, world.")

def onOK():
    # print("Hello, {}".format(entry.get()))
    msg = "Hello, {}".format(entry.get())
    tkinter.messagebox.showinfo(title = 'Hello',
                                message = msg)


window = tk.Tk()
window.title('Hello World')
window.geometry("300x100+350+150")

# 按鈕
# button = tk.Button(window,
#                     text = 'Hello',
#                     command = hello)
#
# button.pack()

# 標示文字
# label = tk.Label(window,
#                 text = 'Holle, world',
#                 bg = '#EEBB00',
#                 font = ('Arial', 12),
#                 width = 15, height = 2)

# label.pack()

# 輸入欄位
label = tk.Label(window, text = "姓名")
label.pack()

entry = tk.Entry(window, width = 20)

entry.pack()

button = tk.Button(window,
                    text = "OK", 
                    command = onOK)
button.pack()

window.mainloop()