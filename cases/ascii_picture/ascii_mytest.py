from PIL import Image
import easygui


"""
命令：(venv) E:\PycharmProjects\shiyanlou\cases\ascii_picture>python ascii_mytest.py E
:\PycharmProjects\shiyanlou\cases\ascii_picture\ascii_dora.png
"""


class AsciiArt:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.charList = list(r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
        self.txt = ''

    # 本项目的核心部分,将RBG转化为灰度值并映射到70个字符
    # 通过图片上某个位置的RGB值，得到灰度，然后返回对应在列表中的字符
    def get_char(self, r, g, b, alpha=256):
        if alpha == 0:
            return ' '
        length = len(self.charList)
        # 将像素RGB值转化成灰度值
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

        unit = (256.0 + 1) / length
        return self.charList[int(gray / unit)]

    # 将图片转化为字符画
    def convert(self, filename):
        im = Image.open(filename)
        im = im.resize((self.width, self.height), Image.NEAREST)
        for i in range(self.height):
            for j in range(self.width):
                self.txt += self.get_char(*im.getpixel((j, i)))  # 在字符串对应的位置中赋值
            self.txt += '\n'

    # 保存文件
    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(self.txt)
            print(self.txt)


if __name__ == '__main__':
    # ascii_art = AsciiArt(width=80, height=80)
    # pic_name = input("请选择要转化的图片：")
    # print("图片转化中....")
    # ascii_art.convert(pic_name)
    # print("图片转化成功！")
    # tar_name = input("请输入要保存文件：")
    # print("正在保存图片....")
    # ascii_art.save(tar_name)
    # print("保存成功！")

    # 实现一个输入框，输入图片的宽和高
    [pic_width, pic_height] = easygui.multenterbox("请输入图片的宽和高", "请输入信息", ['\n宽:\n', '高:'], [])
    # 若输入了宽和高则用输入的,如果未输入则用默认的
    # eval()执行表达式并返回值
    if pic_width != '':
        pic_width = eval(pic_width)
    else:
        pic_width = 80
    if pic_height != '':
        pic_height = eval(pic_height)
    else:
        pic_height = 80

    ascii_art = AsciiArt(pic_width, pic_height)
    pic_name = easygui.fileopenbox("请选择要转化的图片")
    ascii_art.convert(pic_name)
    tar_name = easygui.filesavebox("请选择保存文件的路径，并输入文件名", default="ascii_mytest.txt", filetypes=['*.txt'])
    ascii_art.save(tar_name)
    easygui.msgbox("成功了！", title='', ok_button='确定')
