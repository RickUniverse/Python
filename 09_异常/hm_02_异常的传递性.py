class Demo1(object):
    def demo1(self):
        3 / int(input("输入整数！"))

class Demo2(object):
    @staticmethod
    def demo2():
        return Demo1().demo1()

try:
    Demo2.demo2()
except Exception as result:
    print(result)
