# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/30 17:31'

import os
from threading import Thread
from execute_yaml import Execute_yaml

class Dos(object):
    def __init__(self):
        self.start_list=[]
        self.Execute_yaml=Execute_yaml()
    def get_adb_devices_list(self): #获取设备列表
        result_list=[]
        result=os.popen('adb devices').readlines()  #得到全部dos结果
        for i in result:
            if i=='\n':
                continue
            result_list.append(i.strip('\n'))
        del result_list[0]                          #删除第一个不需要的
        target=[]
        for i in result_list:
            target.append(i.split('\t')[0])              #得到设备名
        return target
    def judge_port(self,port):  #判断端口占用
        result = os.popen("netstat -ano | findstr "+str(port)+"").readlines()
        if result:
            return "Occupyed"
        else:
            return "Empty"
    def port_list(self,start_port,device_list): #生成空端口列表
        ports=[]
        ini_port=start_port-1
        for i in range(len(device_list)):
            port=ini_port+1
            while self.judge_port(port)!="Empty":
                port+=1
            ports.append(port)
            ini_port=port
        return ports
    def start_command_list(self,appium_start_port,bootstrap_start_port):    #生成启动appium dos启动命令列表
        command_list=[]
        device_list=self.get_adb_devices_list()
        appium_port_list=self.port_list(appium_start_port,device_list)
        bootstrap_port_list=self.port_list(bootstrap_start_port,device_list)
        self.Execute_yaml.clearfile()   #写之前先清空yaml文件
        for i in range(len(device_list)):
            command="appium -p "+str(appium_port_list[i])+" -bp "+str(bootstrap_port_list[i])+" -U "+str(device_list[i])+" --no-reset --session-override"
            command_list.append(command)
            self.Execute_yaml.writefile(i,appium_port_list[i],bootstrap_port_list[i],device_list[i])   #将信息写入yaml文件
        self.start_list=command_list
        return command_list
    def kill_server(self):
        os.system("taskkill -F -PID node.exe")
    def thread_method(self,i):  #下面多线程调用的方法，不能单独使用
        os.system(self.start_list[i])
    def threads_start(self,appium_start_port,bootstrap_start_port): #使用多线程启动多个appium服务
        self.kill_server()
        self.start_command_list(appium_start_port,bootstrap_start_port)
        for i in range(len(self.start_list)):
            thread=Thread(target=self.thread_method,args=(i,))
            thread.start()

if __name__ == '__main__':
    dos=Dos()
    print dos.get_adb_devices_list()
    # print dos.judge_port(4723)
    # print dos.port_list(4723,['aaa','bbb'])
    # command=dos.start_command_list(4723,4800)
    # print command
    # os.system(command[0])
    # dos.kill_server()
    # dos.threads_start(4723,4800)
