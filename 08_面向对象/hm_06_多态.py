class Dog(object):
    def __init__(self, name):
        self.name = name
    def wan(self):
        print("%s   wannshua" % self.name)
class XiaoTian(Dog):
    def wan(self):
        print("%s   xiaotianzai!!!" % self.name)

class Person(object):
    def __init__(self, name):
        self.name = name
    def wan_and_dog(self, dog):
        print("%s   xiaotianzai!!! %s" % (self.name, dog.name))
        dog.wan()

dog = Dog("dog")
xiao = XiaoTian("xiao")
lisi = Person("lisi")
wangwu = Person("王五")
lisi.wan_and_dog(dog) # 多态： 传入不同的狗对象跟不同的狗玩，
lisi.wan_and_dog(xiao)