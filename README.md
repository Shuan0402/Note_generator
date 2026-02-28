# Note Generator

這是一個基於 Python 與 Tkinter 開發的自動化工具，旨在將數位文本轉化為具有個人風格的真實手寫感筆記。透過字跡採集、隨機位移算法與圖像合成技術，讓生成的筆記不再生硬。

---

## 核心功能

* **自動文本分析**：掃描 `.txt` 檔案並自動提取所有不重複字元，建立字跡採集清單。
* **多樣本字跡採集**：支援同一個字元上傳多張不同的手寫圖片，增加生成結果的隨機性。
* **手寫感合成算法**：模擬真實書寫時的水平與垂直微小抖動（Random Displacement）。
* **雙平台優化**：相容於 Windows PowerShell 與 Windows 11 WSLg 環境。
* **直覺式 UI 流程**：從檔案選取、字元管理、圖片上傳到最終生成，全流程圖形化操作。

---

## 專案架構

```text
Note_generator/
├── main.py                # 程式進入點
├── config.py              # 全域路徑與參數設定（TXT_DIR, OUTPUT_DIR 等）
├── Resource/              # 存放 UI 按鈕圖示與介面素材 (Next.png, Back.png...)
├── Txt/                   # 原始文本存放區（支援 UTF-8 編碼的 .txt）
├── Generated_txt/         # 自動生成的字元資料夾庫與最終預覽圖
├── Source/
│   ├── ui/
│   │   ├── windows.py     # 視窗底層邏輯（無邊框拖拽、置中功能）
│   │   ├── viewers.py     # 核心介面邏輯（文本預覽、上傳介面、編輯器）
│   │   └── components.py  # 自定義 UI 組件（滾動區域、圖片按鈕）
│   └── core/
│       ├── image_processor.py # 圖片標準化（裁剪、去背、縮放）
│       └── generator.py       # 核心合成引擎（字元拼貼與畫布生成）
└── README.md              # 專案說明文件
```

## 環境架設與安裝
1. 系統需求
   - Python: 3.10 或更高版本。
   - 作業系統: Windows 10/11 或 Ubuntu (WSL2)。
2. 安裝必要套件
  - 本專案使用 Pillow 進行圖像處理：
    ```Bash=
    pip install Pillow
    ```
  - 註：Linux/WSL 用戶若遇到 Tkinter 缺失，請執行 sudo apt install python3-tk。
3. WSLg 用戶建議 (Windows 11)
  - 若在 WSL 中無法開啟視窗，請先在 Windows PowerShell 執行：
    ```PowerShell=
    wsl --update
    wsl --shutdown
    ```
  - 重啟後在 WSL 中執行 unset DISPLAY 即可使用系統內建的圖形支援。

## 使用步驟
1. 準備素材
    將待轉換的文字存為 .txt (UTF-8) 放入 Txt/ 資料夾。確保 Resource/ 內有必要的 UI 圖示。
2. 字元初始化
    執行 python3 main.py 並選取檔案。程式會自動分析字元，並在 Generated_txt/ 下為每個字建立專屬資料夾。
3. 採集手寫字
    點擊 Upload 進入採集介面，為清單中的每個字元上傳手寫圖片（建議使用 80x80 以上的 PNG 檔案）。
4. 生成筆記
    在最後的 Note Settings 頁面點擊 Apply & Preview：
     - 程式會自動拼接所有字跡圖片。
     - 生成的結果會顯示在右側預覽區。
     - 點擊 Open Folder 即可在 Windows 檔案總管中找到 preview.png。
