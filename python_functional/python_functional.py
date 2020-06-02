#!Anaconda/anaconda/python
#coding: utf-8

import functools


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

# list中的数字变为字符串
print(list(map(str, [1, 2, 3])))

# filter
# 用于过滤序列，和map类似，但是根据函数返回的true和false决定是否舍弃该值
# 例：过滤奇数
def is_odd(n):
    return n%2 == 1

odds = list(filter(is_odd, [1, 2 ,3, 4, 5, 6]))

# sorted
# 可以对list进行排序，该函数就是将比较的过程通过函数抽象出来
# 因此可以作用在list上
mylist = [1, 2, 3, -1, -2, -3]
print(sorted(mylist))

# 通过接收一个key函数来实现自定义的排序
# 先将该函数作用于每个元素，然后对返回值进行排序
print(sorted(mylist, key=abs))

# 另一个例子
mystr = ['bob', 'about', 'Zoo', 'credit']
print(sorted(mystr, key=str.lower, reverse=True))

# =================================================
print('='*40)

# 函数作为返回值
# 例：求和时，不立刻返回求和结果
def lazy_sum(*args):
    def sum():
        temp = 0
        for n in args:
            temp += n
        return temp
    return sum

# 此时，调用lazy sum，返回一个函数
print(lazy_sum(1, 2, 3))
# 对其返回结果再次调用
f1 = lazy_sum(1, 2, 3)
print(f1())

# 当lazy sum返回函数sum的时候，参数和变量都保存在返回的函数中
# 这种行为称为【闭包】，closure

# 并且多次调用，不影响
f2 = lazy_sum(1, 2, 3)
print(f2())

# =================================================
print('='*40)

# lambda， 匿名函数
# 没有函数名，只能有一个表达式

# 比如前面应用map的时候，如果匿名函数
# 冒号前面是参数，后面是表达式
L = map(lambda x: x*x, [1, 2, 3])
print(list(L))

# 匿名函数赋值给变量
mylambda = lambda x: x*x
print(mylambda(5))

# 返回匿名函数
def return_lambda(x, y):
    return lambda : x*x + y*y

print(return_lambda(2, 3)())



# =================================================
print('='*40)

# 装饰器
# 之前说过，函数也是一个对象，可以赋值给一个变量，然后通过变量调用该函数
def now():
    print('2020-6-2')

another_now = now
print(another_now())

# 得到函数的名字
print(now.__name__, another_now.__name__)


# 现在想增加now函数的功能，但是又不改变他的原本定义
# 用【装饰器 decorator】实现
# 就是在代码运行期间动态的增加函数功能
# 定义一个完整的decorator
def mylog(function):
    # 将原始函数的__name__属性复制到wrapper中
    # 否则有些依赖函数签名的代码会报错
    @functools.wraps(function)
    def wrapper(*args, **kw):
        print('call %s()' % function.__name__)
        return function(*args, **kw)
    return wrapper

# 使用装饰器增强函数
@mylog
def my_now():
    print('this is now')

print(my_now())
# 通过上面的输出可以发现，它先执行了装饰器里面的函数
# 其实 @mylog 相当于执行了 my_now = mylog(my_now)
# 使得 my_now 这个变量指向了装饰器返回的新的函数，而装饰器里面的那个
# 函数又调用了原始的 my_now 函数。因此实现了函数的增强


# 带参数的decorator
def my_log_new(text):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kw):
            print('text: %s, function: %s()' % (text, function.__name__))
            return function(*args, **kw)
        return wrapper
    return decorator

@my_log_new('to execute')
def print_now():
    print('this is now')

print(print_now())