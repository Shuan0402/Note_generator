from PIL import Image, ImageDraw, ImageFont
import os
import textwrap
from txt_content import format_text

bound = {"normal":[1.25, 1], "narrow":[0.5, 0.5], "width":[2, 1], "medium":[0.75, 1]}

def editor_preview(file_name, bg, fg, bound_size, font_size, bold_tag):
    # 設置圖片的寬度和高度(A4)
    width, height = int(8.27 * 300), int(11.69 * 300)

    # 創建一個新的空白圖片，背景顏色(bg)
    image = Image.new("RGB", (width, height), bg)

    draw = ImageDraw.Draw(image)    # 在畫布上加字

    # 字型大小(font_size)
    font = ImageFont.truetype('./msjhbd.ttc', font_size)

    # 版面配置
    text_width = int(8.27 * 300 - bound[bound_size][0] * 300 * 2) / font_size
    content = format_text(file_name, text_width)
    text_position = (int(bound[bound_size][0] * 300), int(bound[bound_size][1] * 300))  # 文字的位置
    draw.text(text_position, content, font = font, fill = fg)
    
    # 粗體
    if bold_tag:
        text_position_bold = (int(bound[bound_size][0] * 300) + 1, int(bound[bound_size][1] * 300) + 1)
        draw.text(text_position_bold, content, font = font, fill = fg)


    # 儲存圖片
    save_path = os.path.join("..", "Resource", "editor_image.png")
    image.save(save_path)

    image.show()

    print("圖片已生成並儲存", save_path)


if __name__ == "__main__":
    editor_preview("失語者", bg = "blue",fg = "white", bound_size = "narrow", font_size = 50, bold_tag = False)