#!Anaconda/anaconda/python
#coding: utf-8

# 属性 daemon 被设置为 True的线程，称为【守护线程】
# 每个子线程的 daemon 属性默认为 False
# 当主线程结束时，守护线程会被 强制 终止
# 非守护线程的子线程，会在主线程结束后，继续执行自己的代码，直到结束
# join 方法用来同步线程。也就是主线程执行完成后，不会结束，而是进入阻塞状态
# 它会等待所有子线程执行结束后，在终止

# 当有些子线程是无限循环的时候，可能想要子线程和主线程一起结束
# 此时，可以将线程设置为 守护线程

import threading
import time


def sub_task():
    n = 0
    while n<3:
        n += 1
        print('this is a subtask---', threading.current_thread().name)
        time.sleep(1)
    return


if __name__ == '__main__':
    print('this is main thread...')
    myThread = threading.Thread(target=sub_task,name='subThread')
    myThread.daemon = True
    myThread.start()
    print('end main thread...')