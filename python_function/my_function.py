#!Anaconda/anaconda/python
#coding: utf-8
import math as m

# Python中函数名是指向一个对象的引用
# 可以把函数名赋值给一个变量，相当于取个“别名”
a = abs
print(a(-1))

# 函数定义示例
# 增加参数类型检查
def myABS(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(myABS(-100))

# 空函数
def wait():
    pass

# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * m.cos(angle)
    ny = y - step * m.sin(angle)
    return nx, ny

x, y = move(10, 10, 10, m.pi/6)
print('%.2f, %.2f' % (x, y))

# 其实函数只能返回一个值，上面的函数返回的其实是一个元组
value = move(10, 10, 10, m.pi/6)
print(value)

# ==========================================
print('='*40)
# 题目练习
# 计算一元二次方程的解
def quadratic(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError('bad operand type')
    delta = b*b - 4*a*c
    x1 = (-b + m.sqrt(delta)) / (2 * a)
    x2 = (-b - m.sqrt(delta)) / (2 * a)
    return x1, x2

print(quadratic(1, -5, 6))