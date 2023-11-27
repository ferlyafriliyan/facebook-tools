#--> Author's Info
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = '082245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'

#--> Import Module
import os, sys, requests, bs4, re, time, datetime, urllib, random, json
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bs

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

#--> Waktu Saat Komentar Dibuat
def waktu_kom():
    _bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.datetime.now().month - 1]
    _hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.datetime.now().strftime("%A"))]
    hari_ini = ("%s %s %s"%(datetime.datetime.now().day,_bulan_,datetime.datetime.now().year))
    jam      = datetime.datetime.now().strftime("%X")
    tem      = ('\n\n%s, %s --> %s'%(_hari_,hari_ini,str(jam).replace(':','.')))
    return(tem)

# --> Login
class login:
    def __init__(self):
        self.xyz = requests.Session()
        self.cek_cookies()
        menu()
    def cek_cookies(self):
        try:
            global nama_akun, id_akun
            self.cookie     = {'cookie':open('login/cookie.json','r').read()}
            self.token_eaag = open('login/token_eaag.json','r').read()
            language(self.cookie)
            req       = self.xyz.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token_eaag),cookies=self.cookie).json()
            nama_akun = req['name']
            id_akun   = req['id']
            clear()
            print('%sLogin Sebagai %s%s%s'%(P,H,nama_akun,P))
        except Exception as e:
            self.insert_cookie()
    def insert_cookie(self):
        print('%sCookie Invalid!%s'%(M,P))
        time.sleep(2)
        clear()
        print('%sApabila Akun A2F On, Pergi Ke'%(P))
        print('https://business.facebook.com/business_locations')
        print('Untuk Memasukkan Kode Autentikasi')
        ciko = input('%sMasukkan Cookie : %s%s'%(P,H,P))
        try:self.token_eaag = self.generate_token_eaag(ciko)
        except Exception as e: self.insert_cookie()
        try:os.mkdir("login")
        except:pass
        open('login/cookie.json','w').write(ciko)
        open('login/token_eaag.json','w').write(self.token_eaag)
        self.cek_cookies()
    def generate_token_eaag(self,cok):
        url = 'https://business.facebook.com/business_locations'
        req = self.xyz.get(url,cookies={'cookie':cok})
        tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
        return(tok)

#--> Main Menu
class menu:
    def __init__(self):
        self.main()
    def main(self):
        print('\n[ Menu ]'%())
        print('[1] Edit Foto Profil'%())
        print('[2] Edit Foto Sampul'%())
        print('[3] PP Guard'%())
        print('[4] Edit Bio'%())
        print('[5] Edit Kota'%())
        print('[6] Edit Website'%())
        print('[7] Locked Profile'%())
        print('[0] Logout'%())
        x = input('Pilih : ')
        print('')
        if   x in ['1','01','a']: edit_profile_pic(); menu()
        elif x in ['2','02','b']: edit_cover_pic(); menu()
        elif x in ['3','03','c']: profile_guard(); menu()
        elif x in ['4','04','d']: update_bio(); menu()
        elif x in ['5','05','e']: edit_kota(); menu()
        elif x in ['6','06','f']: edit_website(); menu()
        elif x in ['7','07','g']: lock_profile(); menu()
        elif x in ['0','00','z']: 
            try:
                os.remove('login/cookie.json')
                os.remove('login/token_eaag.json')
                print('Good Bye...')
            except Exception :
                print('Good Bye...')
        else : 
            print('%sIsi Yg Benar!%s'%(M,P))

#--> Edit Profile Pict
class edit_profile_pic:
    def __init__(self):
        self.xyz = requests.Session()
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        self.tanya()
    def tanya(self):
        d = input('URL Foto : ')
        self.scrap1(d)
    def scrap1(self,i):
        try:
            fot = urllib.request.urlopen(i)
            url = 'https://mbasic.facebook.com/profile_picture/'
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'submit'  : 'Simpan'}
            fil = {'pic' : fot}
            pos = bs(self.xyz.post(raq['action'],data=dat,files=fil,cookies=self.cookie).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                print('\n%sGagal Mengganti Foto Profil%s'%(M,P))
            else:
                print('\n%sBerhasil Mengganti Foto Profil%s'%(H,P))
        except Exception as e:
            print('\n%sGagal Mengganti Foto Profil%s'%(M,P))

#--> Edit Cover Pict
class edit_cover_pic:
    def __init__(self):
        self.xyz = requests.Session()
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        self.tanya()
    def tanya(self):
        d = input('URL Foto : ')
        self.scrap1(d)
    def scrap1(self,i):
        try:
            fot = urllib.request.urlopen(i)
            url = 'https://mbasic.facebook.com/photos/upload/?cover_photo'
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'                  : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'                  : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'return_uri'               : re.search('name="return_uri" type="hidden" value="(.*?)"',str(raq)).group(1),
                'return_uri_error'         : re.search('name="return_uri_error" type="hidden" value="(.*?)"',str(raq)).group(1),
                'ref'                      : re.search('name="ref" type="hidden" value="(.*?)"',str(raq)).group(1),
                'csid'                     : re.search('name="csid" type="hidden" value="(.*?)"',str(raq)).group(1),
                'ctype'                    : re.search('name="ctype" type="hidden" value="(.*?)"',str(raq)).group(1),
                'profile_edit_logging_ref' : re.search('name="profile_edit_logging_ref" type="hidden" value="(.*?)"',str(raq)).group(1),
                'submit'                   : 'Unggah'}
            fil = {'file1' : fot}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=dat,files=fil,cookies=self.cookie).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                print('\n%sGagal Mengganti Foto Sampul%s'%(M,P))
            else:
                print('\n%sBerhasil Mengganti Foto Sampul%s'%(H,P))
        except Exception as e:
            print('\n%sGagal Mengganti Foto Sampul%s'%(M,P))

#--> Profile Picture Guard
class profile_guard:
    def __init__(self):
        self.xyz = requests.Session()
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        self.token  = open('login/token_eaag.json','r').read()
        self.tanya()
    def tanya(self):
        print('[1] Aktifkan')
        print('[2] Nonaktifkan')
        r = input('Pilih : ').lower()
        print('')
        if r in ['1','01','y']:
            self.scrap1(True)
        else:
            self.scrap1(False)
    def get_id(self):
        id = self.xyz.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token),cookies=self.cookie).json()['id']
        return(id)
    def scrap1(self,stat):
        id   = self.get_id()
        var  = {
            '0': {
                'is_shielded'        : stat,
                'session_id'         : '9b78191c-84fd-4ab6-b0aa-19b39f04a6bc',
                'actor_id'           : str(id),
                'client_mutation_id' : 'b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0'}}
        data = {
            'variables'                : json.dumps(var),
            'method'                   : 'post',
            'doc_id'                   : '1477043292367183',
            'query_name'               : 'IsShieldedSetMutation',
            'strip_defaults'           : 'true',
            'strip_nulls'              : 'true',
            'locale'                   : 'en_US',
            'client_country_code'      : 'US',
            'fb_api_req_friendly_name' : 'IsShieldedSetMutation',
            'fb_api_caller_class'      : 'IsShieldedSetMutation'}
        head = {
            'Content-Type'  : 'application/x-www-form-urlencoded',
            'Authorization' : 'OAuth %s'%self.token}
        url  = 'https://graph.facebook.com/graphql'
        req  = self.xyz.post(url, data=data, headers=head, cookies=self.cookie)
        if '"is_shielded":true' in req.text:
            print('\n%sBerhasil Mengaktifkan Profile Guard%s'%(H,P))
        elif '"is_shielded":false' in req.text:
            print('\n%sBerhasil Menonaktifkan Profile Guard%s'%(M,P))
        else:
            print('\n%sTerjadi Kesalahan!%s'%(M,P))

#--> Update Bio
class update_bio:
    def __init__(self):
        self.xyz    = requests.Session()
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        self.bio    = input('Tulis Bio : ')
        self.scrap1()
    def scrap1(self):
        try:
            url = 'https://mbasic.facebook.com/profile/basic/intro/bio/'
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'         : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'         : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'bio'             : self.bio,
                'publish_to_feed' : True,
                'submit'          : 'Simpan'}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=dat,cookies=self.cookie).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                print('\n%sGagal Mengganti Bio%s'%(M,P))
            else:
                print('\n%sBerhasil Mengganti Bio%s'%(H,P))
        except Exception as e:
            print('\n%sGagal Mengganti Bio%s'%(M,P))

#--> Edit Kota
class edit_kota:
    def __init__(self):
        self.xyz    = requests.Session()
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        kota = input('Nama Kota : ')
        self.scrap('https://mbasic.facebook.com/editprofile.php?type=basic&edit=hometown','hometown','hometown[]',kota)
        self.scrap('https://mbasic.facebook.com/editprofile.php?type=basic&edit=current_city','current_city','current_city[]',kota)
    def scrap(self,url,a,b,kota):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'    : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'    : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'edit'       : a,
                'type'       : 'basic',
                b : kota,
                'save'       : 'Simpan'}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=dat,cookies=self.cookie).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                print('%sGagal Mengganti Kota%s'%(M,P))
            else:
                print('%sBerhasil Mengganti Kota%s'%(H,P))
        except Exception as e:
            print('%sGagal Mengganti Kota%s'%(M,P))

#--> Edit Website
class edit_website:
    def __init__(self):
        self.xyz    = requests.Session()
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        self.web = input('URL Web : ')
        self.scrap('https://mbasic.facebook.com/editprofile.php?type=contact&edit=website')
    def scrap(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            raq = req.find('form',{'method':'post'})
            dat = {
                'fb_dtsg'    : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                'jazoest'    : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                'type'       : 'contact',
                'edit'       : 'website',
                'add_website': '1',
                'new_info'   : self.web,
                'save'       : 'Tambahkan'}
            pos = bs(self.xyz.post('https://mbasic.facebook.com'+raq['action'],data=dat,cookies=self.cookie).content,'html.parser')
            cek = pos.find('title').text
            if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :
                print('\n%sGagal Mengganti Website%s'%(M,P))
            else:
                print('\n%sBerhasil Mengganti Website%s'%(H,P))
        except Exception as e:
            print('\n%sGagal Mengganti Website%s'%(M,P))

#--> Locked Profile
class lock_profile:
    def __init__(self):
        self.xyz = requests.Session()
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        self.headget = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
        self.id = re.search('c_user=(.*?);',self.cookie['cookie']).group(1)
        self.cek_country()
    def cek_country(self):
        r = requests.Session()
        try:
            req = r.get('http://ip-api.com/json/').json()
            con = req['country']
            if con=='Bangladesh' or con=='India':
                self.choose()
            else:
                print('%sAnda Harus Menggunakan VPN Bangladesh/India\nUntuk Mengaktifkan Locked Profile!%s'%(M,P))
                menu()
        except Exception as e:
            print('\n%sGagal Mendeteksi Lokasi%s'%(M,P))
    def choose(self):
        xd = input('Aktifkan/Nonaktifkan [a/n] : ').lower()
        if xd in ['a','aktif','aktifkan','1']:
            stat = True
            self.execute(stat)
        elif xd in ['n','nonaktif','nonaktifkan','2']:
            stat = False
            self.execute(stat)
        else:
            print('Isi Yg Benar!')
    def execute(self,stat):
        try:
            req = bs(self.xyz.get(f'https://www.facebook.com/{self.id}',headers=self.headget,cookies=self.cookie,allow_redirects=True).content,'html.parser')
            haste = re.search('"haste_session":"(.*?)",',str(req)).group(1)
            rev = re.search('{"rev":(.*?)}',str(req)).group(1)
            hsi = re.search('"hsi":"(.*?)",',str(req)).group(1)
            dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',str(req)).group(1)
            jazoest = re.search('&jazoest=(.*?)",',str(req)).group(1)
            lsd = re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1)
            spinr = re.search('"__spin_r":(.*?),',str(req)).group(1)
            spint = re.search('"__spin_t":(.*?),',str(req)).group(1)
            var = {"enable":stat}
            data = {'av':self.id,'__user':self.id,'__a':'1','__hs':haste,'dpr':'1.5','__ccg':'EXCELLENT','__rev':rev,'__hsi':hsi,'__comet_req':'15','fb_dtsg': dtsg,'jazoest': jazoest,'lsd': lsd,'__spin_b':'trunk','__spin_r':spinr,'__spin_t':spint,'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'WemPrivateSharingMutation','variables':json.dumps(var),'server_timestamps':'true','doc_id':'5507005232662559'}
            headpos = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,image/jpeg,image/jpg,image/png,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Origin':'https://www.facebook.com','Referer':'https://www.facebook.com/','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','X-Fb-Friendly-Name':'WemPrivateSharingMutation','X-Fb-Lsd':lsd}
            pos = self.xyz.post('https://www.facebook.com/api/graphql/',data=data,headers=headpos,cookies=self.cookie,allow_redirects=True).json()
            if str(pos['data']['toggle_wem_private_sharing_control_enabled']) == 'None': print('Fitur Locked Profile Tidak Tersedia!')
            elif str(pos['data']['toggle_wem_private_sharing_control_enabled']['private_sharing_enabled']) == 'True': print('\n%sBerhasil Mengaktifkan Fitur Locked Profile!%s'%(H,P))
            elif str(pos['data']['toggle_wem_private_sharing_control_enabled']['private_sharing_enabled']) == 'False': print('\n%sBerhasil Menonaktifkan Fitur Locked Profile!%s'%(H,P))
            else: print(pos)
        except Exception as e:
            print(e)

#--> Trigger
if __name__ == '__main__':
    clear()
    start()
    login()
    finish()