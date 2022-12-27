
from pdf2image import convert_from_path

# 将 PDF 文件转换为 JPEG 格式的图像文件
images = convert_from_path('ISO291195.pdf', dpi=300, fmt='jpeg')

# 保存图像文件
for i, image in enumerate(images):
    image.save('images/output_{}.jpg'.format(i))



