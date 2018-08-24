from PIL import Image
import argparse

"""
命令：python ascii.py E:\PycharmProjects\shiyanlou\tools\ascii_dora.png
"""
# 命令行输入参数处理
# 创建解析器对象
parser = argparse.ArgumentParser()

# 定义参数，如果命令行中带了参数则用命令行中参数值，如果没有则用此处定义的值
# 如命令行：python ascii.py E:\PycharmProjects\shiyanlou\tools\ascii_dora.png
# -o E:\PycharmProjects\shiyanlou\tools\test.txt --width 40 --height 40
parser.add_argument('file')     # 输入文件
parser.add_argument('-o', '--output')   # 输出文件
parser.add_argument('--width', type=int, default=80)    # 输出字符画宽
parser.add_argument('--height', type=int, default=80)   # 输出字符画高

# 解析命令行，获取参数
args = parser.parse_args()

IMG = args.file     # 获取命令行中输入的文件
WIDTH = args.width  # 获取命令行中输入的宽，如果没有则使用上面设置的默认宽度，以下heigth、outputt同理
HEIGHT = args.height
OUTPUT = args.output

# 字符画所使用的字符集
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将256灰度映射到70个字符上
# 灰度值：指黑白图像中点的颜色深度，范围一般从0到255，白色为255，黑色为0，故黑白图片也称灰度图像
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]


if __name__ == '__main__':

    im = Image.open(IMG)
    # 缩放图片。 PIL.Image.NEAREST：最低质量， PIL.Image.BILINEAR：双线性，
    # PIL.Image.BICUBIC：三次样条插值，Image.ANTIALIAS：最高质量
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ""

    # 逐行转化图片灰度为字符，并打印出来
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print(txt)

    # 字符画输出到文件
    # 如果命令行中传入了文件参数则输入到该文件中，否则输入都else中定义的文件中
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open(r"E:\PycharmProjects\shiyanlou\tools\output.txt", 'w') as f:
            f.write(txt)
