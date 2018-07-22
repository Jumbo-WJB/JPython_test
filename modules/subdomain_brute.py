#!/usr/bin/python
# -*- coding:utf-8 -*-
#author:Jumbo
#website:www.chinabaiker.com
import socket
import sys
import threading
import Queue

class SubDomainBrute(object):
    def __init__(self,sdomain,thread):
        self.sdomain = sdomain
        self.thread = thread
        self.queue = Queue.Queue()



    def open_dict(self):
        for sub in open('dict/top1w.txt', 'r'):
            self.queue.put(sub.strip())




    def run(self):
        while True:
            sdomain  = self.queue.get()
            self.domainbrute(sdomain)


    def domainbrute(self, sdomain):
        subdomain = sdomain + '.' + self.sdomain
        try:
            subconnect = socket.gethostbyname_ex(subdomain)
            print subconnect[0] + ':' + subconnect[2][0]
        except:
            pass



def main(sdomain,thread):
    queue  = Queue.Queue()
    work = SubDomainBrute(sdomain,thread)
    work.open_dict()
    for i in range(int(thread)):
        c = threading.Thread(target=work.run)
        c.start()
    print '----end-----'
