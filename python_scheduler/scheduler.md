
## APScheduler中调度器的使用
> APScheduler是Python中定时任务调度框架。它提供基于固定时间间隔、日期的任务调度，并可以持久化任务，或者将任务以守护进程（daemon）的方式执行。


APScheduler中有两种常用的调度器：
- `BlockingScheduler`：调用`start()`方法后，会阻塞主线程的运行。
- `BackgroundScheduler`：调用`start()`方法后，不会阻塞主线程的运行，而是在应用后台执行。并且每个调度任务在主线程中，是以**线程**的形式被定时调用。

