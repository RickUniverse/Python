class MusicPlayer(object):

    instance = None
    count_address = 0
    init_flag = False # 是否进行过初始化事件

    def __new__(cls, *args, **kwargs):

        # 判断是否已经创建了实例
        if cls.instance is None: # 判断空对象使用is
            # 没有创建则返回，地址引用
            cls.instance = super().__new__(cls) # cls是哪个类便返回那个类
            cls.count_address += 1 # 分配地址加1
        # 提示
        print("分配了几次地址：%d,当前地址是：%s" % (cls.count_address, cls.instance))
        # 返回引用
        return cls.instance
    def __init__(self):

        if MusicPlayer.init_flag:
            return
        print("执行了实例化！")
        MusicPlayer.init_flag = True


m = MusicPlayer()
m = MusicPlayer()
m = MusicPlayer()
