def input_result():
    result = int(input("输入整数！"))
    if len(str(result)) >= 6:
        return 8 / result
    ex = Exception("密码长度不够", "重新开始！")
    raise ex # 抛出异常


try:
    print(input_result())
except Exception as result:
    print(result)

print("*" * 45)
print(input_result())
print("*" * 45)