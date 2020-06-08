#!Anaconda/anaconda/python
#coding: utf-8

# 多进程和多线程最大的区别：
# 多进程中，对于同一个变量，每一个进程都有一个该变量的拷贝，互不影响
# 多线程中，所有变量都由所有线程共享，任何一个变量可以由任何一个线程修改

# 线程间最大的危险：多线程会把一个变量给改乱了
# 此时，可以给一个函数上锁，线程只有获得该锁才能修改

import time, threading

balance = 0

# 创建一个锁
lock = threading.Lock()

def change_balance(n):
    global balance
    balance += n
    balance -= n

def run_thread(n):
    for i in range(100):
        # 需要先获取锁
        # 但是同时只能有一个线程能成功获取锁，然后继续执行代码
        # 其他线程只能继续等待，直到获取锁
        lock.acquire()
        try:
            change_balance(n)
        finally:
            # 保证最后能释放锁
            lock.release()
    return

if __name__ == '__main__':
    t1 = threading.Thread(target=run_thread, args=(3,))
    t2 = threading.Thread(target=run_thread, args=(5,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('balance finally: ', balance)


# 锁的好处：
# 确保某段关键代码只能由一个线程从头到尾完整的执行，避免混乱

# 坏处：
# 但是使用锁的时候，会阻止多线程的并发执行
# 包含锁的一段代码，实际上只能以单线程的模式执行
# 还要避免【死锁】现象
# 死锁：因为一个函数可能有多个锁，不同的线程持有不同的锁，但是都在试图获取对方的锁
