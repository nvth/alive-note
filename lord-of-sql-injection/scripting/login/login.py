import requests


def get_cookie():
    uid = 'nvth'
    upw = 'Vboync1997'

    session = requests.Session() 

    url_logon = 'https://los.rubiya.kr/?login'
    post_data = {
        'id': uid,
        'pw': upw
    }

    resp = session.post(url_logon, data=post_data)

    if '<script>location.href=\'./gate.php\';</script>' in resp.text:
        url_gate = 'https://los.rubiya.kr/gate.php'
        session_gate = session.get(url_gate)
        print('Accessing to gate.php')

        my_cookie = session.cookies.get('PHPSESSID')
        
        if my_cookie:
            my_str_cookie = str(my_cookie)
            print('Cookie from gate.php:', my_str_cookie)
            return my_str_cookie
        else:
            print('Cookie PHPSESSID not found in session cookies')
            return None
    else:
        print('Login unsuccessful')
        return None
    return my_str_cookie

#get_cookie()