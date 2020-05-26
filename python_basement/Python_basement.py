#!Anaconda/anaconda/python
#coding: utf-8

# 整数
a = 100
b = -100
c = 0xff

# 浮点数
d = 1.23
e = 1.23e4
f = 1.23e-4

# 字符串
h = 'abc'
i = "abd"
j = "I'm OK"
k = 'I\'m OK'
# r''表示内部的字符串默认不转义
print('\\\t\\')
print(r'\\\t\\')
# 在很多换行的字符串中，可以不用\n，而是使用如下格式
print('''line-1
line-2
line-3''')

# 布尔值，常用在逻辑运算和条件判断中
if True:
    print(True and False)
    print(True or False)
    print(not False)

# 空值，一个特殊的值，不可理解为0，
l = None

# 变量与赋值
m = 'abc'
n = m
m = 'ABC'
print('m: ', m)
print('n: ', n)

# Python中的两种除法
print(10/3)
# 地板除，对结果取整，不是四舍五入
print(5//3)
# 取余数
print(10%3)