import pygame
from plane_sprite import *

rect = pygame.Rect(100, 500, 125, 300)
print("%d\t%d\t%d\t%d" % (rect.x,rect.y,rect.width,rect.height))

pygame.init()
print("游戏代码")

# 绘制窗口
Surface = pygame.display.set_mode((480, 700))
# 加载图片到内存
bg = pygame.image.load("./images/background.png")
# 定位到窗口
Surface.blit(bg, (0, 0))
# 刷新窗口
# pygame.display.update()

# 英雄
hero = pygame.image.load("./images/me1.png")
Surface.blit(hero, (200, 500))

# 记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 游戏时钟对象
clock = pygame.time.Clock()

# 创建敌机精灵
enemy = GameSprite("./images/enemy1.png")
enemy2 = GameSprite("./images/enemy2.png", 2)

# 创建精灵组
enemy_group = pygame.sprite.Group(enemy,enemy2)

# 游戏循环
while True:
    # 帧率
    clock.tick(60)
    # 获取事件
    # event_list = pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # 飞机的位置
    hero_rect.y -= 2
    # 挪动飞机位置
    if hero_rect.y <= 0:
        hero_rect.y = 700
    # 调用blit绘制图像
    Surface.blit(bg, (0, 0))
    Surface.blit(hero, hero_rect)

    # 调用精灵族方法
    enemy_group.update() # 更新位置

    enemy_group.draw(Surface) # 添加到窗口
    # 刷新窗口
    pygame.display.update()
    pass
