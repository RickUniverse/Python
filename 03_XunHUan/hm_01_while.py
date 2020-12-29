# while
i = 0
while i <= 10:
    #print("hello")
    if i == 8:
        break
    if i == 10:
        continue
    i += 1

print(i)
i -= 1
i **= 3
i %= 4
print()

row = 1
while row <= 5:
    count = 1
    while count <= row:
        print("*",end="")
        count += 1
    print("")
    row += 1

# 9*9
row2 = 1
while row2 <= 9:
    count = 1
    while count <= row2:
        print("%d * %d = %d" % (count , row2 , row2 * count),end="\t")
        count += 1
    print("")
    row2 += 1

# zhuan yi fu  \t : zhi biao fu
print("\" \t \n \\")