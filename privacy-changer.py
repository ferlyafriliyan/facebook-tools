#--> Import Module
import os, sys, requests, bs4, re, time, datetime, json
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor

#--> Warna
P = "\x1b[38;5;231m" # Putih
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau

#--> Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

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
        main_menu()
    def cek_cookies(self):
        try:
            self.cookie     = {'cookie':open('login/cookie.json','r').read()}
            self.token_eaag = open('login/token_eaag.json','r').read()
            self.token_eaab = open('login/token_eaab.json','r').read()
            language(self.cookie)
            req1 = self.xyz.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token_eaag),cookies=self.cookie).json()['name']
            req2 = self.xyz.get('https://graph.facebook.com/me/friends?fields=summary&limit=0&access_token=%s'%(self.token_eaab),cookies=self.cookie).json()['summary']['total_count']
            clear()
            print('%sHalo %s%s%s, Selamat Datang !\n'%(P,H,req1,P))
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
        try:
            self.token_eaag = self.generate_token_eaag(ciko)
            self.token_eaab = self.generate_token_eaab(ciko)
        except Exception as e:
            self.insert_cookie()
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

#--> Main Menu
class main_menu:
    def __init__(self):
        self.menu_utama()
    def menu_utama(self):
        print('%s[ %sMain Menu %s]%s'%(H,P,H,P))
        print('%s[%s1%s] %sPhoto Tag Remover%s'%(H,P,H,P,P))
        print('%s[%s2%s] %sPost Privacy Changer%s'%(H,P,H,P,P))
        print('%s[%s3%s] %sPhoto Privacy Changer%s'%(H,P,H,P,P))
        print('%s[%s4%s] %sAlbum Privacy Changer%s'%(H,P,H,P,P))
        print('%s[%s5%s] %sDelete All Photo%s'%(H,P,H,P,P))
        print('%s[%s0%s] %sLogout%s'%(M,P,M,M,P))
        xd = input(' %s└──Pilih : '%(P))
        print('')
        if xd in ['1','01','a']:   tag_remover()
        elif xd in ['2','02','b']: priv_post()
        elif xd in ['3','03','c']: priv_photo()
        elif xd in ['4','04','d']: priv_album()
        elif xd in ['5','05','e']: pass
        elif xd in ['0','00','z']: pass
        else: exit('\n%sIsi Yg Benar!%s\n'%(M,P))

#--> Tag Remover
class tag_remover:
    def __init__(self):
        self.loop       = 0
        self.xyz        = requests.Session()
        self.token_eaag = open('login/token_eaag.json','r').read()
        self.token_eaab = open('login/token_eaab.json','r').read()
        self.cookie     = {'cookie':open('login/cookie.json','r').read()}
        try:
            id  = self.xyz.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token_eaag),cookies=self.cookie).json()['id']
            url = 'https://mbasic.facebook.com/%s/photoset/t.%s/?owner_id=%s'%(id,id,id)
        except Exception as e:
            login()
        self.dump_photo(url)
    def dump_photo(self,url):
        req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
        for x in req.find_all('a',href=True):
            if 'photo.php?fbid' in str(x['href']):
                lk = 'https://mbasic.facebook.com'+x['href']
                self.hapus_tanda(lk)
        try:
            lin = 'https://mbasic.facebook.com' + req.find('a',string='Lihat Foto Lainnya')['href']
            self.dump_photo(lin)
        except Exception as e:
            pass
    def hapus_tanda(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            raq = req.find('a',string='Hapus Tanda')
            ht  = 'https://mbasic.facebook.com'+raq['href']
            roq = bs(self.xyz.get(ht,cookies=self.cookie).content,'html.parser')
            if 'Hapus Tanda' in str(roq):
                pass
            else:
                self.loop += 1
                print('\r%sBerhasil Menghapus %s%s %sTag'%(P,H,str(self.loop),P),end=''); sys.stdout.flush()
        except Exception as e:
            pass

#--> Private Post
class priv_post:
    def __init__(self):
        self.isia = []
        self.putar1 = 0
        self.tampung_id_post = []
        self.xyz   = requests.Session()
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        self.token  = open('login/token_eaag.json','r').read()
        url = 'https://graph.facebook.com/me/posts?fields=id,privacy&limit=10000&access_token='+self.token
        self.pilihan()
        self.dump_post(url)
        self.sort()
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
    def dump_post(self,url):
        req = self.xyz.get(url,cookies=self.cookie).json()
        for x in req['data']:
            try:
                if self.priv_awal == 'SEMUA':
                    if x['privacy']['description'] != self.kata_akhir: self.tampung_id_post.append(x['id']+'|'+x['privacy']['description'])
                    else:pass
                else:
                    if x['privacy']['value'] == self.priv_awal: self.tampung_id_post.append(x['id']+'|'+x['privacy']['description'])
                    else:pass
            except Exception as e:pass
        try:
            nek = req['paging']['next'] + '&limit=10000'
            self.dump_post(nek)
        except Exception as e: pass
    def sort(self):
        if self.priv_awal == 'SEMUA':
            print('Privasi Yg Sudah Sama Akan Di-Skip')
        print('Berhasil Mengumpulkan %s Postingan'%(str(len(self.tampung_id_post))))
        tan = int(input('Berapa Post Yg Ingin Dirubah Privasi : '))
        print('')
        with ThreadPoolExecutor(max_workers=30) as TPE:
            for xd in self.tampung_id_post:
                try:
                    pid = xd.split('|')[0]
                    aw = xd.split('|')[1]
                    TPE.submit(self.privacy_graphql,pid,aw)
                    self.putar1 += 1
                    if self.putar1 == tan:
                        break
                except Exception as e:pass
        exit('')
    def privacy_graphql(self,pid,awal):
        id = pid.split('_')[0]
        head1 = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
        req = bs(self.xyz.get(f'https://www.facebook.com/{pid}',headers=head1,cookies=self.cookie,allow_redirects=True).content,'html.parser')
        try:
            lipwid = sorted(list(set(re.findall('"privacy_write_id":"(.*?)"}',str(req)))))
            for pwid in lipwid:
                haste = re.search('"haste_session":"(.*?)",',str(req)).group(1)
                rev = re.search('{"rev":(.*?)}',str(req)).group(1)
                hsi = re.search('"hsi":"(.*?)",',str(req)).group(1)
                dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',str(req)).group(1)
                jazoest = re.search('&jazoest=(.*?)",',str(req)).group(1)
                lsd = re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1)
                spinr = re.search('"__spin_r":(.*?),',str(req)).group(1)
                spint = re.search('"__spin_t":(.*?),',str(req)).group(1)
                priv = {
                    'input' : {
                        "privacy_mutation_token":'null',
                        "privacy_row_input": {
                            "allow":[],
                            "base_state":"SELF",
                            "deny":[],
                            "tag_expansion_state":"UNSPECIFIED"},
                        "privacy_write_id":pwid,
                        "render_location":"COMET_STREAM",
                        "actor_id":id,
                        "client_mutation_id":"1"},
                    "privacySelectorRenderLocation":"COMET_STREAM",
                    "scale":1.5,
                    "storyRenderLocation":"permalink",
                    "tags":"null"}
                data = {
                    'av':id,'__user':id,'__a':'1','__req':'1a','__hs':haste,'dpr':'1.5','__ccg':'GOOD','__rev':rev,'__hsi':hsi,'__comet_req':'15','fb_dtsg': dtsg,'jazoest': jazoest,'lsd': lsd,'__spin_b':'trunk','__spin_r':spinr,'__spin_t':spint,
                    'fb_api_caller_class':'RelayModern',
                    'fb_api_req_friendly_name':'CometPrivacySelectorSavePrivacyMutation',
                    'variables':json.dumps(priv),
                    'server_timestamps':'true',
                    'doc_id':'6685952068091223'}
                head2 = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Origin':'https://www.facebook.com','Referer':'https://www.facebook.com/pages/creation/?ref_type=launch_point','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','X-Fb-Friendly-Name':'CometPrivacySelectorSavePrivacyMutation','X-Fb-Lsd':lsd}
                pos = self.xyz.post('https://www.facebook.com/api/graphql/',data=data,headers=head2,cookies=self.cookie)
                if 'A server error noncoercible_variable_value occured' in str(pos): pass
                else:
                    self.isia.append(pid)
                    print('\r[%s-->%s] %s'%(awal,self.kata_akhir,pid))
                    print('\rBerhasil Mengubah %s Privasi Postingan'%(str(len(self.isia))),end='');sys.stdout.flush()
        except Exception as e:
            print('\r[Error] %s'%(e),end=''); sys.stdout.flush()

#--> Private Photo
class priv_photo:
    def __init__(self):
        self.data_photo = []
        self.isia = []
        self.xyz = requests.Session()
        self.token_eaag = open('login/token_eaag.json','r').read()
        self.token_eaab = open('login/token_eaab.json','r').read()
        self.cookie     = {'cookie':open('login/cookie.json','r').read()}
        self.id = re.search('c_user=(.*?);',self.cookie['cookie']).group(1)
        self.get_album()
        if len(self.data_photo) == 0:
            print('Tidak Ditemukan Foto')
        else:
            print('Berhasil Mengumpulkan %s Foto\n'%(str(len(self.data_photo))))
            for c in self.data_photo:
                self.privacy_graphql(c)
    def get_album(self):
        url = f'https://graph.facebook.com/me/albums?access_token={self.token_eaag}'
        req = self.xyz.get(url,cookies=self.cookie).json()
        t = ['profile','cover','mobile']
        for x in req['data']:
            if x['type'] in t:
                url = 'https://graph.facebook.com/%s/photos?fields=id&limit=10000&access_token=%s'%(x['id'],self.token_eaag)
                self.get_photo(url)
    def get_photo(self,url):
        req = self.xyz.get(url,cookies=self.cookie).json()
        for x in req['data']:
            self.data_photo.append(x['id'])
        try:
            nek = req['paging']['next'] + '&limit=10000'
            self.get_photo(nek)
        except Exception as e: pass
    def privacy_graphql(self,pid):
        head1 = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
        req = bs(self.xyz.get(f'https://www.facebook.com/{pid}',headers=head1,cookies=self.cookie,allow_redirects=True).content,'html.parser')
        try:
            haste = re.search('"haste_session":"(.*?)",',str(req)).group(1)
            rev = re.search('{"rev":(.*?)}',str(req)).group(1)
            hsi = re.search('"hsi":"(.*?)",',str(req)).group(1)
            dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',str(req)).group(1)
            jazoest = re.search('&jazoest=(.*?)",',str(req)).group(1)
            lsd = re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1)
            spinr = re.search('"__spin_r":(.*?),',str(req)).group(1)
            spint = re.search('"__spin_t":(.*?),',str(req)).group(1)
            pwid = re.search('"privacy_write_id":"(.*?)"}',str(req)).group(1)
            priv = {
                "input":{
                    "privacy_mutation_token":"null",
                    "privacy_row_input":{
                        "allow":[],
                        "base_state":"SELF",
                        "deny":[],
                        "tag_expansion_state":"UNSPECIFIED"},
                    "privacy_write_id":pwid,
                    "render_location":"COMET_MEDIA_VIEWER",
                    "actor_id":self.id,
                    "client_mutation_id":"1"},
                "privacySelectorRenderLocation":"COMET_MEDIA_VIEWER",
                "scale":1.5,
                "storyRenderLocation":"permalink",
                "tags":"null"}
            data = {
                'av':self.id,'__user':self.id,'__a':'1','__req':'1a','__hs':haste,'dpr':'1.5','__ccg':'GOOD','__rev':rev,'__hsi':hsi,'__comet_req':'15','fb_dtsg': dtsg,'lsd': lsd,'jazoest':jazoest,'__spin_b':'trunk','__spin_r':spinr,'__spin_t':spint,
                'fb_api_caller_class':'RelayModern',
                'fb_api_req_friendly_name':'CometPrivacySelectorSavePrivacyMutation',
                'variables':json.dumps(priv),
                'server_timestamps':'true',
                'doc_id':'6685952068091223'}
            head2 = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Origin':'https://www.facebook.com','Referer':'https://www.facebook.com/pages/creation/?ref_type=launch_point','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','X-Fb-Friendly-Name':'CometPrivacySelectorSavePrivacyMutation','X-Fb-Lsd':lsd}
            pos = self.xyz.post('https://www.facebook.com/api/graphql/',data=data,headers=head2,cookies=self.cookie)
            if 'A server error noncoercible_variable_value occured' in str(pos): pass
            else:
                self.isia.append(pid)
                print('\r[Only Me] %s                                     '%(pid))
                print('\rBerhasil Mengubah %s Privasi Foto'%(str(len(self.isia))),end='');sys.stdout.flush()
        except Exception as e:
            print('\r[Error] %s'%(e),end=''); sys.stdout.flush()

#--> Private Album
class priv_album:
    def __init__(self):
        self.isia = []
        self.album = []
        self.xyz = requests.Session()
        self.token_eaag = open('login/token_eaag.json','r').read()
        self.token_eaab = open('login/token_eaab.json','r').read()
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        self.id = re.search('c_user=(.*?);',self.cookie['cookie']).group(1)
        self.get_album()
        if len(self.album) == 0:
            print('Tidak Ditemukan Album')
        else:
            print('Berhasil Mendata %s Album\n'%(str(len(self.album))))
            for c in self.album:
                self.privacy_graphql(c)
    def get_album(self):
        url = f'https://graph.facebook.com/me/albums?access_token={self.token_eaag}'
        req = self.xyz.get(url,cookies=self.cookie).json()
        for x in req['data']:
            try: self.album.append({'id':x['id'],'name':x['name'],'priv':x['privacy']})
            except Exception as e: pass
    def privacy_graphql(self,pid):
        head1 = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
        req = bs(self.xyz.get('https://www.facebook.com/media/set/?set=a.%s&type=3'%(pid['id']),headers=head1,cookies=self.cookie,allow_redirects=True).content,'html.parser')
        try:
            haste = re.search('"haste_session":"(.*?)",',str(req)).group(1)
            rev = re.search('{"rev":(.*?)}',str(req)).group(1)
            hsi = re.search('"hsi":"(.*?)",',str(req)).group(1)
            dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',str(req)).group(1)
            jazoest = re.search('&jazoest=(.*?)",',str(req)).group(1)
            lsd = re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1)
            spinr = re.search('"__spin_r":(.*?),',str(req)).group(1)
            spint = re.search('"__spin_t":(.*?),',str(req)).group(1)
            pwid = re.search('"privacy_write_id":"(.*?)"}',str(req)).group(1)
            akhir = 'SELF'
            var = {
                "input":{
                    "privacy_mutation_token":"null",
                    "privacy_row_input":{
                        "allow":[],
                        "base_state":akhir,
                        "deny":[],
                        "tag_expansion_state":"UNSPECIFIED"},
                    "privacy_write_id":pwid,
                    "render_location":"COMET_STREAM",
                    "actor_id":self.id,
                    "client_mutation_id":"1"},
                    "privacySelectorRenderLocation":"COMET_STREAM",
                    "scale":1.5,
                    "storyRenderLocation":"permalink",
                    "tags":"null"}
            data = {
                'av':self.id,'__user':self.id,'__a':'1','__req':'3l','__hs':haste,'dpr':'1.5','__ccg':'GOOD','__rev':rev,'__hsi':hsi,'__comet_req':'15','fb_dtsg': dtsg,'lsd': lsd,'jazoest':jazoest,'__spin_b':'trunk','__spin_r':spinr,'__spin_t':spint,
                'fb_api_caller_class':'RelayModern',
                'fb_api_req_friendly_name':'CometPrivacySelectorSavePrivacyMutation',
                'variables':json.dumps(var),
                'server_timestamps':'true',
                'doc_id':'6685952068091223'}
            head2 = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Origin':'https://www.facebook.com','Referer':'https://www.facebook.com/pages/creation/?ref_type=launch_point','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','X-Fb-Friendly-Name':'CometPrivacySelectorSavePrivacyMutation','X-Fb-Lsd':lsd}
            pos = self.xyz.post('https://www.facebook.com/api/graphql/',data=data,headers=head2,cookies=self.cookie)
            if 'A server error noncoercible_variable_value occured' in str(pos): pass
            else:
                self.isia.append(pid['id'])
                print('\r[%s-->%s] %s                                  '%(pid['priv'],akhir,pid['id']))
                print('\rBerhasil Mengubah %s Privasi Postingan'%(str(len(self.isia))),end='');sys.stdout.flush()
        except Exception as e:
            print('\r[Error] %s'%(e),end=''); sys.stdout.flush()

#--> Trigger
if __name__ == '__main__':
    clear()
    start()
    login()
    finish()