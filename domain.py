#!/usr/bin/python
# -*- coding:utf-8 -*-
#author:Jumbo
#website:www.chinabaiker.com
import requests
import json
import urllib
import re
class Domain(object):
	def __init__(self,url):
		self.url = url
	
	
	def virustotal(self):
		virustotal_url = 'https://www.virustotal.com/vtapi/v2/domain/report'
		parameters = {'domain': self.url, 'apikey': '213ec3ed8377258bc770968a0feafe725db8a1f9dcdd2a16c74d37282113c912'}
		response = urllib.urlopen('%s?%s' % (virustotal_url, urllib.urlencode(parameters))).read()
		response_dict = json.loads(response)
		if response_dict['response_code'] == 1:
			for i in response_dict['subdomains']:
				print i
		
		
		
	def chinaz(self):
		chinaz_url = "http://s.tool.chinaz.com/same?s= "
		jieguo = urllib.urlopen(chinaz_url + str(self.url))
		content = jieguo.read()
		ree = r"\" target\=\_blank\>(.*?)\<\/a\>\<\/div\>"
		ss = re.findall(ree,content)
		for x in ss:
			print x
				
				
				
	def i_link(self):
		data = "domain=" + self.url + "&b2=1&b3=1&b4=1"
		key = r"value=\"(.+?)\"><input"
		headers = {"Content-type":"application/x-www-form-urlencoded","Referer":"http://i.links.cn/subdomain/"}
		go = requests.post("http://i.links.cn/subdomain/",data=data,headers=headers)
		response = re.findall(key,go.content)
		for r in response:
			print r
