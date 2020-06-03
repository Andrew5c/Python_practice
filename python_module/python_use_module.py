#!Anaconda/anaconda/python
#coding: utf-8

# 一个 .py 文件就是一个模块 module
# 自己编写模块时，尽量避免自己的模块名与系统内置的模块重名
# 不同模块内部可以有相同名字的函数和变量
# Python为了避免不同人编写的模块名相同，引入 包 的概念，package
# 通过package来组织各个模块，包目录下面必须有 __init__.py 文件，可以是空文件，但是必须存在
# __init__.py 本身就是一个模块，他的名字就是 package 的名字

# ====================================
# 任何模块的第一个字符串会被视为文档注释
'learn to use the python modules'

__author__ = 'Andrew'

import sys

def test():
    # sys模块的 argv 变量以list的形式保存了命令行的所有参数
    # 他的第一个元素是这个 py 文件的名称
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!!')
    elif len(args) == 2:
        print('Hello, %s' % args[1])
    else:
        print('too many arguments!!')

# 在命令行运行该模块时，Python解释器吧一个特殊的变量 __name__ 设置为 __main__
# 因此，单独执行时，会执行下面的语句
# 但是当将该模块导入其他模块时。if 判断失效，不会执行下面的代码
# 因此这种风格可以允许模块通过命令行 执行 一些额外的测试代码
# make a script both importable and executable
if __name__ == "__main__":
    test()
