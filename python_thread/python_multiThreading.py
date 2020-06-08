#!Anaconda/anaconda/python
#coding: utf-8

# 进程是由若干线程组成，一个进程至少包含一个线程
# 这里只讨论 threading 这个高级模块

# 启动一个线程就是把一个【函数】传入，并创建 Thread 实例，然后调用start执行
import time,threading

# 定义新线程要执行的函数
def loop():
    # 打印出当前线程的名字
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 3:
        n += 1
        print('thread %s >>> %d' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s is ended.' % threading.current_thread().name)


# 每一个进程执行的时候，默认会启动一个线程----> 主线程
# 主线程又可以启动新的线程
if __name__ == '__main__':

    # 打印主线程的名字，永远是 MainThread
    print('thread %s is running...' % threading.current_thread().name)

    # 创建一个线程，并指定名字，默认是Thread-1  -2...
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)

