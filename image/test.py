import os

from PIL import Image
bg = Image.new('RGB',(1200, 800), '#000000') # 產生一張 1200x800 的全黑圖片
for i in range(1,5):
    img = Image.open(f'{i}.jpg')  # 開啟圖片
    img = img.resize((300, 400))   # 縮小尺寸為 300x400
    x = (i-1)%4                    # 根據開啟的順序，決定 x 座標
    y = (i-1)//4                   # 根據開啟的順序，決定 y 座標 ( // 為快速取整數 )
    bg.paste(img,(x*300, y*400))   # 貼上圖片

bg.save('oxxostudio.jpg')