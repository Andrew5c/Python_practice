#!Anaconda/anaconda/python
#coding: utf-8

# BackgroundScheduler 使用案例
# 它启动后不会阻塞主线程的运行，而是在后台执行

from apscheduler.schedulers.background import BackgroundScheduler
import time

# 每一个任务在调度时，是以【线程】的方式运行的
def job3s():
    print('3s is time')
    return

def job5s():
    print('5s is time')
    return

if __name__ == '__main__':
    mySchedule = BackgroundScheduler(time='MST')

    # 任务以时间间隔执行，间隔3秒
    mySchedule.add_job(job3s, 'interval', id='3s_job', seconds=3)
    mySchedule.add_job(job5s, 'interval', id='5s_job', seconds=5)
    mySchedule.start()

    # 主线程的程序仍然能够执行到
    while True:
        print('main 1s')
        time.sleep(1)