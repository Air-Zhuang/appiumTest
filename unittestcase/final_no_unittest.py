# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/5/1 0:14'

import sys
import os
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

from case.login2 import Login
from dos.dos_cmd import Dos
import time

if __name__ == '__main__':
    dos=Dos()
    login=Login()
    print dos.get_adb_devices_list()
    dos.threads_start(4723, 4800)
    time.sleep(8)
    login.main(0)
    time.sleep(5)
    os.system("taskkill -F -PID node.exe")
    time.sleep(1)
    sys.exit()
