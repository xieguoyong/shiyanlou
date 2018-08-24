# # -*- coding:utf-8 -*-
#
# """命令行火车票查看器
# Usage:
#     tickets [-gdtkz] <from> <to> <date>
#
# Options:
#     -h,--help       显示帮助菜单
#     -g              高铁
#     -d              动车
#     -t              特快
#     -k              快车
#     -z              直达
#
# Example:
#     tickets 北京 上海 2018-07-14
#     tickets -dg 北京 上海 2018-07-14
# """
#
# from docopt import docopt
#
# arguments = docopt(__doc__)
# print(arguments)
# options = ' '.join([key for key, value in arguments.items() if value is True])
# print(options)


# # test正则表达式
# import re
# s = "var station_names ='@bjb|北京北|VAP|beijingbei|bjb|0@bjd|北京东|BOP|beijingdong|bjd|1@bji|北京|BJP|beijing|bj|2@bjn|北京南|VNP|beijingnan|bjn|3@bjx|北京西|BXP|beijingxi|bjx"
#
# # stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', s)
# stations1 = re.findall(u'[\u4e00-\u9fa5]+\|[A-Z]+', s)
# print(stations1)
# stations2 = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', s)
# print(stations2)
#
#
# ls = re.findall(r"[0-9]\d{5}", "HHU 211100 HHU211000")
# print(ls)
#
# st = "FromaaafrombbbbFromcccc"
# print(re.findall(('^From'), st))

from selenium import webdriver
import time
import requests
import json

def get_token():
    api_url = 'https://qa-auth.dr-elephant.com/Token'
    request_data = '{"grant_type":"password","username":"testadmin","password":"123456","client_id":"Elephant.Admin","client_secret":"9CF09F23E2CD43718980F0CD483D4B07"}'
    # HEADER = {
    #     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    # }

    res = requests.post(api_url, data=request_data)
    return json.dumps(res.json()['data']['token'])


driver = webdriver.Chrome()
driver.get('https://qa-admin.dr-elephant.com/slide')

time.sleep(3)
# driver.add_cookie({'name': 'token', 'value': 'f53fe0f1-504b-4cac-adde-eb17e42fde72'})
driver.execute_script('localStorage.setItem("token", %s);' % get_token())

time.sleep(5)
driver.quit()
