# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/28 20:33'

from appium import webdriver
from api import api
import time

def get_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6'
    desired_caps['deviceName'] = '8ae28a45'
    desired_caps['appPackage'] = 'cn.com.open.mooc'
    desired_caps['appActivity'] = 'com.imooc.component.imoocmain.splash.MCSplashActivity'
    desired_caps['udid'] = '8ae28a45'           #苹果id
    desired_caps['noReset'] = 'True'            #如果不是True，每次启动app都会清除数据，是True，不需要再次安装
    desired_caps['unicodeKeyboard'] = 'True'    #unicodeKeyboard的编码方式来发送字符串
    desired_caps['resetKeyboard'] = 'True'      #将键盘隐藏起来
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
if __name__ == '__main__':
    driver=get_driver()
    time.sleep(5)
    api.swipe(driver,'left')
    time.sleep(1)
    api.swipe(driver,'left')
    time.sleep(1)
    api.swipe(driver,'right')
    time.sleep(1)

# examtitle = driver.find_elements_by_id("com.gionee.softmanager:id/exam_title")
# print examtitle
# xy = driver.get_window_size("width")
# print(xy)
# time.sleep(5)
#
# 滑动页面
# driver.swipe(900,1000,100,1000)
# time.sleep(1)
# driver.swipe(900,1000,100,1000,1000)
