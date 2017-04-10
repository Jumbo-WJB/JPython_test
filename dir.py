#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import sys
import re
# import chardet 查看编码的库

class Dir(object):
    def __init__(self,url,dict,errorkey,save_path):
        self.url = url
        self.dict = dict
        self.errorkey = errorkey
        self.save_path= save_path
        print self.errorkey



    def dir_scanner(self):
        save = open(self.save_path, 'w')
        for dict in open(self.dict,'r'):
            dict = dict.strip()
            body = requests.get(self.url+str(dict))
                # print body.content.decode('utf-8')
            if body.status_code == 200 and (self.errorkey.decode('gbk').encode('utf-8') in body.content) == False:
                # print self.errorkey
                print body.url
                save.write(body.url + '\n')
        save.close()

