title = "模块2"

def say_hello():
    print(title)

class Cat():
    pass


def main():
    print("如果是当前页面测试时使用代码，便会执行！")
    print(__name__) # __main__

if __name__ == "__main__":
    main()