# *-* coding:utf8 *-*
import os

hello_word = u"e手动阀手动阀" # u表示告诉python2解释器这是一个utf8编码
for char in hello_word:
    print(char)

# 打开文件
file = open("README", "a")

# r 只读 reader(file) reader(读)
# w 只写 write（覆盖）
# a（追加）append追加
#
file.write("asdfasdfasdf\nasdfasdf")

#　关闭
file.close()

file2 = open("README", "r")
# 一行一行读取
while True:

    text = file2.readline()

    if not text:
        break

    print(text, end="")

file.close()

# 复制文件 , 大文件，逐行复制
file5 = open("README", "r")
file_copy = open("README[复件]", "w")

while True:
    text = file5.readline()

    if not text:
        break

    file_copy.write(text)

file_copy.close()
file5.close()

# 创建目录
print(os.getcwd())
os.mkdir("asdf")