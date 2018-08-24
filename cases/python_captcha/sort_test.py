dic = {'a': 31, 'bc': 5, 'c': 3, 'asd': 4, 'aa': 74, 'd': 0}

print("打印出字典的键和值的列表：", dic.items())

# sorted 方法中 key指定按什么排序
# 这里的 lambda x: x[1] 即指定以列表的x[1] 即value来排序，x[0]则是以key排序
print("指定以value来排序：", sorted(dic.items(), key=lambda x: x[1]))

# sorted 默认从小到大排序，加上reverse=True 参数则翻转为从大到小排序
print("指定从大到小排序：", sorted(dic.items(), key=lambda x: x[1], reverse=True))

# 打印列表前几个值
print("指定打印出前3个值：", sorted(dic.items(), key=lambda x: x[1], reverse=True)[:3])

# 分别打印出key 和 value
for i, j in sorted(dic.items(), key=lambda x: x[1], reverse=True)[:3]:
    print(i, j)

