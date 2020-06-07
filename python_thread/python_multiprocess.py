#!Anaconda/anaconda/python
#coding: utf-8

from multiprocessing import Process
import os

# 在Linux系统上，可以使用 fork() 方法创建子进程
# 在Windows下面，使用 multiprocessing 模块进行多进程的相关操作

# 定义子进程要做的事情
def run_proc(name):
    print('run child process %s (%s)' % (name, os.getpid()))
    return

if __name__ == '__main__':
    print('parent process %s.' % os.getpid())
    # 创建一个子进程
    p = Process(target=run_proc, args=('test',))

    print('child process will start.')
    # 启动子进程
    p.start()
    # 等待子进程执行结束在继续执行往下运行，常用于进程间的同步
    p.join()
    print('child process end.')