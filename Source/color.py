import tkinter as tk
import tkinter.colorchooser

def open_color_chooser():
    color = tk.colorchooser.askcolor(title="Choose a color")
    if color[1]:
        selected_color_label.config(text="Selected Color: " + color[1])
        selected_color_label.config(bg=color[1])



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Color Chooser")

    open_button = tk.Button(root, text="Open Color Chooser", command=open_color_chooser)
    open_button.pack()

    selected_color_label = tk.Label(root, text="Selected Color: ", bg="white")
    selected_color_label.pack()

    root.mainloop()