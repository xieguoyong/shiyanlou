from PIL import Image
import hashlib
import time
import os
import math


class VectorCompare:
    def magnitude(self, concordance):
        total = 0
        for word, count in concordance.items():
            total += count ** 2
        return math.sqrt(total)

    def relation(self,concordance1, concordance2):
        relevance = 0
        topvalue = 0
        for word, count in concordance1.items():
            # if concordance2.has_key(word):
            if word in concordance2:
                topvalue += count * concordance2[word]
        return topvalue / (self.magnitude(concordance1) * self.magnitude(concordance2))


def buildvector(im):
    d1 = {}

    count = 0
    for i in im.getdata():
        d1[count] = i
        count += 1

    return d1


v = VectorCompare()


iconset = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f',
           'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


imageset = []

for letter in iconset:
    for img in os.listdir("E:\PycharmProjects\shiyanlou\cases\python_captcha\iconset\%s"%(letter)):
        temp = []
        if img != "Thumbs.db" and img != ".DS_Store":   # windows check...
            temp.append(buildvector(Image.open("E:\PycharmProjects\shiyanlou\cases\python_captcha\iconset\%s\%s"%(letter,img))))
        imageset.append({letter: temp})


im = Image.open(r"E:\PycharmProjects\shiyanlou\cases\python_captcha\captcha.gif")
im2 = Image.new("P", im.size, 255)
im.convert("P")

# 获取图片中颜色值出现数量最大的10个像素点
his = im.histogram()
values = {}
for i in range(256):
    values[i] = his[i]
for j, k in sorted(values.items(), key=lambda x: x[1], reverse=True)[:15]:
    print(j, k)

# 获取图片像素点位置及对应颜色值
temp = {}
for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y, x))
        print(type(pix), pix)
        temp[pix] = pix
        if pix == 220 or pix == 227:    # these are the numbers to get
            im2.putpixel((y, x), 0)

# 展示转化后的图片
im2.show()

inletter = False
foundletter = False
start = 0
end = 0

letters = []

for y in range(im2.size[0]):    # slice across
    for x in range(im2.size[1]):    # slice down
        pix = im2.getpixel((y, x))
        if pix != 255:
            inletter = True

    if foundletter == False and inletter == True:
        foundletter = True
        start = y

    if foundletter == True and inletter == False:
        foundletter = False
        end = y
        letters.append((start, end))

    inletter=False

count = 0
for letter in letters:
    m = hashlib.md5()
    im3 = im2.crop((letter[0], 0, letter[1], im2.size[1] ))

    guess = []

    for image in imageset:
        for x, y in image.items():
            if len(y) != 0:
                guess.append((v.relation(y[0], buildvector(im3)), x))

    guess.sort(reverse=True)
    print("", guess[0])

    count += 1
