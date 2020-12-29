gl_list1 = [1, 2, 3, 4]

def demo(num_list1, title="", gender=True):

    # num_list1 += num_list1 # 如果是列表，相当于执行了，extend方法
    num_list1 = num_list1 + num_list1 # 不会修改源列表内的值，因为是赋值操作
    print(num_list1)
    # 缺省值
    if gender:
        print("True")
        print(title)
    else:
        print("False")
        print(title)

demo(gl_list1, gender=False)
print(gl_list1)