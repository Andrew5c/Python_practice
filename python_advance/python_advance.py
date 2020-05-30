#!Anaconda/anaconda/python
#coding: utf-8

from collections import Iterable
# 切片： slice
name = ['a', 'b', 'c', 'd']
# 取前两个
print(name[1:3])
# 取后两个
print(name[-2:])
# 全部数据间隔2个取出
print(name[::2])

# tuple和str也可以使用类似切片操作

# 迭代： iteration
# list、tuple、dictionary、str都是可迭代对象
# 可以使用for循环对其进行迭代
dict = {'a':1, 'b':2, 'c':3}
for key in dict:
    print(key)
for v in dict.values():
    print(v)
for key,v in dict.items():
    print(key, v)

# 判断一个对象是可迭代对象
print(isinstance('abc', Iterable))
# 一个整数是不可迭代的
print(isinstance(123, Iterable))
print(isinstance(name, Iterable))

# 对list同时迭代索引和元素值
# enumerate() 函数可以将list变成一个【索引-值】对
for index, value in enumerate(name):
    print(index, value)

# 同时引用两个变量
pair = [(1,2), (3,4), (5,6)]
for x, y in pair:
    print('({0}, {1})'.format(x, y))

# ==========================================
print('='*40)

# 列表生成式