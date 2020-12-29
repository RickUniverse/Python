class Game(object):
    top_score = 0;
    @staticmethod
    def help_():
        print("这是一个帮助信息")
    @classmethod
    def get_top_score(cls):
        print("得到最高分：%d " % cls.top_score)
    def start_game(self):
        print("开始游戏！！！！！！")


Game.help_() # 帮助信息
Game.get_top_score() # 查看最高分
li = Game()
li.start_game() # 开始游戏