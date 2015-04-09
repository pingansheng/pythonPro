#coding: utf-8
#进程与线程单元
import os

#print "process %s started...." % os.getpid()
# pid= os.fork() windows无法使用
# if pid==0:
#     print '''This is the child process, pid is %s,
#      parent process' pid is %s''' % (os.getpid,os.getppid())
# else:
#     print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)

#使用multiprocessing模块进行跨平台多进程支持
from multiprocessing import Process

# 子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    #创建进程对象，传入执行方法与参数列表
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    p.join()#等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print 'Process end.'

