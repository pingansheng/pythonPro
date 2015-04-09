#coding: utf-8
#多线程
#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
import time, threading

# 新线程执行的代码:
def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(0.1)
    print 'thread %s ended.' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t1 = threading.Thread(target=loop, name='LT1')
t1.start()
t1.join()
t2=threading.Thread(target=loop, name='LT2')
t2.start()
#t2.join()
print 'thread %s ended.' % threading.current_thread().name

import time, threading

# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance#不是0，线程执行可能中断


#线程锁
balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance

from multiprocessing import Pool,freeze_support
import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

#死循环测试,多进程占满cpu，多线程不可以，Python机制多线程循环执行，GIL锁问题
#multiprocessing.freeze_support()
#if __name__=="__main__":
p=Pool()
for i in range(multiprocessing.cpu_count()):
    p.apply_async(loop)
p.close()
p.join()
        