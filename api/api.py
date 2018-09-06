# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/28 21:34'

import time

def swipe(driver,direction):
    xy=driver.get_window_size("width")
    x = xy['width']
    y = xy['height']
    if direction=='left':
        driver.swipe(x/10*9, y/2, x/10, y/2)
        print 'left swipe success!'
    elif direction=='right':
        driver.swipe(x/10, y/2, x/10*9, y/2)
        print 'right swipe success!'
    elif direction == 'up':
        driver.swipe(x/2, y/10*9,x/2,y/10)
        print 'up swipe success!'
    elif direction == 'down':
        driver.swipe(x/2, y/10,x/2,y/10*9)
        print 'down swipe success!'