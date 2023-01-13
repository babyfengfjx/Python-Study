---
title: python调度框架APScheduler使用详解（非阻塞模式)
categories: 
- python
tags:
- python
- 任务调度
date: 2022-01-20 11:11:34
---

## 定时任务设置：

定时任务，有阻塞和非阻塞方式两种，这个部分需要取分清楚:

- ```from apscheduler.schedulers.background import BackgroundScheduler``` 这个是非阻塞的；

- ```from apscheduler.schedulers.blocking import BlockingScheduler``` 这个是阻塞的，在没有其他主程序时，就需要用阻塞的方式，不然代码执行完主程序就结束了。



```Python
# coding=utf-8
"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second
intervals.
"""
 
from datetime import datetime
import time
import os
 
from apscheduler.schedulers.background import BackgroundScheduler
 
 
def tick():
    print('Tick! The time is: %s' % datetime.now())
 
 
if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)　　#间隔3秒钟执行一次
    scheduler.start()    #这里的调度任务是独立的一个线程
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
 
    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)    #其他任务是独立的线程执行
            print('sleep!')
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
        print('Exit The Job!')
```

# 非阻塞调度，在指定的时间执行一次

```Python
# coding=utf-8
"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second
intervals.
"""
 
from datetime import datetime
import time
import os
 
from apscheduler.schedulers.background import BackgroundScheduler
 
 
def tick():
    print('Tick! The time is: %s' % datetime.now())
 
 
if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    #scheduler.add_job(tick, 'interval', seconds=3)
    scheduler.add_job(tick, 'date', run_date='2016-02-14 15:01:05')　　#在指定的时间，只执行一次
    scheduler.start()    #这里的调度任务是独立的一个线程
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
 
    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)    #其他任务是独立的线程执行
            print('sleep!')
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
        print('Exit The Job!')
```

# 非阻塞的方式，采用cron的方式执行

```Python
# coding=utf-8
"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second
intervals.
"""
 
from datetime import datetime
import time
import os
 
from apscheduler.schedulers.background import BackgroundScheduler
 
 
def tick():
    print('Tick! The time is: %s' % datetime.now())
 
 
if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    #scheduler.add_job(tick, 'interval', seconds=3)
    #scheduler.add_job(tick, 'date', run_date='2016-02-14 15:01:05')
    scheduler.add_job(tick, 'cron', day_of_week='6', second='*/5')
    '''
        year (int|str) – 4-digit year
        month (int|str) – month (1-12)
        day (int|str) – day of the (1-31)
        week (int|str) – ISO week (1-53)
        day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
        hour (int|str) – hour (0-23)
        minute (int|str) – minute (0-59)
        second (int|str) – second (0-59)
        
        start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)
        end_date (datetime|str) – latest possible date/time to trigger on (inclusive)
        timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)
    
        *    any    Fire on every value
        */a    any    Fire every a values, starting from the minimum
        a-b    any    Fire on any value within the a-b range (a must be smaller than b)
        a-b/c    any    Fire every c values within the a-b range
        xth y    day    Fire on the x -th occurrence of weekday y within the month
        last x    day    Fire on the last occurrence of weekday x within the month
        last    day    Fire on the last day within the month
        x,y,z    any    Fire on any matching expression; can combine any number of any of the above expressions
    '''
    scheduler.start()    #这里的调度任务是独立的一个线程
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
 
    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)    #其他任务是独立的线程执行
            print('sleep!')
    except (KeyboardInterruptSystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
        print('Exit The Job!')
```

# 阻塞的方式，间隔3秒执行一次

```Python
# coding=utf-8
"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second
intervals.
"""
 
from datetime import datetime
import os
 
from apscheduler.schedulers.blocking import BlockingScheduler
 
 
def tick():
    print('Tick! The time is: %s' % datetime.now())
 
 
if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
 
    try:
        scheduler.start()    #采用的是阻塞的方式，只有一个线程专职做调度的任务
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
        print('Exit The Job!')
```

# 采用阻塞的方法，只执行一次

```Python
# coding=utf-8
"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second
intervals.
"""
 
from datetime import datetime
import os
 
from apscheduler.schedulers.blocking import BlockingScheduler
 
 
def tick():
    print('Tick! The time is: %s' % datetime.now())
 
 
if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'date', run_date='2016-02-14 15:23:05')
    
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
 
    try:
        scheduler.start()    #采用的是阻塞的方式，只有一个线程专职做调度的任务
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
        print('Exit The Job!')
```

# 采用阻塞的方式，使用cron的调度方法

```Python
# coding=utf-8
"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second
intervals.
"""
 
from datetime import datetime
import os
 
from apscheduler.schedulers.blocking import BlockingScheduler
 
 
def tick():
    print('Tick! The time is: %s' % datetime.now())
 
 
if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'cron', day_of_week='6', second='*/5')
    '''
        year (int|str) – 4-digit year
        month (int|str) – month (1-12)
        day (int|str) – day of the (1-31)
        week (int|str) – ISO week (1-53)
        day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
        hour (int|str) – hour (0-23)
        minute (int|str) – minute (0-59)
        second (int|str) – second (0-59)
        
        start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)
        end_date (datetime|str) – latest possible date/time to trigger on (inclusive)
        timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)
    
        *    any    Fire on every value
        */a    any    Fire every a values, starting from the minimum
        a-b    any    Fire on any value within the a-b range (a must be smaller than b)
        a-b/c    any    Fire every c values within the a-b range
        xth y    day    Fire on the x -th occurrence of weekday y within the month
        last x    day    Fire on the last occurrence of weekday x within the month
        last    day    Fire on the last day within the month
        x,y,z    any    Fire on any matching expression; can combine any number of any of the above expressions
    '''
    
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
 
    try:
        scheduler.start()    #采用的是阻塞的方式，只有一个线程专职做调度的任务
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
        print('Exit The Job!')
```

[转自此链接](https://www.cnblogs.com/cangqinglang/p/14338220.html)
