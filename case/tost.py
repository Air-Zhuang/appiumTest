# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/29 20:10'

from appium import webdriver
from api import api
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def get_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6'
    desired_caps['automationName'] = 'UiAutomator2' #必须配置这个才能抓到tost
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
    print '点击首页我的'
    driver.find_element_by_name(u'我的').click()
    time.sleep(1)
    print '点击登陆1'
    driver.find_element_by_id('cn.com.open.mooc:id/rl_login_before').click()
    time.sleep(1)
    print '点击登陆2'

    text=u'请输入密码'
    tost_element = ("xpath", "//*[contains(@text,"+text+")]")   #这里的中文必须是unicode
    driver.find_element_by_id('cn.com.open.mooc:id/login').click()
    print WebDriverWait(driver,10,0.1).until(expected_conditions.presence_of_element_located(tost_element))