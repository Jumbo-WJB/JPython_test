-h --help Show basic help message and exit
-u --url  Target URL/Appscan Id/Brute_pass url
-d --dict  Dir_Dict
-e --errorkey  Dir_errorkey
-s --save_path  Dir_save_path
-t --thread  Dir_thread
-m --module Module(Domain/Dir/Appscan/Brute_pass)
-a --sdomain Subdomain_brute_domain
JPentest.py -m Domain -u chinabaiker.com
JPentest.py -m Dir -u https://www.chinabaiker.com -d dir.txt -s saveok.txt -e "sorry" -t 20
JPentest.py -m Appscan -u http://appscan.io/app-report.html?id=your appscan id
JPentest.py -m Brute_pass -u http://www.chinabaiker.com/login.php
JPentest.py -m Subdomain_brute -a chinabaiker.com -t 50
