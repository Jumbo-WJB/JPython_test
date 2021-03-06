#!/usr/bin/python
# -*- coding:utf-8 -*-
#author:Jumbo
#website:www.chinabaiker.com
import requests
import threading
import Queue
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

queue = Queue.Queue()
s = requests.session()
s.keep_alive = False
class Dir(object):
    def __init__(self,url,dict,errorkey,save_path,thread):
        self.url = url
        self.dict = dict
        self.errorkey = errorkey
        self.save_path= save_path
        self.thread = thread
        self.queue = queue
        self.result_list = []

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
        while True:
            url = self.queue.get()
            self.dir_scanner(url)




    def dir_scanner(self, url):
        headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'http://www.google.com'
        }
        suffix = ['.orig', '~', '.~', '.original', '.swo', '.swp', '.txt', '.new', '.7z', '.tar.xz', '.tar.gz', '.rar', '.save', '.zip', '.bak', '.old']
        urlurl = self.url + url
        try:
            body = s.get(urlurl,timeout = 10,headers=headers, verify=False)
            # print body.content.decode('utf-8')
            if body.status_code == 200 and (self.errorkey in body.content) == False:
                print body.url
                self.result_list.append(body.url + '\n')
                for sfx in suffix:
                    sfx_body = s.get(body.url + str(sfx),headers=headers, verify=False)
                    if sfx_body.status_code == 200 and (self.errorkey in sfx_body.content) == False:
                        print sfx_body.url
                        self.result_list.append(sfx_body.url + '\n')
        except Exception as e:
            print e
            pass
        self.save_file()
        self.queue.task_done()
        
        

    def save_file(self):
        with open(self.save_path, 'w+') as f:
            f.writelines(self.result_list)
        f.close()




def main(url,dict,errorkey,save_path,thread):
    thread_list = []
    work = Dir(url, dict, errorkey, save_path,thread)
    work.open_dict()
    for i in range(int(thread)):
        t = threading.Thread(target=work.run)
        thread_list.append(t)
    for t in thread_list:
        t.setDaemon(True)
        t.start()
    queue.join()
    print '----end-----'
