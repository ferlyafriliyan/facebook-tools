# ------ [ Gw Cuma Perecode Biasa Bang!!! ] ------ #
Author = 'Afriliyan Ferly Sishigami X'
Version = 0.1
Facebook = 'Facebook.com/AfriliyanFerly.Shishigami.X'
Instagram = 'Instagram.com/afriliyanferlly_shishigami'

###----------[ MODULES ]---------- ###
import requests,bs4,sys,os,re,time,json
from bs4 import BeautifulSoup as bs

###----------[ CLEAR TERMINAL ]---------- ###
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

###----------[ CHANGE LANGUAGE ]---------- ###
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
                        "submit"  : "Bahasa Indonesia"
                        }
                    url = 'https://mbasic.facebook.com' + x['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass

###----------[ CONVERT COOKIE KE TOKEN ]---------- ###
def generate_token(cok):
    cookie = {'cookie':cok}
    try:
        url = 'https://business.facebook.com/business_locations'
        req = requests.Session().get(url,cookies=cookie)
        tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
        return(tok)
    except Exception as e:exit(main())

###----------[ MENU UTAMA ]---------- ###
class main:
    def __init__(self):
        self.xyz = requests.Session()
        self.cek_cookies()
    def cek_cookies(self):
        try:
            self.token  = open('login/token.json','r').read()
            self.cookie = {'cookie':open('login/cookie.json','r').read()}
            language(self.cookie)
            get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token),cookies=self.cookie)
            jsx = json.loads(get.text)
            nama = jsx["name"]
            clear()
            print('Login Sebagai %s\n'%(nama))
            exit(privacy_changer())
        except Exception as e:
            self.cookie_invalid()
    def cookie_invalid(self):
        print('\nCookie Invalid!')
        time.sleep(2)
        clear()
        self.insert_cookie()
    def insert_cookie(self):
        print('Apabila Akun A2F On, Pergi Ke')
        print('https://business.facebook.com/business_locations')
        print('Untuk Memasukkan Kode Autentikasi')
        ciko = input('Masukkan Cookie : ')
        toke = generate_token(ciko)
        try:os.mkdir("login")
        except:pass
        open('login/cookie.json','w').write(ciko)
        open('login/token.json','w').write(toke)
        self.cek_cookies()

###----------[ PRIVACY CHANGER ]---------- ###
class privacy_changer:
    def __init__(self):
        self.isia = []
        self.requ   = requests.Session()
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        self.token  = self.generate_token()
        self.pilihan()
        self.dump_post()
    def generate_token(self):
        try:
            url = 'https://business.facebook.com/business_locations'
            req = self.requ.get(url,cookies=self.cookie)
            tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
            return(tok)
        except Exception as e:exit('\nCookies Invalid\n')
    def pilihan(self):
            print('[ Pilih Post Berdasar Privasi Saat Ini ]')
            print('[1] Semua    [3] Teman')
            print('[2] Publik   [4] Hanya Saya')
            xd = input('Pilih : ')
            print('')
            if xd in ['1','01','a']:   self.priv_awal = 'SEMUA'
            elif xd in ['2','02','b']: self.priv_awal = 'EVERYONE'
            elif xd in ['3','03','c']: self.priv_awal = 'ALL_FRIENDS'
            elif xd in ['4','04','d']: self.priv_awal = 'SELF'
            else:exit('\nIsi Yang Benar !\n')
            print('[ Ubah Privasi Post Menjadi ]')
            print('[1] Publik')
            print('[2] Teman')
            print('[3] Hanya Saya')
            xd = input('Pilih : ')
            print('')
            if xd in ['1','01','a']:   self.priv_akhir = '300645083384735'; self.kata_akhir = 'Publik'
            elif xd in ['2','02','b']: self.priv_akhir = '291667064279714'; self.kata_akhir = 'Teman'
            elif xd in ['3','03','c']: self.priv_akhir = '286958161406148'; self.kata_akhir = 'Hanya saya'
            else:exit('\nIsi Yang Benar !\n')
    def dump_post(self):
        self.putar1 = 0
        self.tampung_id_post = []
        url = 'https://graph.facebook.com/me/posts?fields=id,privacy&limit=10000&access_token='+self.token
        req = self.requ.get(url,cookies=self.cookie).json()
        for x in req['data']:
            try:
                if self.priv_awal == 'SEMUA':
                    if x['privacy']['description'] != self.kata_akhir: self.tampung_id_post.append(x['id']+'|'+x['privacy']['description'])
                    else:pass
                else:
                    if x['privacy']['value'] == self.priv_awal: self.tampung_id_post.append(x['id']+'|'+x['privacy']['description'])
                    else:pass
            except Exception as e:pass
        if self.priv_awal == 'SEMUA':
            print('Privasi Yg Sudah Sama Akan Di-Skip')
        print('Berhasil Mengumpulkan %s Postingan'%(str(len(self.tampung_id_post))))
        tan = int(input('Berapa Post Yg Ingin Dirubah Privasi : '))
        print('')
        for xd in self.tampung_id_post:
            try:
                id = xd.split('|')[0]
                aw = xd.split('|')[1]
                self.id = id
                url = 'https://mbasic.facebook.com/story.php?story_fbid=%s&id=%s'%(id.split('_')[1],id.split('_')[0])
                self.scrap1(url,aw)
                self.putar1 += 1
                if self.putar1 == tan:
                    break
            except Exception as e:pass
        exit('')
    def scrap1(self,url,awal):
        req = bs(self.requ.get(url,cookies=self.cookie).content,'html.parser')
        xdr = 'https://mbasic.facebook.com' + [x['href'] for x in req.find_all('a',href=True) if 'privacyx/selector' in str(x)][0] + '&priv_expand=see_all'
        self.scrap2(xdr,awal)
    def scrap2(self,url,awal):
        req = bs(self.requ.get(url,cookies=self.cookie).content,'html.parser')
        xdy = 'https://mbasic.facebook.com' + [ x['href'] for x in req.find_all('a',href=True) if '/a/privacy/' in x['href'] if self.priv_akhir in x['href'] ][0]
        self.scrap3(xdy,awal)
    def scrap3(self,url,awal):
        req = bs(self.requ.get(url,cookies=self.cookie).content,'html.parser')
        if self.kata_akhir in str(req):
            self.isia.append(self.id)
            print('\r[%s-->%s] %s'%(awal,self.kata_akhir,self.id))
            print('\rBerhasil Mengubah %s Privasi Postingan'%(str(len(self.isia))),end='');sys.stdout.flush()

if __name__=='__main__':
    clear()
    main()
