# 字符串
str1 = "hello python!"
str2 = 'nihao"大西瓜"'
# 获取单个字符
print(str1[0])
# 字符串总长度
print(len(str1))
# 某一个字符串出现的次数
print(str1.count('o'))
# 字符串出现的下标
print(str1.index('o')) # 不存在会报错
# 迭代
for char in str1:
    print(char)

# 判断空白字符, 制表符\t\n\r也被认为空格
str3 = " \t\n\r"
print(str3.isspace())

str4 = "一"
print(str4.isdecimal())
print(str4.isdigit())
print(str4.isnumeric())

str5 = "hello world"
# 判断是否以指定的字符开头, 区分大小写
print(str5.startswith("He"))
# 判断结束
print(str5.endswith("d"))
# 是否包含一个字符, 返回下标，找不到返回-1
print(str5.find("llo"))
# 替换,返回一个新字符串，不会修改原有的字符串
print(str5.replace(" ", ";"))
print(str5)
# 文本对齐
list_eman = ["早起\t\n",
             "李冀琛",
             "早起的鸟儿有虫吃，",
             "\t\n早起的虫儿被鸟吃。",
             "早起的生活有爸妈，",
             "早起的爸妈叫早起。"]
for zaoqi in list_eman:

    print("|%s|" % zaoqi.strip().center(10, "　"))

# 连接
str6 = " ".join(list_eman)
print(type(str6))
print(str6)
# 拆分
list_eman2 = str6.split()
print(type(list_eman2))
print(list_eman2)