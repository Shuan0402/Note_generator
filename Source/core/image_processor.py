# core/image_processor.py
from PIL import Image, ImageDraw
from config import RESOURCE_DIR

def calculate_center(image):
    """計算字體的上下左右邊界"""
    width, height = image.size
    # 轉為灰階並二值化
    gray_image = image.convert('L')
    threshold = 128
    binary_image = gray_image.point(lambda x: 0 if x < threshold else 255, '1')

    x_min, x_max = width, 0
    y_min, y_max = height, 0
    found_pixel = False

    # 遍歷像素尋找黑點
    for x in range(width):
        for y in range(height):
            if binary_image.getpixel((x, y)) == 0:
                x_min, x_max = min(x, x_min), max(x, x_max)
                y_min, y_max = min(y, y_min), max(y, y_max)
                found_pixel = True

    return (x_min, x_max, y_min, y_max) if found_pixel else None

def crop_and_normalize(image_path):
    """
    裁剪圖片並將其置中放置在正方形畫布上
    """
    if not image_path.exists():
        return

    image = Image.open(image_path).convert('RGB')
    bounds = calculate_center(image)

    if not bounds:
        return

    x_min, x_max, y_min, y_max = bounds
    
    # 裁剪
    cropped = image.crop((x_min, y_min, x_max, y_max))
    
    # 建立正方形畫布 (以長邊為基準)
    img_size = max(cropped.width, cropped.height)
    canvas = Image.new('RGB', (img_size, img_size), (255, 255, 255))

    # 置中貼上
    offset_x = (img_size - cropped.width) // 2
    offset_y = (img_size - cropped.height) // 2
    canvas.paste(cropped, (offset_x, offset_y))

    # 覆蓋原檔儲存
    canvas.save(image_path)