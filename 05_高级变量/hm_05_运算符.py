# 运算符 + *
list_array = ["11", "22"] * 3
print(list_array + ["2"])
list_array.append(["q","d"])
print(list_array)
list_array.extend(["zzz", "zzzcd"])
print(list_array)
# in, not in
tuple_array = ("123", "abc")
print("abc" in tuple_array)
dictionary_dic = {"name": "xiaoming",
                  "age": 15}
print("name" in dictionary_dic) # True
print("xiaoming" in dictionary_dic) # False

# 完整for循环
for nam in list_array:

    print(nam)

    if nam == "aaa":
        break
else:
    print("执行了else")

# 常用应用
list_student = [{"name": "xiaoming"},
                {"name": "lisi"},
                {"name": "wangwu"},
                {"name": "liuliu"}]
str = "lisi"

def get_student(name,list):

    for stu in list:

        if stu["name"] == name:

            return stu
    else:
        print("未找到！")

isFind = get_student(str,list_student)
if isFind != None:
    print(isFind)