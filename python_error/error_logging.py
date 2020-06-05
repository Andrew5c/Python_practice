#!Anaconda/anaconda/python
#coding: utf-8

import logging

# 记录错误
# 如果不捕获错误，我们可以记录并直接打印出错误堆栈
# logging 模块可以实现
# 同时程序会继续执行完毕
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def test():
    try:
        print('result: ', bar('0'))
    # Exception 基本上包含了所有的异常
    except Exception as e:
        # 会在控制台打印出当前的报错信息
        logging.exception(e)
    return

if __name__ == '__main__':
    test()
