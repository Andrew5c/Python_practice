#!Anaconda/anaconda/python
#coding: utf-8

class Animal(object):
    # 增加一个类属性，所有实例都可以访问到
    # 因为他没有使用 self 这个实例变量来定义
    totalClass = 'animal'

    def run(self):
        print('this is animal')

# 继承 animal，它自动拥有父类的所有方法
# 可以重写父类 run 方法
# 并增加自己的方法
class Dog(Animal):
    def run(self):
        print('this is dog')

    def eat(self):
        print('dog is eating')

class Cat(object):
    def run(self):
        print('this is cat')

# 利用多态的好处
def run_twice(animal):
    animal.run()
    animal.run()


if __name__ == '__main__' :
    a = Animal()
    d = Dog()
    c = Cat()

    run_twice(a)
    run_twice(d)
    run_twice(c)

# 上面这种调用方式会依次的调用每个实例的 run() 方法
# 而在 run_twice() 函数中，我们只需要接收 他们共同父类 的类型就可以了
# 然后按照父类的数据类型进行操作即可。
# 那么后面调用这个方法的时候，只要传入的类型是该 父类 的子类，
# 就会自动调用实际类型的 run() 方法

# 开闭原则：
# 对扩展开放，允许新增 Animal 子类
# 对修改封闭，不需要修改依赖 Animal 类型的 run_twice 函数

# ================================================
    print('='*40)

    # dir() 方法
    # 获得一个对象的所有属性和方法
    print(dir('abc'))
    print(dir(d))

    # 配合 getattr(), setattr(), hasattr() 可以直接操作一个对象的状态
    print(hasattr(d, 'eat'))

    myRun = getattr(d, 'run')
    myRun()
