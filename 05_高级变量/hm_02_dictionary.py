# 字典 无序
xiaoming = {"name": "xiaoming",
            "age": 18,
            "sex": "男"}
print(xiaoming)
# 找不到key会报错
print(xiaoming["name"])
# 找不到key不会报错
print(xiaoming.get("name"))
# 存在key便会修改
xiaoming["age"] = 19
print(xiaoming)
# 不存在便会增加一个键值对
xiaoming["height"] = 1.77
print(xiaoming)

xiaoming.pop("name") # 删除一个键值对，不存在程序会报错
# del xiaoming["name"] # 删除一个键值对，不存在程序会报错
# xiaoming.popitem() # 随机删除一个
# 统计键值对数量
print(len(xiaoming))
# 合并字典 如果存在相同的key会覆盖值
temp = {"weight": 100,
        "age": 18}
xiaoming.update(temp)
print(xiaoming)
# 获取所有key
print(xiaoming.keys())
print(type(xiaoming.keys()))
# 获取所有value
print(xiaoming.values())
print(type(xiaoming.values()))
# 如果key不存在会增加一个键值对
# 存在不会修改值
xiaoming.setdefault("name", "lisi")
xiaoming.setdefault("phone", "123123")
print(xiaoming)

# 字典中的迭代
for key in xiaoming:
    print(xiaoming[key])

# 字典的主要应用
student_list = [
    {"name": "zhangsan",
         "age": 13,
         "sex": "男4"},
    {"name": "zhansgsan",
         "age": 18,
         "sex": "男45"},
    {"name": "zhandgsan",
         "age": 18,
         "sex": "男5"}
]
for student in student_list:
    for key in student:
        print(student[key])



# 清除字典
xiaoming.clear()