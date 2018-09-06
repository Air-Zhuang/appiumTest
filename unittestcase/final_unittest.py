# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/5/1 0:26'

import unittest
import HTMLTestRunner
import os
from threading import Thread
from case.login2 import Login
from dos.dos_cmd import Dos
import time

class ParameTestCase(unittest.TestCase):
    def __init__(self,methodName='runTest',parame=None):
        super(ParameTestCase,self).__init__(methodName)
        global parames
        parames=parame

class CaseTest(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        print '============================setUpClass============================'
        dos = Dos()
        print dos.get_adb_devices_list()
        dos.threads_start(4723, 4800)
        time.sleep(8)
    def setUp(self):
        print '============================setUp============================'
    def test_01(self):
        print '============================test_01============================'
        login = Login()
        login.main(0)
    def tearDown(self):
        print '============================tearDown============================'
    @classmethod
    def tearDownClass(cls):
        print '============================tearDownClass============================'
def get_suite(htmlName,param):
    '''自带得TestSuite'''
    # suite=unittest.TestSuite()
    # suite.addTest(CaseTest("test_01"))
    # suite.addTest(CaseTest("test_02"))
    # unittest.TextTestRunner().run(suite)
    '''使用HTMLTestRunner'''
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_01",parame=param))
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\report\\"+'repoet'+str(htmlName)+".html"
    f = file(path, "wb")
    HTMLTestRunner.HTMLTestRunner(f).run(suite)

if __name__ == '__main__':
    # suite=unittest.TestSuite()
    # suite.addTest(CaseTest("test_01",parame='aaa'))
    # unittest.TextTestRunner().run(suite)
    get_suite(1,0)