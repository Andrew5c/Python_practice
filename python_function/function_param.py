#!Anaconda/anaconda/python
#coding: utf-8

# 位置参数
# 调用时，需要按照位置顺序依次传入两个参数
def power_1(x, n):
    if not isinstance(x, (int, float)) or not isinstance(n, int):
        raise TypeError('bad operand type')
    s = 1
    while n > 0:
        n -= 1
        s = s*x
    return s

print(power_1(2, 3))

# 默认参数
# 调用该函数时，没有传入的参数将使用默认参数
# 注意： 必选参数在前，默认参数在后
def power_2(x, n = 2):
    if not isinstance(x, (int, float)) or not isinstance(n, int):
        raise TypeError('bad operand type')
    s = 1
    while n > 0:
        n -= 1
        s = s*x
    return s

print(power_2(2))

# 当有多个默认参数时，有两种传入方式
# 1、按顺序传入，对应位置没有传入的将使用默认参数
# 2、使用参数名指定传入
def power_3(x, n = 2, prise = 10):
    if not isinstance(x, (int, float)) or not isinstance(n, int):
        raise TypeError('bad operand type')
    s = 1
    while n > 0:
        n -= 1
        s = s*x
    return s+prise

# 下面这个调用，prise将使用默认参数
print(power_3(2, 3))
# 下面这个调用，n使用默认参数
print(power_3(2, prise=1))

# 注意： 默认参数必须指向【不变对象】
# 比如下面这个函数，默认参数是一个列表，是可变对象
# 当多次使用默认参数调用时，列表的内容会保存每次调用的改变
def add_end(L = []):
    L.append('END')
    return L
print(add_end())
print(add_end())

# 解决方法 ： 使用不变对象None
# 【不变对象】一旦创建，对象内部的数据就不能被改变。
# 此时，多任务环境下同时读取不变对象就不需要加锁
def add_end_new(L = None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end_new())
print(add_end_new())


# 可变参数
# 输入的参数的个数是可变的
# 要求计算一组任意长度数字的平方和

# 1、利用list或者tuple作为参数
# 但是此时，函数本身传入的还是一个参数，只是参数指向的内容不同
def calc_1(numbers):
    sum = 0
    for i in numbers:
        sum += i*i
    return sum

print(calc_1([1, 2, 3]))
print(calc_1([1, 2]))

# 2、输入单个数字的可变参数
# 形参前面加 *
# 函数内部，将接收到的参数作为一个tuple处理
def cals_2(*numbers):
    sum = 0
    print(numbers)
    for i in numbers:
        sum += i*i
    return sum

print(cals_2(1, 2, 3))
print(cals_2(1, 2))

# 对于这种函数的调用，如果仍想传入一个list或tuple
# 在参数前面加 *
# 表示将list或tuple的所有元素作为可变参数传入
L = [1, 2, 3]
print(cals_2(*L))


# 关键字参数
# 允许用户传入任意个含参数名的参数，内部作为dictionary处理
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'others:', kw)


print(person('andrew', 10))
print(person('andrew', 10, city='Jiangsu', home='kunshan'))

# 或者直接给关键字参数传入一个dictionary
# kw将获得这个dictionary的一个拷贝
dict = {'city':'Jiangsu', 'home':'Kunshan'}
print(person('andrew', 10, **dict))


# 命名关键字参数
# 定义时，要与位置参数分隔，用 *
# 调用时，必须传入参数名
def name_person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

print(name_person('andrew', 10, job='student'))

# ==========================================
print('='*40)

# 递归函数
# 函数在其内部调用自身
# 实现一个n的阶乘
def fact(n):
    if n == 1:
        return n
    return n*fact(n-1)

print(fact(10))
