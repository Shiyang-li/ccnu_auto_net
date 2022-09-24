#!/usr/bin/env python3
import requests,json
import traceback
import sys
from time import sleep

username = "*******"  
passwd  =  "*******"


def success(content=""):
    print("==============================================\n\n[成功] %s\n\n==============================================\n"%content)
def failed(content=""):
    print("==============================================\n\n[失败] %s\n\n==============================================\n"%content)
def check():
    return "<img src=//www.baidu.com/img/gs.gif>" in requests.get("http://www.baidu.com").text
def loginCCNU(username="",passwd="",suffix=""):
    errmessage = None
    try:
        url = "http://10.220.250.50/0.htm"
        payload = {"DDDDD":"%s"%username,
                "upass":"%s"%passwd,
                "suffix":"%s"%suffix,
                "0MKKey":"123"}
        headers = { "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36","Content-Type": "application/x-www-form-urlencoded",}
        r = requests.post(url, data=payload ,headers = headers)
        # print(r.text)
        if "您已登录成功，欢迎使用！请不要关闭本页。" in r.text:
            return str(r.status_code),"1",errmessage
        else:
            return str(r.status_code),"0",errmessage
    except:
        errmessage = str(traceback.format_exc())
        return None,"0",errmessage

def loginoutCCNU(username="",passwd="",suffix=""):
    errmessage = None
    try:
        url = "http://10.220.250.50/F.htm"
        headers = { "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
                    "Content-Type": "application/x-www-form-urlencoded",}
        r = requests.get(url ,headers = headers)
        # print(r.text)
        if "华中师范大学无线校园网登录" in r.text:
            return str(r.status_code),"0","已注销"
        else:
            return str(r.status_code),"0","返回未知网页"
    except:
        errmessage = str(traceback.format_exc())
        return None,"0",errmessage

def testNet(number = 1):
    initnumber = number
    errmessage = None
    code = 0
    headers = { "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    if not str(number).isdigit() or number < 1:
        raise ValueError("设置的循环次数错误")
    try:
        while number >= 1:
            try:
                r = requests.get("http://www.blibili.com",timeout=0.8,headers=headers,verify=False)
                code = r.status_code
                # print(r.text)
                # print("refresh" in r.text)
                if r.status_code == 200:
                    if not "Dr.COMWebLoginID_0.htm" in r.text and not """meta http-equiv='refresh' content='1;""" in r.text:
                        break
                    else:
                        code = 0
            except:
                pass
                # print(str(traceback.format_exc()))
            number -= 1
    except:
        errmessage = str(traceback.format_exc())
    finally:
        if errmessage != None:
            return None,"0",errmessage
        elif code != 0:
            return str(code),"1","测试%s次，最终通过测试。"%(initnumber - number + 1)
        else:
            return None,"0","测试%s次，均未通过测试。"%initnumber

def superLogin(username="",passwd="",choose=""):
    username = str(str(username).split("@")[0])
    if choose == (True,False,False,False,False):
        suffix = "0"
    elif choose == (False,False,True,False,False):
        username += "@chinanet"
        suffix = "1"
    elif choose == (False,False,False,True,False):
        username += "@cmcc"
        suffix = "2"
    elif choose == (False,False,False,False,True):
        username += "@unicom"
        suffix = "3"
    else:
        return None,0,"POST的字段不合法，请重试。"
    # print(username,passwd,suffix)
    return loginCCNU(username,passwd,suffix)



if __name__ == "__main__":
	if len(sys.argv) == 1 or sys.argv[1] != '0':
		count = 1
		while count < 5:
			print("Try for %s time."%count)
			if check():
				success("无需登录，可访问网络。")
				break
			else:
				count += 1
				print(loginCCNU(username,passwd,"2"))
				if check():
					success("已经成功认证，可访问网络。")
					break
				else:
					failed("认证失败，不可访问网络。")
	else:
		print(loginoutCCNU(username,"","2"))

