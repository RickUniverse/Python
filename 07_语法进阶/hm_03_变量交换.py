# 变量交换, 整数变量交换
gl_a = 100
gl_b = 3

# 1
gl_a = gl_a + gl_b
gl_b = gl_a - gl_b
gl_a = gl_a - gl_b
print(gl_a)
print(gl_b)

# 2 字符串也可以进行交换
gl_a, gl_b = gl_b, gl_a
print(gl_a)
print(gl_b)