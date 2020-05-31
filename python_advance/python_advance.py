#!Anaconda/anaconda/python
#coding: utf-8
from collections import Iterable, Iterator


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

# 列表生成式： list comprehensions
# Python内置的用来创建list的生成式
myList1 = [x*x for x in range(1, 11)]
print(myList1)

# 增加if条件
myList2 = [x*x for x in range(1, 11) if x%2==0]
print(myList2)

# 两层循环，实现全排列
full_permutation = [m+n for m in 'ABC' for n in 'XYZ']
print(full_permutation)

# ==========================================
print('='*40)

# 生成器： generator
# 为了节省内存，不创建完整的list，而是将list元素按照某种算法推导出来
# 从而一边循环，一边计算
# generator保存的是计算下一个元素的算法
# 每次调用next，就计算下一个元素的值，直到最有一个元素

# 创建generator与列表生成式类似
g = (x for x in range(5))
print(g)
# 通过next()方法访问元素
print(next(g))
print(next(g))
# 循环遍历g的元素
for n in g:
    print(n)

# 一个普通的函数有类似generator的性质
def fib_1(max):
    print('functional generator')
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n += 1
    return 'Done'
fib_1(6)

# 用函数实现generator
# 包含yield关键字，不在是一个普通的函数
def fib_2(max):
    print('real generator')
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1
    return 'Done'
# 首先生成一个generator对象
f = fib_2(6)
# 调用next执行到yield，然后中断，下一次接着上一次断点继续执行
print(next(f), next(f), next(f))

# 更常用for循环来迭代
for n in fib_2(3):
    print(n)

# 但是for循环得不到generator的最终返回值
# 需要通过捕获一个【错误】来得到函数的return值
my_fib = fib_2(3)
while True:
    try:
        print('fib:', next(my_fib))
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


# ==========================================
print('='*40)

# 迭代器： iterator
# 可以被next()方法调用，并不断返回下一个值的对象称为迭代器
# list，tuple，dictionary，set，str，generator都可以直接作用于for循环
# 这类统称为可迭代对象：iterable
# 但只有generator是iterator
# 其他的也可以通过iter()方法变成iterator

# 判断是否iterator
print(isinstance((x for x in range(2)), Iterator))
print(isinstance([], Iterator))
print(isinstance(iter([]), Iterator))

# iterator对象表示一个数据流，可以看做一个有序的序列，但不知道这个序列的长度
# 只能通过next计算下一个数据，属于【惰性】的。

# for循环的本质是通过iterator的next()方法实现的
for x in [1, 2, 3, 4]:
    print(x)

# 等价于
it = iter([1, 2, 3, 4])
while True:
    try:
        print(next(it))
    except StopIteration:
        break