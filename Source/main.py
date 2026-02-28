# Source/main.py
import tkinter as tk
from tkinter import ttk
import traceback
from config import TXT_DIR
from ui.windows import DraggableWindow
from ui.viewers import txt_viewer

class NoteGeneratorApp:
    def __init__(self, root):
        self.root = root
        
        # 1. 初始化視窗與變數
        self.setup_window()
        
        # 關鍵點：在這裡先定義好變數
        self.selected_option = tk.StringVar() 
        
        # 2. 顯示選單
        self.show_main_menu()

    def setup_window(self):
        width, height = 845, 590
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        self.root.geometry(f"{width}x{height}+{(sw-width)//2}+{(sh-height)//2}")
        # 初始化拖動功能
        self.draggable = DraggableWindow(self.root, [width, height])

    def show_main_menu(self):
        # 清理畫面（保留標題列）
        for widget in self.root.winfo_children()[1:]:
            widget.destroy()

        # 取得所有 txt 檔案
        files = [f.name for f in TXT_DIR.glob("*.txt")]
        if not files:
            files = ["README.txt"]
        
        self.selected_option.set(files[0]) # 設定預設值

        # 下拉選單
        # 注意：這裡要確保第一個參數是 self.root，且 variable 是 self.selected_option
        self.dropdown = ttk.OptionMenu(
            self.root, 
            self.selected_option, 
            files[0], 
            *files
        )
        self.dropdown.pack(pady=50)

        # 啟動按鈕
        self.selection_button = tk.Button(
            self.root, 
            text='Start Processing', 
            width=15, 
            height=2, 
            command=self.safe_start_processing # 呼叫下方的方法
        )
        self.selection_button.pack()

    def safe_start_processing(self):
        try:
            # 現在 self.selected_option 已經被正確定義了
            filename = self.selected_option.get() 
            print(f"--- 偵錯：嘗試開啟 {filename} ---")
            
            # 清除選單介面，準備進入預覽
            for widget in self.root.winfo_children()[1:]:
                widget.pack_forget()

            # 呼叫 ui/viewers.py 裡的 txt_viewer
            txt_viewer(filename, self.root)
            
        except Exception as e:
            print("\n!!! 執行時出錯 !!!")
            traceback.print_exc()

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteGeneratorApp(root)
    root.mainloop()