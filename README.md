# JPentest
Jumbo Python Penetration testing framework


JPentest.py -h<br>
-h --help Show basic help message and exit<br>
-u --url  Target URL/Appscan Id<br>
-d --dict  Dir_Dict<br>
-e --errorkey  Dir_errorkey<br>
-s --save_path  Dir_save_path<br>
-t --thread  Dir_thread<br>
-m --module Module(Domain/Dir/Appscan)<br>
JPentest.py -m Domain -u chinabaiker.com<br>
JPentest.py -m Dir -u https://www.chinabaiker.com -d dir.txt -s saveok.txt -e "sorry" -t 20<br>
JPentest.py -m Appscan -u http://appscan.io/app-report.html?id=your appscan id<br>


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
www.kuaishou.com<br>
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
www.kwai.com<br>
upload.ksapisrv.com<br>
binzhou.s.gifshow.com<br>
yongzhou.s.gifshow.com<br>
ziyang.s2.gifshow.com<br>
zhaotong.s2.gifshow.com<br>
----------i_link----------<br>
http://kuaishou.com<br>
http://www.kuaishou.com<br>
![](https://raw.githubusercontent.com/Jumbo-WJB/JPython_test/master/domain.jpg)

JPentest.py -m Dir -u http://music.163.com -d php.txt -e "很抱歉" -s saveok.txt -t 50<br>
很抱歉<br>
http://music.163.com/<br>
http://music.163.com/login.php<br>
http://music.163.com/logout.php<br>
http://music.163.com/search.php<br>
http://music.163.com/help.php<br>
http://music.163.com/help.php~<br>
http://music.163.com/help.php.bak<br>
