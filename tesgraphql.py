import os, sys, json, requests, re, bs4, datetime, time, urllib
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor
from random import choice as rc
from random import randrange as rr

def clear(): os.system('clear' if 'linux' in sys.platform.lower() else 'cls')

#--> Delay
def jeda(t):
    for x in range(t+1):
        print('\rTunggu %s Detik                                 '%(str(t)),end='');sys.stdout.flush()
        t -= 1
        if t == 0: break
        else: time.sleep(1)

ua_windows = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
hd_get_global = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Prefers-Color-Scheme':'light','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':ua_windows}
hd_post_global = {'Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Origin':'https://www.facebook.com','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent':ua_windows}
default_ua_windows = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
random_ua_windows = lambda : 'Mozilla/5.0 (Windows NT %s.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s.%s.%s.%s Safari/537.36'%(rc(['10','11']),rr(110,201),rr(0,10),rr(0,10),rr(0,10))
headers_get  = lambda i=default_ua_windows : {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Prefers-Color-Scheme':'light','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':i,'Viewport-Width':'924'}
headers_post = lambda i=default_ua_windows : {'Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Origin':'https://www.facebook.com','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent':i}

#--> Get Data
def GetData(req,con='Normal'):
    try:
        if con == 'Normal':
            act = re.search('"actorID":"(.*?)"',str(req)).group(1)
            hst = re.search('"haste_session":"(.*?)",',str(req)).group(1)
            rev = re.search('{"rev":(.*?)}',str(req)).group(1)
            hsi = re.search('"hsi":"(.*?)",',str(req)).group(1)
            dts = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',str(req)).group(1)
            jzt = re.search('&jazoest=(.*?)",',str(req)).group(1)
            lsd = re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1)
            spr = re.search('"__spin_r":(.*?),',str(req)).group(1)
            spt = re.search('"__spin_t":(.*?),',str(req)).group(1)
            dta = {'av':act, '__user':act, '__a':'1', '__hs':hst, 'dpr':'1.5', '__ccg':'EXCELLENT', '__rev':rev, '__hsi':hsi, '__comet_req':'15', 'fb_dtsg': dts, 'jazoest': jzt, 'lsd': lsd, '__spin_b':'trunk', '__spin_r':spr, '__spin_t':spt}
            return(dta)
        else:
            return({None})
    except Exception as e: return({None})

#--> Ulasan Baik/Buruk Halaman Facebook
def page_review(cookie,url):
    r = requests.Session()
    send_text = 'Israel Kontol'
    type_review = ['POSITIVE','NEGATIVE'][1] #--> Positive
    req = bs(r.get(url,headers=hd_get_global,cookies={'cookie':cookie}).content,'html.parser')
    hst=re.search('"haste_session":"(.*?)",',str(req)).group(1); rev=re.search('{"rev":(.*?)}',str(req)).group(1); hsi=re.search('"hsi":"(.*?)",',str(req)).group(1); dts=re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',str(req)).group(1); jzt=re.search('&jazoest=(.*?)",',str(req)).group(1); lsd=re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1); spr=re.search('"__spin_r":(.*?),',str(req)).group(1); spt=re.search('"__spin_t":(.*?),',str(req)).group(1)
    actor=re.search('"actorID":"(.*?)"',str(req)).group(1); target=re.search('{"is_business_page_active":.*?,"id":"(\d+)"}',str(req)).group(1); session_id=re.search('"sessionID":"(.*?)"',str(req)).group(1); 
    dta = {'av':actor,'__user':actor,'__a':'1','__hs':hst,'dpr':'1.5','__ccg':'EXCELLENT','__rev':rev,'__hsi':hsi,'__comet_req':'15','fb_dtsg': dts,'jazoest': jzt,'lsd': lsd,'__spin_b':'trunk','__spin_r':spr,'__spin_t':spt}
    aud = {'privacy':{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"}}; mes = {"ranges":[],"text":send_text}; rec = {"page_id":target,"rec_type":type_review}
    put = {"tracking":[None],"with_tags_ids":[],"actor_id":actor,"message":json.dumps(mes),"audience":json.dumps(aud),"page_recommendation":json.dumps(rec),"idempotence_token":f"{session_id}_FEED","logging":{'composer_session_id':session_id},"source":"WWW","client_mutation_id":"1","text_format_preset_id":"0","composer_entry_point":"inline_composer","event_share_metadata":{'surface':'newsfeed'},"composer_source_surface":"page_recommendation_tab","navigation_data":{'attribution_id_v2':'ProfileCometReviewsTabRoot.react,comet.profile.reviews,via_cold_start,1697712264297,368069,250100865708545,'},}
    var = {"input":json.dumps(put),"hashtag":None,"groupID":None,"focusCommentID":None,"gridMediaWidth":None,"inviteShortLinkKey":None,"displayCommentsFeedbackContext":None,"displayCommentsContextIsStorySet":None,"displayCommentsContextIsAdPreview":None,"displayCommentsContextEnableComment":None,"displayCommentsContextIsAggregatedShare":None,"scale":1,"feedbackSource":0,"renderLocation":"timeline","feedLocation":"PAGE_SURFACE_RECOMMENDATIONS","privacySelectorRenderLocation":"COMET_STREAM","UFI2CommentsProvider_commentsKey":"ProfileCometReviewsTabRoute","isTimeline":True,"isProfileReviews":True,"isFeed":False,"isGroup":False,"isEvent":False,"isFundraiser":False,"isFunFactPost":False,"isPageNewsFeed":False,"useDefaultActor":False,"isSocialLearning":False,"isWorkSharedDraft":False,"canUserManageOffers":False,"__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider":False,"__relay_internal__pv__IsWorkUserrelayprovider":False,"__relay_internal__pv__IsMergQAPollsrelayprovider":False,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":False,"__relay_internal__pv__StoriesRingrelayprovider":False}
    dta.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'ComposerStoryCreateMutation','variables':json.dumps(var),'server_timestamps':True,'doc_id':6308506282588750})
    pos = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=hd_post_global,cookies={'cookie':cookie}).json()
    if ('story_id' in str(pos)) and (actor in str(pos)):
        print('Sukses Rate')
    else:
        print('Gagal Rate')

#--> Auto Join Group
def join_group(cookie,url):
    r = requests.Session()
    req = bs(r.get(url,headers=hd_get_global,cookies={'cookie':cookie}).content,'html.parser')
    hst=re.search('"haste_session":"(.*?)",',str(req)).group(1); rev=re.search('{"rev":(.*?)}',str(req)).group(1); hsi=re.search('"hsi":"(.*?)",',str(req)).group(1); dts=re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',str(req)).group(1); jzt=re.search('&jazoest=(.*?)",',str(req)).group(1); lsd=re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1); spr=re.search('"__spin_r":(.*?),',str(req)).group(1); spt=re.search('"__spin_t":(.*?),',str(req)).group(1)
    feed=re.search('"feedType":"(.*?)"',str(req)).group(1); actor=re.search('"actorID":"(.*?)"',str(req)).group(1); idgrup=re.search('"groupID":"(.*?)"',str(req)).group(1); appid=re.search('"app_id":"(.*?)"',str(req)).group(1)
    dta = {'av':actor,'__user':actor,'__a':'1','__hs':hst,'dpr':'1.5','__ccg':'EXCELLENT','__rev':rev,'__hsi':hsi,'__comet_req':'15','fb_dtsg': dts,'jazoest': jzt,'lsd': lsd,'__spin_b':'trunk','__spin_r':spr,'__spin_t':spt}
    ram = {"app_id":appid,"exp_id":"null","is_from_share":False}
    put = {"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1698041952316,295080,2361831622,","group_id":idgrup,"group_share_tracking_params":json.dumps(ram),"actor_id":actor,"client_mutation_id":"1"}
    var = {"feedType":feed,"groupID":idgrup,"imageMediaType":"image/x-auto","input":json.dumps(put),"inviteShortLinkKey":None,"isChainingRecommendationUnit":False,"isEntityMenu":True,"scale":1.5,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GroupsCometGroupChatLazyLoadLastMessageSnippetrelayprovider":False}
    dta.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'GroupCometJoinForumMutation','variables':json.dumps(var),'server_timestamps':True,'doc_id':'7268226806522641'})
    pos = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=hd_post_global,cookies={'cookie':cookie}).json()
    if 'Admin ingin mengembangkan grup ini. Undang teman yang cocok dengan filter admin grup ini.' in str(pos): print('Berhasil Bergabung Ke Grup')
    else: print('Gagal Bergabung Ke Grup')

#--> Auto Accept Page Admin Invitation
def acc_admin(cookie):
    r = requests.Session()
    req = bs(r.get('https://web.facebook.com/pages/?category=invites&ref=bookmarks',headers=hd_get_global,cookies={'cookie':cookie}).content,'html.parser')
    actor=re.search('"actorID":"(.*?)"',str(req)).group(1); hst=re.search('"haste_session":"(.*?)",',str(req)).group(1); rev=re.search('{"rev":(.*?)}',str(req)).group(1); hsi=re.search('"hsi":"(.*?)",',str(req)).group(1); dts=re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',str(req)).group(1); jzt=re.search('&jazoest=(.*?)",',str(req)).group(1); lsd=re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1); spr=re.search('"__spin_r":(.*?),',str(req)).group(1); spt=re.search('"__spin_t":(.*?),',str(req)).group(1)
    dta = {'av':actor,'__user':actor,'__a':'1','__hs':hst,'dpr':'1.5','__ccg':'EXCELLENT','__rev':rev,'__hsi':hsi,'__comet_req':'15','fb_dtsg': dts,'jazoest': jzt,'lsd': lsd,'__spin_b':'trunk','__spin_r':spr,'__spin_t':spt}
    scrap = eval(re.search('"profile_admin_invites":(.*?),"pages_you_may_like"',str(req)).group(1).replace('true','True').replace('false','False').replace('null','None'))
    for x in scrap:
        try:
            admin_invite_id = x['profile_admin_invite_id']
            inviter_id = x['profile_admin_invitee']['id']
            inviter_name = x['profile_admin_inviter']['name']
            page_id = x['target_profile_for_admin_invite']['delegate_page']['id']
            page_name = x['target_profile_for_admin_invite']['delegate_page']['name']
            dta.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'ProfilePlusCometAcceptOrDeclineAdminInviteMutation','variables':json.dumps({"input":{"client_mutation_id":"1","actor_id":actor,"is_accept":True,"profile_admin_invite_id":admin_invite_id,"user_id":actor},"scale":1.5}),'server_timestamps':True,'doc_id':'6818899424861979'})
            pos = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=hd_post_global,cookies={'cookie':cookie}).json()
            if ('accept_or_decline_profile_plus_admin_invite' in str(pos)) and (actor in str(pos)):
                print('Sukses Claim')
            else:
                print('Gagal Claim')
        except Exception as e: pass

#--> Auto Share To My Feed
def AutoShare(cookie,url):
    r = requests.Session()
    req = bs(r.get(url,headers=hd_get_global,cookies={'cookie':cookie}).content,'html.parser')
    dta = GetData(req)
    param = re.search('"params":{"fbid":"(.*?)"',str(req)).group(1)
    token = re.search('"sessionID":"(.*?)"',str(req)).group(1)
    var = {
        "input":{
            "attachments":{"link":{"share_scrape_data":"{\"share_type\":2,\"share_params\":[%s]}"%(param)}},
            "audiences":{"undirected":{"privacy":{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"}}},
            "idempotence_token":token,"is_tracking_encrypted":True,
            "navigation_data":{"attribution_id_v2":"CometPhotoRoot.react,comet.mediaviewer.photo,via_cold_start,1699124635808,90556,,"},
            "source":"www","tracking":[],"actor_id":dta['__user'],"client_mutation_id":"1"},
        "scale":1,"feedbackSource":1,"focusCommentID":None,"useDefaultActor":False,"feedLocation":"NEWSFEED","renderLocation":"homepage_stream",
        "displayCommentsFeedbackContext":None,"displayCommentsContextIsStorySet":None,"displayCommentsContextIsAdPreview":None,"displayCommentsContextEnableComment":None,"displayCommentsContextIsAggregatedShare":None,"privacySelectorRenderLocation":"COMET_STREAM","UFI2CommentsProvider_commentsKey":"CometModernHomeFeedQuery",
        "__relay_internal__pv__IsWorkUserrelayprovider":False,"__relay_internal__pv__IsMergQAPollsrelayprovider":False,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":False,"__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider":False,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":False,"__relay_internal__pv__StoriesRingrelayprovider":False}
    dta.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'useCometFeedToFeedReshare_FeedToFeedMutation','variables':json.dumps(var),'server_timestamps':True,'doc_id':'6509593895832866'})
    pos = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=hd_post_global,cookies={'cookie':cookie}).json()
    if ('story_create' in str(pos)) and ('feed_story_edge' in str(pos)):
        print('Sukses')
    else:
        print('Gagal')

#--> Auto Report
def auto_report(cookie,url):
    target = '61552638913294'
    r = requests.Session()
    req = bs(r.get(url,headers=hd_get_global,cookies={'cookie':cookie}).content,'html.parser')
    dta = GetData(req)
    ses = re.search('"sessionID":"(.*?)"',str(req)).group(1)

    #--> Tahap 1
    var1 = {"input":{"content_id":target,"entry_point":"PROFILE_REPORT_BUTTON","location":"PROFILE_SOMEONE_ELSE","trigger_event_type":"REPORT_BUTTON_CLICKED","nt_context":None,"trigger_session_id":ses},"scale":1}
    dta.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometIXTFacebookContentTriggerRootQuery','variables':json.dumps(var1),'server_timestamps':True,'doc_id':'6769900669784116'})
    pos1 = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=hd_post_global,cookies={'cookie':cookie}).json()
    dta.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometFacebookIXTNextMutation','server_timestamps':True,'doc_id':'6914576615289569'})

    #--> Tahap 2
    context = pos1['data']['ixt_content_trigger']['screen']['view_model']['context']
    serial  = pos1['data']['ixt_content_trigger']['screen']['view_model']['serialized_state']
    var2 = {"input":{"frx_tag_selection_screen":{"context":context,"serialized_state":serial,"show_tag_search":False,"tags":["PROFILE_FAKE_ACCOUNT"]},"actor_id":dta['__user'],"client_mutation_id":"1"},"scale":1}
    dta.update({'variables':json.dumps(var2)})
    pos2 = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=hd_post_global,cookies={'cookie':cookie}).json()

    #--> Tahap 3
    context = pos2['data']['ixt_screen_next']['view_model']['context']
    serial  = pos2['data']['ixt_screen_next']['view_model']['serialized_state']
    var3 = {"input":{"frx_report_confirmation_screen":{"context":context,"serialized_state":serial},"actor_id":dta['__user'],"client_mutation_id":"3"},"scale":1}
    dta.update({'variables':json.dumps(var3)})
    pos3 = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=hd_post_global,cookies={'cookie':cookie}).json()
    
    #--> Tahap 4
    context = pos3['data']['ixt_screen_next']['view_model']['context']
    serial  = pos3['data']['ixt_screen_next']['view_model']['serialized_state']
    var4 = {"input":{"frx_post_report_process_timeline":{"context":context,"serialized_state":serial},"actor_id":dta['__user'],"client_mutation_id":"4"},"scale":1}
    dta.update({'variables':json.dumps(var4)})
    pos4 = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=hd_post_global,cookies={'cookie':cookie}).json()
    
    if 'Anda telah mengirimkan laporan.' in str(pos4):
        print('Report Success!')
    else:
        print('Report Failed!')

#--> Get Application
class GetAPP():
    def __init__(self,cookie):
        self.cookie = cookie
        self.xyz = requests.Session()
        req = bs(self.xyz.get('https://www.facebook.com/profile.php?',headers=hd_get_global,cookies={'cookie':self.cookie}).content,'html.parser')
        dta = GetData(req)
        dta.update({'fb_api_caller_class':'RelayModern','server_timestamps':True,})
        print('[ Active ]')
        self.CheckAPP('Active',dta,None)
        print('[ Expired ]')
        self.CheckAPP('Expired',dta,None)
    def CheckAPP(self,stat,dta,cursor):
        dta.update({'variables':json.dumps({"after":cursor,"first":6,"id":dta['__user']})})
        if stat == 'Active':
            node = 'activeApps'
            dta.update({'fb_api_req_friendly_name':'ApplicationAndWebsitePaginatedSettingAppGridListActiveQuery','doc_id':'4711129059016316'})
        elif stat == 'Expired':
            node = 'expiredApps'
            dta.update({'fb_api_req_friendly_name':'ApplicationAndWebsitePaginatedSettingAppGridListExpiredQuery','doc_id':'4802508009803010'})
        pos = self.xyz.post('https://www.facebook.com/api/graphql/',data=dta,headers=hd_post_global,cookies={'cookie':self.cookie}).json()
        dat = pos['data']['node'][node]['edges']
        for x in dat:
            dtk = x['node']['apps_and_websites_view']['detailView']
            id, nm, st, wk = dtk['app_id'], dtk['app_name'], dtk['app_status'], dtk['install_timestamp']
            tm = datetime.datetime.utcfromtimestamp(int(wk))
            tgl, bln, thn = tm.day, ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'][int(tm.month)-1], tm.year
            tdt = '%s %s %s'%(tgl,bln,thn)
            print('%s%s| %s%s| %s'%(id,' '*(17-len(str(id))),nm[:14],' '*(15-len(str(nm[:14]))),tdt))
        next = pos['data']['node'][node]['page_info']['has_next_page']
        if next == True:
            cursor = pos['data']['node'][node]['page_info']['end_cursor']
            self.CheckAPP(stat,dta,cursor)
        else: print('')

#--> View Story
def ViewStory(cookie,url):
    r = requests.Session()
    req = bs(r.get(url,headers=hd_get_global,cookies={'cookie':cookie}).content,'html.parser')
    dta = GetData(req)
    dta.update({'fb_api_caller_class':'RelayModern','server_timestamps':True})
    idp = re.search('"userID":"(.*?)",',str(req)).group(1)
    gfind = list(re.findall('"__typename":"User","__isActor":"User","id":"%s","__isEntity":"User","url":\".*?\","work_foreign_entity_info":null,"work_info":null,"story_bucket":{"nodes":\[{"should_show_close_friend_badge":false,"id":"(.*?)","first_story_to_show":{"id":"(.*?)","story_card_seen_state"'%(idp),str(req).replace('\\',''))[0])
    bucket, storyid = gfind[0], gfind[1]
    var = {"input":{"bucket_id":bucket,"story_id":storyid,"actor_id":idp,"client_mutation_id":"1"},"scale":1.5}
    dta.update({'fb_api_req_friendly_name':'storiesUpdateSeenStateMutation','variables':json.dumps(var),'doc_id':'5127393270671537'})
    pos = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=hd_post_global,cookies={'cookie':cookie}).text
    #print(str(pos)[:50000])
    if '"is_seen_by_viewer":true' in str(pos):
        print('Success')
    else:
        print('Failed')

#--> Add Email TempMailIO
def GetEmail():
    r = requests.Session()
    pos = r.post('https://api.internal.temp-mail.io/api/v3/email/new').json()
    email = pos['email']
    return(r,email)
def GetCode(r,email):
    req = r.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages').json()
    kode = re.search('<center>(.*?)<\/center>',str(req)).group(1)
    return(kode)
def AddEmail(cookie):
    r = requests.Session()
    req = bs(r.get('https://www.facebook.com/profile.php',headers=hd_get_global,cookies={'cookie':cookie}).content,'html.parser')
    dta = GetData(req)
    dta.update({'fb_api_caller_class':'RelayModern','server_timestamps':True})
    sesmail, email = GetEmail()
    print('Email Baru : %s'%(email))
    var = {
        "country":"US",
        "contact_point":email,
        "contact_point_type":"email",
        "selected_accounts":[dta['__user']],
        "family_device_id":"device_id_fetch_datr",
        "client_mutation_id":"mutation_id_%s"%(str(time.time()).replace('.','')[:13])}
    dta.update({
        'fb_api_req_friendly_name':'FXAccountsCenterAddContactPointMutation',
        'variables':json.dumps(var),
        'doc_id':'6970150443042883'})
    pos = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=hd_post_global,cookies={'cookie':cookie}).json()
    jeda(30)
    code = GetCode(sesmail,email)
    print('\rKode Verif : %s'%(code))
    var = {
        "contact_point":email,
        "contact_point_type":"email",
        "pin_code":code, #--> Kode Verif
        "selected_accounts":[dta['__user']],
        "family_device_id":"device_id_fetch_datr",
        "client_mutation_id":pos['data']['xfb_add_contact_point']['client_mutation_id'],
        "contact_point_event_type":"ADD",
        "normalized_contact_point_to_replace":""}
    dta.update({
        'fb_api_req_friendly_name':'FXAccountsCenterContactPointConfirmationDialogVerifyContactPointMutation',
        'variables':json.dumps(var),
        'doc_id':'6973420842719905'})
    pos = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=hd_post_global,cookies={'cookie':cookie}).json()
    if "'success': True" in str(pos):
        print('Berhasil Menambah Email Baru')
    else:
        print('Gagal Menambah Email Baru')

#--> Post Caption To Feed
def PostToFeed(cookie):
    r = requests.Session()
    req = bs(r.get('https://www.facebook.com/profile.php',headers=hd_get_global,cookies={'cookie':cookie}).content,'html.parser')
    dta = GetData(req)
    dta.update({'fb_api_caller_class':'RelayModern','server_timestamps':True})
    ses = re.search('"sessionID":"(.*?)"',str(req)).group(1)

    # --> Edit Caption & Link Foto Disini
    # caption = 'Test Tanpa Foto'
    # url_foto = ''
    caption = 'Test Pake Foto'
    url_foto = 'https://i.pinimg.com/736x/80/8c/97/808c97eb9c7e017964857b957c125917.jpg'

    if url_foto == '':
        lampiran = []
    else:
        dtf = {'file':('image.jpg',urllib.request.urlopen(url_foto).read())}
        dat = dta.copy()
        dat.update({'source':'8','profile_id':dta['__user'],'waterfallxapp':'comet','farr':dtf})
        pos = r.post('https://upload.facebook.com/ajax/react_composer/attachments/photo/upload',data=dat,files=dtf,cookies={'cookie':cookie},allow_redirects=True).text
        id_foto = re.search('"photoID":"(.*?)"',str(pos)).group(1)
        lampiran = [{"photo":{"id":id_foto}}]
    
    var = {
        "input":{
            "composer_entry_point":"inline_composer",
            "composer_source_surface":"timeline",
            "idempotence_token":f"{ses}_FEED",
            "source":"WWW",
            "attachments":lampiran,
            "audience":{
                "privacy":{
                    "allow":[],
                    "base_state":"EVERYONE", #--> Privasi Post ['EVERYONE','FRIENDS','SELF']
                    "deny":[],
                    "tag_expansion_state":"UNSPECIFIED"}},
            "message":{
                "ranges":[],
                "text":caption}, #--> Caption Post
            "with_tags_ids":[],
            "inline_activities":[],
            "explicit_place_id":"0",
            "text_format_preset_id":"0",
            "logging":{"composer_session_id":ses},
            "navigation_data":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,tap_bookmark,1700238612634,388758,100064626647103,,"},
            "tracking":[None],
            "event_share_metadata":{"surface":"newsfeed"},
            "actor_id":dta['__user'],
            "client_mutation_id":"1"},
            "displayCommentsFeedbackContext":None,
            "displayCommentsContextEnableComment":None,
            "displayCommentsContextIsAdPreview":None,
            "displayCommentsContextIsAggregatedShare":None,
            "displayCommentsContextIsStorySet":None,
            "feedLocation":"TIMELINE",
            "feedbackSource":0,
            "focusCommentID":None,
            "gridMediaWidth":230,
            "groupID":None,
            "scale":1.5,
            "privacySelectorRenderLocation":"COMET_STREAM",
            "checkPhotosToReelsUpsellEligibility":True,
            "renderLocation":"timeline",
            "useDefaultActor":False,
            "inviteShortLinkKey":None,
            "isFeed":False,
            "isFundraiser":False,
            "isFunFactPost":False,
            "isGroup":False,
            "isEvent":False,
            "isTimeline":True,
            "isSocialLearning":False,
            "isPageNewsFeed":False,
            "isProfileReviews":False,
            "isWorkSharedDraft":False,
            "UFI2CommentsProvider_commentsKey":"ProfileCometTimelineRoute",
            "hashtag":None,
            "canUserManageOffers":False,
            "__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider":False,
            "__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":False,
            "__relay_internal__pv__IsWorkUserrelayprovider":False,
            "__relay_internal__pv__IsMergQAPollsrelayprovider":False,
            "__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":False,
            "__relay_internal__pv__StoriesRingrelayprovider":False}
    dta.update({'fb_api_req_friendly_name':'ComposerStoryCreateMutation','variables':json.dumps(var),'server_timestamps':True,'doc_id':'6897576447022330'})
    pos = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=hd_post_global,cookies={'cookie':cookie}).json()
    if 'story_create' in str(pos) and dta['__user'] in str(pos):
        print('Sukses')
    else:
        print('Failed')

if __name__ == '__main__':
    clear()
    url_target = 'https://www.facebook.com/profile.php'
    cookie = 'Put Your Cookies Here'
    PostToFeed(cookie)