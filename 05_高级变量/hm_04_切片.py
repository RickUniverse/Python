# 切片
str = "0123456789"
print(str[2:6]) # 2 - 5
print(str[2:]) # 2 - 末尾
print(str[:6]) # 开始 - 5
print(str[:]) # 完整的
print(str[0::2]) # 开始位置，每个一个截取一个
print(str[1::2]) # 1 每个一个截取一个
print(str[2:-1]) # 2 - 倒数第二
print(str[-2:]) # 截取末尾两个
print(str[-1::-1]) # 倒叙
print(str[::-1]) # 倒叙
# 针对列表跟元组的切割
print(["a", "d", "s", "q"][-1::-1])
print(("a", "d", "s", "q")[-1::-1])
# 公共方法
print(max(("a", "b", "c")))
print(min(("a", "b", "c")))
len("a")
print(["e", "b"] < ["a", "d"])
