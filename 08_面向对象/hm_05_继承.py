class Animal():
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")


class Dog(Animal):
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
    def bark(self):
        print("叫")
    def __test(self):
        print("num1：%d,num2:%d" % (self.num1, self.__num2))

    def test(self):# 共有方法中调用私有方法，间接访问
        self.__test()


class XiaoTianQuan(Dog): # 继承狗
    def bark(self): # 方法重写
        # 重写后需要做的操作
        print("叫的非常牛！")
        # 父类中做的操作
        # Dog.bark(self)
        super().bark()
        # 其他操作
        print("-" * 30)
    def fly(self):
        print("会飞的狗")
        # 调用父类属性和方法
        # 调用属性
        # self.num2
        # 调用方法
        self.test()

class Person(object):
    def zoulu(self):
        print("走路1！！！！1")


class Person(XiaoTianQuan, Person):
    def fly(self):
        print("化身为会飞的人")


person = Person();
person.fly()
person.zoulu()

class C():
    def c(self):
        print("c")
    def o(self):
        print("c")
class D():
    def d(self):
        print("d")
    def o(self):
        print("d")
class F():
    def f(self):
        print("f")
    def o(self):
        print("f")

class A(C, D, F): # 多继承

    pass

xiaoTian = XiaoTianQuan()

xiaoTian.bark()
xiaoTian.fly()
a = A()
a.d()
a.f()
a.c()
a.o() # 出现同名调用第一个发现的方法，因为是先继承了c在继承了df

# 调用方法的时候，查找方法的顺序
# <class '__main__.A'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.F'>, <class 'object'>)
print(A.__mro__)