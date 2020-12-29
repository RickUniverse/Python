# 递归
def digui(num):
    if num == 0:
        print(num)
        return
    digui(num - 1)
digui(4)
# 两个数字的相加
def num_numbers(num):
    if num == 1:
        return 1
    print(id(num))
    temp = num_numbers(num - 1)

    return temp + num
print(num_numbers(4))