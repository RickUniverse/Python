# 引用
a = 1 # 首先看等号右边的
print(id(a))
print(id(1))
b = a
print(id(b))
a = 2
print(id(a))
c = 1
print(id(b))
print(id(c))

# 函数返回值的引用
def function():
    result = "hello"
    print(id(result))
    return result

print(id(function()))

# hash()
# print(hash([]))
print(hash(1))
print(hash((1,2,3)))