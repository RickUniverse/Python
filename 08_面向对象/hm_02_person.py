class Person:
    """跑步"""
    def __init__(self, new_name, new_weight):
        self.name = new_name
        self.weight = new_weight
    def __str__(self):
        return "名字：%s,体重：%.2f" % (self.name, self.weight)
    def eat(self):
        self.weight += 1
        print("名字：%s,体重：%.2f" % (self.name, self.weight))
    def run(self):
        self.weight -= 0.5
        print("名字：%s,体重：%.2f" % (self.name, self.weight))

lisi = Person("lisi", 40)
lisi.eat()
lisi.eat()
lisi.eat()
lisi.run()