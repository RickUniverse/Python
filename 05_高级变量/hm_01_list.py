# 列表 有序
name_list = ["zhangsan", "lisi", "1", "wangwu", "lisi"]
# name_list = [5, 3, 1, 5, 2]
# print(name_list)
# print(name_list[0])
# 输入列表名之后按下tab键有提示
print(name_list.index("lisi")) # 获取数据第一次出现时的索引
name_list.sort() # 排序,升序  0-9 >a-z
print(name_list, end="升序--\n")
name_list.sort(reverse=True) # 排序,降序序
print(name_list, end="降序--\n")
name_list.reverse() # 翻转逆转
print(name_list, end="降序--\n")
name_list.insert(1, "bngba") # 指定位置插入
print(name_list)
name_list.append("mowei") # 末尾插入
print(name_list)
name_list2 = ["list2", "list23"]
name_list.extend(name_list) # 将另一个列表插入
print(name_list)
name_list.pop() # 删除末尾数据
print(name_list)
name_list.pop() # 删除末尾数据
print(name_list)
del name_list[0] # 删除索引数据
print(name_list)
name_list.pop(0) # 删除指定索引数据
print(name_list)
name_list.pop() # 删除末尾数据
print(name_list)
name_list[0] = "王五" # 修改指定位置数据
print(name_list)
print(len(name_list)) # 获取列表数据的个数
print(name_list.count("lisi")) # 获取该数据出现的次数
print(name_list.copy()) # 复制列表
name_list3 = name_list.copy()
name_list.remove("lisi") # 删除列表中的某个值，只删除第一个匹配到的值，没有匹配到会报错

# 迭代遍历iteration
for name in name_list:
    print(name)


print(name_list, "---")
name_list.clear()
print(name_list)
# print(name_list.insert(0, "zhaoliu"))