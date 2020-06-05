#!Anaconda/anaconda/python
#coding: utf-8

# 抛出错误
# raise 抛出一个错误的实例
def foo(s):
    if int(s) == 0:
        # 向上层调用者抛出一个异常
        raise ValueError('Invalid Value: %s'% s)
    return 10 / int(s)

def error_raise():
    try:
        foo('0')
    except ValueError as e:
        print('Value Error!')
        # 当前函数不知道如何处理这个错误，继续向上抛出
        # 如果去掉下面这句代码，该程序不会输出执行错误
        raise

if __name__ == '__main__':
    error_raise()