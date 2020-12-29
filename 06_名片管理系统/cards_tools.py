# 功能函数

# 名片列表
card_list = [
    {"name": "lisi",
     "phone": "123",
     "qq": "123",
     "email": "qwe"}
]

# 展示菜单
def show_menu():

    """显示菜单"""
    print("*" * 50)
    print("")
    print("1，新增名片")
    print("2，显示全部")
    print("3，搜索名片")

    print("\n\n0，退出系统")
    print("")
    print("*" * 50)

def new_card():

    """新增名片"""
    print("+" * 50)

    # 提示输入信息,并加入到名片列表中
    card_list.append({"name": input("请输入姓名："),
                 "phone": input("请输入电话："),
                 "qq": input("请输入qq："),
                 "email": input("请输入email：")})
    print("名片添加成功！")


def show_all():

    """显示所有名片
    :return: 没有数据就返回上一级，有则打印名片
    """
    print("+" * 50)
    # 判断是否有数据
    if len(card_list) == 0:
        print("没有数据")
        return
    # 打印表头
    for title in ["姓名", "电话", "QQ", "邮箱"]:
        print(title, end="\t\t\t")
    print("")
    # 打印名片信息
    for card in card_list:
        print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card["name"], card["phone"], card["qq"], card["email"]))


def search_card():

    """搜索名片
    :return: 返回上一级
    """
    print("+" * 50)

    find_name = input("请输入名字：")
    # 搜索名片
    for card in card_list:

        if card["name"] == find_name:
            print("姓名\t\t姓名\t\t姓名\t\t姓名")
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s" % (card["name"], card["phone"], card["qq"], card["email"]))

            # TODO 删除修改操作
            deal_or_update(card)

            return
    else:
        print("没有找到！")

# 删除或者修改
def deal_or_update(card):
    """
    查找到用户后的页面
    :param card: 用户查找到的字典
    :return: 返回上一级
    """
    operation = int(input("请选择需要进行的操作【1】删除【2】修改【0】返回上一级："))

    if operation == 1:
        card_list.remove(card)
        return
    elif operation == 2:
        card["name"] = input_card_info(card["name"], input("请输入新名字："))
        card["phone"] = input_card_info(card["phone"], input("请输入新phone："))
        card["qq"] = input_card_info(card["qq"], input("请输入新QQ："))
        card["email"] = input_card_info(card["email"], input("请输入新email："))
        return
    else:
        return

# 判断是否真正输入
def input_card_info(dict_value, tip_message):

    """判断是否真正输入
    :param dict_value: 字典原有的值
    :param tip_message: 用户输入的值
    :return: 如果用户输入了值且不是空格。便会返回用户输入的值，反之返回原有的值
    """
    if str(tip_message).isspace() or len(str(tip_message)) == 0:
        return dict_value
    else:
        return tip_message