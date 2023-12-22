#--> Import Module & Library
import os, sys, requests, bs4, re, json, time, random
from bs4 import BeautifulSoup as bs

#--> Global Variable
DefaultUAWindows = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
HeadersGet  = lambda i=DefaultUAWindows : {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Prefers-Color-Scheme':'light','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':i,'Viewport-Width':'924'}
HeadersPost = lambda i=DefaultUAWindows : {'Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Origin':'https://www.facebook.com','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent':i}

#--> Clear Terminal
def clear(): os.system('cls' if 'win' in sys.platform.lower() else 'clear')

#--> Convert ID/Username To URL
def ConvertURL(i):
    if 'http' in str(i):
        if 'www.facebook.com' in str(i): url = i
        elif 'm.facebook.com' in str(i): url = i.replace('m.facebook.com','www.facebook.com')
        elif 'mbasic.facebook.com' in str(i): url = i.replace('mbasic.facebook.com','www.facebook.com')
    else:
        if 'www.facebook.com' in str(i): url = 'https://' + i
        elif 'm.facebook.com' in str(i): url = 'https://' + i.replace('m.facebook.com','www.facebook.com')
        elif 'mbasic.facebook.com' in str(i): url = 'https://' + i.replace('mbasic.facebook.com','www.facebook.com')
        else:
            if 'facebook.com' in str(i): url = 'https://www.facebook.com' + i.replace('facebook.com','').replace('Facebook.com','')
            else: url = 'https://www.facebook.com/%s'%(i)
    return(url)

#--> Get General Payload For requests.post GraphQL
def GetData(req):
    av = re.search('"actorID":"(.*?)"',str(req)).group(1)
    __user = av
    __a = str(random.randrange(1,6))
    __hs = re.search('"haste_session":"(.*?)"',str(req)).group(1)
    __ccg = re.search('"connectionClass":"(.*?)"',str(req)).group(1)
    __rev = re.search('"__spin_r":(.*?),',str(req)).group(1)
    __spin_r = __rev
    __spin_b = re.search('"__spin_b":"(.*?)"',str(req)).group(1)
    __spin_t = re.search('"__spin_t":(.*?),',str(req)).group(1)
    __hsi = re.search('"hsi":"(.*?)"',str(req)).group(1)
    fb_dtsg = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(req)).group(1)
    jazoest = re.search('jazoest=(.*?)"',str(req)).group(1)
    lsd = re.search('"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1)
    Data = {'av':av,'__user':__user,'__a':__a,'__hs':__hs,'dpr':'1.5','__ccg':__ccg,'__rev':__rev,'__spin_r':__spin_r,'__spin_b':__spin_b,'__spin_t':__spin_t,'__hsi':__hsi,'__comet_req':'15','fb_dtsg':fb_dtsg,'jazoest':jazoest,'lsd':lsd}
    return(Data)

#--> Login Class
class Login():

    #--> Initialization
    def __init__(self):
        try: os.mkdir('login')
        except Exception as e: pass
        try: os.mkdir('dump')
        except Exception as e: pass
        self.CheckCookies()
        Menu()

    #--> Re-Login
    def ReLog(self):
        self.cookie = input('Masukkan Cookies : ')
        open('login/cookie.json','w').write(self.cookie)
        self.CheckCookies()

    #--> Check Cookie ( Valid / Invalid )
    def CheckCookies(self):
        try:
            self.cookie = open('login/cookie.json','r').read()
            self.ChangeLanguage()
            self.Scrap()
        except Exception as e:
            print('Cookies Invalid!')
            time.sleep(3)
            clear()
            self.ReLog()

    #--> Scrap ID & Name To Validate Cookie
    def Scrap(self):
        r = requests.Session()
        req = r.get('https://www.facebook.com/profile.php', headers=HeadersGet(), cookies={'cookie':self.cookie}, allow_redirects=True).text
        id = re.search('"actorID":"(.*?)"',str(req)).group(1)
        nm = re.search('"NAME":"(.*?)"',str(req)).group(1)
        clear()
        print('Login Sebagai %s\n'%(nm))

    #--> Change Language Cookie
    def ChangeLanguage(self):
        r = requests.Session()
        req = r.get('https://www.facebook.com/profile.php', headers=HeadersGet(), cookies={'cookie':self.cookie}, allow_redirects=True).text
        Data = GetData(req)
        Data.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'useCometLocaleSelectorLanguageChangeMutation','variables': json.dumps({"locale":"id_ID","referrer":"WWW_COMET_ACCOUNT_SETTINGS","fallback_locale":None}),'server_timestamps':True,'doc_id':'6451777188273168'})
        r.post('https://www.facebook.com/api/graphql/', data=Data, headers=HeadersPost(), cookies={'cookie':self.cookie}).json()

#--> Menu Class
class Menu():

    #--> Initialization
    def __init__(self):
        self.MainChoose()

    #--> Main Menu
    def MainChoose(self):
        print('[ Dump Menu ]')
        print('[1] From Profile')
        print('[2] From Group')
        # print('[3] From Page')
        # print('[4] From Post')
        # print('[5] From Timeline')
        # print('[6] By Search')
        # print('[0] Logout')
        try: x = int(input('Pilih : '))
        except Exception as e: exit('\nIsi Yang Benar!\n')
        print('')
        if   x == 1: self.ControlDumpProfile()
        elif x == 2: self.ControlDumpGroup()
        # elif x == 3: pass # self.ControlDumpPage()
        # elif x == 4: pass # self.ControlDumpPage()
        # elif x == 5: pass # self.ControlDumpTimeline()
        # elif x == 6: pass # self.ControlDumpSearch()
        # elif x == 0: pass # Logout()
        else: exit('\nIsi Yang Benar!\n')

    #--> Dump Profile Menu
    def ControlDumpProfile(self):
        DP = DumpProfile()
        print('[ Dump From Profile ]')
        print('[1] Friendlist')
        print('[2] Followers')
        # print('[3] Interact')
        try: x = int(input('Pilih : '))
        except Exception as e: exit('\nIsi Yang Benar!\n')
        print('')
        if   x == 1: DP.SortTarget(1)
        elif x == 2: DP.SortTarget(2)
        # elif x == 3: DP.SortTarget(3)
        else: exit('\nIsi Yang Benar!\n')

    #--> Dump Group Menu
    def ControlDumpGroup(self):
        DG = DumpGroup()
        print('[ Dump From Group ]')
        print('[1] Members')
        print('[2] Post')
        try: x = int(input('Pilih : '))
        except Exception as e: exit('\nIsi Yang Benar!\n')
        print('')
        if   x == 1: DG.SortTarget(1)
        elif x == 2: DG.SortTarget(2)
        else: exit('\nIsi Yang Benar!\n')

#--> Dump ID From Profile Class
class DumpProfile():

    #--> Initialization
    def __init__(self):
        self.resultdump = []
        self.cookie = open('login/cookie.json','r').read()

    #--> Check Target Profile ( Exist / Not Exist )
    def CheckProfile(self, url):
        r = requests.Session()
        try:
            req = r.get(url, headers=HeadersGet(), cookies={'cookie':self.cookie}, allow_redirects=True).text
            self.id = re.search('"userID":"(.*?)"',str(req)).group(1)
            self.nm = re.search('"profile_owner":{"id":"%s","name":"(.*?)"'%(self.id),str(req)).group(1)
            print('ID   : %s'%(str(self.id)))
            print('Name : %s'%(str(self.nm)))
            return(1)
        except Exception as e:
            print('Profile With URL %s Not Found!\n'%(url))
            return(0)

    #--> Function Caller (1,2,3)
    def SortTarget(self,type):
        print('Banyak ID/URL, Pisahkan Dengan Koma (,)')
        tgt = [ConvertURL(tg) for tg in input('Target : ').split(',')]
        print('Tekan ctrl+c Untuk Skip/Berhenti')
        print('')
        for url in tgt:
            if self.CheckProfile(url):
                if   type == 1: self.DumpFriendlist(url)
                elif type == 2: self.DumpFollowers(url)
                elif type == 3: self.DumpInteract(url)
            else: continue

    #--> Dump Friendlist
    def DumpFriendlist(self, url):
        try:
            r = requests.Session()
            req = r.get(url, headers=HeadersGet(), cookies={'cookie':self.cookie}, allow_redirects=True).text
            Data = GetData(req)
            flid = re.search('{"tab_key":"friends_all","id":"(.*?)"}',str(req)).group(1)
            Data.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'ProfileCometAppCollectionListRendererPaginationQuery','server_timestamps':True,'doc_id':'6709724792472394'})
            self.loop = 0
            self.file = 'dump/%sfriend.txt'%(self.id)
            open(self.file,'w').write('')
            self.LoopDumpFriendlist(r, Data, url, None, flid)
            if self.loop == 0: print('\rFailed To Dump ID!\n')
            else:
                print('\rSuccess Dump %s ID'%(str(self.loop)))
                print('File Saved At %s\n'%(self.file))
        except Exception as e:
            print('Error, Something Went Wrong!\n')
    def LoopDumpFriendlist(self, r, Data, url, cursor, flid):
        try:
            Data.update({'variables':json.dumps({"count":8,"cursor":cursor,"scale":1.5,"search":None,"id":flid})})
            pos = r.post('https://www.facebook.com/api/graphql/', data=Data, headers=HeadersPost(), cookies={'cookie':self.cookie}).json()
            for x in pos['data']['node']['pageItems']['edges']:
                try:
                    id = x['node']['actions_renderer']['action']['client_handler']['profile_action']['restrictable_profile_owner']['id']
                    nm = x['node']['actions_renderer']['action']['client_handler']['profile_action']['restrictable_profile_owner']['name']
                    fm = '%s|%s'%(str(id),str(nm))
                    if fm in self.resultdump: pass
                    else:
                        self.resultdump.append(fm)
                        open(self.file,'a+').write('%s\n'%(fm))
                        self.loop += 1
                        print('\rDump %s ID'%(str(self.loop)),end=''); sys.stdout.flush()
                except Exception as e: pass
            if pos['data']['node']['pageItems']['page_info']['has_next_page']:
                curs = pos['data']['node']['pageItems']['page_info']['end_cursor']
                self.LoopDumpFriendlist(r, Data, url, curs, flid)
        except KeyboardInterrupt: pass
        except Exception as e: pass

    #--> Dump Followers
    def DumpFollowers(self, url):
        try:
            r = requests.Session()
            req = r.get(url, headers=HeadersGet(), cookies={'cookie':self.cookie}, allow_redirects=True).text
            Data = GetData(req)
            flid = re.search('{"tab_key":"followers","id":"(.*?)"}',str(req)).group(1)
            Data.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'ProfileCometAppCollectionListRendererPaginationQuery','server_timestamps':True,'doc_id':'6709724792472394'})
            self.loop = 0
            self.file = 'dump/%sfolls.txt'%(self.id)
            open(self.file,'w').write('')
            self.LoopDumpFollowers(r, Data, url, None, flid)
            if self.loop == 0: print('\rFailed To Dump ID!\n')
            else:
                print('\rSuccess Dump %s ID'%(str(self.loop)))
                print('File Saved At %s\n'%(self.file))
        except Exception as e:
            print('Error, Something Went Wrong!\n')
    def LoopDumpFollowers(self, r, Data, url, cursor, flid):
        try:
            Data.update({'variables':json.dumps({"count":8,"cursor":cursor,"scale":1.5,"search":None,"id":flid})})
            pos = r.post('https://www.facebook.com/api/graphql/', data=Data, headers=HeadersPost(), cookies={'cookie':self.cookie}).json()
            for x in pos['data']['node']['pageItems']['edges']:
                try:
                    id = x['node']['actions_renderer']['profile_actions'][0]['client_handler']['profile_action']['restrictable_profile_owner']['id']
                    nm = x['node']['actions_renderer']['profile_actions'][0]['client_handler']['profile_action']['restrictable_profile_owner']['name']
                    fm = '%s|%s'%(str(id),str(nm))
                    if fm in self.resultdump: pass
                    else:
                        self.resultdump.append(fm)
                        open(self.file,'a+').write('%s\n'%(fm))
                        self.loop += 1
                        print('\rDump %s ID'%(str(self.loop)),end=''); sys.stdout.flush()
                except Exception as e: pass
            if pos['data']['node']['pageItems']['page_info']['has_next_page']:
                curs = pos['data']['node']['pageItems']['page_info']['end_cursor']
                self.LoopDumpFollowers(r, Data, url, curs, flid)
        except KeyboardInterrupt: pass
        except Exception as e: pass

#--> Dump ID From Group Class
class DumpGroup():

    #--> Initialization
    def __init__(self):
        self.resultdump = []
        self.cookie = open('login/cookie.json','r').read()

    #--> Check Target Group ( Exist / Not Exist )
    def CheckGroup(self,url):
        r = requests.Session()
        try:
            req = r.get(url, headers=HeadersGet(), cookies={'cookie':self.cookie}, allow_redirects=True).text
            self.id = re.search('"groupID":"(.*?)"',str(req)).group(1)
            nm = re.search('"__isProfile":"Group","name":"(.*?)"',str(req)).group(1)
            ty = re.search('"text":"Grup (.*?)"}},"group_member_profiles"',str(req)).group(1)
            st = re.search('"viewer_join_state":"(.*?)"',str(req)).group(1)
            if st == 'CAN_REQUEST' or st == 'CAN_JOIN': su = 'Belum Bergabung'
            elif st == 'MEMBER': su = 'Sudah Bergabung'
            else: su = 'Error'
            print('ID   : %s'%(str(self.id)))
            print('Name : %s'%(str(nm)))
            print('Type : %s'%(str(ty)))
            print('Stat : %s'%(str(su)))
            if ty == 'Privat' and su == 'Belum Bergabung':
                print('Harus Bergabung Terlebih Dahulu!\n')
                return(0)
            else: return(1)
        except Exception as e:
            print('Group With URL %s Not Found!\n'%(url))
            return(0)

    #--> Function Caller (1,2,3)
    def SortTarget(self,type):
        print('Banyak ID/URL, Pisahkan Dengan Koma (,)')
        tgt = [ConvertURL(tg) for tg in input('Target : ').split(',')]
        print('Tekan ctrl+c Untuk Skip/Berhenti')
        print('')
        for url in tgt:
            if self.CheckGroup(url):
                if   type == 1: self.DumpMember(url)
                elif type == 2: self.DumpPost(url)
            else: continue

    #--> Dump Group Members
    def DumpMember(self,url):
        try:
            r = requests.Session()
            req = r.get(url, headers=HeadersGet(), cookies={'cookie':self.cookie}, allow_redirects=True).text
            Data = GetData(req)
            groupid = re.search('"groupID":"(.*?)"',str(req)).group(1)
            Data.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'GroupsCometMembersPageNewMembersSectionRefetchQuery','server_timestamps':True,'doc_id':'6621621524622624'})
            self.loop = 0
            self.file = 'dump/%smember.txt'%(self.id)
            open(self.file,'w').write('')
            self.LoopDumpMember(r, Data, url, None, groupid)
            if self.loop == 0: print('\rFailed To Dump ID!\n')
            else:
                print('\rSuccess Dump %s ID'%(str(self.loop)))
                print('File Saved At %s\n'%(self.file))
        except Exception as e:
            print('Error, Something Went Wrong!\n')
    def LoopDumpMember(self, r, Data, url, cursor, groupid):
        try:
            Data.update({'variables':json.dumps({"count":10,"cursor":cursor,"groupID":groupid,"recruitingGroupFilterNonCompliant":False,"scale":1.5,"id":groupid})})
            pos = r.post('https://www.facebook.com/api/graphql/', data=Data, headers=HeadersPost(), cookies={'cookie':self.cookie}).json()
            for x in pos['data']['node']['new_members']['edges']:
                try:
                    id = x['node']['id']
                    nm = x['node']['name']
                    fm = '%s|%s'%(str(id),str(nm))
                    if fm in self.resultdump: pass
                    else:
                        self.resultdump.append(fm)
                        open(self.file,'a+').write('%s\n'%(fm))
                        self.loop += 1
                        print('\rDump %s ID'%(str(self.loop)),end=''); sys.stdout.flush()
                except Exception as e: pass
            if pos['data']['node']['new_members']['page_info']['has_next_page']:
                curs = pos['data']['node']['new_members']['page_info']['end_cursor']
                self.LoopDumpMember(r, Data, url, curs, groupid)
        except KeyboardInterrupt: pass
        except Exception as e: pass

    #--> Dump Post, React
    def DumpPost(self,url):
        try:
            r = requests.Session()
            req = r.get(url, headers=HeadersGet(), cookies={'cookie':self.cookie}, allow_redirects=True).text
            Data = GetData(req)
            groupid = re.search('"groupID":"(.*?)"',str(req)).group(1)
            self.loop = 0
            self.file = 'dump/%spost.txt'%(self.id)
            open(self.file,'w').write('')
            self.LoopDumpPost(r, Data, url, None, groupid)
            if self.loop == 0: print('\rFailed To Dump ID!\n')
            else:
                print('\rSuccess Dump %s ID'%(str(self.loop)))
                print('File Saved At %s\n'%(self.file))
        except Exception as e:
            print('Error, Something Went Wrong!\n')
    def LoopDumpPost(self, r, Data, url, cursor, groupid):
        try:
            Var = {"UFI2CommentsProvider_commentsKey":"CometGroupDiscussionRootSuccessQuery","count":3,"cursor":cursor,"displayCommentsContextEnableComment":None,"displayCommentsContextIsAdPreview":None,"displayCommentsContextIsAggregatedShare":None,"displayCommentsContextIsStorySet":None,"displayCommentsFeedbackContext":None,"feedLocation":"GROUP","feedType":"DISCUSSION","feedbackSource":0,"focusCommentID":None,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"group","scale":1.5,"sortingSetting":None,"stream_initial_count":1,"useDefaultActor":False,"id":groupid,"__relay_internal__pv__IsWorkUserrelayprovider":False,"__relay_internal__pv__IsMergQAPollsrelayprovider":False,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":False,"__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider":False,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":False,"__relay_internal__pv__StoriesRingrelayprovider":False}
            Data.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'GroupsCometFeedRegularStoriesPaginationQuery','server_timestamps':True,'doc_id':'6700031716789984','variables':json.dumps(Var)})
            pos = r.post('https://www.facebook.com/api/graphql/', data=Data, headers=HeadersPost(), cookies={'cookie':self.cookie}).text
            try:
                sem = []
                x = ['%s|%s'%(str(list(i)[0]),str(list(i)[1])) for i in re.findall('"author":{"__typename":"User","id":"(.*?)","name":"(.*?)"',str(pos))]
                for j in x:
                    if j in sem: pass
                    else: sem.append(j)
                for fm in sem:
                    if fm in self.resultdump: pass
                    else:
                        self.resultdump.append(fm)
                        open(self.file,'a+').write('%s\n'%(fm))
                        self.loop += 1
                        print('\rDump %s ID'%(str(self.loop)),end=''); sys.stdout.flush()
            except Exception as e: pass
            try:
                fdb = re.findall('"story":{"feedback":{"id":"(.*?)"}',str(pos))
                for idp in fdb:
                    try: self.LoopDumpReactPost(r, Data, url, None, idp)
                    except KeyboardInterrupt: pass
            except Exception as e: pass
            if bool(re.search('"has_next_page":(.*?)}',str(pos)).group(1)):
                curs = re.search('"end_cursor":"(.*?)",',str(pos)).group(1)
                self.LoopDumpPost(r, Data, url, curs, groupid)
        except KeyboardInterrupt: pass
        except Exception as e: pass
    def LoopDumpReactPost(self, r, Data, url, cursor, idp):
        try:
            Data.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometUFIReactionsDialogQuery','variables':json.dumps({"count":10,"cursor":cursor,"feedbackTargetID":idp,"reactionID":None,"scale":1.5,"id":idp}),'server_timestamps':True,'doc_id':'24094105923567748'})
            pos = r.post('https://www.facebook.com/api/graphql/', data=Data, headers=HeadersPost(), cookies={'cookie':self.cookie}).json()
            for x in pos['data']['node']['reactors']['edges']:
                try:
                    id = x['node']['id']
                    nm = x['node']['name']
                    fm = '%s|%s'%(str(id),str(nm))
                    if fm in self.resultdump: pass
                    else:
                        self.resultdump.append(fm)
                        open(self.file,'a+').write('%s\n'%(fm))
                        self.loop += 1
                        print('\rDump %s ID'%(str(self.loop)),end=''); sys.stdout.flush()
                except Exception as e: pass
            if pos['data']['node']['reactors']['page_info']['has_next_page']:
                curs = pos['data']['node']['reactors']['page_info']['end_cursor']
                self.LoopDumpReactPost(r, Data, url, curs, idp)
        except KeyboardInterrupt: pass
        except Exception as e: pass

#--> Trigger
if __name__ == '__main__':
    clear()
    Login()

#--> Test
# Friendlist : 100038807226660,100063475212440
# Followers  : 100001617352620
# Group      : 804848814300940,137217003638571,1730188640566597