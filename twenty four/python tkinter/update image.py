from PIL import Image

def split_image(image_path):
    # 打开图片
    img = Image.open(image_path)

    # 获取图片的宽度和高度
    width, height = img.size

    # 计算分割线的位置
    middle = height // 2

    # 分割图片
    top_img = img.crop((0, 0, width, middle))
    bottom_img = img.crop((0, middle, width, height))

    # 保存分割后的图片
    top_img.save("icon-up.png")
    bottom_img.save("icon-down.png")

# 调用函数
split_image("sort-arrows-couple-pointing-up-and-down.png")  # 请将"your_image_file.png"替换为你的图片文件路径
