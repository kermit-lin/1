#-*- codeing = utf-8 -*-
#@Time : 2020/9/2 11:59
#@Author : qxd
#@File : abi_a.py
#@Software : PyCharm
import pandas
import requests
import csv
import json

data = pandas.read_csv('F:\庞氏\智能合约\阈值\label_sc_open_hive.csv',header=None)
for i in range(0,1):
    #
    ponzi_name = data.iloc[:,0].get(i)
    url = 'https://api-cn.etherscan.com/api?module=contract&action=getabi&address='+ponzi_name+'&apikey=YourApiKeyToken'

    r = requests.get(url).text
    filename = ponzi_name + ".text"
    with open(filename, 'w',encoding='utf-8') as f:
        f.write(r)