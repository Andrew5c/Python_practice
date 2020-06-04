#!Anaconda/anaconda/python
#coding: utf-8

# 面向对象编程，把对象作为程序的基本单元
# 一个对象包含了【数据】和【操作数据的函数】
# 面向对象的三大特性： 封装、继承、多态

# Python中，所有数据类型都可以视为对象，也可以自定义对象
# 自定义的对象数据类型就是面向对象中的【类】的概念

# 定义一个类
# 当我们定义了一个class 的时候，实际上定义了一种数据类型
# 这种数据类型和 list，str，dic 没什么区别
class Student(object):

    # init 中的第一个参数self，表示创建的实例本身
    def __init__(self, name, score, num):
        self.name = name
        self.score = score

        # 属性的名称前面加 __ 双下划线，将其变为私有属性，外部不能直接访问
        self.__number = num

    # 类似 __xxx__ 的属性和方法在Python中有特殊的用途
    def __len__(self):
        return len(self.name)

    # 类 中定义的函数，一般称为【方法】，第一个参数永远是实例变量 self
    # 利用类内函数访问数据，实现数据的【封装】
    def print_score(self):
        print('the score is %s' % self.score)

    # 通过自定义的方法来访问私有属性
    def get_num(self):
        return self.__number

    # 通过这种方法，可以做参数检查
    def set_num(self, newNum):
        self.__number = newNum

# 实例化一个对象
andrew = Student('andrew', 90, '123456789')

# 调用对象的关联函数，实际上是给对象发消息
andrew.print_score()

# 这样使用 类似 __xxx__ 的属性和方法
# 如果没有定义这种方法，不能直接对 实例 使用 len()
print(len(andrew))

# 可以自由的给实例变量绑定属性
andrew.rank = 'good'
print(andrew.rank)

# 上面说了，定义的一个类就是一种数据类型，因此我们可以判断一个变量是否指向了这个数据类型
print(isinstance(andrew, Student))