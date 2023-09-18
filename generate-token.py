import os, sys, requests, re, bs4
from bs4 import BeautifulSoup as bs

M = "\x1b[38;5;196m" # Merah
J = "\x1b[38;5;208m" # Jingga
H = "\x1b[38;5;46m"  # Hijau
P = "\x1b[38;5;231m" # Putih

def clear():
    if "linux" in sys.platform.lower():
        try:os.system("clear")
        except:pass
    elif "win" in sys.platform.lower():
        try:os.system("cls")
        except:pass
    else:
        try:os.system("clear")
        except:pass

def input_cookie():
    print('%sApabila A2F On, Buka Link Dibawah, Lalu Masukkan Kode A2F'%(P))
    print('%shttps://business.facebook.com/business_locations\n'%(P))
    cookie = input('%sMasukkan Cookie : %s'%(P,J))
    pilih  = input('\n%sGeneral%s/%sSpecific %sToken [%sg%s/%ss%s] : '%(H,P,M,P,H,P,M,P)).lower()
    if pilih in ['1','01','g']: general_token(cookie)
    elif pilih in ['0','02','s']: specific_token(cookie)
    else: exit('\n%sIsi Yg Benar!%s'%(M,P))

def general_token(cookie):
    Token1 = generate_token_eaab(cookie); Perm1 = req_info_token(cookie,Token1) # Power Editor Token
    Token2 = generate_token_eaag(cookie); Perm2 = req_info_token(cookie,Token2) # Business Manager Token
    Token3 = generate_token_eaai(cookie); Perm3 = req_info_token(cookie,Token3) # Ads Management Token
    Token4 = generate_token_eaad(cookie); Perm4 = req_info_token(cookie,Token4) # Ads Event Manager Token
    Token5 = generate_token_eaaC(cookie); Perm5 = req_info_token(cookie,Token5) # Ads Block List Token
    Token6 = generate_token_eaae(cookie); Perm6 = req_info_token(cookie,Token6) # Account Quality Token
    Token7 = generate_token_eaaf(cookie); Perm7 = req_info_token(cookie,Token7) # Lift Study Creation Token
    Token8 = generate_token_eabb(cookie); Perm8 = req_info_token(cookie,Token8) # Hub Materi Iklan Token
    print('\n%s[ Power Editor Token ]\n%s%s\n%s[ Permissions ]\n%s%s%s'        %(P,J,Token1,P,H,Perm1,P))
    print('\n%s[ Business Manager Token ]\n%s%s\n%s[ Permissions ]\n%s%s%s'    %(P,J,Token2,P,H,Perm2,P))
    print('\n%s[ Ads Management Token ]\n%s%s\n%s[ Permissions ]\n%s%s%s'      %(P,J,Token3,P,H,Perm3,P))
    print('\n%s[ Ads Event Manager Token ]\n%s%s\n%s[ Permissions ]\n%s%s%s'   %(P,J,Token4,P,H,Perm4,P))
    print('\n%s[ Ads Block List Token ]\n%s%s\n%s[ Permissions ]\n%s%s%s'      %(P,J,Token5,P,H,Perm5,P))
    print('\n%s[ Account Quality Token ]\n%s%s\n%s[ Permissions ]\n%s%s%s'     %(P,J,Token6,P,H,Perm6,P))
    print('\n%s[ Lift Study Creation Token ]\n%s%s\n%s[ Permissions ]\n%s%s%s' %(P,J,Token7,P,H,Perm7,P))
    print('\n%s[ Hub Materi Iklan Token ]\n%s%s\n%s[ Permissions ]\n%s%s%s'    %(P,J,Token8,P,H,Perm8,P))

def req_info_token(cooki,token):
    try:
        cookie = {'cookie':cooki}
        url    = 'https://developers.facebook.com/tools/debug/accesstoken/?access_token=%s&version=v15.0'%(token)
        with requests.Session() as xyz:
            req = bs(xyz.get(url,cookies=cookie).content,'html.parser')
            crf = req.find('a',href='/docs/reference/login/#permissions')
            return(crf.text)
    except Exception as e:
        return('%sPermissions Not Available%s'%(M,P))

def generate_token_eaab(cok): # Power Editor Token
    try:
        cookie = {'cookie':cok}
        with requests.Session() as xyz:
            url = 'https://www.facebook.com/adsmanager/manage/campaigns'
            req = xyz.get(url,cookies=cookie)
            set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
            nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
            roq = xyz.get(nek,cookies=cookie)
            tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
            return(tok)
    except Exception as e:
        return('Cookies Invalid')

def generate_token_eaag(cok): # Business Manager Token
    try:
        cookie = {'cookie':cok}
        with requests.Session() as xyz:
            url = 'https://business.facebook.com/business_locations'
            req = xyz.get(url,cookies=cookie)
            tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
            return(tok)
    except Exception as e:
        return('Cookies Invalid')

def generate_token_eaai(cok): # Ads Management Token
    try:
        cookie = {'cookie':cok}
        with requests.Session() as xyz:
            url = 'https://www.facebook.com/ads/manager/billing_history/summary/'
            req = xyz.get(url,cookies=cookie)
            tok = re.search('{access_token:"(.*?)"',req.text).group(1)
            return(tok)
    except Exception as e:
        return('Cookies Invalid')

def generate_token_eaad(cok): # Ads Event Manager Token
    try:
        cookie = {'cookie':cok}
        with requests.Session() as xyz:
            url = 'https://www.facebook.com/events_manager2/overview'
            req = xyz.get(url,cookies=cookie)
            tok = re.search('{"accessToken":"(EAAd\w+)',req.text).group(1)
            return(tok)
    except Exception as e:
        return('Cookies Invalid')

def generate_token_eaaC(cok): # Ads Block List Token
    try:
        cookie = {'cookie':cok}
        with requests.Session() as xyz:
            url = 'https://www.facebook.com/brand_safety/controls'
            req = xyz.get(url,cookies=cookie)
            tok = re.search('{"accessToken":"(EAAC\w+)',req.text).group(1)
            return(tok)
    except Exception as e:
        return('Cookies Invalid')

def generate_token_eaae(cok): # Account Quality Token
    try:
        cookie = {'cookie':cok}
        with requests.Session() as xyz:
            url = 'https://www.facebook.com/accountquality/'
            req = xyz.get(url,cookies=cookie)
            tok = re.search('"accessToken":"(EAAE\w+)',req.text).group(1)
            return(tok)
    except Exception as e:
        return('Cookies Invalid')

def generate_token_eaaf(cok): # Lift Study Creation Token
    try:
        cookie = {'cookie':cok}
        with requests.Session() as xyz:
            url = 'https://www.facebook.com/test-and-learn/test'
            req = xyz.get(url,cookies=cookie)
            tok = re.search('{"accessToken":"(EAAF\w+)',req.text).group(1)
            return(tok)
    except Exception as e:
        return('Cookies Invalid')

def generate_token_eabb(cok): # Hub Materi Iklan Token
    try:
        cookie = {'cookie':cok}
        with requests.Session() as xyz:
            url = 'https://www.facebook.com/ads/adbuilder/home'
            req = xyz.get(url,cookies=cookie)
            tok = re.search('"accessToken":"(EABB\w+)',req.text).group(1)
            return(tok)
    except Exception as e:
        return('Cookies Invalid')

class specific_token:
    def __init__(self,cookie):
        self.xyz    = requests.Session()
        self.cookie = {'cookie':cookie}
        app_id      = [
            '1348564698517390|007c0a9101b9e1c8ffab727666805038', #--> Meta Portal
            '1174099472704185|0722a7d5b5a4ac06b11450f7114eb2e9', #--> Messenger Kids for iOS
            '155327495133707|a151725bc9b8808a800f4c891505e558' , #--> Facebook Watch for Oculus
            '1331685116912965|e334a1eca4d4ea9ac0c0132a31730663', #--> Facebook Watch for Xbox
            '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01' , #--> Facebook Watch for Amazon Fire TV
            '437340816620806|04a36c2558cde98e185d7f4f701e4d94' , #--> Facebook Watch for Android TV
            '661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e' , #--> Facebook Watch for Apple TV
            '1692575501067666|3168904bd42ebb12bf981327de99179f', #--> Facebook Watch for Samsung TV
            ]
        for x in app_id:
            self.get_kode(x)
    def get_kode(self,act):
        data = {
            'access_token': act,
            'scope': ''}
        req  = self.xyz.post('https://graph.facebook.com/v16.0/device/login/',data=data).json()
        try:
            cd, ucd = req['code'], req['user_code']
            url = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=%s'%(cd,act)
            self.verify1(ucd,act)
            self.get_token(url)
        except Exception as e:
            print('Login Gagal --> %s'%(act))
    def verify1(self,ucd,act):
        req = bs(self.xyz.get('https://mbasic.facebook.com/device',cookies=self.cookie).content,'html.parser')
        raq = req.find('form',{'method':'post'})
        dat = {
            'jazoest'   : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
            'fb_dtsg'   : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1),
            'qr'        : '0',
            'user_code' : ucd}
        rel = 'https://mbasic.facebook.com' + raq['action']
        pos = bs(self.xyz.post(rel,data=dat,cookies=self.cookie).content,'html.parser')
        self.verify2(pos,ucd,act)
    def verify2(self,req,ucd,act):
        dat = {}
        raq = req.find('form',{'method':'post'})
        for x in raq('input',{'value':True}):
            try:
                if x['name'] == '__CANCEL__' :
                    pass
                else:
                    dat.update({x['name']:x['value']})
            except Exception as e:
                pass
        rel = 'https://mbasic.facebook.com' + raq['action']
        pos = bs(self.xyz.post(rel,data=dat,cookies=self.cookie).content,'html.parser')
        if 'Sukses!' in str(pos):
            pass
        else:
            print('Login Gagal --> %s'%(act))
    def get_token(self,url):
        req = self.xyz.get(url,cookies=self.cookie).json()
        tok = req['access_token']
        self.req_info_token(tok)
    def req_info_token(self,tok):
        try:
            url = 'https://developers.facebook.com/tools/debug/accesstoken/?access_token=%s&version=v16.0'%(tok)
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            try: gtx = req.find_all('tr')[0].find_all('td')[1].text
            except Exception as e: gtx = 'App : Unknown'
            try: crf = req.find('a',href='/docs/reference/login/#permissions').text
            except Exception as e: crf = '%sPermissions Not Available%s'%(M,P)
            print('')
            print('%s[ %s ]%s'%(P,gtx,P))
            print('%s%s%s'%(J,tok,P))
            print('%s%s%s'%(H,crf,P))
        except Exception as e:
            pass

if __name__ == '__main__':
    clear()
    input_cookie()
    exit('')