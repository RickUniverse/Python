class HouseItem:
    def __init__(self, new_name, new_area):
        self.name = new_name
        self.area = new_area
    def __str__(self):
        return "家具名：%s；占地面积：%.3f"


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []
    def __str__(self):
        return ("户型：%s;\t\n总面积：%.3f;\t\n剩余面积：%s;\t\n家具列表：%s;"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):
        """添加家具"""
        print("-" * 40)
        print("将要添加的家具%s" % item.name)
        if item.area > self.free_area:
            print("家具太大：添加失败！")
            return
        self.item_list.append(item.name)

        self.free_area -= item.area
        print("添加成功！")

# 实例化家具
chuang = HouseItem("床", 10)
chuang2 = HouseItem("床2", 1)
chuang3 = HouseItem("床3", 14)
chuang4 = HouseItem("床4", 40)
# 实例化家
jia = House("超大户型", 100)
print(jia)
# 添加家具
jia.add_item(chuang2)
print(jia)
jia.add_item(chuang)
print(jia)
jia.add_item(chuang4)
print(jia)
jia.add_item(chuang4)
print(jia)
jia.add_item(chuang4)
print(jia)
