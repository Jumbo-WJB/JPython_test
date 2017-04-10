#!/usr/bin/python
# -*- coding:utf-8 -*-
import getopt
import sys
from domain import Domain
from dir import Dir
			
			
opts, args = getopt.getopt(sys.argv[1:], "hu:m:d:e:s:", ["help","url=","module=","dict=","errorkey=","save_path="])
url,module,dict,errorkey,save_path="","","","",""


for option, value in opts:
    if option in ["-u","--url"]:
        url = value
    elif option in ["-m","--module"]:
        module = value
    elif option in ["-d","--dict"]:
        dict = value
    elif option in ["-e","--errorkey"]:
        errorkey = value
    elif option in ["-s", "--save_path"]:
        save_path = value
    elif option in ["-h","--help"]:
        print "-h --help Show basic help message and exit"
        print "-u --url  Target URL"
        print "-d --dict  Dict"
        print "-e --errorkey  Dir_errorkey"
        print "-s --save_path  Dir_save_path"
        print "-m --module Module(Domain/Dir)"

		
if url and module == 'Domain':		
	domain = Domain(url)
	print '-'*10 + 'virustotal' + '-'*10
	domain.virustotal()
	print '-'*10 + 'chinaz' + '-'*10
	domain.chinaz()
	print '-'*10 + 'i_link' + '-'*10
	domain.i_link()

elif url and dict and errorkey and save_path and module == 'Dir':
	dir_scanner = Dir(url,dict,errorkey,save_path)
	dir_scanner.dir_scanner()


