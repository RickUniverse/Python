import pygame
from plane_sprite import *

class PlaneGame(object):
    """飞机大战"""
    def __init__(self):
        # 定义窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 定义时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法
        self.create_sprites()
        # 设置定时器
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)
    def create_sprites(self):
        # 创建背景精灵
        back = Background()
        back2 = Background(is_alt=True) # 表示是 上方背景
        # 创建精灵组
        self.back_group = pygame.sprite.Group(back, back2)
        #　创建敌机组
        self.enemy_group = pygame.sprite.Group(Enemy())
        # 英雄精灵
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
    def start_game(self):
        while True:
            # 1，游戏帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2，事件监听
            self.__event_handler()
            # 3，碰撞检测
            self.__check_collide()
            # 4，绘制精灵
            self.__update_sprites()
            # 5，更新画面
            pygame.display.update()

        print("游戏开始！")
    def __event_handler(self):
        """私有方法事件监听"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print(CREATE_ENEMY_EVENT+event.type)
                self.enemy_group.add(Enemy())
            #elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #    print("右")
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire() # 发射子弹

        keys_pressed = pygame.key.get_pressed() # 按键元组
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 5
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -5
        else:
            self.hero.speed = 0
    def __check_collide(self):
        """私有碰撞检测"""
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()

            self.game_over()
    def __update_sprites(self):
        """绘制精灵"""

        # 绘制背景精灵
        self.back_group.update()
        # 画到屏幕上
        self.back_group.draw(self.screen)

        # 绘制敌机
        self.enemy_group.update()
        # 画到屏幕上
        self.enemy_group.draw(self.screen)
        # 英雄
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        # 子弹
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)
    @staticmethod
    def game_over():
        print("游戏结束！")
        # 卸载模块
        pygame.quit()
        # 退出
        exit()


if __name__ == '__main__':
    game = PlaneGame()

    game.start_game()