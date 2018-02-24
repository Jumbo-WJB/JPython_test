# JPentest
Jumbo Python Penetration testing framework


JPentest.py -h<br>
-h --help Show basic help message and exit<br>
-u --url  Target URL/Appscan Id/Brute_pass url<br>
-d --dict  Dir_Dict<br>
-e --errorkey  Dir_errorkey<br>
-s --save_path  Dir_save_path<br>
-t --thread  Dir_thread<br>
-m --module Module(Domain/Dir/Appscan/Brute_pass)<br>
JPentest.py -m Domain -u chinabaiker.com<br>
JPentest.py -m Dir -u https://www.chinabaiker.com -d dir.txt -s saveok.txt -e "sorry" -t 20<br>
JPentest.py -m Appscan -u http://appscan.io/app-report.html?id=your appscan id<br>
JPentest.py -m Brute_pass -u http://www.chinabaiker.com/login.php<br>
JPentest.py -m Subdomain_brute -a chinabaiker.com -t 50<br>
<br>

从三个接口获取子域名：<br>
JPentest.py -m Domain -u kuaishou.com<br>
----------virustotal----------<br>
mail.kuaishou.com<br>
forget.ssl.kuaishou.com<br>
sctrack.email.kuaishou.com<br>
m.ssl.kuaishou.com<br>
live.kuaishou.com<br>
yushu.s.kuaishou.com<br>
m.kuaishou.com<br>
pay.ssl.kuaishou.com<br>
bijie.s.kuaishou.com<br>
baoshan.s.kuaishou.com<br>
----------chinaz----------<br>
wap.gifshow.com<br>
baoshan.s.gifshow.com<br>
bijie.s.gifshow.com<br>
yichun1.s.gifshow.com<br>
beijing.s.gifshow.com<br>
yili.s.gifshow.com<br>
yiyang.s.gifshow.com<br>
yushu.s.gifshow.com<br>
chifeng.s.gifshow.com<br>
yaan.s.gifshow.com<br>
bozhou.s.gifshow.com<br>
yingtan.s.gifshow.com<br>
baisha.s.gifshow.com<br>
baoting.s.gifshow.com<br>
upload.ksapisrv.com<br>
binzhou.s.gifshow.com<br>
yongzhou.s.gifshow.com<br>
ziyang.s2.gifshow.com<br>
zhaotong.s2.gifshow.com<br>
----------i_link----------<br>
yongzhou.s.gifshow.com<br>
yushu.s.gifshow.com<br>
![](https://raw.githubusercontent.com/Jumbo-WJB/JPython_test/master/domain.jpg)

目录文件扫描：<br>
-d指定字典，-e指定404页面的关键词，-s指定保存路径，-t指定线程，如果扫描到存在的文件，会继续扫描是否有备份文件<br>
JPentest.py -m Dir -u http://music.163.com -d php.txt -e "很抱歉" -s saveok.txt -t 50<br>
很抱歉<br>
http://music.163.com/<br>
http://music.163.com/login.php<br>
http://music.163.com/logout.php<br>
http://music.163.com/search.php<br>
http://music.163.com/help.php<br>
http://music.163.com/help.php~<br>
http://music.163.com/help.php.bak<br>

APpscan扫描:<br>
会从appscan.io里获取app里存在的url、ip、邮箱<br>



突破自定义密码爆破：<br>
有的时候密码是自定义的，要么分析加密算法，还有一种就是模拟真实浏览器去登录即可


子域名爆破：<br>
十行代码进行子域名爆破

<br>
THINK
根据输入的域名进行子域名收集（api、爆破），然后把是外网ip的子域名进行端口扫描（先利用masscan进行快速扫描，然后利用nmap进行banner识别），把端口扫描的结果存入到excel中，然后如果service是http（s）就利用目录扫描扫描web敏感文件。
<br>
