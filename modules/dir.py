#!/usr/bin/python
# -*- coding:utf-8 -*-
#author:Jumbo
#website:www.chinabaiker.com
import requests
import threading
import Queue
import time

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
            if "%Domain%" in dict:
                dict = dict.replace("%Domain%",self.url.split("/")[2])
            if "%SubDomain%" in dict:
                dict = dict.replace("%SubDomain%",self.url.split('.')[0].split('/')[2])
            if "%DomainCenter%" in dict:
                dict = dict.replace("%DomainCenter%",self.url.split('.')[1])
            if "%DomainCenterAndTld%" in dict:
                dict = dict.replace("%DomainCenterAndTld%",self.url.split('/')[2].split('.')[1] + '.' + self.url.split('/')[2].split('.')[2])
            if "%DomainNoPoint%" in dict:
                dict = dict.replace("%DomainNoPoint%",self.url.split('/')[2].strip('.').replace('.',''))
            if "%DomainUnderLine%" in dict:
                dict = dict.replace("%DomainUnderLine%",self.url.split('/')[2].strip('.').replace('.','_'))
            if "%DomainCenterAndTldUnderLine%" in dict:
                dict = dict.replace("%DomainCenterAndTldUnderLine%",self.url.split('/')[2].strip('.').replace('.','_').split('_')[1] + '_' +  self.url.split('/')[2].strip('.').replace('.','_').split('_')[2])
            self.queue.put(dict.strip())
            

    def run(self):
        while not self.queue.empty():
            url = self.queue.get()
            self.dir_scanner(url)
            # self.queue.task_done()

    def save_file(self):
        with open(self.save_path, 'w+') as f:
            f.writelines(self.result_list)
        f.close()
        # self.queue.join()


    def dir_scanner(self, url):
        suffix = ['.orig', '~', '.~', '.original', '.swo', '.swp', '.txt', '.new', '.7z', '.tar.xz', '.tar.gz', '.rar', '.save', '.zip', '.bak', '.old']
        urlurl = self.url + url
        body = requests.get(urlurl,timeout = 3)
        # print body.content.decode('utf-8')
        if body.status_code == 200 and (self.errorkey in body.content) == False:
            print body.url
            self.result_list.append(body.url + '\n')
            for sfx in suffix:
                sfx_body = requests.head(body.url + str(sfx))
                if sfx_body.status_code == 200 and (self.errorkey in sfx_body.content) == False:
                    print sfx_body.url
                    self.result_list.append(sfx_body.url + '\n')
        




def main(url,dict,errorkey,save_path,thread):
    work = Dir(url, dict, errorkey, save_path,thread)
    work.open_dict()
    threads = []
    for i in range(int(thread)):
        s = threading.Thread(target=work.run)
        s.setDaemon(True)
        s.start()
        threads.append(s)
    for t in threads:
        t.join()
    work.save_file()
    print '----end-----'
