# Python 3.10
# Made With Mobile, Web, And GraphQL Facebook

#--> Author's Info
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = 'Wa.me/6282245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'

#--> Import Default Module & Library
import os, sys, random, json, re, concurrent
from concurrent.futures import ThreadPoolExecutor

#--> Clear Terminal
def clear():
    if 'linux' in sys.platform.lower():os.system('clear')
    elif 'win' in sys.platform.lower():os.system('cls')

#--> Import Extra Module & Library
def mod():
    global requests, bs4, bs
    clear()
    try: import requests
    except Exception as e: os.system('pip install requests'); import requests
    try: import bs4
    except Exception as e: os.system('pip install bs4'); import bs4
    from bs4 import BeautifulSoup as bs
    clear()

#--> Dump ID From Facebook Group Or Page
class TimelineNoLogin():

    #--> Cara Pasang
    # Copy Seluruh Class TimelineNoLogin() Ini, Tempel Ke SCmu.
    # Cara Panggil :
    #     Tanpa Cookies, Cuma Bisa Dump Grup Publik    : TimelineNoLogin()
    #     Pakai Cookies, Bisa Dump Grup Publik/Private : TimelineNoLogin('CookiesAkunmuYgUdhJoinGrupnya')
    # Kamu Juga Bisa Ubah URL Grup (ID Grup)
    # Fungsi Ini Tidak Hanya Untuk Grup, Tapi Bisa Juga Untuk Page Facebook, Karena Yang Di Scrap Adalah Postingannya
    # Ubah Di Bagian url, Dalam def LandingTimeline(self), Kasih Input

    #--> Initialization
    def __init__(self,cookie=''):
        self.xyz = requests.Session()
        self.dump = 0
        self.result = []
        self.cookie = cookie
        self.ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        self.head = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Dpr':'1.125','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':self.ua,'Viewport-Width':'924'}
        self.LandingTimeline()

    #--> Dump From Facebook Group
    def LandingTimeline(self):
        print('[ Dump ID Dari Timeline ]')
        print('[1] Grup\n[2] Page')
        x = input('Pilih : ')
        print('')
        if   x in ['1','01','a']:
            typ = 'Grup'
            idt = input('Masukkan ID Grup : ')
            url = f'https://www.facebook.com/groups/{idt}' #--> 175107520598383
        elif x in ['2','02','b']:
            typ = 'Page'
            idt = input('Masukkan ID Page : ')
            url = f'https://www.facebook.com/{idt}' #--> 100069058853738
        else:
            print('Isi Yang Benar!')
            exit()
        self.data_post, self.data_scrap = self.ScrapData(url,typ)
        print('Nama %s : %s'%(typ,self.data_scrap['name']))
        self.lim = int(input('Berapa ID : '))
        print('')
        self.ScrapOverall(type=typ)

    #--> Scrap Data
    def ScrapData(self,url,type):
        try:
            req = bs(self.xyz.get(url,headers=self.head,cookies={'cookie':self.cookie},allow_redirects=True).content,'html.parser')
            data_post = {'av':re.search('__user=(.*?)&',str(req)).group(1),'__user':re.search('__user=(.*?)&',str(req)).group(1),'__a':re.search('__a=(.*?)&',str(req)).group(1),'__req':random.choice(['a','1','2','3','4','5']),'__hs':re.search('"haste_session":"(.*?)"',str(req)).group(1),'dpr':re.search('"pr":(.*?),',str(req)).group(1),'__ccg':random.choice(['EXCELLENT','GOOD']),'__rev':re.search('{"rev":(.*?)}',str(req)).group(1),'__hsi':re.search('"hsi":"(.*?)"',str(req)).group(1),'__comet_req':re.search('__comet_req=(.*?)&',str(req)).group(1),'lsd':re.search('"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1),'jazoest':re.search('&jazoest=(.*?)"',str(req)).group(1),'__spin_r':re.search('"__spin_r":(.*?),',str(req)).group(1),'__spin_b':re.search('"__spin_b":"(.*?)"',str(req)).group(1),'__spin_t':re.search('"__spin_t":(.*?),',str(req)).group(1),'fb_api_caller_class':'RelayModern','server_timestamps':True}
            if type == 'Grup':
                data_scrap = {'id':re.search('"groupID":"(.*?)"',str(req)).group(1),'name':re.search('"meta":{"title":"(.*?)"',str(req)).group(1),'username':re.search('"idorvanity":"(.*?)"',str(req)).group(1),'f_location':re.search('"feedLocation":"(.*?)"',str(req)).group(1),'f_type':re.search('"feedType":"(.*?)"',str(req)).group(1)}
            elif type == 'Page':
                data_scrap = {'id':re.search('"userID":"(.*?)"',str(req)).group(1),'name':re.search('"meta":{"title":"(.*?)"',str(req)).group(1)}
            return(data_post,data_scrap)
        except Exception as e:
            print('ID Not Found or Something Went Wrong')
            exit()

    #--> Get Overall Info
    def ScrapOverall(self,type,cursor=None):
        if type == 'Grup':
            dtp, dtg = self.data_post.copy(), self.data_scrap.copy()
            var = {"UFI2CommentsProvider_commentsKey":"CometGroupDiscussionRootSuccessQuery","count":3,"cursor":cursor,"id":dtg['id'],"feedLocation":dtg['f_location'],"feedType":dtg['f_type'],"renderLocation":"group","stream_initial_count":1,"feedbackSource":0,"focusCommentID":None,"scale":1.5,"sortingSetting":None,"useDefaultActor":False,"privacySelectorRenderLocation":"COMET_STREAM","__relay_internal__pv__IsWorkUserrelayprovider":False,"__relay_internal__pv__IsMergQAPollsrelayprovider":False,"__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider":False,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":False,"__relay_internal__pv__StoriesRingrelayprovider":False,"displayCommentsContextEnableComment":None,"displayCommentsContextIsAdPreview":None,"displayCommentsContextIsAggregatedShare":None,"displayCommentsContextIsStorySet":None,"displayCommentsFeedbackContext":None,}
            dtp.update({'fb_api_req_friendly_name':'GroupsCometFeedRegularStoriesPaginationQuery','variables':json.dumps(var),'doc_id':'6617440634998224'})
        elif type == 'Page':
            dtp, dtg = self.data_post.copy(), self.data_scrap.copy()
            var = {"UFI2CommentsProvider_commentsKey":"ProfileCometTimelineRoute","afterTime":None,"beforeTime":None,"count":3,"cursor":cursor,"displayCommentsContextEnableComment":None,"displayCommentsContextIsAdPreview":None,"displayCommentsContextIsAggregatedShare":None,"displayCommentsContextIsStorySet":None,"displayCommentsFeedbackContext":None,"feedLocation":"TIMELINE","feedbackSource":0,"focusCommentID":None,"memorializedSplitTimeFilter":None,"omitPinnedPost":True,"postedBy":None,"privacy":None,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"timeline","scale":1.5,"stream_count":1,"taggedInOnly":None,"useDefaultActor":False,"id":dtg['id'],"__relay_internal__pv__IsWorkUserrelayprovider":False,"__relay_internal__pv__IsMergQAPollsrelayprovider":False,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":False,"__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider":False,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":False,"__relay_internal__pv__StoriesRingrelayprovider":False}
            dtp.update({'fb_api_req_friendly_name':'ProfileCometTimelineFeedRefetchQuery','variables':json.dumps(var),'doc_id':'5689925947799218'})

        try:

            pos = self.xyz.post('https://www.facebook.com/api/graphql/',data=dtp,cookies={'cookie':self.cookie}).text
            feedback = list(set(re.findall('"feedback":{"id":"(.*?)"',str(pos))))

            #--> Submit To Post
            with ThreadPoolExecutor(max_workers=30) as TPE:
                for x in list(set(re.findall(r'"__typename":"User","name":"(.*?)","id":"(.*?)"',str(pos)))):
                    if self.dump >= self.lim: break
                    else:
                        if 'short_name' in str(x): pass
                        else: TPE.submit(self.ScrapPost,list(x))

            #--> Submit To Comment
            with ThreadPoolExecutor(max_workers=30) as TPE:
                for fbid in feedback:
                    if self.dump >= self.lim: break
                    else: TPE.submit(self.ScrapComment,fbid)

            #--> Submit To React
            with ThreadPoolExecutor(max_workers=30) as TPE:
                for fbid in feedback:
                    if self.dump >= self.lim: break
                    else: TPE.submit(self.ScrapReact,fbid)

            #--> Loop
            if self.dump >= self.lim: pass
            else:
                try: self.ScrapOverall(type,re.search('"end_cursor":"(.*?)"',str(pos)).group(1))
                except Exception as e: pass
        
        except Exception as e: pass

    #--> Get ID From Who Posted In Group
    def ScrapPost(self,dat):
        try:
            ray = {'id':self.ConvertID(dat[-1]),'name':dat[0]}
            if 'pfbid' in ray['id']: pass
            else:
                if ray in self.result: pass
                else:
                    self.result.append(ray)
                    print('%s|%s'%(ray['id'],ray['name']))
                    # open('namafile.txt','a+').write('%s|%s\n'%(ray['id'],ray['name']))
                    self.dump += 1
        except Exception as e: pass

    #--> Get ID From Who Commented On Each Post In Group
    def ScrapComment(self,fbid):
        try:
            dtp = self.data_post.copy()
            dtp.update({'fb_api_req_friendly_name':'CometUFICommentsCountTooltipContentQuery','variables':json.dumps({"feedbackTargetID":fbid}),'doc_id':'6381324631954417'})
            pos = self.xyz.post('https://www.facebook.com/api/graphql/',data=dtp,cookies={'cookie':self.cookie}).json()
            for p in pos['data']['feedback']['commenters']['edges']:
                try:
                    ray = {'id':self.ConvertID(p['node']['id']),'name':p['node']['name']}
                    if 'pfbid' in ray['id']: pass
                    else:
                        if ray in self.result: pass
                        else:
                            self.result.append(ray)
                            print('%s|%s'%(ray['id'],ray['name']))
                            # open('namafile.txt','a+').write('%s|%s\n'%(ray['id'],ray['name']))
                            self.dump += 1
                except Exception as e: pass
        except Exception as e: pass

    #--> Get ID From Who Reacted On Each Post In Group
    def ScrapReact(self,fbid):
        for react in ["1635855486666999","1678524932434102","115940658764963","478547315650144","908563459236466","444813342392137","613557422527858"]:
            try:
                dtp = self.data_post.copy()
                dtp.update({'fb_api_req_friendly_name':'CometUFIReactionIconTooltipContentQuery','variables':json.dumps({"feedbackTargetID":fbid,"reactionID":react}),'doc_id':'6235145276554312'})
                pos = self.xyz.post('https://www.facebook.com/api/graphql/',data=dtp,cookies={'cookie':self.cookie}).json()
                for p in pos['data']['feedback']['reactors']['nodes']:
                    try:
                        ray = {'id':self.ConvertID(p['id']),'name':p['name']}
                        if 'pfbid' in ray['id']: pass
                        else:
                            if ray in self.result: pass
                            else:
                                self.result.append(ray)
                                print('%s|%s'%(ray['id'],ray['name']))
                                # open('namafile.txt','a+').write('%s|%s\n'%(ray['id'],ray['name']))
                                self.dump += 1
                    except Exception as e: pass
            except Exception as e: pass

    #--> Convert PFBID To ID
    def ConvertID(self,id):
        try:
            r = requests.Session()
            q = r.get(f'https://web.facebook.com/{id}',headers=self.head,allow_redirects=True).text
            return(re.search('"userID":"(.*?)"',str(q)).group(1))
        except Exception as e: return(id)

#--> Dump ID By Search Name
class SearchName():

    #--> Cara Pasang
    # Copy Seluruh Class SearchName() Ini, Tempel Ke SCmu.
    # Cara Panggil :
    #     SearchName()
    # Fungsi Ini Generate Nama Secara Otomatis Dari Web Ninjaname.net

    #--> Initialization
    def __init__(self):
        self.xyz = requests.Session()
        self.result = []
        self.dump = 0
        self.ua = 'Mozilla/5.0 (Linux; Android 11; vivo 1918 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.0000.00 Mobile Safari/537.36'
        self.hdg = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Dpr':'1.125','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':"",'Sec-Ch-Ua-Full-Version-List':"",'Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Model':"",'Sec-Ch-Ua-Platform':"",'Sec-Ch-Ua-Platform-Version':"",'Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':self.ua}
        self.hdp = {'Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Dpr':'1.25','Origin':'https://m.facebook.com','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':"",'Sec-Ch-Ua-Full-Version-List':"",'Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Model':"",'Sec-Ch-Ua-Platform':"",'Sec-Ch-Ua-Platform-Version':"",'Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent':self.ua,'X-Requested-With':'XMLHttpRequest','X-Response-Format':'JSONStream'}
        self.lim = int(input('Berapa ID : '))
        print('')
        self.GetName()
    
    #--> Get Name From Ninjaname.net
    def GetName(self):
        self.daftar_nama = []
        url = 'http://ninjaname.net/indonesian_name.php' #--> You Can Change With Other Country (Check At http://ninjaname.net)
        try:
            pos = bs(self.xyz.post(url,data={'number_generate':'50','gender_type':random.choice(['male','female']),'submit':'Generate'}).content,'html.parser')
            xd = re.findall('• (.*?)<br',str(pos))
            for nm in xd:
                self.GenerateRandomName(nm)
                self.daftar_nama.append(nm)
            with ThreadPoolExecutor(max_workers=30) as ABC:
                for nama in self.daftar_nama: ABC.submit(self.Scrap,nama.lower().replace(' ','+'))
        except Exception as e:
            print('\nSomething Went Wrong, Error At Ninjaname.net')
            exit()

    #--> Generate Random Name
    def GenerateRandomName(self,df):
        for tg in df.split(' '):
            if tg in self.daftar_nama: pass
            else: self.daftar_nama.append(tg)

    #--> Scrap
    def Scrap(self,nama):
        self.url = f'https://m.facebook.com/public/{nama}'
        try:
            req = bs(self.xyz.get(self.url,headers=self.hdg,allow_redirects=True).content,'html.parser')
            self.data_post = {'fb_dtsg':re.search('{"dtsg":{"token":"(.*?)",',str(req)).group(1),'lsd':re.search('"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1),'__user':re.search('"USER_ID":"(.*?)"',str(req)).group(1)}
            kid = list(set([str(url).split('=')[1] for url in re.findall('payload:{link:null,url:"(.*?)",',str(req))]))
            with ThreadPoolExecutor(max_workers=30) as TPE:
                for id in kid:
                    if self.dump >= self.lim: break
                    else: TPE.submit(self.GenerateID,id)
            try:
                if self.dump >= self.lim: pass
                else:
                    x,y,z = list(re.findall('cursor=(.*?)&pn=(.*?)&usid=(.*?)&tsid',str(req))[0])
                    next = {'cursor':x,'pn':y,'usid':z,'tsid':''}
                    self.Scroll(next)
            except Exception as e: pass
        except Exception as e: pass
    
    #--> Scroll
    def Scroll(self,next):
        dat = self.data_post.copy()
        dat.update(next)
        try:
            pos = bs(self.xyz.post(self.url,data=dat,headers=self.hdp,allow_redirects=True).content,'html.parser')
            kid = list(set([str(url).split('=')[1] for url in re.findall('payload:{link:null,url:"(.*?)",',str(pos))]))
            with ThreadPoolExecutor(max_workers=30) as TPE:
                for id in kid:
                    if self.dump >= self.lim: break
                    else: TPE.submit(self.GenerateID,id)
            try:
                if self.dump >= self.lim: pass
                else:
                    x,y,z = list(re.findall('cursor=(.*?)&pn=(.*?)&usid=(.*?)&tsid',str(pos))[0])
                    next = {'cursor':x,'pn':y,'usid':z,'tsid':''}
                    self.Scroll(next)
            except Exception as e: pass
        except Exception as e: pass
    
    #--> Generate ID
    def GenerateID(self,id):
        try:
            r = requests.Session()
            req = bs(r.get(f'https://m.facebook.com/p/{id}',headers=self.hdg,allow_redirects=True).content,'html.parser')
            nama = req.find('title').text.split(' | ')[0]
            if nama=='Content not found' or nama=='Log in to Facebook': pass
            else:
                ray = {'id':id,'name':nama}
                if ray in self.result: pass
                else:
                    self.result.append(ray)
                    print('%s|%s'%(ray['id'],ray['name']))
                    # open('namafile.txt','a+').write('%s|%s\n'%(ray['id'],ray['name']))
                    self.dump += 1
        except Exception as e: pass

#--> Dump ID By Random ID
class RandomID():

    #--> Cara Pasang
    # Copy Seluruh Class RandomID() Ini, Tempel Ke SCmu.
    # Cara Panggil :
    #     RandomID()

    #--> Initialization
    def __init__(self):
        print('Contoh Digit     : 10 atau 15')
        dig = int(input('Berapa Digit     : '))
        print('Contoh ID Awal   : 175004 atau 10009108507')
        dep = input('Masukkan ID Awal : ')
        print('')
        if len(str(dep)) >= dig:
            print('Digit Awal Tidak Boleh Melebihi Jumlah Digit!')
            exit()
        sis = dig - len(dep)
        awal = 10**(sis-1)
        akhir = 10**(sis)
        with ThreadPoolExecutor(max_workers=35) as TPE:
            for ls in range(awal,akhir):
                TPE.submit(self.Scrap,dep,ls)

    #--> User-Agent
    def UserAgent(self):
        ua = 'Mozilla/5.0 (Linux; Android 11; vivo 1918 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.0000.00 Mobile Safari/537.36'
        return(ua)

    #--> Scrap
    def Scrap(self,aw,ls):
        try:
            r = requests.Session()
            head = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Dpr':'1.125','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':self.UserAgent(),'Viewport-Width':'320'}
            id = '%s%s'%(aw,str(ls))
            url = 'https://m.facebook.com/profile.php?id=%s'%(id)
            req = r.get(url,headers=head)
            if 'next=' in str(req.url): pass
            else:
                nama = bs(req.content,'html.parser').find('title').text.split(' | ')[0]
                if nama=='Content not found' or nama=='Error Facebook' or re.search(r'\d',nama): pass
                else:
                    print('%s|%s'%(id,nama))
                    # open('namafile.txt','a+').write('%s|%s\n'%(id,nama))
        except Exception as e: pass

#--> Trigger
if __name__ == '__main__':
    mod()
    # TimelineNoLogin()
    # SearchName()
    # RandomID()

#--> Kalau Mau Test, Hapus # Dalam if __name__
#--> Kalau Mau Save File Hasil Dump, Hapus Aja # Di Bagian open(namafile). Terus Ganti Namafile Terserahmu