from PIL import Image, ImageDraw

# 計算上下界
def calculate_center(image_path):
    # 打開圖片
    image = Image.open(image_path) 

    # 圖片的高度
    width, height = image.size
 
    # 灰階 
    image = image.convert('L')
    
    # 二值化
    # 二值化判斷的門檻(取背景與文字顏色的平均)
    # pixel_sum = 0
    # for x in range(width):
    #     for y in range(height):
    #         pixel_sum += image.getpixel((x,y))
    # pixel_average = pixel_sum / (width * height) 
    # 為增快速度，先暫時註解

    pixel_average = 128 # 設黑白兩色的平均
    threshold = pixel_average # 二值化判斷的門檻
    image = image.point(lambda x: 0 if x < threshold else 255, '1') 

    
    # 初始化邊界
    x_min = width
    x_max = 0
    y_min = height
    y_max = 0

    # 遍歷像素
    for x in range(width):
        for y in range(height):
            if image.getpixel((x,y)) == 0:
                x_min = min(x, x_min)
                y_min = min(y, y_min)
                x_max = max(x, x_max)
                y_max = max(y, y_max)

    return x_min, x_max, y_min, y_max

# 裁剪圖片
def crop_image(image_path):
    # 打開圖片
    image = Image.open(image_path)

    # 轉為 RGB (暫時無法解決 JPG 的透明度問題)
    image = image.convert('RGB')

    x_min, x_max, y_min, y_max = calculate_center(image_path)

    # 劃出剪裁圖片的上下左右
    left = x_min
    upper = y_min
    right = x_max
    lower = y_max

    # 裁剪圖片
    cropped_image = image.crop((left, upper, right, lower))
    width, height = cropped_image.size
    img_size = max(width, height)
    
    # 创建空白画布
    canvas = Image.new('RGB', (img_size, img_size), (255, 255, 255))

    # 计算图像在画布中的位置
    x = (img_size - cropped_image.width) // 2
    y = (img_size - cropped_image.height) // 2

    # 在画布上粘贴图像
    canvas.paste(cropped_image, (x, y))

    # 保存画布
    canvas.save(image_path)

    # canvas.show()




# 測試
image_path = 'test.jpg'
cropped_image_path = crop_image(image_path)
print(f"cropped：{cropped_image_path}")
