#--> Author
Author = 'Dapunta Khurayra X'
Version = 0.1
Facebook = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/ratya.anonym.id'

#--> Import Module
import os, sys, requests, bs4, re, time, datetime, random
from bs4 import BeautifulSoup as bs

#--> Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

#--> Tanggal
skrng = datetime.datetime.now()
tahun, bulan, hari = skrng.year, skrng.month, skrng.day
bulan_cek = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
tanggal = ("%s-%s-%s"%(hari,bulan_cek[bulan-1],tahun))

#--> Waktu Jalannya Program
def start():
    global Mulai_Jalan
    Mulai_Jalan = datetime.datetime.now()
def finish():
    global Akhir_Jalan, Total_Waktu
    Akhir_Jalan = datetime.datetime.now()
    Total_Waktu = Akhir_Jalan - Mulai_Jalan
    try:
        Menit = str(Total_Waktu).split(':')[1]
        Detik = str(Total_Waktu).split(':')[2].replace('.',',').split(',')[0] + ',' + str(Total_Waktu).split(':')[2].replace('.',',').split(',')[1][:1]
        print('\nProgram Selesai Dalam Waktu %s Menit %s Detik\n'%(Menit,Detik))
    except Exception as e:
        print('\nProgram Selesai Dalam Waktu 0 Detik\n')

#--> Animasi
def animasi():
    print('\rSedang Dump %s ID'%(str(len(dump))),end=''); sys.stdout.flush()

#--> Global Variable
pemisah = '|'

#--> Ubah Bahasa
def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = bs(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"}
                    url = 'https://mbasic.facebook.com' + x['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass

#--> Convert
def user_to_id(username):
    try:
        req = bs(requests.Session().get('https://mbasic.facebook.com/%s'%(username), cookies={'cookie':open('login/cookie.json','r').read()}).content, 'html.parser')
        kut = req.find('a',string='Lainnya')
        id = str(kut['href']).split('=')[1].split('&')[0]
        # id = re.search('owner_id=(.*?)"',str(kut)).group(1)
        return(id)
    except Exception as e:return(username)
def group_to_id(username):
    try:
        req = bs(requests.Session().get('https://mbasic.facebook.com/groups/%s'%(username), cookies={'cookie':open('login/cookie.json','r').read()}).content, 'html.parser')
        kut = req.find('a',string='Lihat Postingan Lainnya')
        id = str(kut['href']).split('?')[0].split('/')[2]
        return(id)
    except Exception as e:return(username)

#--> Logo
def logo():
    print('.___________                                     ')
    print('|   \______ \  __ __  _____ ______   ___________ ')
    print('|   ||    |  \|  |  \/     \\\____ \_/ __ \_  __ \\')
    print('|   ||    `   \  |  /  Y Y  \  |_> >  ___/|  | \/')
    print('|___/_______  /____/|__|_|  /   __/ \___  >__|   ')
    print('            \/  Facebook  \/|__|        \/       \n')

#--> Login
class login:
    def __init__(self):
        self.xyz = requests.Session()
        self.cek_cookies()
        main_menu()
    def cek_cookies(self):
        try:
            self.cookie     = {'cookie':open('login/cookie.json','r').read()}
            self.token_eaag = open('login/token_eaag.json','r').read()
            self.token_eaab = open('login/token_eaab.json','r').read()
            self.token_eaaj = open('login/token_eaaj.json','r').read()
            language(self.cookie)
            req1 = self.xyz.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token_eaag),cookies=self.cookie).json()['name']
            req2 = self.xyz.get('https://graph.facebook.com/me/friends?fields=summary&limit=0&access_token=%s'%(self.token_eaab),cookies=self.cookie).json()['summary']['total_count']
            req3 = self.xyz.get('https://graph.facebook.com/me?fields=friends.limit(0).fields(id,name,birthday)&access_token=%s'%(self.token_eaaj),cookies=self.cookie).json()['friends']
            clear()
            logo()
        except Exception as e:
            self.insert_cookie()
    def insert_cookie(self):
        print('\nCookie Invalid!')
        time.sleep(2)
        clear()
        logo()
        print('Apabila Akun A2F On, Pergi Ke')
        print('https://business.facebook.com/business_locations')
        print('Untuk Memasukkan Kode Autentikasi')
        ciko = input('Masukkan Cookie : ')
        self.token_eaag = self.generate_token_eaag(ciko)
        self.token_eaab = self.generate_token_eaab(ciko)
        self.token_eaaj = self.generate_token_eaaj(ciko)
        try:os.mkdir("login")
        except:pass
        open('login/cookie.json','w').write(ciko)
        open('login/token_eaag.json','w').write(self.token_eaag)
        open('login/token_eaab.json','w').write(self.token_eaab)
        open('login/token_eaaj.json','w').write(self.token_eaaj)
        self.cek_cookies()
    def generate_token_eaag(self,cok):
        url = 'https://business.facebook.com/business_locations'
        req = self.xyz.get(url,cookies={'cookie':cok})
        tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
        return(str(tok))
    def generate_token_eaab(self,cok):
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = self.xyz.get(url,cookies={'cookie':cok})
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = self.xyz.get(nek,cookies={'cookie':cok})
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        return(str(tok))
    def generate_token_eaaj(self,cok):
        self.cookie = {'cookie':cok}
        apk  = '661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e'
        data = {'access_token': apk, 'scope': ''}
        req  = self.xyz.post('https://graph.facebook.com/v16.0/device/login/',data=data).json()
        cd   = req['code']
        ucd  = req['user_code']
        url  = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=%s'%(cd,apk)
        req  = bs(self.xyz.get('https://mbasic.facebook.com/device',cookies=self.cookie).content,'html.parser')
        raq  = req.find('form',{'method':'post'})
        dat  = {'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1), 'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1), 'qr' : '0', 'user_code' : ucd}
        rel  = 'https://mbasic.facebook.com' + raq['action']
        pos  = bs(self.xyz.post(rel,data=dat,cookies=self.cookie).content,'html.parser')
        dat  = {}
        raq  = pos.find('form',{'method':'post'})
        for x in raq('input',{'value':True}):
            try:
                if x['name'] == '__CANCEL__' : pass
                else: dat.update({x['name']:x['value']})
            except Exception as e: pass
        rel = 'https://mbasic.facebook.com' + raq['action']
        pos = bs(self.xyz.post(rel,data=dat,cookies=self.cookie).content,'html.parser')
        req = self.xyz.get(url,cookies=self.cookie).json()
        tok = req['access_token']
        return(str(tok))

#--> Menu Utama
class main_menu:
    def __init__(self):
        self.xyz        = requests.Session()
        self.cookie     = {'cookie':open('login/cookie.json','r').read()}
        self.token_eaag = open('login/token_eaag.json','r').read()
        self.token_eaab = open('login/token_eaab.json','r').read()
        self.dasbor()
        self.menu()
        self.pilih_menu()
    def dasbor(self):
        q = ' '*6
        z = {}
        try:
            req = self.xyz.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token_eaag),cookies=self.cookie).json()
            if len(req['name']) > 18: z.update({'Nama':str(req['name'])[:15]+'...'})
            else: z.update({'Nama':str(req['name'])[:15]})
            z.update({'ID':str(req['id'])})
        except Exception as e: login()
        try:
            bln    = {'01':'Januari', '02':'Februari', '03':'Maret', '04':'April', '05':'Mei', '06':'Juni', '07':'Juli', '08':'Agustus', '09':'September', '10':'Oktober', '11':'November', '12':'Desember'}
            t,m,h  = [x['created_time'].split('T')[0] for x in self.xyz.get('https://graph.facebook.com/me/albums?fields=id,name,created_time&limit=1000&access_token=%s'%(self.token_eaag),cookies=self.cookie).json()['data'] if x['name']=='Foto Profil'][0].split('-')
            z.update({'Buat':'%s %s %s'%(h,bln[m],t)})
        except Exception as e: pass
        try:
            fren = str(self.xyz.get('https://graph.facebook.com/me/friends?fields=summary&limit=0&access_token=%s'%(self.token_eaab),cookies=self.cookie).json()['summary']['total_count'])
            z.update({'Teman':fren})
        except Exception as e: pass
        try:
            fols = str(self.xyz.get('https://graph.facebook.com/me/subscribers?limit=0&access_token=%s'%(self.token_eaag),cookies=self.cookie).json()['summary']['total_count'])
            z.update({'Folls':fols})
        except Exception as e: pass
        print('%s╭────────────[ Welcome ]───────────╮'%(q))
        for x,y in zip(z.keys(),z.values()):
            print('%s│    %s%s: %s%s│'%(q,x,' '*(6-len(x)),y,' '*(22-len(y))))
        print('%s╰──────────────────────────────────╯'%(q))
    def menu(self):
        c = ' '*0
        print('\n%s  [ Account ]        [ Group ]        [ Post ]\n'%(c))
        print('%s[01] Friendlist    [15] Members     [19] Comment'%(c))
        print('%s[02] Followers     [16] Timeline    [20] React'%(c))
        print('%s[03] Comment       [17] Comment'%(c))
        print('%s[04] React         [18] React'%(c))
        print('%s[05] Message'%(c))
        print('%s[06] Name'%(c))
        print('%s[07] Timeline'%(c))
        print('%s[08] Hashtag'%(c))
        print('%s[09] Email'%(c))
        print('%s[10] Phone'%(c))
        print('%s[11] Username'%(c))
        print('%s[12] ID Random'%(c))
        print('%s[13] Suggestion'%(c))
        print('%s[14] FL Dari FL'%(c))
    def pilih_menu(self):
        xo = input('\nPilih : ')
        print('')
        if xo in   ['1', '01' ,'a']: dump_friendlist()
        elif xo in ['2', '02' ,'b']: dump_followers()
        elif xo in ['3', '03' ,'c']: dump_react_comment('A_K')
        elif xo in ['4', '04' ,'d']: dump_react_comment('A_R')
        elif xo in ['5', '05' ,'e']: dump_owner_account('PS')
        elif xo in ['6', '06' ,'f']: dump_owner_account('NM')
        elif xo in ['7', '07' ,'g']: dump_owner_account('TL')
        elif xo in ['8', '08' ,'h']: dump_owner_account('HS')
        elif xo in ['9', '009','i']: dump_random('EM')
        elif xo in ['10','010','j']: dump_random('PO')
        elif xo in ['11','011','k']: dump_random('US')
        elif xo in ['12','012','l']: dump_random('ID')
        elif xo in ['13','013','m']: dump_owner_account('SU')
        elif xo in ['14','014','n']: dump_fl_fl()
        elif xo in ['15','015','o']: dump_react_comment('MB')
        elif xo in ['16','016','p']: dump_react_comment('TL')
        elif xo in ['17','017','q']: dump_react_comment('G_K')
        elif xo in ['18','018','r']: dump_react_comment('G_R')
        elif xo in ['19','019','s']: dump_react_comment('P_K')
        elif xo in ['20','020','t']: dump_react_comment('P_R')
        simpan_file()

#--> Dump Friendlist
class dump_friendlist:
    def __init__(self):
        global dump
        dump = self.dump = []
        self.fail        = []
        self.pisah       = pemisah
        self.xyz         = requests.Session()
        self.cookie      = {'cookie':open('login/cookie.json','r').read()}
        self.token_eaag  = open('login/token_eaag.json','r').read()
        self.token_eaab  = open('login/token_eaab.json','r').read()
        self.token_eaaj  = open('login/token_eaaj.json','r').read()
        self.main()
    def main(self):
        print('Banyak ID, Pisahkan Dgn (,)')
        id = input('Masukkan ID : ').split(',')
        print('')
        for f in id:
            if f == 'me': io = f
            elif (re.findall("[a-zA-Z]",str(f))) : io = user_to_id(f)
            else : io = f
            self.cek(io)
        print('')
        for d in self.fail:
            try: id.remove(d)
            except Exception as e: continue
        for s in id:
            if s == 'me': io = s
            elif (re.findall("[a-zA-Z]",str(s))) : io = user_to_id(s)
            else : io = s
            self.requ(io)
        if len(self.dump) == 0: print('\rDump ID Gagal')
        else: print('\rBerhasil Mendapat %s ID'%(str(len(self.dump))))
    def cek(self,id):
        try: 
            nama  = str(self.xyz.get('https://graph.facebook.com/%s?fields=name&access_token=%s'%(id,self.token_eaag),cookies=self.cookie).json()['name'])
            teman = str(self.xyz.get('https://graph.facebook.com/%s?fields=friends.limit(0).fields(id,name,birthday)&access_token=%s'%(id,self.token_eaaj),cookies=self.cookie).json()['friends']['summary']['total_count'])
            print(' • %s --> %s Teman'%(nama,teman))
        except Exception as e:
            print(' • %s --> Kesalahan/Private'%(id))
            self.fail.append(id)
    def requ(self,id):
        url = 'https://graph.facebook.com/%s?fields=friends.limit(5000).fields(id,name,birthday)&access_token=%s'%(id,self.token_eaaj)
        try:
            req = self.xyz.get(url,cookies=self.cookie).json()
            for y in req['friends']['data']:
                try:
                    id, nama = y['id'], y['name']
                    format = '%s%s%s'%(id,self.pisah,nama)
                    self.dump.append(format)
                    animasi()
                except Exception as e: pass
        except Exception as e: pass

#--> Dump Followers
class dump_followers:
    def __init__(self):
        global dump
        dump = self.dump = []
        self.fail        = []
        self.pisah       = pemisah
        self.xyz         = requests.Session()
        self.cookie      = {'cookie':open('login/cookie.json','r').read()}
        self.token_eaag  = open('login/token_eaag.json','r').read()
        self.token_eaab  = open('login/token_eaab.json','r').read()
        self.main()
    def main(self):
        print('Banyak ID, Pisahkan Dgn (,)')
        id = input('Masukkan ID : ').split(',')
        print('')
        for f in id:
            if f == 'me': io = f
            elif (re.findall("[a-zA-Z]",str(f))) : io = user_to_id(f)
            else : io = f
            self.cek(io)
        print('')
        for d in self.fail:
            try: id.remove(d)
            except Exception as e: continue
        for s in id:
            if s == 'me': io = s
            elif (re.findall("[a-zA-Z]",str(s))) : io = user_to_id(s)
            else : io = s
            self.requ('https://graph.facebook.com/%s/subscribers?limit=1000&access_token=%s'%(io,self.token_eaag))
        if len(self.dump) == 0: print('\rDump ID Gagal')
        else: print('\rBerhasil Mendapat %s ID'%(str(len(self.dump))))
    def cek(self,id):
        try: 
            nama  = str(self.xyz.get('https://graph.facebook.com/%s?fields=name&access_token=%s'%(id,self.token_eaag),cookies=self.cookie).json()['name'])
            folls = str(self.xyz.get('https://graph.facebook.com/%s/subscribers?limit=0&access_token=%s'%(id,self.token_eaag),cookies=self.cookie).json()['summary']['total_count'])
            print(' • %s --> %s Folls'%(nama,folls))
        except Exception as e:
            print(' • %s --> Kesalahan/Private'%(id))
            self.fail.append(id)
    def requ(self,url):
        try:
            req = self.xyz.get(url,cookies=self.cookie).json()
            for y in req['data']:
                try:
                    id, nama = y['id'], y['name']
                    format = '%s%s%s'%(id,self.pisah,nama)
                    self.dump.append(format)
                    animasi()
                except Exception as e: pass
            self.requ(req['paging']['next'])
        except Exception as e: pass

#--> Dump Friendlist Dari Friendlist
class dump_fl_fl:
    def __init__(self):
        global dump
        dump = self.dump = []
        self.fail        = []
        self.pisah       = pemisah
        self.xyz         = requests.Session()
        self.cookie      = {'cookie':open('login/cookie.json','r').read()}
        self.token_eaag  = open('login/token_eaag.json','r').read()
        self.token_eaab  = open('login/token_eaab.json','r').read()
        self.main()
    def main(self):
        print('Banyak ID, Pisahkan Dgn (,)')
        id = input('Masukkan ID : ').split(',')
        print('')
        for f in id:
            if f == 'me': io = f
            elif (re.findall("[a-zA-Z]",str(f))) : io = user_to_id(f)
            else : io = f
            self.cek(io)
        print('')
        for d in self.fail:
            try: id.remove(d)
            except Exception as e: continue
        self.t1 = input('Pilih ID Tua/Muda [t/m] : ').lower()
        self.t2 = input('Berapa ID Per Masing" Akun : ')
        print('')
        try:
            for s in id:
                if s == 'me': io = s
                elif (re.findall("[a-zA-Z]",str(s))) : io = user_to_id(s)
                else : io = s
                lid = self.requ(io,'1')
            try:
                for h in lid:
                    self.requ(h.split(self.pisah)[0],'2')
            except Exception as e:
                pass
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\rDump ID Gagal')
        else: print('\rBerhasil Mendapat %s ID'%(str(len(self.dump))))
    def cek(self,id):
        try: 
            nama  = str(self.xyz.get('https://graph.facebook.com/%s?fields=name&access_token=%s'%(id,self.token_eaag),cookies=self.cookie).json()['name'])
            teman = str(self.xyz.get('https://graph.facebook.com/%s/friends?fields=summary&limit=0&access_token=%s'%(id,self.token_eaab),cookies=self.cookie).json()['summary']['total_count'])
            print(' • %s --> %s Teman'%(nama,teman))
        except Exception as e:
            print(' • %s --> Kesalahan/Private'%(id))
            self.fail.append(id)
    def requ(self,id,tp):
        url = 'https://graph.facebook.com/%s/friends?fields=id,name&limit=5000&access_token=%s'%(id,self.token_eaab)
        try:
            req = self.xyz.get(url,cookies=self.cookie).json()
            pen = [ '%s%s%s'%(y['id'],self.pisah,y['name']) for y in req['data']]
            sm_ = []
            sm  = []
            if self.t1 in ['1','01','t','tua']:
                for z in pen:
                    sm.append(z)
                    if len(sm) == int(self.t2): break
            else:
                for z in pen:
                    sm_.insert(0,z)
                for z_ in sm_:
                    sm.append(z_)
                    if len(sm) == int(self.t2): break
                if tp == '1':
                    return(sm)
                else:
                    for h in sm:
                        if h in self.dump:pass
                        else:self.dump.append(h)
                        animasi()
        except Exception as e: pass

#--> Dump React, Comment, Member, Photo, Timeline
class dump_react_comment:

    #--> Penampungan Awal
    def __init__(self,tp):
        global dump
        dump = self.dump = []
        self.fail        = []
        self.pisah       = pemisah
        self.limit       = '100'
        self.xyz         = requests.Session()
        self.cookie      = {'cookie':open('login/cookie.json','r').read()}
        self.token_eaag  = open('login/token_eaag.json','r').read()
        self.token_eaab  = open('login/token_eaab.json','r').read()
        if tp   == 'A_K': self.modul = 'K'; self.main_A() #--> Dump Comment Account
        elif tp == 'A_R': self.modul = 'R'; self.main_A() #--> Dump React Account
        elif tp == 'G_K': self.modul = 'K'; self.main_G() #--> Dump Comment Group
        elif tp == 'G_R': self.modul = 'R'; self.main_G() #--> Dump React Group
        elif tp == 'P_K': self.modul = 'K'; self.main_P() #--> Dump Comment Post
        elif tp == 'P_R': self.modul = 'R'; self.main_P() #--> Dump React Post
        elif tp == 'TL' : self.modul = 'T'; self.main_tl_mb() #--> Dump Timeline
        elif tp == 'MB' : self.modul = 'M'; self.main_tl_mb() #--> Dump Member
    
    #--> Dump Post Account
    def main_A(self):
        print('Banyak ID, Pisahkan Dgn (,)')
        id = input('Masukkan ID : ').split(',')
        print('')
        for f in id:
            if f == 'me': io = f
            elif (re.findall("[a-zA-Z]",str(f))) : io = user_to_id(f)
            else : io = f
            self.cek_A(io)
        print('')
        print('Tekan ctrl+c Untuk Berhenti')
        for d in self.fail:
            try: id.remove(d)
            except Exception as e: continue
        try:
            for s in id:
                if s == 'me': io = s
                elif (re.findall("[a-zA-Z]",str(s))) : io = user_to_id(s)
                else : io = s
                self.requ1_A(io)
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\rDump ID Gagal')
        else: print('\rBerhasil Mendapat %s ID'%(str(len(self.dump))))
    def cek_A(self,id):
        try: 
            nama  = str(self.xyz.get('https://graph.facebook.com/%s?fields=name&access_token=%s'%(id,self.token_eaag),cookies=self.cookie).json()['name'])
            lisz  = [x['id'] for x in self.xyz.get('https://graph.facebook.com/%s/posts?fields=id&limit=%s&access_token=%s'%(id,self.limit,self.token_eaag),cookies=self.cookie).json()['data']]
            post  = str(len(lisz))
            print(' • %s --> %s Post'%(nama,post))
        except Exception as e:
            print(' • %s --> Kesalahan/Private'%(id))
            self.fail.append(id)
    def requ1_A(self,id):
        lisz  = [x['id'] for x in self.xyz.get('https://graph.facebook.com/%s/posts?fields=id&limit=%s&access_token=%s'%(id,self.limit,self.token_eaag),cookies=self.cookie).json()['data']]
        try:
            for pid in lisz:
                if self.modul == 'K':
                    url = 'https://mbasic.facebook.com/' + pid
                    self.main_requ_comment(url)
                else:
                    self.main_requ_react(pid)
        except Exception as e: pass
    
    #--> Dump Post Group
    def main_G(self):
        print('Banyak ID, Pisahkan Dgn (,)')
        id = input('Masukkan ID Grup : ').split(',')
        print('')
        for f in id:
            if (re.findall("[a-zA-Z]",str(f))) : io = group_to_id(f)
            else : io = f
            self.cek_G(io)
        print('')
        print('Tekan ctrl+c Untuk Berhenti')
        for d in self.fail:
            try: id.remove(d)
            except Exception as e: continue
        try:
            for s in id:
                if (re.findall("[a-zA-Z]",str(s))) : io = group_to_id(s)
                else : io = s
                self.requ1_G(io)
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\rDump ID Gagal')
        else: print('\rBerhasil Mendapat %s ID'%(str(len(self.dump))))
    def cek_G(self,id):
        try:
            req = self.xyz.get('https://graph.facebook.com/%s?access_token=%s'%(id,self.token_eaag),cookies=self.cookie).json()
            if req['privacy'] == 'OPEN':
                try:
                    raq = bs(self.xyz.get('https://mbasic.facebook.com/groups/%s?view=info'%(id),cookies=self.cookie).content,'html.parser')
                    agt = str([c.text for c in raq.find_all('tr') if 'Anggota' in str(c)][0].replace('Anggota',''))
                    pos = [x['id'] for x in self.xyz.get('https://graph.facebook.com/%s/feed?fields=id&limit=%s&access_token=%s'%(id,self.limit,self.token_eaag),cookies=self.cookie).json()['data']]
                except Exception as e: pass
                print(' • %s --> %s Members & %s Posts'%(str(req['name']),agt,str(len(pos))))
            else:
                print(' • %s --> Kesalahan/Private'%(id))
                self.fail.append(id)
        except Exception as e:
            print(' • %s --> Kesalahan/Private'%(id))
            self.fail.append(id)
    def requ1_G(self,id):
        lisz  = [x['id'] for x in self.xyz.get('https://graph.facebook.com/%s/feed?fields=id&limit=%s&access_token=%s'%(id,self.limit,self.token_eaag),cookies=self.cookie).json()['data']]
        try:
            for pid in lisz:
                if self.modul == 'K':
                    url = 'https://mbasic.facebook.com/' + pid
                    self.main_requ_comment(url)
                else:
                    self.main_requ_react(pid)
        except Exception as e: pass
    
    #--> Dump Post
    def main_P(self):
        print('Banyak ID, Pisahkan Dgn (,)')
        id = input('Masukkan ID Post : ').split(',')
        print('')
        print('Tekan ctrl+c Untuk Berhenti')
        try:
            for pid in id:
                if self.modul == 'K':
                    url = 'https://mbasic.facebook.com/' + pid
                    self.main_requ_comment(url)
                else:
                    self.main_requ_react(pid)
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\rDump ID Gagal')
        else: print('\rBerhasil Mendapat %s ID'%(str(len(self.dump))))

    #--> Main Dump Comment
    def main_requ_comment(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for x in req.find_all('h3'):
                try:
                    v    = x.find('a',href=True)
                    nama = v.text
                    if 'profile.php' in v['href']: id = re.search('profile.php\?id\=(.*?)\&amp',str(v)).group(1)
                    else: id = user_to_id(v['href'].split('?')[0].replace('/',''))
                    format = '%s%s%s'%(id,self.pisah,nama)
                    if format in self.dump:pass
                    else:self.dump.append(format)
                    animasi()
                except Exception as e: continue
            nek = 'https://mbasic.facebook.com' + req.find('a',string=' Lihat komentar sebelumnya…')['href']
            self.main_requ_comment(nek)
        except Exception as e: pass

    #--> Main Dump React
    def main_requ_react(self,id):
        try:
            url = 'https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier=' + id.split('_')[1]
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for y in req.find_all('a',href=True):
                try:
                    if '/ufi/reaction/profile/browser/fetch/?ft_ent_identifier' in y['href']:
                        if 'Semua' in y.text: pass
                        elif 'reaction_type=0' in str(y): pass
                        else:
                            lk1 = 'https://mbasic.facebook.com' + y['href'].replace('limit=10','limit=50')
                            self.scrap_react(lk1)
                except Exception as e: continue
        except Exception as e: pass
    def scrap_react(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for z in req.find_all('h3'):
                try:
                    v    = z.find('a',href=True)
                    nama = v.text
                    if 'profile.php' in v['href']: id = re.search('profile.php\?id\=(.*?)\&amp',str(v)).group(1)
                    else: id = v['href'].split('?')[0].replace('/','')
                    format = '%s%s%s'%(id,self.pisah,nama)
                    if format in self.dump:pass
                    else:self.dump.append(format)
                    animasi()
                except Exception as e: continue
            nek = 'https://mbasic.facebook.com' + req.find('a',string='Lihat Selengkapnya')['href'].replace('limit=10','limit=50')
            self.scrap_react(nek)
        except Exception as e: pass

    #--> Dump Timeline & Member Group
    def main_tl_mb(self):
        print('Banyak ID, Pisahkan Dgn (,)')
        id = input('Masukkan ID Grup : ').split(',')
        print('')
        for f in id:
            if (re.findall("[a-zA-Z]",str(f))) : io = group_to_id(f)
            else : io = f
            self.cek_G(io)
        print('')
        print('Tekan ctrl+c Untuk Berhenti')
        for d in self.fail:
            try: id.remove(d)
            except Exception as e: continue
        try:
            for s in id:
                if (re.findall("[a-zA-Z]",str(s))) : io = group_to_id(s)
                else : io = s
                if self.modul == 'T':
                    self.scrape_tl('https://mbasic.facebook.com/groups/'+io)
                elif self.modul == 'M':
                    self.scrape_mb('https://mbasic.facebook.com/browse/group/members/?id=%s&start=0'%(io))
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\rDump ID Gagal')
        else: print('\rBerhasil Mendapat %s ID'%(str(len(self.dump))))
    
    #--> Dump Timeline Group
    def scrape_tl(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for z in req.find_all('h3'):
                for po in z.find_all('a',href=True):
                    try:
                        if 'mbasic.facebook.com' in po['href']:pass
                        elif 'story.php' in po['href']:pass
                        elif 'Halaman' in po.text:pass
                        elif 'profile.php' in po['href']:
                            id = re.findall('profile\.php\?id=(.*?)&',str(po['href']))[0]
                            nm = po.text
                        else:
                            id = user_to_id(re.findall('\/(.*?)\/\?refid',str(po['href']))[0])
                            nm = po.text
                        format = '%s%s%s'%(id,self.pisah,nm)
                        if format in self.dump:pass
                        else:self.dump.append(format)
                        animasi()
                    except Exception as e: continue
            nek = 'https://mbasic.facebook.com' + req.find('a',string='Lihat Postingan Lainnya')['href']
            self.scrape_tl(nek)
        except Exception as e: pass
    
    #--> Dump Member Group
    def scrape_mb(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for z in req.find_all('h3'):
                for po in z.find_all('a',href=True):
                    try:
                        if 'a/friends/add' in po['href']:pass
                        elif 'profile.php' in po['href']:
                            id = re.findall('profile\.php\?id=(.*?)&',str(po['href']))[0]
                            nm = po.text
                        else:
                            id = user_to_id(re.findall('\/(.*?)\/\?refid',str(po['href']))[0])
                            nm = po.text
                        format = '%s%s%s'%(id,self.pisah,nm)
                        if format in self.dump:pass
                        else:self.dump.append(format)
                        animasi()
                    except Exception as e: continue
            nek = 'https://mbasic.facebook.com' + req.find('a',string='Lihat Selengkapnya')['href']
            self.scrape_mb(nek)
        except Exception as e: pass

#--> Dump Message, Name, Timeline, Hashtag, Suggestion
class dump_owner_account:
    
    #--> Penampungan Awal
    def __init__(self,tp):
        global dump
        dump = self.dump = []
        self.fail        = []
        self.pisah       = pemisah
        self.xyz         = requests.Session()
        self.cookie      = {'cookie':open('login/cookie.json','r').read()}
        self.token_eaag  = open('login/token_eaag.json','r').read()
        self.token_eaab  = open('login/token_eaab.json','r').read()
        if tp   == 'PS': self.main_message()    #--> Dump ID From Message
        elif tp == 'NM': self.main_name()       #--> Dump ID From Name
        elif tp == 'TL': self.main_timeline()   #--> Dump ID From Timeline
        elif tp == 'HS': self.main_hashtag()    #--> Dump ID From Hashtag
        elif tp == 'SU': self.main_suggestion() #--> Dump ID From Suggestion
    
    #--> Dump ID From Message
    def main_message(self):
        print('Tekan ctrl+c Untuk Berhenti')
        try: self.scrape_message('https://mbasic.facebook.com/messages')
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\rDump ID Gagal')
        else: print('\rBerhasil Mendapat %s ID'%(str(len(self.dump))))
    def scrape_message(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for p in req.find_all('a',href=True):
                if '/messages/read/?tid=cid.c' in p['href']:
                    try:
                        if p.text == 'Pengguna Facebook': continue
                        else:
                            id   = str(re.search('%3A(.*?)&',p['href']).group(1))
                            nama = p.text
                        format = '%s%s%s'%(id,self.pisah,nama)
                        if format in self.dump: pass
                        else: self.dump.append(format)
                        animasi()
                    except Exception as e: continue
            nek = 'https://mbasic.facebook.com' + req.find('a',string='Lihat Pesan Sebelumnya')['href']
            self.scrape_message(nek)
        except Exception as e: pass

    #--> Dump ID From Name
    def main_name(self):
        lid = []
        print('Banyak Nama, Pisahkan Dgn (,)')
        id = input('Masukkan Nama : ').lower().split(',')
        common = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
        for x in id:
            for y in common:
                lid.append('%s %s'%(x,y))
                lid.append('%s %s'%(y,x))
        print('')
        print('Tekan ctrl+c Untuk Berhenti')
        try:
            for z in lid:
                url = 'https://mbasic.facebook.com/search/people/?q=' + z
                self.scrape_name(url)
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\rDump ID Gagal')
        else: print('\rBerhasil Mendapat %s ID'%(str(len(self.dump))))
    def scrape_name(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for p in req.find_all('a',href=True):
                try:
                    if "<img alt=" in str(p):
                        if "home.php" in str(p["href"]): continue
                        elif 'profile.php' in str(p["href"]):
                            id   = re.search('"/profile\.php\?id=(.*?)&"',str(p)).group(1)
                            nama = p.find("img")['alt'].replace(", profile picture","")
                        elif 'refid' in str(p["href"]):
                            id   = user_to_id(re.search("/(.*?)\?",str(p)).group(1))
                            nama = p.find("img")['alt'].replace(", profile picture","")
                        format = '%s%s%s'%(id,self.pisah,nama)
                        if format in self.dump: pass
                        else: self.dump.append(format)
                    animasi()
                except Exception as e: continue
            nek = req.find('a',string='Lihat Hasil Selanjutnya')['href']
            self.scrape_name(nek)
        except Exception as e: pass
    
    #--> Dump ID From Timeline
    def main_timeline(self):
        print('Tekan ctrl+c Untuk Berhenti')
        try: self.scrape_timeline('https://mbasic.facebook.com/')
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\rDump ID Gagal')
        else: print('\rBerhasil Mendapat %s ID'%(str(len(self.dump))))
    def scrape_timeline(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for q in req.find_all('h3'):
                for p in q.find_all('a',href=True):
                    try:
                        if 'mbasic.facebook.com' in p['href']:pass
                        elif 'sub_view' in p['href']:pass
                        elif '/?' in p['href']:pass
                        elif 'profile.php' in str(p["href"]):
                            id   = str(re.search('\?id=(.*?)&',p['href']).group(1))
                            nama = str(re.search('>(.*?)<\/a>',str(p)).group(1))
                        else:
                            id   = user_to_id(str(re.search('\/(.*?)\?',p['href']).group(1)))
                            nama = str(re.search('>(.*?)<\/a>',str(p)).group(1))
                        format = '%s%s%s'%(id,self.pisah,nama)
                        if format in self.dump: pass
                        else: self.dump.append(format)
                        animasi()
                    except Exception as e: continue
            nek = 'https://mbasic.facebook.com' + req.find('a',string='Lihat Berita Lain')['href']
            self.scrape_timeline(nek)
        except Exception as e: pass

    #--> Dump ID From Hashtag
    def main_hashtag(self):
        print('Banyak Hashtag, Pisahkan Dgn (,)')
        id = input('Masukkan Hashtag : ').replace(' ','').split(',')
        print('')
        print('Tekan ctrl+c Untuk Berhenti')
        try:
            for z in id:
                url = 'https://mbasic.facebook.com/hashtag/' + z
                self.scrape_hashtag(url)
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\rDump ID Gagal')
        else: print('\rBerhasil Mendapat %s ID'%(str(len(self.dump))))
    def scrape_hashtag(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for q in req.find_all('h3'):
                for p in q.find_all('a',href=True):
                    try:
                        if 'mbasic.facebook.com' in p['href']:pass
                        elif 'sub_view' in p['href']:pass
                        elif '/?' in p['href']:pass
                        elif 'profile.php' in str(p["href"]):
                            id   = str(re.search('\?id=(.*?)&',p['href']).group(1))
                            nama = str(re.search('>(.*?)<\/a>',str(p)).group(1))
                        else:
                            id   = user_to_id(str(re.search('\/(.*?)\?',p['href']).group(1)))
                            nama = str(re.search('>(.*?)<\/a>',str(p)).group(1))
                        format = '%s%s%s'%(id,self.pisah,nama)
                        if format in self.dump: pass
                        else: self.dump.append(format)
                        animasi()
                    except Exception as e: continue
            nek = req.find('a',string='Lihat Hasil Selanjutnya')['href']
            self.scrape_hashtag(nek)
        except Exception as e: pass
    
    #--> Dump ID From Suggestion
    def main_suggestion(self):
        print('Tekan ctrl+c Untuk Berhenti')
        try: self.scrape_suggestion('https://mbasic.facebook.com/friends/center/suggestions')
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\rDump ID Gagal')
        else: print('\rBerhasil Mendapat %s ID'%(str(len(self.dump))))
    def scrape_suggestion(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for p in req.find_all('a',href=True):
                try:
                    if "friends/hovercard/mbasic" in str(p['href']):
                        id   = p['href'].split('&')[0].split('=')[1]
                        nama = p.text
                    format = '%s%s%s'%(id,self.pisah,nama)
                    if format in self.dump: pass
                    else: self.dump.append(format)
                    animasi()
                except Exception as e: pass
            nek = 'https://mbasic.facebook.com' + req.find('a',string='Lihat selengkapnya')['href']
            self.scrape_suggestion(nek)
        except Exception as e: pass

#--> Dump Random Email, Phone, Username, ID
class dump_random:
    
    #--> Penampungan Awal
    def __init__(self,tp):
        global dump
        dump = self.dump = []
        self.fail        = []
        self.pisah       = pemisah
        self.xyz         = requests.Session()
        self.cookie      = {'cookie':open('login/cookie.json','r').read()}
        self.token_eaag  = open('login/token_eaag.json','r').read()
        self.token_eaab  = open('login/token_eaab.json','r').read()
        if tp   == 'EM': self.main_email()    #--> Random Email
        elif tp == 'PO': self.main_phone()    #--> Random Phone
        elif tp == 'US': self.main_username() #--> Random Username
        elif tp == 'ID': self.main_id()       #--> Random ID
    
    #--> Auto Generate Random Email
    def main_email(self):
        belum_bisa()

    #--> Auto Generate Random Phone
    def main_phone(self):
        belum_bisa()

    #--> Auto Generate Random Username
    def main_username(self):
        belum_bisa()

    #--> Auto Generate Random ID
    def main_id(self):
        aw = input('Masukkan ID Awal Sbg Acuan : ')
        print('')
        print('Tekan ctrl+c Untuk Berhenti')
        try:
            self.tamp(int(aw))
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\rDump ID Gagal')
        else: print('\rBerhasil Mendapat %s ID'%(str(len(self.dump))))
    def tamp(self,a):
        t = a+10000
        r = random.sample(range(a,t), t-a)
        r.append(t)
        r.sort()
        for n in r:
            self.cek_id(n)
    def cek_id(self,id):
        url = 'https://mbasic.facebook.com/login/device-based/password/?uid=%s&flow=login_no_pin&refsrc=deprecated&_rdr'%(id)
        try:
            req = bs(self.xyz.get(url).content,'html.parser')
            if "Sorry, this content isn't available right now" in req: pass
            elif 'Temporarily Blocked' in str(req):
                print('\rAkunmu Kena Spam',end=''); sys.stdout.flush()
            else:
                nama = req.find_all('img')[1]['alt'].split(',')[0]
                if nama == 'Foto Profil Pengguna': pass
                elif nama == '': pass
                else:
                    format = '%s%s%s'%(id,self.pisah,nama)
                    self.dump.append(format)
                    animasi()
        except Exception as e: pass

#--> Simpan File Ke Perangkat
class simpan_file:
    def __init__(self):
        self.main()
    def main(self):
        print('')
        ty = input('Simpan File? [y/t] : ').lower()
        if ty in ['1','01','y','ya','iya']: self.main2()
        else: pass
    def main2(self):
        try:os.mkdir('dump')
        except:pass
        try:
            nm  = input('Tulis Nama File : ').replace(' ','_') + '.txt'
            lk  = input('Tulis Lokasi Penyimpanan : ')
            lok = '%s\%s'%(lk,nm)
            open(lok,'a+')
            for d in dump:
                try: open(lok,'a+').write(d+'\n')
                except Exception as e: pass
            print('\nFile Dump Tersimpan Di %s'%(lok))
        except Exception as e:
            print('\nGagal Menemukan Lokasi File')
            lok = 'dump/%s.txt'%(tanggal)
            open(lok,'a+')
            for d in dump:
                try: open(lok,'a+').write(d+'\n')
                except Exception as e: pass
            print('File Dump Tersimpan Di %s'%(lok))

#--> Warning
def belum_bisa():
    print('Sorry Bos, Fiturnya Belum Tersedia\nMasih Pusing Mikirin Logikanya\nDoakan Semoga Cepat Selesai Yaa!\nSemoga SC Ini Bisa Membantu Orang Banyak...\nTerima Kasih!\n\n- Dapunta Khurayra X')
    finish()
    exit()

#--> Trigger
if __name__ == '__main__':
    clear()
    start()
    login()
    finish()