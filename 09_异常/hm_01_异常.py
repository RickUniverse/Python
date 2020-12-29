try:
    num = int(input("请输入一个整数："))

    3 / num
except ValueError:
    print("请输入正确的值！")
except ZeroDivisionError:
    print("除零异常！")
except Exception as result:
    print("其他异常：%s" % (result))
else:
    print("没有异常才会执行！")
finally:
    print("不管有没有异常都会执行!")
