###----------[ AUTHOR ]---------- ###
Author = 'Dapunta Khurayra X'
Version = 0.1
Facebook = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/ratya.anonym.id'

###----------[ MODULES ]---------- ###
import requests,bs4,sys,os,re,time,random,json
from concurrent.futures import ThreadPoolExecutor
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
def clotox(cookie):
    with requests.Session() as xyz:
        get_tok = xyz.get('https://business.facebook.com/business_locations', headers = {
            "user-agent"                :'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
            "referer"                   : 'https://www.facebook.com/',
            "host"                      : "business.facebook.com",
            "origin"                    : 'https://business.facebook.com',
            "upgrade-insecure-requests" : "1",
            "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control"             : "max-age=0",
            "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type"              : "text/html; charset=utf-8"},
            cookies = {"cookie":cookie})
        return(re.search('(\["EAAG\w+)', get_tok.text).group(1).replace('["',''))

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
            exit(self.menu())
        except Exception as e:
            self.cookie_invalid()
    def cookie_invalid(self):
        print('Cookie Invalid!')
        time.sleep(2)
        clear()
        self.insert_cookie()
    def insert_cookie(self):
        print('Apabila Akun A2F On, Pergi Ke')
        print('https://business.facebook.com/business_locations')
        print('Untuk Memasukkan Kode Autentikasi')
        ciko = input('Masukkan Cookie : ')
        toke = clotox(ciko)
        try:os.mkdir("login")
        except:pass
        open('login/cookie.json','w').write(ciko)
        open('login/token.json','w').write(toke)
        self.cek_cookies()
    def menu(self):
        print('[1] Link URL\n[2] Galeri\n[3] Unsplash\n[4] Freepik\n[5] Anime')
        xd = input('Pilih : ')
        print('')
        if xd in ['1','01','a']:link_url(self.token,self.cookie)
        elif xd in ['2','2','b']:galeri(self.token,self.cookie)
        elif xd in ['3','3','c']:unsplash();random_post_foto(self.token,self.cookie)
        elif xd in ['4','4','d']:freepik();random_post_foto(self.token,self.cookie)
        elif xd in ['5','5','e']:myanime();random_post_foto(self.token,self.cookie)
        else:print('Isi Yg Benar!');exit()

###----------[ DUMP IMAGE LINK URL ]---------- ###
class link_url:
    def __init__(self,token,cookie):
        global data_image
        print('Pisahkan Dengan Koma (,)')
        data_image = input('Masukkan URL Gambar : ').split(',')
        df = input('\nPosting Urut/Random [u/r] : ').lower()
        if df in ['1','01','a','u']:
            album = input('Masukkan ID Album : ')
            pesan = input('Tulis Pesan Teks : ')
            jumlah = int(input('Berapa Unggahan Per Foto : '))
            print('Jumlah Foto Yg Akan Diunggah : %s'%(str(jumlah*len(data_image))))
            with ThreadPoolExecutor(max_workers=35) as TPE:
                for gambar in data_image:
                    TPE.submit(ordinal_post_foto,album,pesan,gambar,jumlah,token,cookie)
        elif df in ['2','02','b','r']:
            random_post_foto(token,cookie)

###----------[ DUMP IMAGE FILE/GALERY ]---------- ###
class galeri:
    def __init__(self,token,cookie):
        global data_image
        print('Pisahkan Dengan Koma (,)')
        data_image = input('Masukkan Lokasi Penyimpanan Gambar : ').split(',')
        df = input('\nPosting Urut/Random [u/r] : ').lower()
        if df in ['1','01','a','u']:
            album = input('Masukkan ID Album : ')
            pesan = input('Tulis Pesan Teks : ')
            jumlah = int(input('Berapa Unggahan Per Foto : '))
            print('Jumlah Foto Yg Akan Diunggah : %s'%(str(jumlah*len(data_image))))
            with ThreadPoolExecutor(max_workers=35) as TPE:
                for gambar in data_image:
                    TPE.submit(ordinal_post_foto,album,pesan,gambar,jumlah,token,cookie)
        elif df in ['2','02','b','r']:
            random_post_foto(token,cookie)  

###----------[ DUMP IMAGE UNSPLASH ]---------- ###
class unsplash:
    def __init__(self):
        url = 'https://unsplash.com/'
        self.xyz = requests.Session()
        self.scrasp(url)
    def scrasp(self,url):
        global data_image
        data_image = []
        req = bs(self.xyz.get(url).content,'html.parser')
        for x in req.find_all('img'):
            try:
                if 'images.unsplash.com/photo' in str(x['src']):
                    data_image.append(x['src'])
            except Exception as e:pass

###----------[ DUMP IMAGE FREEPIK ]---------- ###
class freepik:
    def __init__(self):
        url = 'https://www.freepik.com/free-photos-vectors/colorful-backgrounds'
        self.xyz = requests.Session()
        self.scrasp(url)
    def scrasp(self,url):
        global data_image
        data_image = []
        head = {'user-agent' : 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'}
        req = bs(self.xyz.get(url,headers=head).content,'html.parser')
        for x in req.find_all('figure'):
            try:
                if 'img.freepik.com' in str(x['data-image']):
                    data_image.append(x['data-image'])
            except Exception as e:pass

###----------[ DUMP IMAGE MYANIMELIST ]---------- ###
class myanime:
    def __init__(self):
        url = 'https://myanimelist.net/character.php'
        self.xyz = requests.Session()
        self.scrasp(url)
    def scrasp(self,url):
        global data_image
        data_image = []
        req = bs(self.xyz.get(url).content,'html.parser')
        for x in req.find_all('img'):
            try:
                if 'cdn.myanimelist.net/r' in str(x['data-src']):
                    data_image.append(x['data-src'])
            except Exception as e:pass

###----------[ POST ACTION ORDINAL ]---------- ###
class ordinal_post_foto:
    def __init__(self,album,pesan,gambar,jumlah,token,cookie):
        loop = 0
        for x in range(int(jumlah)):
            try:
                url = f'https://graph.facebook.com/{album}/photos?'
                data = {
                    'method' : 'POST',
                    'message' : pesan + ' ' + str(loop+1),
                    'url' : gambar,
                    'access_token' : token
                    }
                req = requests.Session().post(url,data=data,cookies=cookie)
                if 'error' in str(req.json()):
                    loop += 1
                    print('\rAkun Spam %s'%(str(loop)),end='');sys.stdout.flush()
                else:
                    loop += 1
                    print('\rBerhasil Posting %s Gambar'%(str(loop)),end='')
                sys.stdout.flush()
            except Exception as e:
                print('\rAkun Spam',end='');sys.stdout.flush()

###----------[ POST ACTION RANDOM ]---------- ###
class random_post_foto:
    def __init__(self,token,cookie):
        self.token = token
        self.cookie = cookie
        self.xyz = requests.Session()
        self.takon()
    def takon(self):
        self.album = input('Masukkan ID Album : ')
        self.jumla = input('Berapa Jumlah Foto : ')
        self.pesan = input('Tulis Pesan Teks : ')
        self.requ()
    def requ(self):
        loop = 0
        for x in range(int(self.jumla)):
            try:
                url = f'https://graph.facebook.com/{self.album}/photos?'
                data = {
                    'method' : 'POST',
                    'message' : self.pesan + ' ' + str(loop+1),
                    'url' : random.choice(data_image),
                    'access_token' : self.token
                    }
                req = self.xyz.post(url,data=data,cookies=self.cookie)
                if 'error' in str(req.json()):
                    loop += 1
                    print('\rAkun Spam %s'%(str(loop)),end='');sys.stdout.flush()
                else:
                    loop += 1
                    print('\rBerhasil Posting %s Gambar'%(str(loop)),end='')
                sys.stdout.flush()
            except Exception as e:
                print('\rAkun Spam',end='');sys.stdout.flush()


if __name__=='__main__':
    clear()
    main()