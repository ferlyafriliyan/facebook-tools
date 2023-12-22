import os, re, sys, json, requests
from bs4 import BeautifulSoup as par
from time import sleep as facetime

P = "\x1b[1;97m"  # PUTIH
M = "\x1b[1;91m"  # MERAH
H = "\x1b[1;92m"  # HIJAU
K = "\x1b[1;93m"  # KUNING
B = "\x1b[1;94m"  # BIRU
U = "\x1b[1;95m"  # UNGU
O = "\x1b[1;96m"  # ORANGE
N = "\x1b[0m"  # DEFAULT


def clear():
    os.system("cls" if os.name == "nt" else "clear")


class GetCookieFB:
    def __init__(self):
        self.LoginCookie()

    def LoginCookie(self):
        print(
            " %s[%s‰%s] input ID/Email dengan benar, kalo salah maka terjadi nyetuk :v"
            % (N, H, N)
        )
        userid = input(" %s[%s‰%s] ID/Email %s: " % (N, H, N, H))
        userpas = input(" %s[%s‰%s] Sandi %s: " % (N, H, N, H))
        response = requests.get(
            "https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8"
        ).text
        lsd = re.search('name="lsd" value="(.*?)"', str(response)).group(1)
        jazoest = re.search('name="jazoest" value="(\d+)"', str(response)).group(1)
        m_ts = re.search('name="m_ts" value="(.*?)"', str(response)).group(1)
        li = re.search('name="li" value="(.*?)"', str(response)).group(1)
        while True:
            try:
                with requests.Session() as r:
                    r.headers.update(
                        {
                            "Host": "mbasic.facebook.com",
                            "Cache-Control": "max-age=0",
                            "Upgrade-Insecure-Requests": "1",
                            "Sech-Ch-Ua": "Chrome",
                            "Sec-Ch-Ua-Mobile": "?0",
                            "Sec-Ch-Ua-Platform": '"Linux"',
                            "Sec-Ch-Ua-Platform-version": '"10.0.0"',
                            "Sec-Ch-Ua-Model": '""',
                            "Origin": "https://mbasic.facebook.com",
                            "Content-Type": "application/x-www-form-urlencoded",
                            "X-FB-lsd": lsd,
                            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                            "X-Requested-With": "com.android.chrome",
                            "Sec-Fetch-Site": "none",
                            "Sec-Fetch-Mode": "navigate",
                            "Sec-Fetch-User": "?1",
                            "Sec-Fetch-Dest": "document",
                            "Accept": "*/*",
                            "Referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
                            "Accept-Encoding": "gzip, deflate br",
                            "Accept-Language": "en-US;q=0.8,en;q=0.9",
                            "View-Width": "980",
                            "Connection": "Keep-Alive",
                        }
                    )
                    params = {
                        "lsd": lsd,
                        "jazoest": jazoest,
                        "m_ts": m_ts,
                        "li": li,
                        "try_number": 0,
                        "unrecognized_tries": 0,
                        "email": userid,
                        "pass": userpas,
                        "login": "Log + In",
                        "bi_xrwh": 0,
                    }
                    response = r.post(
                        "https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
                        data=params,
                        cookies={
                            "cookie": ";".join(
                                [
                                    "%s=%s" % (name, value)
                                    for name, value in r.cookies.get_dict().items()
                                ]
                            )
                        },
                    )
                    while True:
                        try:
                            payload = r.cookies.get_dict()
                            if "c_user" in payload.keys():
                                cookies = ";".join(
                                    [
                                        "%s=%s" % (name, value)
                                        for name, value in r.cookies.get_dict().items()
                                    ]
                                )
                                clear()
                                print(
                                    " %s[%s‰%s] Cookie %s: %s" % (N, H, N, H, cookies)
                                )
                                with open(".Cookie.txt", "w") as wr:
                                    wr.write(f"{cookies}")
                                    wr.close()
                                self.Token_Eaag(r, cookies)
                                sys.exit(
                                    " %s[%s‰%s] Suckses, silakan jalankan ulang perintahnya"
                                    % (N, H, N)
                                )
                                break
                            elif "checkpoint" in payload.keys():
                                sys.exit(
                                    " %s[%s‰%s] Checkpoint, silakan ganti tumbal"
                                    % (N, K, N)
                                )
                                break
                            else:
                                continue
                        except (Exception) as e:
                            sys.exit(e)
            except (requests.exceptions.ConnectionError) as e:
                sys.exit(e)

    def Token_Eaag(self, r, cookies):
        try:
            r.headers.update(
                {
                    "Host": "business.facebook.com",
                    "Cache-Control": "max-age=0",
                    "Upgrade-Insecure-Requests": "1",
                    "Sech-Ch-Ua": "Chrome",
                    "Sec-Ch-Ua-Mobile": "?0",
                    "Sec-Ch-Ua-Platform": '"Linux"',
                    "Sec-Ch-Ua-Platform-version": '"10.0.0"',
                    "Sec-Ch-Ua-Model": '""',
                    "Origin": "https://business.facebook.com",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "X-Requested-With": "com.android.chrome",
                    "Sec-Fetch-Site": "none",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-User": "?1",
                    "Sec-Fetch-Dest": "document",
                    "Accept": "*/*",
                    "Referer": "https://business.facebook.com/login/?next=https%3A%2F%2Fbusiness.facebook.com%2F%3Fnav_ref%3Dbizweb_landing_fb_login_button%26biz_login_source%3Dbizweb_landing_fb_login_button&refsrc=deprecated&_rdr",
                    "Accept-Encoding": "gzip, deflate br",
                    "Accept-Language": "en-US;q=0.8,en;q=0.9",
                    "View-Width": "980",
                    "Connection": "Keep-Alive",
                }
            )
            params = {
                "next": "https://business.facebook.com/?nav_ref=bizweb_landing_fb_login_button&biz_login_source=bizweb_landing_fb_login_button",
                "ref": "dbl",
                "fl": "",
                "login_from_aymh": "1",
            }
            get_tok = r.get(
                "https://business.facebook.com/business_locations",
                data=params,
                cookies={"cookie": cookies},
            ).text
            token = re.search('(\["EAAG\w+)', get_tok).group(1).replace('["', "")
            with open(".Tookie.txt", "w") as wr:
                wr.write(f"{token}")
                wr.close()
            print(" %s[%s‰%s] Token %s: %s" % (N, H, N, H, token))
            return token
        except (Exception) as e:
            sys.exit(e)


if __name__ == "__main__":
    try:
        GetCookieFB()
    except (Exception) as e:
        print(e)
