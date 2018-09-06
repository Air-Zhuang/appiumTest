# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/30 12:57'

import unittest
import HTMLTestRunner
import os
from threading import Thread
import time

class CaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print 'setUpClass'
    def setUp(self):
        print 'setUp'
    def test_01(self):
        print 'test_01'
    def test_02(self):
        print 'test_02'
    def tearDown(self):
        print 'tearDown'
    @classmethod
    def tearDownClass(cls):
        print 'tearDownClass'
def get_suite(htmlName):
    '''自带得TestSuite'''
    # suite=unittest.TestSuite()
    # suite.addTest(CaseTest("test_01"))
    # suite.addTest(CaseTest("test_02"))
    # unittest.TextTestRunner().run(suite)
    '''使用HTMLTestRunner'''
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_01"))
    suite.addTest(CaseTest("test_02"))
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\report\\"+'repoet'+str(htmlName)+".html"
    f = file(path, "wb")
    HTMLTestRunner.HTMLTestRunner(f).run(suite)

if __name__ == '__main__':
    '''多线程+HTMLTestRunner'''
    Threads = []
    for i in range(30):
        t = Thread(target=get_suite, args=(i+1,))
        Threads.append(t)
    for i in Threads:
        time.sleep(0.1)     #一定要加等待，不然会因为速度太快生成不了最后一个报告
        i.start()


