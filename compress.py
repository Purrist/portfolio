from PIL import Image
import os

# 输入和输出文件夹
input_dir = "pages"
output_dir = "pages_compressed"
os.makedirs(output_dir, exist_ok=True)

# 遍历所有 PNG 文件
for filename in os.listdir(input_dir):
    if filename.lower().endswith(".png"):
        img_path = os.path.join(input_dir, filename)
        img = Image.open(img_path)

        # 按宽度 1920 等比缩放
        w_percent = 1920 / float(img.size[0])
        h_size = int(float(img.size[1]) * w_percent)
        img = img.resize((1920, h_size), Image.LANCZOS)

        # 输出路径
        output_path = os.path.join(output_dir, filename)
        img.save(output_path, optimize=True, quality=85)

        print(f"✅ 压缩完成: {filename} ({img.size[0]}x{img.size[1]})")
