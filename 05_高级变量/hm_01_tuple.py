# 元组 有序
info_tuple = ("zhangsan", 1, 1.75)
info_tuple2 = ("wangwu",) # 只有一个元素的时候需要加 ",",意味着是元组

print(info_tuple[0]) # 获取tuple
print(info_tuple.count("zhangsan")) # 该元素在元组中出现的次数
print(info_tuple.index("zhangsan")) # 该元素所在位置的索引
print(len(info_tuple)) # 元组内的元素个数量

for info in info_tuple:

    print(type(type(info))) #都是type类型的

    print(info)


info_tuple3 = ("zhangsan", 1, 1.75)
# 格式化字符串后面的 ‘（）’本质上就是一个元组
print("name:%s,年龄：%d,身高：%.2f" % info_tuple3)


# 元组跟列表之间的转换

info_tuple4 = ("a", 1, "2", "1,")
list_param = list(info_tuple4) # 转换为list列表
print(type(list_param))
tuple_param = tuple(list_param) # 转换为tuple元祖
print(type(tuple_param))

print(type(list))
print(type(type))
print(type(print("s")))