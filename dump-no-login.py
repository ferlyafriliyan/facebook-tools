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
class group_or_page():

    #--> Landing
    def __init__(self):
        self.xyz = requests.Session()
        self.result = []
        self.ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        self.head = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Dpr':'1.125','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':self.ua,'Viewport-Width':'924'}
        self.landing_group()

    #--> Dump From Facebook Group
    def landing_group(self):
        url = 'https://www.facebook.com/groups/175107520598383' #--> Change Facebook Group URL
        self.data_post, self.data_grup = self.scrap_data_group(url)
        self.scrap_overall()
    #--> Scrap Data Group For Query
    def scrap_data_group(self,url):
        req = bs(self.xyz.get(url,headers=self.head,allow_redirects=True).content,'html.parser')
        data_post = {'av':re.search('__user=(.*?)&',str(req)).group(1),'__user':re.search('__user=(.*?)&',str(req)).group(1),'__a':re.search('__a=(.*?)&',str(req)).group(1),'__req':random.choice(['a','1','2','3','4','5']),'__hs':re.search('"haste_session":"(.*?)"',str(req)).group(1),'dpr':re.search('"pr":(.*?),',str(req)).group(1),'__ccg':random.choice(['EXCELLENT','GOOD']),'__rev':re.search('{"rev":(.*?)}',str(req)).group(1),'__hsi':re.search('"hsi":"(.*?)"',str(req)).group(1),'__comet_req':re.search('__comet_req=(.*?)&',str(req)).group(1),'lsd':re.search('"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1),'jazoest':re.search('&jazoest=(.*?)"',str(req)).group(1),'__spin_r':re.search('"__spin_r":(.*?),',str(req)).group(1),'__spin_b':re.search('"__spin_b":"(.*?)"',str(req)).group(1),'__spin_t':re.search('"__spin_t":(.*?),',str(req)).group(1),'fb_api_caller_class':'RelayModern','server_timestamps':True}
        data_grup = {'id':re.search('"groupID":"(.*?)"',str(req)).group(1),'name':re.search('"meta":{"title":"(.*?)"',str(req)).group(1),'username':re.search('"idorvanity":"(.*?)"',str(req)).group(1),'f_location':re.search('"feedLocation":"(.*?)"',str(req)).group(1),'f_type':re.search('"feedType":"(.*?)"',str(req)).group(1)}
        return(data_post,data_grup)
    
    #--> Get Overall Info
    def scrap_overall(self,cursor=None):
        dtp, dtg = self.data_post.copy(), self.data_grup.copy()
        var = {"UFI2CommentsProvider_commentsKey":"CometGroupDiscussionRootSuccessQuery","count":3,"cursor":cursor,"id":dtg['id'],"feedLocation":dtg['f_location'],"feedType":dtg['f_type'],"renderLocation":"group","stream_initial_count":1,"feedbackSource":0,"focusCommentID":None,"scale":1.5,"sortingSetting":None,"useDefaultActor":False,"privacySelectorRenderLocation":"COMET_STREAM","__relay_internal__pv__IsWorkUserrelayprovider":False,"__relay_internal__pv__IsMergQAPollsrelayprovider":False,"__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider":False,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":False,"__relay_internal__pv__StoriesRingrelayprovider":False,"displayCommentsContextEnableComment":None,"displayCommentsContextIsAdPreview":None,"displayCommentsContextIsAggregatedShare":None,"displayCommentsContextIsStorySet":None,"displayCommentsFeedbackContext":None,}
        dtp.update({'fb_api_req_friendly_name':'GroupsCometFeedRegularStoriesPaginationQuery','variables':json.dumps(var),'doc_id':'6617440634998224'})
        pos = self.xyz.post('https://www.facebook.com/api/graphql/',data=dtp).text
        feedback = list(set(re.findall('"feedback":{"id":"(.*?)"',str(pos))))

        #--> Submit To Post
        with ThreadPoolExecutor(max_workers=30) as TPE:
            for x in list(set(re.findall(r'"__typename":"User","name":"(.*?)","id":"(.*?)"',str(pos)))):
                if 'short_name' in str(x): pass
                else: TPE.submit(self.scrap_post,list(x))

        #--> Submit To Comment
        with ThreadPoolExecutor(max_workers=30) as TPE:
            for fbid in feedback: TPE.submit(self.scrap_comment,fbid)

        #--> Submit To React
        with ThreadPoolExecutor(max_workers=30) as TPE:
            for fbid in feedback: TPE.submit(self.scrap_react,fbid)

        #--> Loop
        try: self.scrap_overall(re.search('"end_cursor":"(.*?)"',str(pos)).group(1))
        except Exception as e: pass

    #--> Get ID From Who Posted In Group
    def scrap_post(self,dat):
        ray = {'id':self.convert_id(dat[-1]),'name':dat[0]}
        if 'pfbid' in ray['id']: pass
        else:
            if ray in self.result: pass
            else: self.result.append(ray); print(ray)

    #--> Get ID From Who Commented On Each Post In Group
    def scrap_comment(self,fbid):
        dtp = self.data_post.copy()
        dtp.update({'fb_api_req_friendly_name':'CometUFICommentsCountTooltipContentQuery','variables':json.dumps({"feedbackTargetID":fbid}),'doc_id':'6381324631954417'})
        pos = self.xyz.post('https://www.facebook.com/api/graphql/',data=dtp).json()
        for p in pos['data']['feedback']['commenters']['edges']:
            ray = {'id':self.convert_id(p['node']['id']),'name':p['node']['name']}
            if 'pfbid' in ray['id']: pass
            else:
                if ray in self.result: pass
                else: self.result.append(ray); print(ray)

    #--> Get ID From Who Reacted On Each Post In Group
    def scrap_react(self,fbid):
        for react in ["1635855486666999","1678524932434102","115940658764963","478547315650144","908563459236466","444813342392137","613557422527858"]:
            dtp = self.data_post.copy()
            dtp.update({'fb_api_req_friendly_name':'CometUFIReactionIconTooltipContentQuery','variables':json.dumps({"feedbackTargetID":fbid,"reactionID":react}),'doc_id':'6235145276554312'})
            pos = self.xyz.post('https://www.facebook.com/api/graphql/',data=dtp).json()
            for p in pos['data']['feedback']['reactors']['nodes']:
                ray = {'id':self.convert_id(p['id']),'name':p['name']}
                if 'pfbid' in ray['id']: pass
                else:
                    if ray in self.result: pass
                    else: self.result.append(ray); print(ray)

    #--> Convert PFBID To ID
    def convert_id(self,id):
        try:
            r = requests.Session()
            q = r.get(f'https://web.facebook.com/{id}',headers=self.head,allow_redirects=True).text
            return(re.search('"userID":"(.*?)"',str(q)).group(1))
        except Exception as e: return(id)

class search_name():
    def __init__(self):
        self.xyz = requests.Session()
        self.result = []
        self.ua = 'Mozilla/5.0 (Linux; Android 11; vivo 1918 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.0000.00 Mobile Safari/537.36'
        self.hdg = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Dpr':'1.125','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':"",'Sec-Ch-Ua-Full-Version-List':"",'Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Model':"",'Sec-Ch-Ua-Platform':"",'Sec-Ch-Ua-Platform-Version':"",'Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':self.ua}
        self.hdp = {'Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Dpr':'1.25','Origin':'https://m.facebook.com','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':"",'Sec-Ch-Ua-Full-Version-List':"",'Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Model':"",'Sec-Ch-Ua-Platform':"",'Sec-Ch-Ua-Platform-Version':"",'Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent':self.ua,'X-Requested-With':'XMLHttpRequest','X-Response-Format':'JSONStream'}
        self.generate_name()
    def generate_name(self):
        url = 'http://ninjaname.net/indonesian_name.php' #--> You Can Change With Other Country (Check At http://ninjaname.net)
        pos = bs(self.xyz.post(url,data={'number_generate':'50','gender_type':random.choice(['male','female']),'submit':'Generate'}).content,'html.parser')
        xd = re.findall('• (.*?)<br',str(pos))
        with ThreadPoolExecutor(max_workers=30) as ABC:
            for nama in xd: ABC.submit(self.scrap_data_awal,nama.lower().replace(' ','+'))
    def scrap_data_awal(self,nama):
        self.url = f'https://m.facebook.com/public/{nama}'
        req = bs(self.xyz.get(self.url,headers=self.hdg,allow_redirects=True).content,'html.parser')
        self.data_post = {'fb_dtsg':re.search('{"dtsg":{"token":"(.*?)",',str(req)).group(1),'lsd':re.search('"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1),'__user':re.search('"USER_ID":"(.*?)"',str(req)).group(1)}
        kid = list(set([str(url).split('=')[1] for url in re.findall('payload:{link:null,url:"(.*?)",',str(req))]))
        with ThreadPoolExecutor(max_workers=30) as TPE:
            for id in kid: TPE.submit(self.generate,id)
        try:
            x,y,z = list(re.findall('cursor=(.*?)&pn=(.*?)&usid=(.*?)&tsid',str(req))[0])
            next = {'cursor':x,'pn':y,'usid':z,'tsid':''}
            self.scroll(next)
        except Exception as e: pass
    def scroll(self,next):
        dat = self.data_post.copy()
        dat.update(next)
        pos = bs(self.xyz.post(self.url,data=dat,headers=self.hdp,allow_redirects=True).content,'html.parser')
        kid = list(set([str(url).split('=')[1] for url in re.findall('payload:{link:null,url:"(.*?)",',str(pos))]))
        with ThreadPoolExecutor(max_workers=30) as TPE:
            for id in kid: TPE.submit(self.generate,id)
        try:
            x,y,z = list(re.findall('cursor=(.*?)&pn=(.*?)&usid=(.*?)&tsid',str(pos))[0])
            next = {'cursor':x,'pn':y,'usid':z,'tsid':''}
            self.scroll(next)
        except Exception as e: pass
    def generate(self,id):
        try:
            r = requests.Session()
            req = bs(r.get(f'https://m.facebook.com/p/{id}',headers=self.hdg,allow_redirects=True).content,'html.parser')
            nama = req.find('title').text.split(' | ')[0]
            if nama == 'Content not found': pass
            else:
                ray = {'id':id,'name':nama}
                if ray in self.result: pass
                else: self.result.append(ray); print(ray)
        except Exception as e: pass

#--> Trigger
if __name__ == '__main__':
    mod()
    #group_or_page()
    search_name()