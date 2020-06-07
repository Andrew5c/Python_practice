#!Anaconda/anaconda/python
#coding: utf-8

# 如果要启动大量的子进程，可以使用进程池的方法批量创建

from multiprocessing import Pool
import os, time, random

# 每个进程执行的任务就是 等待一个任意的时间
def long_time_task(p):
    print('run task %s (%s).' % (p, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('task %s run %.2f seconds.' % (p, (end-start)))
    return


if __name__ == '__main__':
    print('parent process %s.' % os.getpid())

    # 创建一个可以容纳4个进程的 进程池，表明一次可以同时跑4个进程
    p = Pool(4)

    # 进程池的容量默认大小是 CPU 的核心数
    # 我当前电脑是4个核心，因此如果上面不给参数的话，它就默认是4
    # 当然你也可以填入任意 n>4 的数，那么多余的进程会被平均分配给每个核心进行分时处理
    # 此时程序输出的结果是n个进程都同时运行了，其实是每个核心分时处理的结果

    # 启动5个进程，那么就必然有一个进程要等到前面进程池中的4个之一结束
    # 才可以执行第5个进程
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))

    # 启动之后，他们开始自动执行进程池中的所有进程
    print('waitting for all processes done...')

    # 进程join之前，必须先close，之后不能添加新的进程
    p.close()
    # 等待所有进程执行完毕
    p.join()