from PIL import Image
import easygui as g  # 引入第三方GUI库easygui，需提前安装

charList = list(r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r, g, b, alpha=256):          # 本项目的核心部分
    if alpha == 0:                           # 通过图片上某个位置的RGB值，得到灰度，然后返回对应在列表中的字符
        return ' '
    length = len(charList)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)    # 将像素RGB值转化成灰度值

    unit = (256.0 + 1) / length
    return charList[int(gray/unit)]


def main():
    width = 120  # 宽和高默认为120和60
    height = 60
    [width_str, height_str] = g.multenterbox("请输入宽和高", "请输入信息", ["宽", '高'], [])  # 实现一个输入信息框
    if width_str != "":      # 如果没有输入，则使用默认值
        width = eval(width_str)
    if height_str != "":
        height = eval(height_str)
    pic_path = g.fileopenbox("请选择要转换的图像文件")        # 得到完整的图片路径
    im = Image.open(pic_path)
    im = im.resize((width, height), Image.NEAREST)
    # 文件存储目录选择，并返回完整的路径，有默认的设置
    in_path = g.filesavebox("请选择存储的文件路径，并输入文件名", default='ascii_test.txt', filetypes=['*.txt'])
    str = ""
    for i in range(height):
        for j in range(width):
            str += get_char(*im.getpixel((j, i)))  # 在字符串对应的位置中赋值
        str += '\n'
    with open(in_path, 'w') as f:
        f.write(str)
        g.msgbox("成功了！", title="", ok_button="厉害了")  # 提示信息框
        print(str)


main()
