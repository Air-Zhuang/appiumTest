# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/5/1 0:06'

from appium import webdriver
from api import api
import time
import os
from dos.execute_yaml import Execute_yaml

class Login(object):
    def __init__(self):
        self.driver=None
        self.Execute_yaml=Execute_yaml()
    def get_driver(self,i):
        device=self.Execute_yaml.readfile("user_info_"+str(i),"deviceName")
        port=self.Execute_yaml.readfile("user_info_"+str(i),"port")
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6'
        desired_caps['deviceName'] = device
        desired_caps['appPackage'] = 'cn.com.open.mooc'
        desired_caps['appActivity'] = 'com.imooc.component.imoocmain.splash.MCSplashActivity'
        desired_caps['udid'] = device           #苹果id
        desired_caps['noReset'] = 'True'            #如果不是True，每次启动app都会清除数据，是True，不需要再次安装
        desired_caps['unicodeKeyboard'] = 'True'    #unicodeKeyboard的编码方式来发送字符串
        desired_caps['resetKeyboard'] = 'True'      #将键盘隐藏起来
        driver = webdriver.Remote("http://127.0.0.1:"+str(port)+"/wd/hub", desired_caps)
        self.driver=driver
    def main(self,i):
        self.get_driver(i)
        driver=self.driver
        time.sleep(5)
        print '点击首页我的'
        driver.find_element_by_name(u'我的').click()
        time.sleep(1)
        print '点击登陆'
        driver.find_element_by_id('cn.com.open.mooc:id/rl_login_before').click()
        time.sleep(1)
        print '清除用户名'
        driver.find_element_by_id('cn.com.open.mooc:id/account_edit').clear()
        time.sleep(1)
        print '输入用户名'
        driver.find_element_by_id('cn.com.open.mooc:id/account_edit').send_keys('18363990025')
        time.sleep(1)
        print '输入密码'
        driver.find_element_by_id('cn.com.open.mooc:id/password_edit').send_keys('111aaa')
        time.sleep(1)
        print '点击登陆'
        driver.find_element_by_id('cn.com.open.mooc:id/login').click()
        time.sleep(1)
        print '向上滑动'
        api.swipe(driver,'up')
        time.sleep(1)
        print '点击设置'
        driver.find_element_by_id('cn.com.open.mooc:id/setting').click()
        time.sleep(1)
        print '向上滑动'
        api.swipe(driver, 'up')
        time.sleep(1)
        print '点击退出登陆'
        driver.find_element_by_id('cn.com.open.mooc:id/logout_label').click()
        time.sleep(1)
        print '点击确定'
        driver.find_element_by_id('cn.com.open.mooc:id/positiveBtn').click()

if __name__ == '__main__':
    login=Login()
    login.main(0)
