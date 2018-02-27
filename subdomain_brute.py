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
        self.mutex = threading.Lock()


    def open_dict(self):
        for sub in open('sub.txt', 'r'):
            self.queue.put(sub.strip())




    def run(self):
        while not self.queue.empty():
            sdomain  = self.queue.get()
            self.domainbrute(sdomain)



    def domainbrute(self, sdomain):
        self.mutex.acquire()
        subdomain = sdomain + '.' + self.sdomain
        try:
            subconnect = socket.gethostbyname_ex(subdomain)
            print subconnect[0] + ':' + subconnect[2][0]
            self.mutex.release()
        except:
            pass

# domain = sys.argv[1]
# thread = sys.argv[2]
# work = SubDomainBrute(domain,thread)
# mutex = threading.Lock()
# work.open_dict()
# for x in range(int(thread)):
#     t = threading.Thread(target=work.run)
#     t.start()
#     t.join()


def main(sdomain,thread):
    work = SubDomainBrute(sdomain,thread)
    # global mutex
    # mutex = threading.Lock()
    work.open_dict()
    for x in range(int(thread)):
        threadlist = [threading.Thread(target=work.run) for x in xrange(int(thread))]
        for t in threadlist:
            t.start()
        for t in threadlist:
            t.join()
    
