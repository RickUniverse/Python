# str
name = "lisi"
# int
age = 18
# float
score = 52.9
# bool
isOk = True
# type
print(type(isOk))

# isOk + score = 53.9
print(isOk + score)

# name + age
print(name + age.__str__())

# input
password = input("input password:")
print(type(password)) # str
print(type(int(password))) # int

# input two
print(type(float(input("input float:"))))
