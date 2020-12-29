class Tools(object):
    tools_count = 0
    @classmethod # 创建类方法
    def show_toole_count(cls):
        print("数量是：%d" % cls.tools_count)
    @staticmethod # 静态方法
    def static():
        print("这是一个静态方法，不需要创建对象也能直接使用类名调用，")
    def __init__(self):
        # 每次创建一个实例化对象便让类属性加1,记得加类名，不然会变成谁调用，便给谁加1
        Tools.tools_count += 1
        # self.tools_count += 1 这样相当于每次给添加了一个属性（不是类属性）tools_count +1

tools1 = Tools()

tools2 = Tools()

tools3 = Tools()

tools4 = Tools()
tools4.tools_count = 99 # 添加了一个属性
print(Tools.tools_count) # 两种获取机制 ，
print(tools4.tools_count) # 两种获取机制 ， 向上查找，直到查找到一个tools_count

tools4.show_toole_count() # 调用类方法

Tools.show_toole_count() # 调用类方法

Tools.static() # 这是一个静态方法