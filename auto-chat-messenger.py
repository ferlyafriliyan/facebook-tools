###----------[ AUTHOR ]---------- ###
Author = 'Dapunta Khurayra X'
Version = 0.1
Facebook = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/ratya.anonym.id'

# --> Modules
import requests,bs4,sys,os,datetime,re,time,json
from bs4 import BeautifulSoup as bs
from datetime import datetime

# -->  Clear Terminal
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

# --> Waktu
def start():
    global Mulai_Jalan
    Mulai_Jalan = datetime.now()
def akhir():
    global Akhir_Jalan, Total_Waktu
    Akhir_Jalan = datetime.now()
    Total_Waktu = Akhir_Jalan - Mulai_Jalan
    try:
        Menit = str(Total_Waktu).split(':')[1]
        Detik = str(Total_Waktu).split(':')[2].replace('.',',').split(',')[0] + ',' + str(Total_Waktu).split(':')[2].replace('.',',').split(',')[1][:1]
        print('\nProgram Selesai Dalam Waktu %s Menit %s Detik\n'%(Menit,Detik))
    except Exception as e:
        print('\nProgram Selesai Dalam Waktu 0 Detik\n')

# --> Login
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
            auto_chat_messenger()
        except Exception as e:
            self.cookie_invalid()
    def cookie_invalid(self):
        print('\nCookie Invalid!')
        time.sleep(2)
        clear()
        self.insert_cookie()
    def insert_cookie(self):
        print('Apabila Akun A2F On, Pergi Ke')
        print('https://business.facebook.com/business_locations')
        print('Untuk Memasukkan Kode Autentikasi')
        ciko = input('Masukkan Cookie : ')
        toke = self.generate_token(ciko)
        try:os.mkdir("login")
        except:pass
        open('login/cookie.json','w').write(ciko)
        open('login/token.json','w').write(toke)
        self.cek_cookies()
    def generate_token(self,cok):
        try:
            url = 'https://business.facebook.com/business_locations'
            req = self.xyz.get(url,cookies={'cookie':cok})
            tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
            return(tok)
        except Exception as e:exit(main())

class auto_chat_messenger:
    
    # --> Trigger
    def __init__(self):
        self.gagal    = 0
        self.berhasil = 0
        self.for_loop = 0
        self.tararget = []
        self.listchat = []
        self.datapend = {}
        self.all_history = []
        self.xyz = requests.Session()
        self.cookie = {'cookie':open('login/cookie.json','r').read()}
        self.token  = self.generate_token()
        self.menu()

    # --> Generate Token
    def generate_token(self):
        try:
            url = 'https://business.facebook.com/business_locations'
            req = self.xyz.get(url,cookies=self.cookie)
            tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
            return(tok)
        except Exception as e:exit('\nCookies Invalid\n')

    # --> Main Menu Chat
    def menu(self):
        print('[ Menu Spam Chat ]')
        print('[1] Manual')
        print('[2] Otomatis (Banyak)')
        print('[3] Hapus Chat')
        xa = input('Pilih : ')
        print('')
        if xa in ['1','01','a']:
            print('[ Menu Spam Chat Manual ]')
            print('[1] Input Target Berdasar ID')
            print('[2] Pilih Target Dari Riwayat Chat')
            print('[3] Pilih Target Dari Daftar Teman')
            xb = input('Pilih : ')
            print('')
            if   xb in ['1','01','a']: self.manual_input(); self.tulis_chat(); self.jumlah_chat(); self.kalkulasi(); self.sortir()
            elif xb in ['2','02','b']: self.choice_input_scrap('https://mbasic.facebook.com/messages/read'); self.pilih_riwayat_scrap('Dapunta'); self.tulis_chat(); self.jumlah_chat(); self.kalkulasi(); self.sortir()
            elif xb in ['3','03','c']: self.choice_input_graph('https://graph.facebook.com/me?fields=friends.fields(id,name)&limit=5000&access_token='+self.token); self.pilih_riwayat_graph('Dapunta'); self.tulis_chat(); self.jumlah_chat(); self.kalkulasi(); self.sortir()
            else:exit('\nIsi Yang Benar !\n')
        elif xa in ['2','02','b']:
            print('[ Menu Spam Chat Otomatis ]')
            print('[1] Spam Chat Semua Riwayat Chat')
            print('[2] Spam Chat Semua Daftar Teman')
            xc = input('Pilih : ')
            print('')
            if   xc in ['1','01','a']: self.choice_input_scrap('https://mbasic.facebook.com/messages/read'); self.pilih_riwayat_scrap('SuciMHR'); self.tulis_chat(); self.jumlah_chat(); self.kalkulasi(); self.sortir()
            elif xc in ['2','02','b']: self.choice_input_graph('https://graph.facebook.com/me?fields=friends.fields(id,name)&limit=5000&access_token='+self.token); self.pilih_riwayat_graph('SuciMHR'); self.tulis_chat(); self.jumlah_chat(); self.kalkulasi(); self.sortir()
            else:exit('\nIsi Yang Benar !\n')
        elif xa in ['3','03','c']:
            print('[ Menu Hapus Chat ]')
            print('[1] Hapus Semua Riwayat Chat')
            print('[2] Hapus Chat Pilihan')
            print('[3] Hapus Chat Kecuali')
            xd = input('Pilih : ')
            print('')
            if   xd in ['1','01','a']: self.choice_input_scrap('https://mbasic.facebook.com/messages/read'); self.pilih_riwayat_scrap('SuciMHR'); self.sortir_delete()
            elif xd in ['2','02','b']: self.choice_input_scrap('https://mbasic.facebook.com/messages/read'); self.pilih_riwayat_scrap('Dapunta'); self.sortir_delete()
            elif xd in ['3','03','c']: self.choice_input_scrap('https://mbasic.facebook.com/messages/read'); self.pilih_riwayat_scrap('Rancay');  self.sortir_delete()
            else:exit('\nIsi Yang Benar !\n')
        else:
            exit('\nIsi Yang Benar !\n')

    # --> Input Manual Berdasar ID
    def manual_input(self):
        print('Banyak Target? Pisahkan Dengan Koma (,)')
        id  = input('Masukkan ID Target : ').split(',')
        for x in id:
            self.tararget.append(x) # --> Array ID

    # --> Pilih Berdasar Riwayat Chat
    def choice_input_scrap(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for x in req.find_all('h3'):
                try:
                    y = x.find('a',href=True)
                    if str(y) == 'None': pass
                    else:
                        z = re.search('tid=(.*?)&amp',str(y)).group(1).split('.')[2].split('%')[0]
                        self.for_loop += 1
                        print('[%s] %s'%(str(self.for_loop),y.text[:30]))
                        self.all_history.append(z)
                        self.datapend.update({str(self.for_loop):z})
                except Exception as e:pass
            net = 'https://mbasic.facebook.com' + req.find('a',string='Lihat Pesan Sebelumnya')['href']
            self.choice_input_scrap(net)
        except Exception as e:pass
    def pilih_riwayat_scrap(self,tp):
        if tp == 'Dapunta':
            print('\nBanyak Target? Pisahkan Dengan Koma (,)')
            xd = input('Pilih : ').split(',')
            for x in xd:
                self.tararget.append(self.datapend[x]) # --> Array ID
        elif tp == 'Rancay':
            print('\nKecualikan Chat? Pisahkan Dengan Koma (,)')
            xx = input('Pilih : ').split(',')
            for d in xx:
                self.all_history.remove(str(self.datapend[d]))
            self.tararget = self.all_history # --> Array ID
        else:
            self.tararget = self.all_history # --> Array ID
    
    # --> Pilih Berdasar Daftar Teman
    def choice_input_graph(self,url):
        try:
            req = self.xyz.get(url,cookies=self.cookie).json()
            for x in req['friends']['data']:
                try:
                    self.for_loop += 1
                    print('[%s] %s'%(str(self.for_loop),x['name'][:30]))
                    self.all_history.append(x['id'])
                    self.datapend.update({str(self.for_loop):x['id']})
                except Exception as e:pass
        except Exception as e:exit('\nTeman Tidak Ditemukan')
    def pilih_riwayat_graph(self,tp):
        if tp == 'Dapunta':
            print('\nBanyak Target? Pisahkan Dengan Koma (,)')
            xd = input('Pilih : ').split(',')
            for x in xd:
                self.tararget.append(self.datapend[x]) # --> Array ID
        else:
            self.tararget = self.all_history # --> Array ID

    # --> Pilihan Opsi Lain
    def tulis_chat(self):
        print('\nBanyak Chat? Pisahkan Dengan (<>)')
        chat = input('Tulis Chat : ').split('<>')
        for x in chat:
            self.listchat.append(x) # --> Array Chat
        if len(chat) > 1:self.choice_chat()
        else:self.urut_chat = False
    def jumlah_chat(self):
        self.jc = input('\nJumlah Kelipatan Tiap Chat : ') # --> Jumlah Masing² Chat
    def choice_chat(self):
        print('\n[ Pilih Urutan Chat ]')
        print('[1] A, B, A, B, A, B')
        print('[2] A, A, A, B, B, B')
        xd = input('Pilih : ')
        if   xd in ['1','01','a']: self.urut_chat = 'bolak'
        elif xd in ['2','02','b']: self.urut_chat = 'balik'
        else:exit('\nIsi Yang Benar !\n')
    def kalkulasi(self):
        print('\n[ Kalkulasi ]')
        print('Jenis Chat            : %s'%(str(len(self.listchat))))
        print('Jumlah Penerima       : %s'%(str(len(self.tararget))))
        print('Jumlah Kelipatan Chat : %s'%(str(int(self.jc))))
        print('Total %s Chat Akan Dikirim\n'%(str(len(self.listchat)*len(self.tararget)*int(self.jc))))

    # --> Sortir Chat & Target
    def sortir(self):
        if self.urut_chat == 'balik':
            for x in self.tararget:
                self.perorangan_berhasil = 0
                self.perorangan_gagal    = 0
                for y in self.listchat:
                    for s in range(int(self.jc)):
                        self.exec(x,y)
                try:
                    print('\rSpam Chat %s                      '%(self.nama[:20]))
                    print('\r   • Berhasil : %s                      '%(str(self.perorangan_berhasil)))
                    print('\r   • Gagal    : %s                      '%(str(self.perorangan_gagal)))
                    print('\r')
                except Exception as e:pass
        else:
            for x in self.tararget:
                self.perorangan_berhasil = 0
                self.perorangan_gagal    = 0
                for s in range(int(self.jc)):
                    for y in self.listchat:
                        self.exec(x,y)
                try:
                    print('\rSpam Chat %s                      '%(self.nama[:20]))
                    print('\r   • Berhasil : %s                      '%(str(self.perorangan_berhasil)))
                    print('\r   • Gagal    : %s                      '%(str(self.perorangan_gagal)))
                    print('\r')
                except Exception as e:pass

    # --> Requests Post Message
    def exec(self,id,cet):
        url = 'https://mbasic.facebook.com/messages/thread/'+id
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            fom = req.find('form',{'method':'post'})
            try:
                data = {
                    'fb_dtsg'      : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
                    'jazoest'      : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
                    'tids'         : re.search('name="tids" type="hidden" value="(.*?)"',   str(fom)).group(1),
                    'csid'         : re.search('name="csid" type="hidden" value="(.*?)"'   ,str(fom)).group(1),
                    'cver'         : 'legacy',
                    'ids[%s]'%(id) : id,
                    'wwwupp'       : 'C3',
                    'platform_xmd' : ''}
            except Exception as e:
                data = {
                    'fb_dtsg'      : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
                    'jazoest'      : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
                    'ids[%s]'%(id) : id}
            data.update({'body':cet,'send':'Kirim'})
            nek = 'https://mbasic.facebook.com' + fom['action']
            cuy = bs(self.xyz.post(nek,data=data,cookies=self.cookie).content,'html.parser').find('title').text
            if cuy == 'Kesalahan':
                self.gagal += 1
                self.perorangan_gagal += 1
                print('\r[Proses] [Berhasil:%s] [Gagal:%s]'%(str(self.berhasil),str(self.gagal)),end='');sys.stdout.flush()
            else:
                self.berhasil += 1
                self.perorangan_berhasil += 1
                self.nama = cuy
                print('\r[Proses] [Berhasil:%s] [Gagal:%s]'%(str(self.berhasil),str(self.gagal)),end='');sys.stdout.flush()
        except Exception as e:pass

    # --> Delete Chat
    def sortir_delete(self):
        self.delchat = 0
        for id in self.tararget:
            url = 'https://mbasic.facebook.com/messages/thread/'+id
            self.delete1(url)
    def delete1(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            fom = req.find_all('form',{'method':'post'})[1]
            data = {
                'fb_dtsg'      : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
                'jazoest'      : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
                'delete'       : 'Hapus'}
            nek = 'https://mbasic.facebook.com' + fom['action']
            self.delete2(nek,data)
        except Exception as e:pass
    def delete2(self,url,data):
        try:
            req = bs(self.xyz.post(url,data=data,cookies=self.cookie).content,'html.parser')
            got = req.find('a',string='Hapus')['href']
            nok = 'https://mbasic.facebook.com'+got
            roq = bs(self.xyz.get(nok,cookies=self.cookie).content,'html.parser')
            self.delchat += 1
        except Exception as e:
            pass
        print('\rBerhasil Menghapus %s Chat'%(str(self.delchat)),end='');sys.stdout.flush()

if __name__=='__main__':
    clear()
    start()
    main()
    akhir()