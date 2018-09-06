# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/29 16:20'

from appium import webdriver
from api import api
import time
import os
import subprocess

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
    # desired_caps['newCommandTimeout']='60'      #设置自动退出session的时间
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
if __name__ == '__main__':
    os.system('start startAppiumServer.bat')
    time.sleep(8)

    driver=get_driver()
    time.sleep(5)
    element=driver.find_element_by_id('cn.com.open.mooc:id/tab_layout')
    element.find_element_by_android_uiautomator('new UiSelector().index(3)').click()

    time.sleep(2)
    os.system('start stopAppiumServer.bat')
    time.sleep(2)
    os.system('start startAppiumServer.bat')
    time.sleep(8)

    driver2 = get_driver()
    time.sleep(5)
    element = driver2.find_element_by_id('cn.com.open.mooc:id/tab_layout')
    element.find_element_by_android_uiautomator('new UiSelector().index(3)').click()

    time.sleep(2)
    os.system('start stopAppiumServer.bat')


