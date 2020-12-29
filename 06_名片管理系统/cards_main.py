#！ /usr/bin/python3

import cards_tools
# 程序的入口
while True:
    # TODO(lisir) 显示功能菜单

    cards_tools.show_menu()

    action = int(input("请输入您想做的操作："))
    print("您选择的操作是【%s】" % action)

    # 判断操作是否存在
    if action in [1, 2, 3]:

        # 判断输入的是谁
        if action == 1:
            cards_tools.new_card()
        elif action == 2:
            cards_tools.show_all()
        elif action == 3:
            cards_tools.search_card()
        # pass
    elif action == 0:

        print("欢迎再次光临")
        break
        # pass
    else:
        print("操作不存在，请重新输入！")
