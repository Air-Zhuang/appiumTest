# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/30 14:39'

from threading import Thread
from multiprocessing import Process

def show(a):
    print a

# Threads=[]
# for i in range(3):
#     t=Thread(target=show,args=(i,))
#     Threads.append(t)
# for i in Threads:
#     i.start()

# for i in range(3):
t=Process(target=show,args=(1,))
t.start()