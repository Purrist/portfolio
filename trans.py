from pdf2image import convert_from_path
import os

# PDF 文件路径
pdf_file = "portfolio.pdf"

# 图片输出目录
img_dir = "pages"
os.makedirs(img_dir, exist_ok=True)

# 转 PDF 为图片，指定 poppler_path
pages = convert_from_path(
    pdf_file,
    dpi=150,
    poppler_path=r"D:\program\poppler-25.07.0\Library\bin"
)

img_files = []
for i, page in enumerate(pages, start=1):
    img_path = os.path.join(img_dir, f"page_{i}.png")
    page.save(img_path, "PNG")
    img_files.append(img_path)

# 生成 index.html
html_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>作品集</title>
<style>
body { margin:0; padding:0; text-align:center; background:#f5f5f5; }
img { max-width:100%; height:auto; display:block; margin:10px auto; }
</style>
</head>
<body>
"""

for img in img_files:
    html_content += f'  <img src="{img}" alt="{os.path.basename(img)}">\n'

html_content += "</body>\n</html>"

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("转换完成！生成的图片在 pages/ 目录，index.html 已生成。")
