# 多值参数
def demo(num, *args, **kwargs):
    print(num)
    print(args)
    i = 0
    for num in args:
        i += num
    print("和为：%s" % i)
    print(kwargs)

##
demo(1, 2, 3, 4, 5, 6, name = "lisi", age = "19")
##
tuple_num = (1, 2, 3)
dict_stu = {"name": "kll",
            "age": "2323"}
demo(*tuple_num,**dict_stu) # 拆包