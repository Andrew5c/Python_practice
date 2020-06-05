#!Anaconda/anaconda/python
#coding: utf-8

import logging
# Python中程序执行遇到异常情况的处理

# try 执行可能会出现异常的代码
# except 用来捕获出现的异常，并执行相应的处理代码
# 当可能出现多个异常错误的时候，可以加多个 except 语句
# except 语句后面可以加 else， 当没有出现异常的时候，执行else
# 最后可以选择是否加上 finally 语句，进行善后工作

def fun_error(value):
    try:
        print('try...')
        r = 10 / int(value)
        print('result:', value)
    except ZeroDivisionError as e:
        print('zero division error: ', e)
    except ValueError as e:
        print('value error: ', e)
    else:
        print('no error!')
    finally:
        print('====END====')
    return


# Python的错误机制也是 class，所有的错误类型都继承自 BaseException
# 所以 except 不但捕获当前类型的错误，还会捕获它所有子类的错误


if __name__ == '__main__':
    # 以下调用分别会触发三种情况
    fun_error(2)
    fun_error(0)
    fun_error('a')
