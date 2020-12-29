class Cat:
    """毛磊"""

    def __init__(self, new_name, new_age):
        """初始化变量"""
        # self.name = "zhangsan"
        # self.age = 23
        self.name = new_name
        self.age = new_age
    def __del__(self):
        """销毁时被掉用"""
        print("被销毁！")
    def __str__(self):
        return "[%s, %d]" % (self.name, self.age)
    def eat(self):
        print("%schi" % self.name)
    def drink(self):
        print("%sdirnk%d" % (self.name, self.age))

black_cat = Cat("阿斯蒂芬", 123)
# black_cat.name = "lisi"
black_cat2 = Cat("dddd", 1233)
# black_cat2.name = "手动阀手动阀"
# black_cat2.age = 123
black_cat.eat()
black_cat.drink()
black_cat2.eat()
black_cat2.drink()
# del black_cat
print(black_cat)
print("%d" % id(black_cat)) # 十进制输出数字
print("%x" % id(black_cat)) # 十六进制输出数字
print("*" * 50)
print(black_cat)
