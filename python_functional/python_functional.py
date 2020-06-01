#!Anaconda/anaconda/python
#coding: utf-8

# 一个普通的变量也可以指向函数
# 函数名其实就是指向函数的变量
print(abs(-10))
f = abs
print(f(-10))

# 高阶函数：将其他函数作为参数传入
def add(x, y, f):
    mysum = f(x) + f(y)
    return mysum

print(add(-1, 1, f))

# map方法
# 接收一个函数和iterable作为参数，该函数作用于每一个元素
# 并返回一个iterator
def squar(x):
    return x*x

r = map(squar, [1, 2, 3])
print(list(r))