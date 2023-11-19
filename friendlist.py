# Python 3.10
# Made With Graph & GraphQL Facebook

#--> Author's Info
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = 'Wa.me/6282245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'

#--> Import Default Module & Library
import os, sys, random, time, json, re, concurrent, urllib, shutil
from concurrent.futures import ThreadPoolExecutor
from random import choice as rc
from random import randrange as rr

#--> Import Extra Module & Library
def mod():
    global requests, bs4, bs
    clear()
    try: import requests
    except Exception as e: os.system('pip install requests'); import requests
    try: import bs4
    except Exception as e: os.system('pip install bs4'); import bs4
    from bs4 import BeautifulSoup as bs
    try: os.mkdir('BotFriend')
    except Exception as e: pass
    clear()

#--> Global Variable
default_ua_windows = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
random_ua_windows = lambda : 'Mozilla/5.0 (Windows NT %s.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s.%s.%s.%s Safari/537.36'%(rc(['10','11']),rr(110,201),rr(0,10),rr(0,10),rr(0,10))
headers_get  = lambda i=default_ua_windows : {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Dpr':'1','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':i}
headers_post = lambda i=default_ua_windows : {'Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Length':'1545','Content-Type':'application/x-www-form-urlencoded','Dpr':'1','Origin':'https://www.facebook.com','Referer':'https://www.facebook.com','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':"",'Sec-Ch-Ua-Full-Version-List':"",'Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':"",'Sec-Ch-Ua-Platform':"",'Sec-Ch-Ua-Platform-Version':"",'Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent':i}

#--> Color
Z = '\x1b[38;5;232m' # Hitam
M = '\x1b[38;5;196m' # Merah
H = '\x1b[38;5;46m'  # Hijau
K = '\x1b[38;5;226m' # Kuning
B = '\x1b[38;5;44m'  # Biru
U = '\x1b[38;5;54m'  # Ungu
O = '\x1b[38;5;51m'  # Biru Muda
P = '\x1b[38;5;231m' # Putih
J = '\x1b[38;5;208m' # Jingga
A = '\x1b[38;5;248m' # Abu-Abu
MR = '\033[3m'       # Miring (Italic)
BI = '\033[0m'       # Biasa

#--> Logo
def logo(n='\n\n'):
    print('%s╔╦═╗   %s╦═╗╦ ╦╦═╗╔╦╗╦ ╦ %s'%(K,H,P))
    print('%s ║ ║%s1.0%s╠╦╝╚╦╝╠╦╝ ║ ╠═╣ %sFacebook%s Friendlist Bot'%(K,P,H,O,P))
    print('%s ║ ╠═══%s╩╚═ ╩ ╩╚═ ╩ ╩ ╩ %s%sBy %sDapunta %sand %sHans Rayartha%s%s'%(K,H,P,MR,K,P,K,BI,P))
    print('%s═╩═╩═══════%s══════════%s'%(K,H,P),end=n)

#--> Clear Terminal
def clear(): os.system('clear' if 'linux' in sys.platform.lower() else 'cls')

#--> IP Geolocator
def geolocator():
    global country
    try:
        _r_ = requests.Session()
        _g_ = _r_.get('https://ip-api.org/json/').json()
        if _g_['country'] == 'ID': country = 'INDONESIA'
        else: country = 'OTHER'
    except Exception as e: country = 'OTHER'

#--> Delay
def jeda(t):
    for x in range(t+1):
        print('\r%sTunggu %s Detik                                 '%(P,str(t)),end='');sys.stdout.flush()
        t -= 1
        if t == 0: break
        else: time.sleep(1)

#--> Change Language
def language(cookie):
    try:
        xyz = requests.Session()
        req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
        pra = bs(req.content,'html.parser')
        for x in pra.find_all('form',{'method':'post'}):
            if 'Bahasa Indonesia' in str(x):
                bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),"submit"  : "Bahasa Indonesia"}
                exec = xyz.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)
    except Exception as e:pass

#--> Convert Cookie
def ConvertCookie(cok):
    try:
        sb     = re.search('sb=(.*?);',     str(cok)).group(1)
        datr   = re.search('datr=(.*?);',   str(cok)).group(1)
        c_user = re.search('c_user=(.*?);', str(cok)).group(1)
        xs     = re.search('xs=(.*?);',     str(cok)).group(1)
        fr     = re.search('fr=(.*?);',     str(cok)).group(1)
        cookie = f'sb={sb}; datr={datr}; c_user={c_user}; xs={xs}; fr={fr};'
    except Exception as e:
        cookie = cok
    return(cookie)

#--> Attribute Cookie
def AttrCookie():
    locale   = 'id_ID'
    wd       = '1707x811'
    presence = GetTime()
    attr     = f' locale={locale}; wd={wd}; presence={presence};'
    return(attr)

#--> Get Presence Cookie
def GetTime():
    temi = str(time.time()).replace('.','')[:13]
    pres = f'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A{temi}%2C%22v%22%3A1%7D'
    return(pres)

#--> Login
class login:

    #--> Initialization
    def __init__(self):
        global file_interaction, file_mutual, file_gender
        self.xyz = requests.Session()
        self.cek_cookies()
        #id_login = '100064626647103'
        file_interaction = 'Interaction_%s.txt'%(id_login)
        file_mutual = 'Mutual_%s.txt'%(id_login)
        file_gender = 'Gender_%s.txt'%(id_login)
        Menu()

    #--> Validate Cookie (Die/Live)
    def cek_cookies(self):
        try:
            global id_login, nama_login
            self.cookie     = {'cookie':open('login/cookie.json','r').read()}
            self.token_eaag = open('login/token_eaag.json','r').read()
            self.token_eaab = open('login/token_eaab.json','r').read()
            self.token_eaat = open('login/token_eaat.json','r').read()
            language(self.cookie)
            req_eaag = self.xyz.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token_eaag),cookies=self.cookie).json()
            req_eaab = self.xyz.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token_eaab),cookies=self.cookie).json()['id']
            req_eaat = self.xyz.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token_eaat),cookies=self.cookie).json()['id']
            id_login = req_eaag['id']
            nama_login = req_eaag['name']
            clear()
            logo('  ')
            if len(nama_login) <= 20: print('%sHello %s%s%s\n'%(P,H,str(nama_login),P))
            else: print('%sHello %s%s%s\n'%(P,H,str(nama_login)[:20],P))
        except Exception as e:
            self.insert_cookie()
    
    #--> Get Cookie > Generate and Save Token To File
    def insert_cookie(self):
        print('\n%sCookie Invalid!%s'%(M,P))
        time.sleep(2)
        clear()
        logo()
        if country == 'INDONESIA':
            print('%s[ %sPeringatan %s]'%(M,P,M))
            print('Memakai Tools Ini, Akun Sudah Pasti Sesi/Checkpoint!')
            print('Gunakan Akun Kuat Atau Setidaknya Memiliki ID Card')
            print('Agar Bisa Dipulihkan Jika Terjadi Sesi\n')
            print('%sJika A2F Aktif, Pergi Ke'%(P))
            print('https://business.facebook.com/business_locations')
            print('Kemudian Masukkan Kode Autentikasi')
            ciko = input('\n%sMasukkan Cookie : %s%s'%(P,H,P))
        else:
            print('%s[ %sWarning %s]'%(M,P,M))
            print('Using This Tools, Your Account Will Be Checkpoint!')
            print('Use Strong Account Or Have ID Card')
            print('So It Can Be Recovered If Checkpoint\n')
            print('%sIf 2 Factor Authenticator On, Go To'%(P))
            print('https://business.facebook.com/business_locations')
            print('To Enter Authentication Code')
            ciko = input('\n%sInput Cookie : %s%s'%(P,H,P))
        if ciko.lower() == 't': pass# print(''); Tutorial(); exit()
        else:
            cookie = ConvertCookie(ciko)
            print('')
            try:
                self.token_eaag = self.generate_token_eaag(cookie)
                print('%s[%s•%s] %sSuccess Get EAAG Token'%(H,P,H,P))
            except Exception as e:
                print('%s[%s•%s] %sFailed Get EAAG Token'%(M,P,M,P))
                time.sleep(2)
                self.insert_cookie()
            try:
                self.token_eaab = self.generate_token_eaab(cookie)
                print('%s[%s•%s] %sSuccess Get EAAB Token'%(H,P,H,P))
            except Exception as e:
                print('%s[%s•%s] %sFailed Get EAAB Token'%(M,P,M,P))
                time.sleep(2)
                self.insert_cookie()
            try:
                self.token_eaat = self.generate_token_eaat(cookie)
                print('%s[%s•%s] %sSuccess Get EAAT Token'%(H,P,H,P))
            except Exception as e:
                print('%s[%s•%s] %sFailed Get EAAT Token'%(M,P,M,P))
                time.sleep(2)
                self.insert_cookie()
            try:os.mkdir("login")
            except:pass
            open('login/cookie.json','w').write(cookie)
            open('login/token_eaag.json','w').write(self.token_eaag)
            open('login/token_eaab.json','w').write(self.token_eaab)
            open('login/token_eaat.json','w').write(self.token_eaat)
            self.cek_cookies()

    #--> Generate Token [EAAG,EAAB,EAAT]
    def generate_token_eaag(self,cok):
        url = 'https://business.facebook.com/business_locations'
        req = self.xyz.get(url,cookies={'cookie':cok})
        tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
        return(tok)
    def generate_token_eaab(self,cok):
        req1 = bs(self.xyz.get('https://www.facebook.com/adsmanager/manage/campaigns',cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
        nek1 = re.search('window\.location\.replace\("(.*?)"\)',str(req1)).group(1).replace('\\','')
        req2 = bs(self.xyz.get(nek1,cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
        tok  = re.search('accessToken="(.*?)"',str(req2)).group(1)
        return(tok)
    def generate_token_eaat(self,cok):
        re1 = self.xyz.post('https://graph.facebook.com/v16.0/device/login/',data={'access_token':'1348564698517390|007c0a9101b9e1c8ffab727666805038','scope':''}).json()
        re2 = bs(self.xyz.get('https://m.facebook.com/device',cookies={'cookie':cok},allow_redirects=True).content,'html.parser').find('form',{'method':'post'})
        po1 = bs(self.xyz.post('https://m.facebook.com'+re2['action'],data={'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(re2)).group(1),'fb_dtsg':re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(re2)).group(1),'qr':'0','user_code':re1['user_code']},cookies={'cookie':cok},allow_redirects=True).content,'html.parser').find('form',{'method':'post'})
        po2 = bs(self.xyz.post('https://m.facebook.com'+po1['action'],data={x['name']:x['value'] for x in po1.find_all('input',{'name':True,'value':True}) if x['name'] != '__CANCEL__'},cookies={'cookie':cok},allow_redirects=True).content,'html.parser')
        tok = self.xyz.get('https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=%s'%(re1['code'],'1348564698517390|007c0a9101b9e1c8ffab727666805038'),cookies={'cookie':cok}).json()['access_token']
        return(tok)

#--> Logout
def logout():
    c = input('%sYakin Ingin %sLogout %s? [%sy%s/%st%s] : '%(P,M,P,M,P,H,P)).lower()
    if c=='y':
        try: shutil.rmtree('login'); print('%sBerhasil Logout%s\n'%(P,P))
        except Exception as e: print('%sGagal Logout%s\n'%(M,P))
    else: print('%sBatal Logout%s\n'%(H,P))

#--> Control Menu
class Menu():

    def __init__(self):
        try:
            self.cookie     = open('login/cookie.json','r').read()
            self.token_eaag = open('login/token_eaag.json','r').read()
            self.token_eaab = open('login/token_eaab.json','r').read()
            self.token_eaat = open('login/token_eaat.json','r').read()
            self.file_inter = 'BotFriend/%s'%(file_interaction)
            self.file_mutua = 'BotFriend/%s'%(file_mutual)
            self.file_gende = 'BotFriend/%s'%(file_gender)
        except Exception as e: login()
        self.Main()

    def Main(self):
        if country == 'INDONESIA':
            print('%s[1] Seleksi Teman'%(P))
            print('[2] Unfriend Massal')
            print('[3] AddFriend Massal')
            print('[0] Logout')
            put = 'Pilih : '
            fls = 'Salah, Isi Yg Benar!'
        else:
            print('[1] Select Friend')
            print('[2] Mass Unfriend')
            print('[3] Mass AddFriend')
            print('[0] Logout')
            put = 'Choose : '
            fls = 'Wrong Input!'
        x = input(put)
        print('')
        if   x in ['0','00','z']: logout()
        elif x in ['1','01','a']:
            if country == 'INDONESIA':
                print('[ Seleksi Berdasarkan ]')
                print('[1] Reaksi')
                print('[2] Komentar')
                print('[3] Reaksi & Komentar')
                print('[4] Gender')
                print('[5] Mutual')
            else:
                print('[ Selection Based ]')
                print('[1] Reaction')
                print('[2] Comment')
                print('[3] Reaction & Comment')
                print('[4] Gender')
                print('[5] Mutual')
            y = input(put)
            print('')
            if   y in ['1','01','a']: self.InteractionMenu(1)
            elif y in ['2','02','b']: self.InteractionMenu(2)
            elif y in ['3','03','c']: self.InteractionMenu(3)
            elif y in ['4','04','d']: self.GenderMenu()
            elif y in ['5','05','e']: self.MutualMenu()
            else: print(fls); exit()
        elif x in ['2','02','b']:
            w_i = H if os.path.exists(self.file_inter) else M
            w_g = H if os.path.exists(self.file_gende) else M
            w_m = H if os.path.exists(self.file_mutua) else M
            if country == 'INDONESIA':
                print('[ Unfriend Berdasarkan ]')
                print('%s[%s1%s] %sSemua'    %(H,P,H,P))
                print('%s[%s2%s] %sMutual'   %(w_m,P,w_m,P))
                print('%s[%s3%s] %sGender'   %(w_g,P,w_g,P))
                print('%s[%s4%s] %sInteraksi'%(w_i,P,w_i,P))
            else:
                print('[ Unfriend Based ]')
                print('%s[%s1%s] %sAll'        %(H,P,H,P))
                print('%s[%s2%s] %sMutual'     %(w_m,P,w_m,P))
                print('%s[%s3%s] %sGender'     %(w_g,P,w_g,P))
                print('%s[%s4%s] %sInteraction'%(w_i,P,w_i,P))
            y = input(put)
            print('')
            if   y in ['1','01','a']: self.UnfriendAllFriend()
            elif y in ['2','02','b']: self.UnfriendBasedMutual()
            elif y in ['3','03','c']: self.UnfriendBasedGender()
            elif y in ['4','04','d']: self.UnfriendBasedInteraction()
            else: print(fls); exit()
        elif x in ['3','03','c']: pass
        else: print(fls); exit()
    
    def InteractionMenu(self,ch):
        loop = 0
        Inter = CheckInteraction()
        open(self.file_inter,'a+')
        open(self.file_inter,'w').write('')
        post = Inter.DumpLatestPost()
        for i in post:
            if   ch == 1: Inter.DumpReaction(loop,i)
            elif ch == 2: Inter.DumpComment(loop,i)
            elif ch == 3: Inter.DumpReaction(loop,i); Inter.DumpComment(loop,i)
            loop += 1
        o = open(self.file_inter,'r').read().splitlines()
        if len(o) == 0:
            print('Tidak Ada Interaksi' if country == 'INDONESIA' else 'No Interaction')
            print('Cek Interaksi Reaksi/Komentar Terlebih Dahulu!' if country == 'INDONESIA' else 'Check Interaction Reaction/Comment First!')
            exit('')
        else:
            print('\rMendapat %s ID Dari %s Post                    '%(str(len(o)),str(loop)) if country == 'INDONESIA' else '\rSuccess Get %s ID From %s Posts                      '%(str(len(o)),str(loop)))
    
    def GenderMenu(self):
        GD = CheckFriendlistByGraphQL(1)
        open(self.file_gende,'a+')
        open(self.file_gende,'w').write('')
        GD.Main()
    
    def MutualMenu(self):
        MT = CheckFriendlistByGraphQL(2)
        open(self.file_mutua,'a+')
        open(self.file_mutua,'w').write('')
        MT.Main()

    def UnfriendAllFriend(self):
        UF = UnFriend()
        total_fl, friendlist = GetFriendlist()
        print('Total Friendlist : %s'%(total_fl) if country=='INDONESIA' else 'Total Friendlist : %s'%(total_fl))
        print('')
        with ThreadPoolExecutor(max_workers=5) as TPE:
            for i in friendlist:
                TPE.submit(UF.Unfriend,i.split('|')[0],len(friendlist))

    def UnfriendBasedMutual(self):
        if country == 'INDONESIA': print('Format\n (<)  Kurang Dari\n (>)  Lebih Dari\n (<=) Kurang Dari Sama Dengan\n (>=) Lebih Dari Sama Dengan\n (==) Sama Dengan\n (!=) Tidak Sama Dengan\n\nContoh\n <10  (Hapus FL Yg Mutualnya Kurang Dari 10)\n ==10 (Hapus FL Yg Mutualnya Sama Dengan 10)\n !=10 (Hapus FL Yg Mutualnya Tidak Sama Dengan 10)')
        else: print('Format\n (<)  Less Than\n (>)  Greater Than\n (<=) Less Than Or Equal To\n (>=) Greater Than Or Equal To\n (==) Equal To\n (!=) Not Equal To\n\nExample\n <10  (Delete FL Whose Mutuals Are Less Than 10)\n ==10 (Delete FL Whose Mutuals Are Equal To 10)\n !=10 (Delete FL Whose Mutuals Are Not Equal To 10)')
        t = input('\nInput : ')
        print('')
        y = re.search(r'\d+',t).group(0)
        oper = t.replace(y,'')
        UF = UnFriend()
        total, removed = UF.GetSelectedMutual(oper,y)
        print('Total Friendlist : %s'%(str(len(total))))
        print('Friendlist %s %s Mutual : %s'%(oper,str(y),str(len(removed))))
        print('')
        with ThreadPoolExecutor(max_workers=5) as TPE:
            for i in removed:
                TPE.submit(UF.Unfriend,i.split('|')[0],len(removed))

    def UnfriendBasedGender(self):
        k = 'Hapus Friendlist Laki/Perempuan [l/p] : ' if country == 'INDONESIA' else 'Delete Men/Women Friendlist [m/w] : '
        f = 'Salah, Isi Yg Benar!' if country == 'INDONESIA' else 'Wrong Input!'
        p = input(k).lower()
        if p in ['1','l','m','laki','men']:
            c = 'MALE'
            g = 'Friendlist Laki-Laki' if country == 'INDONESIA' else 'Men Friendlist'
        elif p in ['2','p','w','perempuan','women']:
            c = 'FEMALE'
            g = 'Friendlist Perempuan' if country == 'INDONESIA' else  'Women Friendlist'
        else: print('\n%s'%(f)); exit()
        UF = UnFriend()
        total, removed = UF.GetSelectedGender(c)
        print('Total Friendlist : %s'%(str(len(total))))
        print('%s : %s'%(g,str(len(removed))))
        print('')
        with ThreadPoolExecutor(max_workers=5) as TPE:
            for i in removed:
                TPE.submit(UF.Unfriend,i.split('|')[0],len(removed))

    def UnfriendBasedInteraction(self):
        UF = UnFriend()
        total_fl, no_interact = UF.GetNoInteract()
        print('Total Friendlist : %s'%(total_fl) if country=='INDONESIA' else 'Total Friendlist : %s'%(total_fl))
        print('Tidak Berinteraksi : %s'%(str(len(no_interact))) if country=='INDONESIA' else 'No Interaction : %s'%(str(len(no_interact))))
        print('')
        with ThreadPoolExecutor(max_workers=5) as TPE:
            for i in no_interact:
                TPE.submit(UF.Unfriend,i.split('|')[0],len(no_interact))

#--> Get Data
def GetData(req):
    actor = re.search('"actorID":"(.*?)"',str(req)).group(1)
    haste = re.search('"haste_session":"(.*?)"',str(req)).group(1)
    conne = re.search('"connectionClass":"(.*?)"',str(req)).group(1)
    spinr = re.search('"__spin_r":(.*?),',str(req)).group(1)
    spinb = re.search('"__spin_b":"(.*?)"',str(req)).group(1)
    spint = re.search('"__spin_t":(.*?),',str(req)).group(1)
    hsi = re.search('"hsi":"(.*?)"',str(req)).group(1)
    comet = re.search('"comet_env":(.*?),',str(req)).group(1)
    dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(req)).group(1)
    jazoest = re.search('&jazoest=(.*?)"',str(req)).group(1)
    lsd = re.search('"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1)
    dta  = {'av':actor,'__user':actor,'__a':'1','__hs':haste,'dpr':'1','__ccg':conne,'__rev':spinr,'__hsi':hsi,'__comet_req':comet,'fb_dtsg':dtsg,'jazoest':jazoest,'lsd':lsd,'__spin_r':spinr,'__spin_b':spinb,'__spin_t':spint}
    return(dta)

#--> Get Friendlist With Token
def GetFriendlist():
    friendlist = []
    try:
        cookie = open('login/cookie.json','r').read()
        token_eaat = open('login/token_eaat.json','r').read()
        r = requests.Session()
        req = r.get(f'https://graph.facebook.com/me?fields=friends.fields(id,name,birthday)&access_token={token_eaat}',headers=headers_get(),cookies={'cookie':cookie}).json()
        total_fl = str(req['friends']['summary']['total_count'])
        for x in req['friends']['data']:
            try: bd = x['birthday']
            except Exception as e: bd = ''
            try:
                friendlist.append('%s|%s|%s'%(x['id'],x['name'],bd))
            except Exception as e: pass
        return(total_fl,friendlist)
    except Exception as e:
        print(e)
        print('Gagal Dump Friendlist\nAkun Spam/Checkpoint' if country=='INDONESIA' else 'Failed To Dump Friendlist\nAccount Spam/Checkpoint')
        exit()

#--> Check Friendlist With GraphQL
class CheckFriendlistByGraphQL():

    def __init__(self,obj):
        try:
            self.loop = 0
            self.obj = obj
            self.cookie     = open('login/cookie.json','r').read()
            self.token_eaag = open('login/token_eaag.json','r').read()
            self.token_eaab = open('login/token_eaab.json','r').read()
            self.token_eaat = open('login/token_eaat.json','r').read()
            self.file_gende = 'BotFriend/%s'%(file_gender)
            self.file_mutua = 'BotFriend/%s'%(file_mutual)
        except Exception as e: login()
    
    def Main(self):
        try:
            r = requests.Session()
            req = bs(r.get(f'https://www.facebook.com/me/friends',headers=headers_get(),cookies={'cookie':self.cookie},allow_redirects=True,timeout=(10,20)).content,'html.parser')
            dta = GetData(req)
            tabkey = re.search('{"tab_key":"friends_all","id":"(.*?)"}',str(req)).group(1)
            if self.obj == 1: self.ScrapGender(r,dta,None,tabkey)
            elif self.obj == 2: self.ScrapMutual(r,dta,None,tabkey)
        except Exception as e:
            print(e)
            print('Gagal Dump Akun\nAkun Spam/Checkpoint' if country=='INDONESIA' else 'Failed To Dump\nAccount Spam/Checkpoint')
            exit()

    def ScrapGender(self,r,dta,cursor,tabkey):
        try:
            var = {"count":8,"cursor":cursor,"scale":1.5,"search":None,"id":tabkey}
            dta.update({'fb_api_req_friendly_name':'ProfileCometAppCollectionListRendererPaginationQuery','variables':json.dumps(var),'server_timestamps':True,'doc_id':'6767163196701249'})
            pos = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=headers_post(),cookies={'cookie':self.cookie}).json()
            for x in pos['data']['node']['pageItems']['edges']:
                try:
                    id = x['node']['actions_renderer']['action']['client_handler']['profile_action']['restrictable_profile_owner']['id']
                    nm = x['node']['actions_renderer']['action']['client_handler']['profile_action']['restrictable_profile_owner']['name']
                    gd = x['node']['actions_renderer']['action']['client_handler']['profile_action']['restrictable_profile_owner']['gender']
                    #print('%s|%s|%s'%(id,nm,gd))
                    f = '%s|%s|%s'%(id,nm,gd)
                    if f in open(self.file_gende,'r').read().splitlines(): pass
                    else:
                        open(self.file_gende,'a+').write('%s\n'%(f))
                        self.loop += 1
                        print('\rDump %s ID By Gender'%(str(self.loop)),end=''); sys.stdout.flush()
                except Exception as e: pass
            try:
                cur = pos['data']['node']['pageItems']['page_info']['end_cursor']
                end = pos['data']['node']['pageItems']['page_info']['has_next_page']
                if end: self.ScrapGender(r,dta,cur,tabkey)
                else: pass
            except Exception as e: pass
        except Exception as e: pass
    
    def ScrapMutual(self,r,dta,cursor,tabkey):
        try:
            var = {"count":8,"cursor":cursor,"scale":1.5,"search":None,"id":tabkey}
            dta.update({'fb_api_req_friendly_name':'ProfileCometAppCollectionListRendererPaginationQuery','variables':json.dumps(var),'server_timestamps':True,'doc_id':'6767163196701249'})
            pos = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=headers_post(),cookies={'cookie':self.cookie}).json()
            for x in pos['data']['node']['pageItems']['edges']:
                try:
                    id = x['node']['actions_renderer']['action']['client_handler']['profile_action']['restrictable_profile_owner']['id']
                    nm = x['node']['actions_renderer']['action']['client_handler']['profile_action']['restrictable_profile_owner']['name']
                    try: mt = int(str(x['node']['subtitle_text']['text']).split(' ')[0])
                    except Exception as e: mt = '0'
                    # print('%s|%s|%s'%(id,nm,mt))
                    f = '%s|%s|%s'%(id,nm,str(mt))
                    if f in open(self.file_mutua,'r').read().splitlines(): pass
                    else:
                        open(self.file_mutua,'a+').write('%s\n'%(f))
                        self.loop += 1
                        print('\rDump %s ID By Mutual'%(str(self.loop)),end=''); sys.stdout.flush()
                except Exception as e: pass
            try:
                cur = pos['data']['node']['pageItems']['page_info']['end_cursor']
                end = pos['data']['node']['pageItems']['page_info']['has_next_page']
                if end: self.ScrapMutual(r,dta,cur,tabkey)
                else: pass
            except Exception as e: pass
        except Exception as e: pass

#--> Check Interaction
class CheckInteraction():

    def __init__(self):
        try:
            self.cookie     = open('login/cookie.json','r').read()
            self.token_eaag = open('login/token_eaag.json','r').read()
            self.token_eaab = open('login/token_eaab.json','r').read()
            self.token_eaat = open('login/token_eaat.json','r').read()
            self.file_inter = 'BotFriend/%s'%(file_interaction)
        except Exception as e: login()

    def DumpLatestPost(self):
        data = []
        if country == 'INDONESIA':
            print('Seleksi Berdasar Postingan')
            tkn = 'Berapa Post Terakhir : '
            tdk = 'Tidak Boleh Lebih Dari 500'
        else:
            print('Selection Based On Posts')
            tkn = 'How Many Last Posts? : '
            tdk = 'Cannot Be More Than 500'
        limit = int(input(tkn))
        print('')
        if limit >= 500: print(tdk)
        else:
            try:
                l = 0
                r = requests.Session()
                req = r.get(f'https://graph.facebook.com/me/posts?fields=id&limit=1000&access_token={self.token_eaag}',headers=headers_get(),cookies={'cookie':self.cookie}).json()
                for i in req['data']:
                    if l==limit: break
                    data.append(i['id'])
                    l += 1
                return(data)
            except Exception as e:
                print('Gagal Dump Postingan\nAkun Spam/Checkpoint' if country=='INDONESIA' else 'Failed To Dump Posts\nAccount Spam/Checkpoint')
                exit()

    def DumpReaction(self,loop,id_post):
        try:
            r = requests.Session()
            req = r.get(f'https://graph.facebook.com/{id_post}?fields=reactions.summary(true).limit(10000)&access_token={self.token_eaab}',headers=headers_get(),cookies={'cookie':self.cookie}).json()
            for x in req['reactions']['data']:
                try:
                    o = open(self.file_inter,'r').read().splitlines()
                    f = '%s|%s'%(x['id'],x['name'])
                    if f in o: pass
                    else: open(self.file_inter,'a+').write('%s\n'%(f))
                except Exception as e: pass
                if country == 'INDONESIA': print('\rSedang Dump %s ID Dari %s Post'%(str(len(o)),str(loop)),end=''); sys.stdout.flush()
                else: print('\rDumping %s ID From %s Post'%(str(len(o)),str(loop)),end=''); sys.stdout.flush()
        except Exception as e: pass

    def DumpComment(self,loop,id_post):
        try:
            r = requests.Session()
            req = r.get(f'https://graph.facebook.com/{id_post}?fields=comments.summary(true).limit(10000)&access_token={self.token_eaab}',headers=headers_get(),cookies={'cookie':self.cookie}).json()
            for x in req['comments']['data']:
                try:
                    o = open(self.file_inter,'r').read().splitlines()
                    f = '%s|%s'%(x['from']['id'],x['from']['name'])
                    if f in o: pass
                    else: open(self.file_inter,'a+').write('%s\n'%(f))
                except Exception as e: pass
                if country == 'INDONESIA': print('\rSedang Dump %s ID Dari %s Post'%(str(len(o)),str(loop)),end=''); sys.stdout.flush()
                else: print('\rDumping %s ID From %s Post'%(str(len(o)),str(loop)),end=''); sys.stdout.flush()
        except Exception as e: pass

#--> Unfriend
class UnFriend():

    def __init__(self,):
        try:
            self.cookie     = open('login/cookie.json','r').read()
            self.token_eaag = open('login/token_eaag.json','r').read()
            self.token_eaab = open('login/token_eaab.json','r').read()
            self.token_eaat = open('login/token_eaat.json','r').read()
            self.loop = 0
            self.success = 0
            self.failed = 0
        except Exception as e: login()

    def GetSelectedMutual(self,oper,y):
        removed = []
        try:
            self.file_mutua = 'BotFriend/%s'%(file_mutual)
            self.data_mutua = open(self.file_mutua,'r').read().splitlines()
            if len(self.data_mutua) == 0:
                print('Tidak Ada Data Mutual' if country == 'INDONESIA' else 'No Data Mutual')
                print('Seleksi Teman Berdasar Mutual Terlebih Dahulu!' if country == 'INDONESIA' else 'Select Friend Based On Mutual First!')
                exit('')
            else: pass
        except Exception as e:
            print('Tidak Ada Data Mutual' if country == 'INDONESIA' else 'No Data Mutual')
            print('Seleksi Teman Berdasar Mutual Terlebih Dahulu!' if country == 'INDONESIA' else 'Select Friend Based On Mutual First!')
            exit('')
        for x in self.data_mutua:
            try:
                if eval('%s%s%s'%(x.split('|')[2],oper,y)):
                    removed.append(x.split('|')[0])
            except Exception as e: pass
        return(self.data_mutua,removed)

    def GetSelectedGender(self,c):
        removed = []
        try:
            self.file_gende = 'BotFriend/%s'%(file_gender)
            self.data_gende = open(self.file_gende,'r').read().splitlines()
            if len(self.data_gende) == 0:
                print('Tidak Ada Data Gender' if country == 'INDONESIA' else 'No Data Gender')
                print('Seleksi Teman Berdasar Gender Terlebih Dahulu!' if country == 'INDONESIA' else 'Select Friend Based On Gender First!')
                exit('')
            else: pass
        except Exception as e:
            print('Tidak Ada Data Gender' if country == 'INDONESIA' else 'No Data Gender')
            print('Seleksi Teman Berdasar Gender Terlebih Dahulu!' if country == 'INDONESIA' else 'Select Friend Based On Gender First!')
            exit('')
        for x in self.data_gende:
            try:
                if x.split('|')[2] == c:
                    removed.append(x.split('|')[0])
            except Exception as e: pass
        return(self.data_gende,removed)

    def GetNoInteract(self):
        self.no_interact = []
        try:
            self.file_inter = 'BotFriend/%s'%(file_interaction)
            self.data_inter = open(self.file_inter,'r').read().splitlines()
            if len(self.data_inter) == 0:
                print('Tidak Ada Interaksi' if country == 'INDONESIA' else 'No Interaction')
                print('Seleksi Teman Berdasar Reaksi/Komentar Terlebih Dahulu!' if country == 'INDONESIA' else 'Select Friend Based On React/Comment First!')
                exit('')
            else: pass
        except Exception as e:
            print('Tidak Ada Interaksi' if country == 'INDONESIA' else 'No Interaction')
            print('Seleksi Teman Berdasar Reaksi/Komentar Terlebih Dahulu!' if country == 'INDONESIA' else 'Select Friend Based On React/Comment First!')
            exit('')
        try:
            to, fl = GetFriendlist()
            for x in fl:
                try:
                    if x in self.data_inter: pass
                    else: self.no_interact.append(x)
                except Exception as e: pass
            return(to, self.no_interact)
        except Exception as e:
            print(e)
            print('Gagal Menyortir Interaksi\nAkun Spam/Checkpoint' if country=='INDONESIA' else 'Failed To Sort Interaction\nAccount Spam/Checkpoint')
            exit()

    def Unfriend(self,id_target,total):
        r = requests.Session()
        #url = f'https://www.facebook.com/profile.php?id={id_target}'
        url = 'https://www.facebook.com'
        req = bs(r.get(url,headers=headers_get(),cookies={'cookie':self.cookie}).content,'html.parser')
        dta = GetData(req)
        dta.update({
            'fb_api_caller_class':'RelayModern',
            'fb_api_req_friendly_name':'FriendingCometUnfriendMutation',
            'variables': json.dumps({"input":{"source":"bd_profile_button","unfriended_user_id":id_target,"actor_id":dta['__user'],"client_mutation_id":"1"},"scale":1}),
            'server_timestamps':True,
            'doc_id':'8752443744796374'})
        pos = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=headers_post(),cookies={'cookie':self.cookie}).json()
        if 'unfriended_person' in str(pos):
            self.success += 1
        else:
            self.failed += 1
        self.loop += 1
        print('\rUnfriend [%s/%s] Success:%s Failed:%s'%( str(self.loop), str(total), str(self.success), str(self.failed) ), end=''); sys.stdout.flush()

def AddFriend(cok):
    target = '100000415317575'
    r = requests.Session()
    url = 'https://www.facebook.com/profile.php'
    req = bs(r.get(url,headers=headers_get(),cookies={'cookie':cok}).content,'html.parser')
    dta = GetData(req)
    var = {
        "input":{
            "attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1700060250257,939817,190055527696468,",
            "friend_requestee_ids":[target],
            "refs":[None],
            "source":"profile_button",
            "warn_ack_for_ids":[],
            "actor_id":dta['__user'],
            "client_mutation_id":"1"},
        "scale":1}
    dta.update({
        'fb_api_caller_class':'RelayModern',
        'fb_api_req_friendly_name':'FriendingCometFriendRequestSendMutation',
        'variables':json.dumps(var),
        'server_timestamps':True,
        'doc_id':'7033797416660129'})
    pos = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=headers_post(),cookies={'cookie':cok}).json()
    if 'friend_requestees' in str(pos) and 'OUTGOING_REQUEST' in str(pos):
        print('Success')
    else:
        print('Failed')

#--> Trigger
if __name__ == '__main__':
    mod()
    geolocator()
    logo()
    login()

#--> Base URL
# https://graph.facebook.com/me/posts?fields=id&limit=1000&access_token={token_eaag}
# https://graph.facebook.com/{id_post}?fields=reactions.summary(true).limit(10000)&access_token={token_eaab}
# https://graph.facebook.com/{id_post}?fields=comments.summary(true).limit(10000)&access_token={token_eaab}
# https://www.facebook.com/profile.php?id={id_target}
# https://www.facebook.com/api/graphql/


# {"tab_key":"friends_all","id":"(.*?)"}
# {"tab_key":"friends_mutual","id":"(.*?)"}
# {"tab_key":"friends_recent","id":"(.*?)"}
# {"tab_key":"friends_with_upcoming_birthdays","id":"(.*?)"}
# {"tab_key":"friends_work","id":"(.*?)"}
# {"tab_key":"friends_college","id":"(.*?)"}
# {"tab_key":"friends_high_school","id":"(.*?)"}
# {"tab_key":"friends_current_city","id":"(.*?)"}
# {"tab_key":"friends_hometown","id":"(.*?)"}
# {"tab_key":"followers","id":"(.*?)"}
# {"tab_key":"following","id":"(.*?)"}
# {"tab_key":"followers_engaged","id":"(.*?)"}