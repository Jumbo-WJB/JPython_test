# JPython_test
Jumbo Python Penetration testing framework


C:\Users\Jumbo\Desktop\渗透框架>main.py -h
-h --help Show basic help message and exit
-u --url  Target URL
-d --dict  Dict
-e --errorkey  Dir_errorkey
-s --save_path  Dir_save_path
-m --module Module(Domain/Dir)


C:\Users\Jumbo\Desktop\渗透框架>main.py -m Domain -u kuaishou.com
----------virustotal----------
mail.kuaishou.com
forget.ssl.kuaishou.com
sctrack.email.kuaishou.com
m.ssl.kuaishou.com
live.kuaishou.com
yushu.s.kuaishou.com
m.kuaishou.com
pay.ssl.kuaishou.com
www.kuaishou.com
bijie.s.kuaishou.com
baoshan.s.kuaishou.com
----------chinaz----------
wap.gifshow.com
baoshan.s.gifshow.com
bijie.s.gifshow.com
yichun1.s.gifshow.com
beijing.s.gifshow.com
yili.s.gifshow.com
yiyang.s.gifshow.com
yushu.s.gifshow.com
chifeng.s.gifshow.com
yaan.s.gifshow.com
bozhou.s.gifshow.com
yingtan.s.gifshow.com
baisha.s.gifshow.com
baoting.s.gifshow.com
www.kwai.com
upload.ksapisrv.com
binzhou.s.gifshow.com
yongzhou.s.gifshow.com
ziyang.s2.gifshow.com
zhaotong.s2.gifshow.com
----------i_link----------
http://kuaishou.com
http://www.kuaishou.com


C:\Users\Jumbo\Desktop\渗透框架>main.py -m Dir -u http://music.163.com -d php.txt -e "很抱歉" -s 111.txt
很抱歉
http://music.163.com/
http://music.163.com/login.php
http://music.163.com/logout.php
http://music.163.com/search.php
http://music.163.com/help.php
