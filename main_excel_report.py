# encoding: utf-8
"""
@author: lileilei
@site: 
@software: PyCharm
@file: main_excel_report.py
@time: 2017/6/9 12:45
"""
from  Public.pyreport_excel import create
import os,time,unittest,datetime
from Case.ceshiyongli import Testinface

suite = unittest.TestSuite()
suite.addTest(Testinface("testinterface"))
me=Testinface()
list_fail, list_pass, list_json, listurls, listkeys, listconeents, listfangshis, listqiwangs, listids, listrelust, listnames=me.testinterface()
filepath =r'C:\Users\Administrator\Desktop\jiekou\report\relult.xls'
create(filepath,list_fail=list_fail, list_pass=list_pass, list_json=list_json, listurls=listurls, listkeys=listkeys,listconeents=listconeents, listfangshis=listfangshis, listqiwangs=listqiwangs, listids=listids, listrelust=listrelust, listnames=listnames)