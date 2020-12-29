class Gun:
    def __init__(self, model):
        # 1，枪的类型
        self.model = model
        # 2, 枪的子弹
        self.bullet_count = 0
    def add_bullet(self, bullet):
        # 1,增加子弹
        self.bullet_count += bullet
    def __siyou(self):
        print("sdfasdfasdf")
    def shoot(self):
        # 1,判断子弹
        if self.bullet_count <= 0:
            print("没有子弹！")
            return
        # 2,发射子弹
        while self.bullet_count > 0:
            self.bullet_count -= 1
            print("[%s：正在发射子弹，还剩：%d颗子弹！]" % (self.model, self.bullet_count))
        print("发射完成！没有子弹了")

class Soldier:
    def __init__(self, name, gun):
        # 名字
        self.name = name
        # 枪
        self.gun = gun
    def fire(self):
        # 判断是否有枪

        if self.gun is None:
            print("还没有枪！")
            return
        # 装填子弹
        self.gun.add_bullet(50)
        # 发射子弹
        self.gun.shoot()

ak = Gun("ak47")

soldier = Soldier("zhangsan", None)
soldier.gun = ak
soldier.fire()
str = None
str3 = None
print(id(None))
print(id(str))
print(id(str3))
print(str == "None")
print(id(str3))

ak._Gun__siyou()