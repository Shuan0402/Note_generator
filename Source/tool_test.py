import tkinter as tk

def update(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

window = tk.Tk()
window.title('資料庫寫入程式')
window.configure(bg="#7AFEC6")
window.geometry("350x150+300+200")
text = []

## 調整canvas畫布的大小與視窗對齊
canvas = tk.Canvas(window, width=330,height=150, bg="#FFFFFF")
canvas.grid(column=0, row=0)
scrollbar = tk.Scrollbar(window, orient='vertical',command=canvas.yview)
scrollbar.grid(column=1, row=0,sticky = 'ns')

frame = tk.Frame(canvas)   # 建立 Frame
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>", update)
canvas.config(yscrollcommand=scrollbar.set)

## 測試效果，可放你想放的元件內容
for i in range(100):
    tmp_text = tk.Label(frame, text = 'Hello world '+ str(i))
    tmp_text.grid(column=0, row=i)
    text.append(tmp_text)



window.mainloop()