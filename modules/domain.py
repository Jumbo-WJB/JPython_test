#!/usr/bin/python
# -*- coding:utf-8 -*-
#author:Jumbo
#website:www.chinabaiker.com
import requests
import json
import urllib
import re
import time
import os
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
			jieguo = urllib.urlopen(chinaz_url + str(self.url))
			content = jieguo.read()
			ree = r"\" target\=\_blank\>(.*?)\<\/a\>\<\/div\>"
			ss = re.findall(ree,content)
			for x in ss:
				print x
				x = x.replace('http://','')
				x = x.replace('https://','')
				self.domains.append(x)
		except:
			pass
				
				
	def i_link(self):
		try:
			data = "domain=" + self.url + "&b2=1&b3=1&b4=1"
			key = r"value=\"(.+?)\"><input"
			headers = {"Content-type":"application/x-www-form-urlencoded","Referer":"http://i.links.cn/subdomain/"}
			go = requests.post("http://i.links.cn/subdomain/",data=data,headers=headers)
			response = re.findall(key,go.content)
			for r in response:
				print r
				r = r.replace('http://','')
				r = r.replace('https://','')
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
			
	def Findsubdomains(self):
		try:
			findsubdomains_url = "https://findsubdomains.com/subdomains-of/"
			jieguo = urllib.urlopen(findsubdomains_url + str(self.url))
			content = jieguo.read()
			ree = r"\<a class\=\"aggregated\-link\" rel\=\"nofollow\" href\=\".*?\" target\=\"\_blank\"\> (.*?)\<\/a\>"
			ss = re.findall(ree,content)
			for z in ss:
				print z
				self.domains.append(z)
		except:
			pass


	def Securitytrails(self):
		try:
			Securitytrails_url = "https://securitytrails.com/list/apex_domain/"
			jieguo = urllib.urlopen(Securitytrails_url + str(self.url))
			content = jieguo.read()
			regex_page = r"\"max\_page\"\:(\d)\}\}\}"
			page_key = re.findall(regex_page,content)
			page_result = int(page_key[0])
			page_result_end = page_result + 1
			for p in range(1,page_result_end):
				securitytrails_url_page = 'https://securitytrails.com/list/apex_domain/%s?page=%s' %(str(self.url),p)
				securitytrails_url_content = requests.get(securitytrails_url_page).content
				regex_domain = r'<a href=\".*?/dns\">(.*?)</a></td>'
				domains = re.findall(regex_domain,securitytrails_url_content)
				for do in domains:
					print do
					self.domains.append(do)
		except:
			pass



	def fht_im(self):
		try:
			fht_im_url = "https://url.fht.im/domain_search?domain="
			jieguo = requests.get(fht_im_url + str(self.url))
			content = jieguo.content
			print content
			self.domains.append(content)
		except:
			pass



	def all_domain(self):
		with open('%s.txt'%(self.url),'w') as f:
			print self.domains
			domain_set = set(self.domains)
			for domainsss in domain_set:
				print domainsss
				f.write(domainsss + '\n')
		f.close()

			
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
	print '-' * 10 + 'Findsubdomains' + '-' * 10
	domain.Findsubdomains()
	print '-' * 10 + 'Securitytrails' + '-' * 10
	domain.Securitytrails()
	print '-' * 10 + 'fht_im' + '-' * 10
	domain.fht_im()
	print '-' * 10 + 'all' + '-' * 10
	domain.all_domain()
	print '-' * 10 + 'all' + '-' * 10
	print '国外api需要翻墙'
