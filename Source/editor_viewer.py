from PIL import Image, ImageDraw, ImageFont
import os
import textwrap
from txt_content import format_text

bound = {"normal":[1.25, 1], "narrow":[0.5, 0.5], "width":[2, 1], "medium":[0.75, 1]}

class EditorPreview:
    def __init__(self):
        self.width = int(8.27 * 300)
        self.height = int(11.69 * 300)
        self.bg = "blue"
        self.fg = "white"
        self.bound_size = "normal"
        self.font_size = 12
        self.bold_tag = False
        self.save_path = None  # 初始化为 None

    def config(self, **kwargs):
        if 'width' in kwargs:
            self.width = kwargs['width']
        if 'height' in kwargs:
            self.height = kwargs['height']
        if 'bg' in kwargs:
            self.bg = kwargs['bg']
        if 'fg' in kwargs:
            self.fg = kwargs['fg']
        if 'bound_size' in kwargs:
            self.bound_size = kwargs['bound_size']
        if 'font_size' in kwargs:
            self.font_size = kwargs['font_size']
        if 'bold_tag' in kwargs:
            self.bold_tag = kwargs['bold_tag']

    def editor_preview(self, file_name):
        # 创建新的空白图像，背景颜色(self.bg)
        image = Image.new("RGB", (self.width, self.height), self.bg)
        draw = ImageDraw.Draw(image)  # 在画布上添加字

        # 字体大小(self.font_size)
        font = ImageFont.truetype('./msjhbd.ttc', int(self.font_size * (40 / 12)))

        # 版面配置
        text_width = int(self.width - bound[self.bound_size][0] * 300 * 2) / self.font_size
        content = format_text(file_name, text_width)
        text_position = (int(bound[self.bound_size][0] * 300), int(bound[self.bound_size][1] * 300))  # 文字的位置
        draw.text(text_position, content, font=font, fill=self.fg)
        
        # 粗体
        if self.bold_tag:
            text_position_bold = (int(bound[self.bound_size][0]) + 1, int(bound[self.bound_size][1]) + 1)
            draw.text(text_position_bold, content, font=font, fill=self.fg)

        # 储存图像
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        self.save_path = os.path.join(parent_dir, "Resource", "editor_image.png")  # 假設txt資料夾的名稱是'txt資料夾'
        
        image.save(self.save_path)
        # image.show()

    def update_image_property(self, key, value):
        if hasattr(self, key):
            setattr(self, key, value)
            self.editor_preview("test3.txt")
            image = Image.open(self.save_path)
            # image.show()

if __name__ == "__main__":
    editor_viewer = EditorPreview()
    editor_viewer.config(bg="white", fg="black", bound_size="normal", font_size=18)
    editor_viewer.editor_preview("test3.txt")
    
    # 更新图像属性并显示更新后的图像
    editor_viewer.update_image_property('bg', 'red')
