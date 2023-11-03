from PIL import Image

def resize_image(input_image_path, output_image_path, scale_factor):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print(f"The original image size is {width} wide x {height} tall")

    # 计算新的宽度和高度
    new_height = int(height / scale_factor)
    new_width = int(width * new_height / height)

    resized_image = original_image.resize((new_width, new_height))
    width, height = resized_image.size
    print(f"The resized image size is {width} wide x {height} tall")
    resized_image.show()
    resized_image.save(output_image_path)

# 使用方法
# resize_image('images/ufo.png', 'images/ufo.png', 8)
