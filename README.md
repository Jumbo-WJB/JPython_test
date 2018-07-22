# JPentest
Jumbo Python Penetration testing framework

usage: JPentest.py [-h] [-u URL] [-d DICT] [-e ERRORKEY] [-s SAVE_PATH]


                   [-t THREAD] [-m MODULE] [-a SDOMAIN]
                   
                   

optional arguments:


  -h, --help            show this help message and exit
  
  
  -u URL, --url URL     Target URL/Appscan Id/Brute_pass url
  
  
  -d DICT, --dict DICT  Dir_Dict
  
  
  -e ERRORKEY, --errorkey ERRORKEY
  
  
                        Dir_errorkey
                        
                        
  -s SAVE_PATH, --save_path SAVE_PATH
  
  
                        Dir_save_path
                        
                        
  -t THREAD, --thread THREAD
  
  
                        Dir_thread
                        
                        
  -m MODULE, --module MODULE
  
  
                        Module(Domain/Dir/Appscan/Brute_pass)
                        
                        
  -a SDOMAIN, --sdomain SDOMAIN
  
  
                        Subdomain_brute_domain
                        
                        
                        
                        
JPentest.py -m Domain -u chinabaiker.com


JPentest.py -m Dir -u https://www.chinabaiker.com -d dir.txt -s saveok.txt -e "sorry" -t 20


JPentest.py -m Appscan -u http://appscan.io/app-report.html?id=your appscan id


JPentest.py -m Brute_pass -u http://www.chinabaiker.com/login.php


JPentest.py -m Subdomain_brute -a chinabaiker.com -t 50
