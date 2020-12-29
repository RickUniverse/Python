import random
import pygame

# 飞机大战窗口常量
SCREEN_RECT =  pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PER_SEC = 60
# 敌方飞机事件常量
CREATE_ENEMY_EVENT =  pygame.USEREVENT
# 发射子弹事件常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        """飞机大战游戏精灵"""
        # 调用父类初始化方法
        super().__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
    def update(self):
        # 在游戏上方移动
        self.rect.y += self.speed


# 背景子类
class Background(GameSprite):
    """背景精灵子类"""

    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):
        # 调用父类
        super().update()
        # 判断是否移动到了高度位置
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


# enemy敌机
class Enemy(GameSprite):
    """敌机精灵类"""

    def __init__(self):
        image = ""
        # 1，初始化敌机
        random_int = random.randint(1, 3)
        if random_int == 1:
            image = "./images/enemy3_hit.png"
        elif random_int == 2:
            image = "./images/enemy2.png"
        elif random_int == 3:
            image = "./images/enemy1.png"
        super().__init__(image)
        # 2，指定敌机初始随机速度
        self.speed = random_int
        # 3，指定敌机初始随机位置
        self.rect.bottom = 0 # 相当于敌机的y=-height
        max_x = SCREEN_RECT.width - self.rect.width # 最大x轴
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕！")
            self.kill() # 将敌机清除
    def __del__(self):
        # print("敌机在：%s;处挂了" % self.rect)
        pass


# 英雄精灵
class Hero(GameSprite):
    """英雄精灵类"""
    def __init__(self):
        super().__init__("./images/life.png", 0)
        # 初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 子弹精灵组
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
    def fire(self):

        # 发射三颗子弹
        for i in (0, 1, 2):

            # 添加子弹到子弹精灵组
            bullet = Bullet()
            # 初始位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 添加子弹到子弹精灵组
            self.bullet_group.add(bullet)

# 子弹类
class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        super().__init__("./images/bullet1.png", -2)
    def update(self):
        super().update()

        if self.rect.bottom < 0:
            self.kill()
    def __del__(self):
        print("销毁子弹1")