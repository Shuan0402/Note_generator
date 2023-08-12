import tkinter as tk

def minimize_window():
    root.wm_state('iconic')

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('300x200')
    root.title("最小化視窗示例")

    label = tk.Label(root, text="這是一個Label")
    label.pack()

    button = tk.Button(root, text="最小化視窗", command=minimize_window)
    button.pack()

    root.mainloop()
