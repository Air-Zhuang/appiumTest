# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/28 16:25'

from appium import webdriver

# import sys        #想要在命令行和jenkins上运行，必须将项目目录append
# import os
# path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(path)

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
# desired_caps['app']='apk路径'             #新版appium这一条可代替'appPackage'和'appActivity'
# desired_caps['appWaitActivity'] = 'com.imooc.component.imoocmain.splash.MCSplashActivity' #新版appium真机无法启动加上appWaitActivity
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

xy = driver.get_window_size("width")
print(xy)
x = xy['width']
y = xy['height']

# os.system("taskkill /F /IM node.exe")
