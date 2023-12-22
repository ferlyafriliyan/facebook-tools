#--> Ini Buat Import Module
import sys, requests, json, re

#--> Buat Login Cookies
def login():
    cookie = input('Masukkan Cookies : ')
    token_eaab = generate_token_eaab(cookie)
    print('\nToken : %s\n'%(token_eaab))
    #--> Terserah Gimana Alur Kodingannya, Intinya Kirim Cookies Dan Token EAAB Ke Fungsi DumpFriendlist()
    DumpFriendlist(cookie,token_eaab) #--> Ini Yg Penting

#--> Buat Dapetin Token EAAB
def generate_token_eaab(cok):
    r = requests.Session()
    req1 = r.get('https://www.facebook.com/adsmanager/manage/campaigns',cookies={'cookie':cok},allow_redirects=True).text
    nek1 = re.search('window\.location\.replace\("(.*?)"\)',str(req1)).group(1).replace('\\','')
    req2 = r.get(nek1,cookies={'cookie':cok},allow_redirects=True).text
    tok  = re.search('accessToken="(.*?)"',str(req2)).group(1)
    return(tok)

#--> Buat Control Dump Kamu, Input Dan Output Dari Sini
def DumpFriendlist(cok, tok):
    result = []
    print('Banyak ID, Pisahkan Dengan Koma (,)')
    lid = input('Masukkan ID : ').split(',')
    print('')
    print('Tekan ctrl+c Untuk Berhenti')
    for id in lid:
        try:
            r = requests.Session()
            url = f'https://graph.facebook.com/v12.0/{id}/friends'
            LoopDump(r, cok, tok, url, result, None)
        except KeyboardInterrupt: pass
        except Exception as e: pass
    print("\rBerhasil Dump %s ID                  "%(str(len(result))) )
    print('')
    print(result) #--> ID Kesimpen Disini, Kirim Aja Ke Def Lain Buat Crack

#--> Buat Ngelooping Dump
def LoopDump(r, cok, tok, url, dump, after):
    try:
        dta = {'access_token':tok,'after':after,'pretty':'1'}
        req = r.get(url,params=dta,cookies={'cookies':cok}).json()
        if 'temporarily blocked' in str(req):
            print('Oops, Sepertinya Akunmu Spam!')
            exit('')
        for d in req['data']:
            try:
                h = '%s|%s'%(d['id'],d['name'])
                if h in dump: pass
                else: dump.append(h)
                print('\rSedang Dump %s ID'%(str(len(dump))),end=''); sys.stdout.flush()
            except Exception as e: continue
        after = req['paging']['cursors']['after']
        LoopDump(r,cok,tok,url,dump,after)
    except KeyboardInterrupt: pass
    except Exception as e: pass

if __name__ == '__main__':
    login()