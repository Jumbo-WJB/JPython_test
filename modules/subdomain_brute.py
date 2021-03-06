#!/usr/bin/python
# -*- coding:utf-8 -*-
#author:Jumbo
#website:www.chinabaiker.com
import dns.resolver
import threading
import Queue

queue = Queue.Queue()

class SubDomainBrute(object):
    def __init__(self,sdomain,thread):
        self.sdomain = sdomain
        self.thread = thread
        self.rsv = dns.resolver.Resolver()
        self.queue = queue



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
            answers = self.rsv.query(subdomain)
            # print answers
            for answer in answers:
                print subdomain + ' ',answer

        except:
            pass

        self.queue.task_done()

def main(sdomain,thread):
    work = SubDomainBrute(sdomain,thread)
    work.open_dict()
    for i in range(int(thread)):
        c = threading.Thread(target=work.run)
        c.setDaemon(True)
        c.start()
    queue.join()
    print '----end-----'
