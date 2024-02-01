_AN='client_mutation_id'
_AM='\rDumping %s ID From %s Post'
_AL='\rSedang Dump %s ID Dari %s Post'
_AK='6767163196701249'
_AJ='ProfileCometAppCollectionListRendererPaginationQuery'
_AI='perempuan'
_AH='[ Seleksi Berdasarkan ]'
_AG='Wrong Input!'
_AF='Salah, Isi Yg Benar!'
_AE='en-US,en;q=0.9'
_AD='gzip, deflate'
_AC='User-Agent'
_AB='Sec-Fetch-Site'
_AA='Sec-Fetch-Mode'
_A9='Sec-Fetch-Dest'
_A8='Sec-Ch-Ua-Platform-Version'
_A7='Sec-Ch-Ua-Platform'
_A6='Sec-Ch-Ua-Model'
_A5='Sec-Ch-Ua-Mobile'
_A4='Sec-Ch-Ua-Full-Version-List'
_A3='Sec-Ch-Ua'
_A2='Sec-Ch-Prefers-Color-Scheme'
_A1='Accept-Language'
_A0='Accept-Encoding'
_z='RelayModern'
_y='fb_api_caller_class'
_x='has_next_page'
_w='end_cursor'
_v='edges'
_u='cursor'
_t='count'
_s='%s|%s'
_r='%s|%s|%s'
_q='__user'
_p='No Interaction'
_o='Tidak Ada Interaksi'
_n='Pilih : '
_m='https://business.facebook.com/business_locations'
_l='%s\n'
_k='03'
_j='restrictable_profile_owner'
_i='profile_action'
_h='client_handler'
_g='actions_renderer'
_f='https://www.facebook.com/api/graphql/'
_e='doc_id'
_d='server_timestamps'
_c='variables'
_b='fb_api_req_friendly_name'
_a='scale'
_Z='02'
_Y='01'
_X='https://www.facebook.com'
_W='page_info'
_V='pageItems'
_U='Total Friendlist : %s'
_T='action'
_S='a+'
_R='2'
_Q='login/token_eaag.json'
_P='|'
_O=None
_N=True
_M='w'
_L='name'
_K='html.parser'
_J='BotFriend/%s'
_I='login/token_eaab.json'
_H='login/cookie.json'
_G='id'
_F='node'
_E='data'
_D='1'
_C='cookie'
_B='r'
_A='INDONESIA'
Author='Dapunta Khurayra X'
Facebook='Facebook.com/Dapunta.Khurayra.X'
Instagram='Instagram.com/Dapunta.Ratya'
Whatsapp='Wa.me/6282245780524'
YouTube='Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'
import os,sys,random,time,json,re,concurrent,urllib,shutil
from concurrent.futures import ThreadPoolExecutor
from random import choice as rc
from random import randrange as rr
def mod():
	global requests,bs4,bs;clear()
	try:import requests
	except Exception as e:os.system('pip install requests');import requests
	try:import bs4
	except Exception as e:os.system('pip install bs4');import bs4
	from bs4 import BeautifulSoup as bs
	try:os.mkdir('BotFriend')
	except Exception as e:pass
	clear()
default_ua_windows='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
random_ua_windows=lambda:'Mozilla/5.0 (Windows NT %s.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s.%s.%s.%s Safari/537.36'%(rc(['10','11']),rr(110,201),rr(0,10),rr(0,10),rr(0,10))
headers_get=lambda i=default_ua_windows:{'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',_A0:_AD,_A1:_AE,'Cache-Control':'max-age=0','Dpr':_D,'Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace',_A2:'dark',_A3:'',_A4:'',_A5:'?0',_A6:'',_A7:'',_A8:'',_A9:'document',_AA:'navigate',_AB:'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':_D,_AC:i}
headers_post=lambda i=default_ua_windows:{'Accept':'*/*',_A0:_AD,_A1:_AE,'Content-Length':'1545','Content-Type':'application/x-www-form-urlencoded','Dpr':_D,'Origin':_X,'Referer':_X,_A2:'dark',_A3:'',_A4:'',_A5:'?0',_A6:'',_A7:'',_A8:'',_A9:'empty',_AA:'cors',_AB:'same-origin',_AC:i}
friendlist=[]
Z='\x1b[38;5;232m'
M='\x1b[38;5;196m'
H='\x1b[38;5;46m'
K='\x1b[38;5;226m'
B='\x1b[38;5;44m'
U='\x1b[38;5;54m'
O='\x1b[38;5;51m'
P='\x1b[38;5;231m'
J='\x1b[38;5;208m'
A='\x1b[38;5;248m'
MR='\x1b[3m'
BI='\x1b[0m'
def logo(n='\n\n'):print('%s╔╦═╗   %s╦═╗╦ ╦╦═╗╔╦╗╦ ╦ %s'%(K,H,P));print('%s ║ ║%s1.0%s╠╦╝╚╦╝╠╦╝ ║ ╠═╣ %sFacebook%s Friendlist Bot'%(K,P,H,O,P));print('%s ║ ╠═══%s╩╚═ ╩ ╩╚═ ╩ ╩ ╩ %s%sBy %sDapunta %sand %sHans Rayartha%s%s'%(K,H,P,MR,K,P,K,BI,P));print('%s═╩═╩═══════%s══════════%s'%(K,H,P),end=n)
def clear():os.system('clear'if'linux'in sys.platform.lower()else'cls')
def geolocator():
	A='OTHER';global country
	try:
		_r_=requests.Session();_g_=_r_.get('https://ip-api.org/json/').json()
		if _g_['country']=='ID':country=_A
		else:country=A
	except Exception as e:country=A
def jeda(t):
	for x in range(t+1):
		print('\r%sTunggu %s Detik                                 '%(P,str(t)),end='');sys.stdout.flush();t-=1
		if t==0:break
		else:time.sleep(1)
def language(cookie):
	A='Bahasa Indonesia'
	try:
		xyz=requests.Session();req=xyz.get('https://mbasic.facebook.com/language/',cookies=cookie);pra=bs(req.content,_K)
		for x in pra.find_all('form',{'method':'post'}):
			if A in str(x):bahasa={'fb_dtsg':re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),'jazoest':re.search('name="jazoest" value="(.*?)"',str(req.text)).group(1),'submit':A};exec=xyz.post('https://mbasic.facebook.com'+x[_T],data=bahasa,cookies=cookie)
	except Exception as e:pass
def ConvertCookie(cok):
	try:sb=re.search('sb=(.*?);',str(cok)).group(1);datr=re.search('datr=(.*?);',str(cok)).group(1);c_user=re.search('c_user=(.*?);',str(cok)).group(1);xs=re.search('xs=(.*?);',str(cok)).group(1);fr=re.search('fr=(.*?);',str(cok)).group(1);cookie=f"sb={sb}; datr={datr}; c_user={c_user}; xs={xs}; fr={fr};"
	except Exception as e:cookie=cok
	return cookie
def AttrCookie():locale='id_ID';wd='1707x811';presence=GetTime();attr=f" locale={locale}; wd={wd}; presence={presence};";return attr
def GetTime():temi=str(time.time()).replace('.','')[:13];pres=f"C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A{temi}%2C%22v%22%3A1%7D";return pres
class login:
	def __init__(self):global file_interaction,file_mutual,file_gender;self.xyz=requests.Session();self.cek_cookies();file_interaction='Interaction_%s.txt'%id_login;file_mutual='Mutual_%s.txt'%id_login;file_gender='Gender_%s.txt'%id_login;Menu()
	def cek_cookies(self):
		B='%sHello %s%s%s\n';A='https://graph.facebook.com/me?fields=name,id&access_token=%s'
		try:
			global id_login,nama_login;self.cookie={_C:open(_H,_B).read()};self.token_eaag=open(_Q,_B).read();self.token_eaab=open(_I,_B).read();language(self.cookie);req_eaag=self.xyz.get(A%self.token_eaag,cookies=self.cookie).json();req_eaab=self.xyz.get(A%self.token_eaab,cookies=self.cookie).json()[_G];id_login=req_eaag[_G];nama_login=req_eaag[_L];clear();logo('  ')
			if len(nama_login)<=20:print(B%(P,H,str(nama_login),P))
			else:print(B%(P,H,str(nama_login)[:20],P))
		except Exception as e:self.insert_cookie()
	def insert_cookie(self):
		print('\n%sCookie Invalid!%s'%(M,P));time.sleep(2);clear();logo()
		if country==_A:print('%s[ %sPeringatan %s]'%(M,P,M));print('Memakai Tools Ini, Akun Sudah Pasti Sesi/Checkpoint!');print('Gunakan Akun Kuat Atau Setidaknya Memiliki ID Card');print('Agar Bisa Dipulihkan Jika Terjadi Sesi\n');print('%sJika A2F Aktif, Pergi Ke'%P);print(_m);print('Kemudian Masukkan Kode Autentikasi');ciko=input('\n%sMasukkan Cookie : %s%s'%(P,H,P))
		else:print('%s[ %sWarning %s]'%(M,P,M));print('Using This Tools, Your Account Will Be Checkpoint!');print('Use Strong Account Or Have ID Card');print('So It Can Be Recovered If Checkpoint\n');print('%sIf 2 Factor Authenticator On, Go To'%P);print(_m);print('To Enter Authentication Code');ciko=input('\n%sInput Cookie : %s%s'%(P,H,P))
		if ciko.lower()=='t':0
		else:
			cookie=ConvertCookie(ciko);print('')
			try:self.token_eaag=self.generate_token_eaag(cookie);print('%s[%s•%s] %sSuccess Get EAAG Token'%(H,P,H,P))
			except Exception as e:print('%s[%s•%s] %sFailed Get EAAG Token'%(M,P,M,P));time.sleep(2);self.insert_cookie()
			try:self.token_eaab=self.generate_token_eaab(cookie);print('%s[%s•%s] %sSuccess Get EAAB Token'%(H,P,H,P))
			except Exception as e:print('%s[%s•%s] %sFailed Get EAAB Token'%(M,P,M,P));time.sleep(2);self.insert_cookie()
			try:os.mkdir('login')
			except:pass
			open(_H,_M).write(cookie);open(_Q,_M).write(self.token_eaag);open(_I,_M).write(self.token_eaab);self.cek_cookies()
	def generate_token_eaag(self,cok):url=_m;req=self.xyz.get(url,cookies={_C:cok});tok=re.search('(\\["EAAG\\w+)',req.text).group(1).replace('["','');return tok
	def generate_token_eaab(self,cok):req1=bs(self.xyz.get('https://www.facebook.com/adsmanager/manage/campaigns',cookies={_C:cok},allow_redirects=_N).content,_K);nek1=re.search('window\\.location\\.replace\\("(.*?)"\\)',str(req1)).group(1).replace('\\','');req2=bs(self.xyz.get(nek1,cookies={_C:cok},allow_redirects=_N).content,_K);tok=re.search('accessToken="(.*?)"',str(req2)).group(1);return tok
def logout():
	c=input('%sYakin Ingin %sLogout %s? [%sy%s/%st%s] : '%(P,M,P,M,P,H,P)).lower()
	if c=='y':
		try:shutil.rmtree('login');print('%sBerhasil Logout%s\n'%(P,P))
		except Exception as e:print('%sGagal Logout%s\n'%(M,P))
	else:print('%sBatal Logout%s\n'%(H,P))
class Menu:
	def __init__(self):
		try:self.cookie=open(_H,_B).read();self.token_eaag=open(_Q,_B).read();self.token_eaab=open(_I,_B).read();self.file_inter=_J%file_interaction;self.file_mutua=_J%file_mutual;self.file_gende=_J%file_gender
		except Exception as e:login()
		self.Main()
	def Main(self):
		E='%s[%s3%s] %sGender';D='%s[%s2%s] %sMutual';C='[5] Mutual';B='[4] Gender';A='[0] Logout'
		if country==_A:print('%s[1] Seleksi Teman'%P);print('[2] Unfriend Massal');print('[3] AddFriend Massal');print(A);put=_n;fls=_AF
		else:print('[1] Select Friend');print('[2] Mass Unfriend');print('[3] Mass AddFriend');print(A);put='Choose : ';fls=_AG
		x=input(put);print('')
		if x in['0','00','z']:logout()
		elif x in[_D,_Y,'a']:
			if country==_A:print(_AH);print('[1] Reaksi');print('[2] Komentar');print('[3] Reaksi & Komentar');print(B);print(C)
			else:print('[ Selection Based ]');print('[1] Reaction');print('[2] Comment');print('[3] Reaction & Comment');print(B);print(C)
			y=input(put);print('')
			if y in[_D,_Y,'a']:self.InteractionMenu(1)
			elif y in[_R,_Z,'b']:self.InteractionMenu(2)
			elif y in['3',_k,'c']:self.InteractionMenu(3)
			elif y in['4','04','d']:self.GenderMenu()
			elif y in['5','05','e']:self.MutualMenu()
			else:print(fls);exit()
		elif x in[_R,_Z,'b']:
			w_i=H if os.path.exists(self.file_inter)else M;w_g=H if os.path.exists(self.file_gende)else M;w_m=H if os.path.exists(self.file_mutua)else M
			if country==_A:print('[ Unfriend Berdasarkan ]');print('%s[%s1%s] %sSemua'%(H,P,H,P));print(D%(w_m,P,w_m,P));print(E%(w_g,P,w_g,P));print('%s[%s4%s] %sInteraksi'%(w_i,P,w_i,P))
			else:print('[ Unfriend Based ]');print('%s[%s1%s] %sAll'%(H,P,H,P));print(D%(w_m,P,w_m,P));print(E%(w_g,P,w_g,P));print('%s[%s4%s] %sInteraction'%(w_i,P,w_i,P))
			y=input(put);print('')
			if y in[_D,_Y,'a']:self.UnfriendAllFriend()
			elif y in[_R,_Z,'b']:self.UnfriendBasedMutual()
			elif y in['3',_k,'c']:self.UnfriendBasedGender()
			elif y in['4','04','d']:self.UnfriendBasedInteraction()
			else:print(fls);exit()
		elif x in['3',_k,'c']:AddFriend()
		else:print(fls);exit()
	def InteractionMenu(self,ch):
		loop=0;Inter=CheckInteraction();open(self.file_inter,_S);open(self.file_inter,_M).write('');post=Inter.DumpLatestPost()
		for i in post:
			if ch==1:Inter.DumpReaction(loop,i)
			elif ch==2:Inter.DumpComment(loop,i)
			elif ch==3:Inter.DumpReaction(loop,i);Inter.DumpComment(loop,i)
			loop+=1
		o=open(self.file_inter,_B).read().splitlines()
		if len(o)==0:print(_o if country==_A else _p);print('Cek Interaksi Reaksi/Komentar Terlebih Dahulu!'if country==_A else'Check Interaction Reaction/Comment First!');exit('')
		else:print('\rMendapat %s ID Dari %s Post                    '%(str(len(o)),str(loop))if country==_A else'\rSuccess Get %s ID From %s Posts                      '%(str(len(o)),str(loop)))
	def GenderMenu(self):GD=CheckFriendlistByGraphQL(1);open(self.file_gende,_S);open(self.file_gende,_M).write('');GD.Main()
	def MutualMenu(self):MT=CheckFriendlistByGraphQL(2);open(self.file_mutua,_S);open(self.file_mutua,_M).write('');MT.Main()
	def UnfriendAllFriend(self):
		UF=UnFriend();GetFriendlist(requests.Session(),_O);total_fl=str(len(friendlist));print(_U%total_fl if country==_A else _U%total_fl);print('')
		with ThreadPoolExecutor(max_workers=5)as TPE:
			for i in friendlist:TPE.submit(UF.Unfriend,i.split(_P)[0],len(friendlist))
	def UnfriendBasedMutual(self):
		if country==_A:print('Format\n (<)  Kurang Dari\n (>)  Lebih Dari\n (<=) Kurang Dari Sama Dengan\n (>=) Lebih Dari Sama Dengan\n (==) Sama Dengan\n (!=) Tidak Sama Dengan\n\nContoh\n <10  (Hapus FL Yg Mutualnya Kurang Dari 10)\n ==10 (Hapus FL Yg Mutualnya Sama Dengan 10)\n !=10 (Hapus FL Yg Mutualnya Tidak Sama Dengan 10)')
		else:print('Format\n (<)  Less Than\n (>)  Greater Than\n (<=) Less Than Or Equal To\n (>=) Greater Than Or Equal To\n (==) Equal To\n (!=) Not Equal To\n\nExample\n <10  (Delete FL Whose Mutuals Are Less Than 10)\n ==10 (Delete FL Whose Mutuals Are Equal To 10)\n !=10 (Delete FL Whose Mutuals Are Not Equal To 10)')
		t=input('\nInput : ');print('');y=re.search('\\d+',t).group(0);oper=t.replace(y,'');UF=UnFriend();total,removed=UF.GetSelectedMutual(oper,y);print(_U%str(len(total)));print('Friendlist %s %s Mutual : %s'%(oper,str(y),str(len(removed))));print('')
		with ThreadPoolExecutor(max_workers=5)as TPE:
			for i in removed:TPE.submit(UF.Unfriend,i.split(_P)[0],len(removed))
	def UnfriendBasedGender(self):
		k='Hapus Friendlist Laki/Perempuan [l/p] : 'if country==_A else'Delete Men/Women Friendlist [m/w] : ';f=_AF if country==_A else _AG;p=input(k).lower()
		if p in[_D,'l','m','laki','men']:c='MALE';g='Friendlist Laki-Laki'if country==_A else'Men Friendlist'
		elif p in[_R,'p',_M,_AI,'women']:c='FEMALE';g='Friendlist Perempuan'if country==_A else'Women Friendlist'
		else:print('\n%s'%f);exit()
		UF=UnFriend();total,removed=UF.GetSelectedGender(c);print(_U%str(len(total)));print('%s : %s'%(g,str(len(removed))));print('')
		with ThreadPoolExecutor(max_workers=5)as TPE:
			for i in removed:TPE.submit(UF.Unfriend,i.split(_P)[0],len(removed))
	def UnfriendBasedInteraction(self):
		UF=UnFriend();total_fl,no_interact=UF.GetNoInteract();print(_U%total_fl if country==_A else _U%total_fl);print('Tidak Berinteraksi : %s'%str(len(no_interact))if country==_A else'No Interaction : %s'%str(len(no_interact)));print('')
		with ThreadPoolExecutor(max_workers=5)as TPE:
			for i in no_interact:TPE.submit(UF.Unfriend,i.split(_P)[0],len(no_interact))
def GetData(req):actor=re.search('"actorID":"(.*?)"',str(req)).group(1);haste=re.search('"haste_session":"(.*?)"',str(req)).group(1);conne=re.search('"connectionClass":"(.*?)"',str(req)).group(1);spinr=re.search('"__spin_r":(.*?),',str(req)).group(1);spinb=re.search('"__spin_b":"(.*?)"',str(req)).group(1);spint=re.search('"__spin_t":(.*?),',str(req)).group(1);hsi=re.search('"hsi":"(.*?)"',str(req)).group(1);comet=re.search('"comet_env":(.*?),',str(req)).group(1);dtsg=re.search('"DTSGInitialData",\\[\\],{"token":"(.*?)"}',str(req)).group(1);jazoest=re.search('&jazoest=(.*?)"',str(req)).group(1);lsd=re.search('"LSD",\\[\\],{"token":"(.*?)"}',str(req)).group(1);dta={'av':actor,_q:actor,'__a':_D,'__hs':haste,'dpr':_D,'__ccg':conne,'__rev':spinr,'__hsi':hsi,'__comet_req':comet,'fb_dtsg':dtsg,'jazoest':jazoest,'lsd':lsd,'__spin_r':spinr,'__spin_b':spinb,'__spin_t':spint};return dta
def GetFriendlist2():
	A='friends';friendlist=[]
	try:
		cookie=open(_H,_B).read();token_eaab=open(_I,_B).read();r=requests.Session();req=r.get(f"https://graph.facebook.com/me?fields=friends.fields(id,name,birthday)&access_token={token_eaab}",headers=headers_get(),cookies={_C:cookie}).json();total_fl=str(req[A]['summary']['total_count'])
		for x in req[A][_E]:
			try:bd=x['birthday']
			except Exception as e:bd=''
			try:friendlist.append(_r%(x[_G],x[_L],bd))
			except Exception as e:pass
		return total_fl,friendlist
	except Exception as e:print(e);print('Gagal Dump Friendlist\nAkun Spam/Checkpoint'if country==_A else'Failed To Dump Friendlist\nAccount Spam/Checkpoint');exit()
def GetFriendlist(r,after):
	B='\rBerhasil Mendeteksi %s Teman';A='after';global friendlist
	try:
		cookie=open(_H,_B).read();token=open(_I,_B).read();req=r.get('https://graph.facebook.com/me/friends',params={'access_token':token,A:after,'pretty':_D},cookies={'cookies':cookie}).json()
		for d in req[_E]:
			try:
				h=_s%(d[_G],d[_L])
				if h in friendlist:0
				else:friendlist.append(h);print('\rSedang Mengumpulkan %s Teman'%str(len(friendlist)),end='');sys.stdout.flush()
			except Exception as e:continue
		after=req['paging']['cursors'][A];GetFriendlist(r,after)
	except KeyboardInterrupt:print(B%str(len(friendlist)))
	except Exception as e:print(B%str(len(friendlist)))
class CheckFriendlistByGraphQL:
	def __init__(self,obj):
		try:self.loop=0;self.obj=obj;self.cookie=open(_H,_B).read();self.token_eaag=open(_Q,_B).read();self.token_eaab=open(_I,_B).read();self.file_gende=_J%file_gender;self.file_mutua=_J%file_mutual
		except Exception as e:login()
	def Main(self):
		try:
			r=requests.Session();req=bs(r.get(f"https://www.facebook.com/me/friends",headers=headers_get(),cookies={_C:self.cookie},allow_redirects=_N,timeout=(10,20)).content,_K);dta=GetData(req);tabkey=re.search('{"tab_key":"friends_all","id":"(.*?)"}',str(req)).group(1)
			if self.obj==1:self.ScrapGender(r,dta,_O,tabkey)
			elif self.obj==2:self.ScrapMutual(r,dta,_O,tabkey)
		except Exception as e:print(e);print('Gagal Dump Akun\nAkun Spam/Checkpoint'if country==_A else'Failed To Dump\nAccount Spam/Checkpoint');exit()
	def ScrapGender(self,r,dta,cursor,tabkey):
		try:
			var={_t:8,_u:cursor,_a:1.5,'search':_O,_G:tabkey};dta.update({_b:_AJ,_c:json.dumps(var),_d:_N,_e:_AK});pos=r.post(_f,data=dta,headers=headers_post(),cookies={_C:self.cookie}).json()
			for x in pos[_E][_F][_V][_v]:
				try:
					id=x[_F][_g][_T][_h][_i][_j][_G];nm=x[_F][_g][_T][_h][_i][_j][_L];gd=x[_F][_g][_T][_h][_i][_j]['gender'];f=_r%(id,nm,gd)
					if f in open(self.file_gende,_B).read().splitlines():0
					else:open(self.file_gende,_S).write(_l%f);self.loop+=1;print('\rDump %s ID By Gender'%str(self.loop),end='');sys.stdout.flush()
				except Exception as e:pass
			try:
				cur=pos[_E][_F][_V][_W][_w];end=pos[_E][_F][_V][_W][_x]
				if end:self.ScrapGender(r,dta,cur,tabkey)
				else:0
			except Exception as e:pass
		except Exception as e:pass
	def ScrapMutual(self,r,dta,cursor,tabkey):
		try:
			var={_t:8,_u:cursor,_a:1.5,'search':_O,_G:tabkey};dta.update({_b:_AJ,_c:json.dumps(var),_d:_N,_e:_AK});pos=r.post(_f,data=dta,headers=headers_post(),cookies={_C:self.cookie}).json()
			for x in pos[_E][_F][_V][_v]:
				try:
					id=x[_F][_g][_T][_h][_i][_j][_G];nm=x[_F][_g][_T][_h][_i][_j][_L]
					try:mt=int(str(x[_F]['subtitle_text']['text']).split(' ')[0])
					except Exception as e:mt='0'
					f=_r%(id,nm,str(mt))
					if f in open(self.file_mutua,_B).read().splitlines():0
					else:open(self.file_mutua,_S).write(_l%f);self.loop+=1;print('\rDump %s ID By Mutual'%str(self.loop),end='');sys.stdout.flush()
				except Exception as e:pass
			try:
				cur=pos[_E][_F][_V][_W][_w];end=pos[_E][_F][_V][_W][_x]
				if end:self.ScrapMutual(r,dta,cur,tabkey)
				else:0
			except Exception as e:pass
		except Exception as e:pass
class CheckInteraction:
	def __init__(self):
		try:self.cookie=open(_H,_B).read();self.token_eaag=open(_Q,_B).read();self.token_eaab=open(_I,_B).read();self.file_inter=_J%file_interaction
		except Exception as e:login()
	def DumpLatestPost(self):
		data=[]
		if country==_A:print('Seleksi Berdasar Postingan');tkn='Berapa Post Terakhir : ';tdk='Tidak Boleh Lebih Dari 500'
		else:print('Selection Based On Posts');tkn='How Many Last Posts? : ';tdk='Cannot Be More Than 500'
		limit=int(input(tkn));print('')
		if limit>=500:print(tdk)
		else:
			try:
				l=0;r=requests.Session();req=r.get(f"https://graph.facebook.com/me/posts?fields=id&limit=1000&access_token={self.token_eaag}",headers=headers_get(),cookies={_C:self.cookie}).json()
				for i in req[_E]:
					if l==limit:break
					data.append(i[_G]);l+=1
				return data
			except Exception as e:print('Gagal Dump Postingan\nAkun Spam/Checkpoint'if country==_A else'Failed To Dump Posts\nAccount Spam/Checkpoint');exit()
	def DumpReaction(self,loop,id_post):
		try:
			r=requests.Session();req=r.get(f"https://graph.facebook.com/{id_post}?fields=reactions.summary(true).limit(10000)&access_token={self.token_eaab}",headers=headers_get(),cookies={_C:self.cookie}).json()
			for x in req['reactions'][_E]:
				try:
					o=open(self.file_inter,_B).read().splitlines();f=_s%(x[_G],x[_L])
					if f in o:0
					else:open(self.file_inter,_S).write(_l%f)
				except Exception as e:pass
				if country==_A:print(_AL%(str(len(o)),str(loop)),end='');sys.stdout.flush()
				else:print(_AM%(str(len(o)),str(loop)),end='');sys.stdout.flush()
		except Exception as e:pass
	def DumpComment(self,loop,id_post):
		A='from'
		try:
			r=requests.Session();req=r.get(f"https://graph.facebook.com/{id_post}?fields=comments.summary(true).limit(10000)&access_token={self.token_eaab}",headers=headers_get(),cookies={_C:self.cookie}).json()
			for x in req['comments'][_E]:
				try:
					o=open(self.file_inter,_B).read().splitlines();f=_s%(x[A][_G],x[A][_L])
					if f in o:0
					else:open(self.file_inter,_S).write(_l%f)
				except Exception as e:pass
				if country==_A:print(_AL%(str(len(o)),str(loop)),end='');sys.stdout.flush()
				else:print(_AM%(str(len(o)),str(loop)),end='');sys.stdout.flush()
		except Exception as e:pass
class UnFriend:
	def __init__(self):
		try:self.cookie=open(_H,_B).read();self.token_eaag=open(_Q,_B).read();self.token_eaab=open(_I,_B).read();self.loop=0;self.success=0;self.failed=0
		except Exception as e:login()
	def GetSelectedMutual(self,oper,y):
		D='Select Friend Based On Mutual First!';C='Seleksi Teman Berdasar Mutual Terlebih Dahulu!';B='No Data Mutual';A='Tidak Ada Data Mutual';removed=[]
		try:
			self.file_mutua=_J%file_mutual;self.data_mutua=open(self.file_mutua,_B).read().splitlines()
			if len(self.data_mutua)==0:print(A if country==_A else B);print(C if country==_A else D);exit('')
			else:0
		except Exception as e:print(A if country==_A else B);print(C if country==_A else D);exit('')
		for x in self.data_mutua:
			try:
				if eval('%s%s%s'%(x.split(_P)[2],oper,y)):removed.append(x.split(_P)[0])
			except Exception as e:pass
		return self.data_mutua,removed
	def GetSelectedGender(self,c):
		D='Select Friend Based On Gender First!';C='Seleksi Teman Berdasar Gender Terlebih Dahulu!';B='No Data Gender';A='Tidak Ada Data Gender';removed=[]
		try:
			self.file_gende=_J%file_gender;self.data_gende=open(self.file_gende,_B).read().splitlines()
			if len(self.data_gende)==0:print(A if country==_A else B);print(C if country==_A else D);exit('')
			else:0
		except Exception as e:print(A if country==_A else B);print(C if country==_A else D);exit('')
		for x in self.data_gende:
			try:
				if x.split(_P)[2]==c:removed.append(x.split(_P)[0])
			except Exception as e:pass
		return self.data_gende,removed
	def GetNoInteract(self):
		B='Select Friend Based On React/Comment First!';A='Seleksi Teman Berdasar Reaksi/Komentar Terlebih Dahulu!';self.no_interact=[]
		try:
			self.file_inter=_J%file_interaction;self.data_inter=open(self.file_inter,_B).read().splitlines()
			if len(self.data_inter)==0:print(_o if country==_A else _p);print(A if country==_A else B);exit('')
			else:0
		except Exception as e:print(_o if country==_A else _p);print(A if country==_A else B);exit('')
		try:
			GetFriendlist(requests.Session(),_O);to,fl=str(len(friendlist)),friendlist
			for x in fl:
				try:
					if x in self.data_inter:0
					else:self.no_interact.append(x)
				except Exception as e:pass
			return to,self.no_interact
		except Exception as e:print(e);print('Gagal Menyortir Interaksi\nAkun Spam/Checkpoint'if country==_A else'Failed To Sort Interaction\nAccount Spam/Checkpoint');exit()
	def Unfriend(self,id_target,total):
		r=requests.Session();url=_X;req=bs(r.get(url,headers=headers_get(),cookies={_C:self.cookie}).content,_K);dta=GetData(req);dta.update({_y:_z,_b:'FriendingCometUnfriendMutation',_c:json.dumps({'input':{'source':'bd_profile_button','unfriended_user_id':id_target,'actor_id':dta[_q],_AN:_D},_a:1}),_d:_N,_e:'8752443744796374'});pos=r.post(_f,data=dta,headers=headers_post(),cookies={_C:self.cookie}).json()
		if'unfriended_person'in str(pos):self.success+=1
		else:self.failed+=1
		self.loop+=1;print('\rUnfriend [%s/%s] Success:%s Failed:%s'%(str(self.loop),str(total),str(self.success),str(self.failed)),end='');sys.stdout.flush()
class AddFriend:
	def __init__(self):
		try:self.cookie=open(_H,_B).read();self.token_eaag=open(_Q,_B).read();self.token_eaab=open(_I,_B).read();self.loop=0;self.skip=0;self.success=0;self.failed=0
		except Exception as e:login()
		self.MenuAdd()
	def MenuAdd(self):
		A='Isi Yang Benar!';print('[ Tambah Dari ]');print('[1] Saran Teman');print('[2] Scrap Timeline');print('[3] Target Friendlist');x=input(_n);print('')
		if x in[_D,_Y,'a']:
			print(_AH);print('[1] Mutual');print('[2] Gender');y=input(_n);print('');z=input('Akun Laki/Perempuan [l/p] : ').lower();print('')
			if z in[_D,'l','m','laki','men']:self.gender_pilihan='MALE'
			elif z in[_R,'p',_M,_AI,'women']:self.gender_pilihan='FEMALE'
			else:print(A);exit()
			r=requests.Session();url=_X;req=bs(r.get(url,headers=headers_get(),cookies={_C:self.cookie}).content,_K);dta=GetData(req);dta.update({_y:_z,_d:_N})
			if y in[_D,_Y,'a']:0
			elif y in[_R,_Z,'b']:self.Suggestion(r,dta,2,_O)
		elif x in[_R,_Z,'b']:0
		elif x in['3',_k,'c']:0
		else:print(A);exit()
	def Suggestion(self,r,dta,type,cursor):
		B='people_you_may_know';A='viewer'
		try:
			dta.update({_b:'FriendingCometPYMKPanelPaginationQuery',_c:json.dumps({_t:30,_u:cursor,'location':'FRIENDS_CENTER',_a:1.5}),_e:'7426902770683771'});pos=r.post(_f,data=dta,headers=headers_post(),cookies={_C:self.cookie}).json()
			with ThreadPoolExecutor(max_workers=5)as TPE:
				for x in pos[_E][A][B][_v]:
					try:
						id=x[_F][_G];nm=x[_F][_L]
						if type==2:TPE.submit(self.ScrapGender,id)
					except Exception as e:pass
			try:
				cur=pos[_E][A][B][_W][_w];end=pos[_E][A][B][_W][_x]
				if end:self.Suggestion(r,dta,type,cur)
				else:0
			except Exception as e:pass
		except Exception as e:pass
	def ScrapGender(self,id):
		try:
			r=requests.Session();req=bs(r.get(f"https://www.facebook.com/{id}",headers=headers_get()).content,_K);gd=re.search('"gender":"(.*?)"',str(req)).group(1)
			if gd==self.gender_pilihan:self.Add(id)
			else:self.skip+=1
		except Exception as e:pass
		print('\rSkip:%s Success:%s Failed:%s    '%(str(self.skip),str(self.success),str(self.failed)),end='');sys.stdout.flush()
	def Add(self,target):
		r=requests.Session();url=_X;req=bs(r.get(url,headers=headers_get(),cookies={_C:self.cookie}).content,_K);dta=GetData(req);var={'input':{'attribution_id_v2':'ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1700060250257,939817,190055527696468,','friend_requestee_ids':[target],'refs':[_O],'source':'profile_button','warn_ack_for_ids':[],'actor_id':dta[_q],_AN:_D},_a:1};dta.update({_y:_z,_b:'FriendingCometFriendRequestSendMutation',_c:json.dumps(var),_d:_N,_e:'7033797416660129'});pos=r.post(_f,data=dta,headers=headers_post(),cookies={_C:self.cookie}).json()
		if'friend_requestees'in str(pos)and'OUTGOING_REQUEST'in str(pos):self.success+=1
		else:self.failed+=1
if __name__=='__main__':mod();geolocator();logo();login()
