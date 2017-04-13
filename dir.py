#!/usr/bin/python
# -*- coding:utf-8 -*-
#author:Jumbo
#website:www.chinabaiker.com
import requests
import sys
import re
# import chardet 查看编码的库

class Dir(object):
    def __init__(self,url,dict,errorkey,save_path,thread):
        self.url = url
        self.dict = dict
        self.errorkey = errorkey
        self.save_path= save_path
        self.thread = thread
        self.queue = Queue.Queue()
        self.result_list = []
        # print self.errorkey

    def open_dict(self):
        for dict in open(self.dict, 'r'):
            self.queue.put(dict.strip())

    def run(self):
        while not self.queue.empty():
            url = self.queue.get()
            self.dir_scanner(url)



    def dir_scanner(self, url):
        suffix = ['.orig', '~', '.~', '.original', '.swo', '.swp', '.txt', '.new', '.7z', '.tar.xz', '.tar.gz', '.rar', '.save', '.zip', '.bak', '.old']
        urlurl = self.url + url
        body = requests.get(urlurl)
        # print body.content.decode('utf-8')
        # print urlurl
        if body.status_code == 200 and (self.errorkey.decode('gbk').encode('utf-8') in body.content) == False:
            print body.url
            self.result_list.append(body.url + '\n')
            for sfx in suffix:
                sfx_body = requests.head(body.url + str(sfx))
                if sfx_body.status_code == 200 and (self.errorkey.decode('gbk').encode('utf-8') in sfx_body.content) == False:
                    print sfx_body.url
                    self.result_list.append(sfx_body.url + '\n')



    def save_file(self):
        with open(self.save_path, 'w+') as f:
            f.writelines(self.result_list)
        f.close()
def main(url,dict,errorkey,save_path,thread):
    # print dict
    work = Dir(url, dict, errorkey, save_path,thread)
    work.open_dict()  ##获取所有待爆破的url
    for x in range(int(thread)):
        t = threading.Thread(target=work.run)
        t.start()
    work.save_file() ##爆破结果
