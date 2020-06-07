#!Anaconda/anaconda/python
#coding: utf-8

# process之间有时是需要进行通信的
# Python提供了 Queue 、 Pipes 等多种方式来交换数据

from multiprocessing import Process, Queue
import time, os, random

# 向queue中写数据函数
def write(q):
    print('process to write: %s' % os.getpid())
    for x in ['A', 'B', 'C']:
        print('put %s to queue...' % x)
        q.put(x)
        time.sleep(random.random())
    return

# 从queue中读取数据函数
def read(q):
    print('process to read %s' % os.getpid())
    # 该进程一旦启动就不停的读取
    while(True):
        x = q.get(True)
        print('get %s from queue' % x)
    return

if __name__ == '__main__':

    # 父进程创建 Queue，并传递给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()

    # 等待写操作完成，在这个过程中，读操作会同步执行
    # 最终结果是写一个、读一个，估计是queue的put方法和get方法内部的机制导致的
    pw.join()

    # read 内部是死循环，需要强行终止
    # 如果不强行终止的话，程序会一直停留在queue的读操作中
    pr.terminate()