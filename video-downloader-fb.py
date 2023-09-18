#--> Import Module
import os, sys, requests, bs4, re, time, datetime, shutil
from bs4 import BeautifulSoup as bs
try: import moviepy.editor as mv
except Exception as e: os.system('pip install moviepy'); import moviepy.editor as mv

#--> Warna
P = "\x1b[38;5;231m" # Putih
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau

#--> Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

#--> Animasi
def urut(i):
    s = 0.005
    for e in i + '\n': sys.stdout.write(e); sys.stdout.flush(); time.sleep(s)

# --> Ubah Bahasa
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

# --> Login
class login:
    def __init__(self):
        self.xyz = requests.Session()
        self.cek_cookies()
        get_url()
    def cek_cookies(self):
        try:
            self.cookie     = {'cookie':open('login/cookie.json','r').read()}
            self.token_eaag = open('login/token_eaag.json','r').read()
            self.token_eaab = open('login/token_eaab.json','r').read()
            language(self.cookie)
            req1 = self.xyz.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token_eaag),cookies=self.cookie).json()['name']
            req2 = self.xyz.get('https://graph.facebook.com/me/friends?fields=summary&limit=0&access_token=%s'%(self.token_eaab),cookies=self.cookie).json()['summary']['total_count']
            clear()
            print('%sLogin Sebagai %s%s%s\n'%(P,H,req1,P))
        except Exception as e:
            self.insert_cookie()
    def insert_cookie(self):
        print('\n%sCookie Invalid!%s'%(M,P))
        time.sleep(2)
        clear()
        print('%sApabila Akun A2F On, Pergi Ke'%(P))
        print('https://business.facebook.com/business_locations')
        print('Untuk Memasukkan Kode Autentikasi')
        ciko = input('%sMasukkan Cookie : %s%s'%(P,H,P))
        self.token_eaag = self.generate_token_eaag(ciko)
        self.token_eaab = self.generate_token_eaab(ciko)
        try:os.mkdir("login")
        except:pass
        open('login/cookie.json','w').write(ciko)
        open('login/token_eaag.json','w').write(self.token_eaag)
        open('login/token_eaab.json','w').write(self.token_eaab)
        self.cek_cookies()
    def generate_token_eaag(self,cok):
        url = 'https://business.facebook.com/business_locations'
        req = self.xyz.get(url,cookies={'cookie':cok})
        tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
        return(tok)
    def generate_token_eaab(self,cok):
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = self.xyz.get(url,cookies={'cookie':cok})
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = self.xyz.get(nek,cookies={'cookie':cok})
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        return(tok)

#--> Get URL Video
class get_url:
    def __init__(self):
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        self.xyz    = requests.Session()
        self.head   = {
            'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language'           : 'en-US,en;q=0.9',
            'cache-control'             : 'max-age=0',
            'origin'                    : 'https://www.facebook.com',
            'pragma'                    : 'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace',
            'referer'                   : 'https://www.facebook.com',
            'sec-ch-ua'                 : '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile'          : '?1',
            'sec-ch-ua-platform'        : '"Android"',
            'sec-fetch-dest'            : 'document',
            'sec-fetch-mode'            : 'navigate',
            'sec-fetch-site'            : 'same-origin',
            'sec-fetch-user'            : '?1',
            'upgrade-insecure-requests' : '1',
            'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'}
        print("%sKetik 'set' Untuk Mengatur Penyimpanan Video"%(P))
        irl = input('%sMasukkan URL : '%(P))
        if irl in ['set','Set','SET']:self.set()
        else:
            if 'www.facebook.com' in irl:      url = irl.replace('www.facebook.com','m.facebook.com')
            elif 'mbasic.facebook.com' in irl: url = irl.replace('mbasic.facebook.com','m.facebook.com')
            elif 'm.facebook.com' in irl:      url = irl
            else: exit('\n%sIsi Yg Benar!%s\n'%(M,P))
            self.scrap(url)
    def set(self):
        z = input('\n%sAtur Lokasi Penyimpanan : '%(P))
        try: os.mkdir('FVD/default')
        except Exception as e: pass
        try: open('FVD/default/default.json','w').write(z)
        except Exception as e: exit('\n%sIsi Yg Benar!%s\n'%(M,P))
    def scrap(self,url):
        try: req   = bs(self.xyz.get(url,headers=self.head,cookies=self.cookie).content,'html.parser'); raq   = str(req)[:100000].replace('\\','').replace('u003C','').replace('amp;','').replace('gt;','').replace('lt;','').replace('&&','&').replace('','')
        except Exception as e: exit('\n%sPostingan Tidak Ditemukan!%s\n'%(M,P))
        try: self.aud   = re.search('value="2"/&BaseURL&(.*?)/BaseURL',raq).group(1)
        except Exception as e: self.aud   = re.search('value="2"/&BaseURL&(.*?)/BaseURL',raq).group(1)
        try: self.fql24 = re.search('FBQualityLabel="240p"&BaseURL&(.*?)/BaseURL',raq).group(1); self.stat1 = ' %s✔'%(H)
        except Exception as e: self.fql24 = 'null'; self.stat1 = ' %s✘'%(M)
        try: self.fql27 = re.search('FBQualityLabel="270p"&BaseURL&(.*?)/BaseURL',raq).group(1); self.stat2 = ' %s✔'%(H)
        except Exception as e: self.fql27 = 'null'; self.stat2 = ' %s✘'%(M)
        try: self.fql36 = re.search('FBQualityLabel="360p"&BaseURL&(.*?)/BaseURL',raq).group(1); self.stat3 = ' %s✔'%(H)
        except Exception as e: self.fql36 = 'null'; self.stat3 = ' %s✘'%(M)
        try: self.fql48 = re.search('FBQualityLabel="480p"&BaseURL&(.*?)/BaseURL',raq).group(1); self.stat4 = ' %s✔'%(H)
        except Exception as e: self.fql48 = 'null'; self.stat4 = ' %s✘'%(M)
        try: self.fql54 = re.search('FBQualityLabel="540p"&BaseURL&(.*?)/BaseURL',raq).group(1); self.stat5 = ' %s✔'%(H)
        except Exception as e: self.fql54 = 'null'; self.stat5 = ' %s✘'%(M)
        try: self.fql64 = re.search('FBQualityLabel="640p"&BaseURL&(.*?)/BaseURL',raq).group(1); self.stat6 = ' %s✔'%(H)
        except Exception as e: self.fql64 = 'null'; self.stat6 = ' %s✘'%(M)
        try: self.fql72 = re.search('FBQualityLabel="720p"&BaseURL&(.*?)/BaseURL',raq).group(1); self.stat7 = ' %s✔'%(H)
        except Exception as e: self.fql72 = 'null'; self.stat7 = ' %s✘'%(M)
        try: self.fql108 = re.search('FBQualityLabel="1080p"&BaseURL&(.*?)/BaseURL',raq).group(1); self.stat8 = ' %s✔'%(H)
        except Exception as e: self.fql10 = 'null'; self.stat8 = ' %s✘'%(M)
        try: self.fql128 = re.search('FBQualityLabel="1280p"&BaseURL&(.*?)/BaseURL',raq).group(1); self.stat9 = ' %s✔'%(H)
        except Exception as e: self.fql12 = 'null'; self.stat9 = ' %s✘'%(M)
        try: self.fqlSC = re.search('FBQualityLabel="Source"&BaseURL&(.*?)/BaseURL',raq).group(1); self.stat10 = ' %s✔'%(H)
        except Exception as e: self.fqls = 'null'; self.stat10 = ' %s✘'%(M)
        self.pilih()
    def pilih(self):
        print('\n%s[ Pilih Kualitas Video ]\n'%(P))
        print('%s[1] 240p%s   %s[6] 640p%s'%(P,self.stat1,P,self.stat6))
        print('%s[2] 270p%s   %s[7] 720p%s'%(P,self.stat2,P,self.stat7))
        print('%s[3] 360p%s   %s[8] 1080p%s'%(P,self.stat3,P,self.stat8))
        print('%s[4] 480p%s   %s[9] 1280p%s'%(P,self.stat4,P,self.stat9))
        print('%s[5] 540p%s   %s[0] Source%s'%(P,self.stat5,P,self.stat10))
        xd = input('%sPilih : '%(P))
        if xd in ['1','01','a']:   url = self.fql24
        elif xd in ['2','02','b']: url = self.fql27
        elif xd in ['3','03','c']: url = self.fql36
        elif xd in ['4','04','d']: url = self.fql48
        elif xd in ['5','05','e']: url = self.fql54
        elif xd in ['6','06','f']: url = self.fql64
        elif xd in ['7','07','g']: url = self.fql72
        elif xd in ['8','08','h']: url = self.fql108
        elif xd in ['9','09','i']: url = self.fql128
        elif xd in ['0','00','z']: url = self.fqlSC
        else: exit('\n%sIsi Yg Benar!%s\n'%(M,P))
        if url == 'null':
            exit('\n%sIsi Yg Benar!%s\n'%(M,P))
        else: self.printn(url); savendown(url,self.aud)
    def printn(self,url):
        print('\n%s[ URL Video ]'%(P))
        print('%s%s'%(P,url))
        print('\n%s[ URL Audio ]'%(P))
        print('%s%s'%(P,self.aud))

#--> Download And Save Video
class savendown:
    def __init__(self,vid,aud):
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        self.xyz    = requests.Session()
        self.vid    = vid
        self.aud    = aud
        self.cf     = input('%s\nSimpan File Dengan Nama : '%(P)).replace(' ','_')
        print('')
        try:os.mkdir('FVD')
        except:pass
        try:os.mkdir('FVD/'+self.cf)
        except:pass
        self.filevid = 'FVD/%s/%s.mp4'%(self.cf,self.cf)
        self.fileaud = 'FVD/%s/%s.mp3'%(self.cf,self.cf)
        open(self.filevid,'a+')
        open(self.fileaud,'a+')
        self.savedown()
        try: self.render()
        except Exception as e:
            try:shutil.rmtree('FVD/'+self.cf)
            except:pass
            exit('\n%sProses Gagal'%(M))
        self.move()
    def savedown(self):
        reqvid = self.xyz.get(self.vid,cookies=self.cookie).content
        reqaud = self.xyz.get(self.aud,cookies=self.cookie).content
        open(self.filevid, "wb").write(reqvid)
        open(self.fileaud, "wb").write(reqaud)
    def render(self):
        self.fileout = 'FVD/%s.mp4'%(self.cf)
        vclip = mv.VideoFileClip(self.filevid)
        aclip = mv.AudioFileClip(self.fileaud)
        oclip = vclip.set_audio(aclip)
        oclip.write_videofile(self.fileout, fps=60)
        try:shutil.rmtree('FVD/'+self.cf)
        except:pass
    def move(self):
        try:
            xd = open('FVD/default/default.json','r').read()
            shutil.move(self.fileout, xd)
            print('\n%sBerhasil Disimpan Ke : %s%s%s'%(P,H,xd,P))
        except Exception as e: pass

#--> Trigger
if __name__ == '__main__':
    clear()
    start()
    login()
    finish()