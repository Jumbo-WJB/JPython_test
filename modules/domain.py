#!/usr/bin/python
# -*- coding:utf-8 -*-
#author:Jumbo
#website:www.chinabaiker.com
import requests
import json
import urllib
import re
import time
class Domain(object):
	def __init__(self,url):
		self.url = url
		self.domains = []
	
	def virustotal(self):
		try:
			domain = self.url
			apikey = '213ec3ed8377258bc770968a0feafe725db8a1f9dcdd2a16c74d37282113c912'
			virustotal_url = 'https://www.virustotal.com/vtapi/v2/domain/report?apikey=%s&domain=%s' %(apikey,domain)
			response = requests.get(virustotal_url).content
			response_dict = json.loads(response)
			if response_dict['response_code'] == 1:
				for i in response_dict['subdomains']:
					print i
					self.domains.append(i)
		except:
			pass
		
		
		
	def chinaz(self):
		try:
			chinaz_url = "http://s.tool.chinaz.com/same?s= "
			jieguo = urllib.urlopen(chinaz_url + str(self.url),timeout=5)
			content = jieguo.read()
			ree = r"\" target\=\_blank\>(.*?)\<\/a\>\<\/div\>"
			ss = re.findall(ree,content)
			for x in ss:
				print x
				self.domains.append(x)
		except:
			pass
				
				
	def i_link(self):
		try:
			data = "domain=" + self.url + "&b2=1&b3=1&b4=1"
			key = r"value=\"(.+?)\"><input"
			headers = {"Content-type":"application/x-www-form-urlencoded","Referer":"http://i.links.cn/subdomain/"}
			go = requests.post("http://i.links.cn/subdomain/",data=data,headers=headers,timeout=5)
			response = re.findall(key,go.content)
			for r in response:
				print r
				self.domains.append(r)
		except:
			pass


	def baidu_ce(self):
		try:
			baidu_ce_url = "http://ce.baidu.com/index/getRelatedSites?site_address="
			jieguo = urllib.urlopen(baidu_ce_url + str(self.url))
			content = json.loads(jieguo.read())
			content2 = content['data']
			if len(content2) > 0:
				for domain_s in content2:
					domainss = domain_s['domain']
					print domainss
					self.domains.append(domainss)
		except:
			pass


	def ThreatCrowd(self):
		try:
			s = requests.session()
			result =  s.get("https://www.threatcrowd.org/")
			time.sleep(8)
			result =  s.get("https://www.threatcrowd.org/searchApi/v2/domain/report/?domain=" + str(self.url))
			j = json.loads(result.text)
			for subdomainss in j['subdomains']:
				print subdomainss
				self.domains.append(subdomainss)
		except:
			pass


	def all_domain(self):
		domain_set = set(self.domains)
		for domainsss in domain_set:
			print domainsss
			
			
def main(url):
	domain = Domain(url)
	print '-' * 10 + 'virustotal' + '-' * 10
	domain.virustotal()
	print '-' * 10 + 'chinaz' + '-' * 10
	domain.chinaz()
	print '-' * 10 + 'i_link' + '-' * 10
	domain.i_link()
	print '-' * 10 + 'baidu_ce' + '-' * 10
	domain.baidu_ce()
	print '-' * 10 + 'ThreatCrowd' + '-' * 10
	domain.ThreatCrowd()
	print '-' * 10 + 'all' + '-' * 10
	domain.all_domain()
