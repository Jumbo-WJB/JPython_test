#!/usr/bin/python
# -*- coding:utf-8 -*-
#author:Jumbo
#website:www.chinabaiker.com


from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time

class Appscan(object):
    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Chrome()


    def Browser(self):
        c1 = {'name': u'Hm_lvt_2d9a49e839eXXXXXXXXXXXXXX80','value': u'1494xxx55,1494xx40,149xxx0,1496294xx20'}
        c2 = {'name': u'Hm_lpvt_2d9a49e839e5xx897ae80','value': u'1496xx925'}
        c3 = {'name': u'PGSessionId','value': u'8b5exxxc-8d513db5a6b7'}
        self.driver.get(self.url )
        self.driver.delete_all_cookies()
        self.driver.add_cookie(c1)
        self.driver.add_cookie(c2)
        self.driver.add_cookie(c3)
        time.sleep(2)
        self.driver.get(self.url )
        time.sleep(2)


    def Result(self):
        soup = BeautifulSoup(self.driver.page_source,'html.parser')
        ip_body = soup.find_all(class_="padd-20 c-f c_list c_list_4 ovyau min-h-100 h-m-500")[0]
        ip_regex = "ip\:'(.*?)'"
        ip_key = re.findall(ip_regex,str(ip_body))
        domain_body = soup.find_all(class_="padd-20 c-f c_list c_list_2 ovyau min-h-100 h-m-500")[0]
        domain_regex = "domain\:'(.*?)'"
        domain_key = re.findall(domain_regex,str(domain_body))
        mail_body = soup.find_all(class_="padd-20 c-f c_list ovyau min-h-100 h-m-500")[0]
        mail_regex = "email\:'(.*?)'"
        mail_key = re.findall(mail_regex,str(mail_body))
        print '-' * 10 + 'IP' + '-' * 10
        for ip_k in ip_key:
            print ip_k.strip()
        print '-' * 10 + 'Domain' + '-' * 10
        for domain_k in domain_key:
            print domain_k.strip()
        print '-' * 10 + 'Mail' + '-' * 10
        for mail_k in mail_key:
            print mail_k.strip()
        self.driver.quit()

def main(url):
    appscan = Appscan(url)
    appscan.Browser()
    appscan.Result()



# work = Appscan("http://appscan.io/app-report.html?id=xxxxxxxxxxxxxxx")
# work.Browser()
# work.Result()

