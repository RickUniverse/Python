import hm_01_99

hm_01_99.multiple_table()


def sum_2_num(sum, num):
    """"求和函数
    :param sum 值1
    :param num 值2
    """
    return sum + num

print(sum_2_num(1 , 2))


def print_line(char, times):
    """打印一行"""

    print("%s" % char * times)


def print_lines(char, times):
    """打印多行"""

    i = 1

    while i <= 5:

        print_line(char, times)

        i += 1

print_lines(9, 9)

