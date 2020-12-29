def multiple_table():
    # 9*9
    row2 = 1
    while row2 <= 9:
        count = 1
        while count <= row2:
            print("%d * %d = %d" % (count, row2, row2 * count), end="\t")
            count += 1
        print("")
        row2 += 1
