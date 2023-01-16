import requests

def start(work, r, acc, password, twoFa):
    content = work.txtContent.toPlainText()
    work.signal.emit({'stt': r, 'progress': 1})
    session = requests.Session()
    headers = {
            'authority': 'm.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
            'origin': 'https://m.facebook.com',
            'referer': 'https://www.facebook.com',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }
    session.headers = headers
    res = session.get('https://mbasic.facebook.com').text
    lsd = res[int(res.find('name="lsd"')) + 18 : int(res.find('name="lsd"')) + 29]
    payload = {
        'email': acc,
        'pass': password,
        'lsd': lsd
    }
    res = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8', data=payload).text
    try:
        fb_dtsg = res.split('name="fb_dtsg" value="')[1].split('"')[0]
    except:
        work.signal.emit({'stt': r, 'progress': 14})
        return
    jazoest = res.split('name="jazoest" value="')[1].split('"')[0]
    nh = res.split('nh" value="')[1].split('"')[0]
    code2fa = requests.get('https://2fa.live/tok/' + twoFa).json()['token']
    work.signal.emit({'stt': r, 'progress': 2})
    payload = {
        'fb_dtsg':fb_dtsg,
        'jazoest':jazoest,
        'nh': nh,
        'checkpoint': '',
        'approvals_code': code2fa,
        'codes_submitted': 0,
        'submit[Submit Code]': 'Submit Code',
        'fb_dtsg':fb_dtsg,
        'jazoest':jazoest,
    }
    res = session.post('https://mbasic.facebook.com/login/checkpoint/', data=payload).text
    work.signal.emit({'stt': r, 'progress': 3, '2fa': code2fa})
    flag_checkpoint = res.find('id="checkpoint_title"')
    count=0
    res = res
    while(flag_checkpoint>0):
        count+=1
        payload = {}
        flag_savebrowser = res.find('value="save_device"')
        flag_thiswasme = res.find('name="submit[This was me]"')
        if flag_savebrowser > 0:
            payload = {
            'fb_dtsg':fb_dtsg,
            'jazoest':jazoest,
            'nh': nh,
            'checkpoint_data': '',
            'name_action_selected': 'save_device',
            'submit[Continue]': 'Continue',
            'fb_dtsg':fb_dtsg,
            'jazoest':jazoest,
            }
            work.signal.emit({'stt': r, 'progress': 5})
        if flag_thiswasme > 0: 
            payload = {
                'fb_dtsg':fb_dtsg,
                'jazoest':jazoest,
                'checkpoint_data': '',
                'submit[This was me]': 'This was me',
                'nh': nh,
                'fb_dtsg':fb_dtsg,
                'jazoest':jazoest,
            }
            work.signal.emit({'stt': r, 'progress': 4})
        if flag_savebrowser < 0 and flag_thiswasme< 0:
            payload = {
            'fb_dtsg':fb_dtsg,
            'jazoest':jazoest,
            'nh': nh,
            'checkpoint_data': '',
            'submit[Continue]': 'Continue',
            'fb_dtsg':fb_dtsg,
            'jazoest':jazoest,
            }
        res = session.post('https://mbasic.facebook.com/login/checkpoint/', data=payload).text
        flag_checkpoint =  res.find('id="checkpoint_title"')
        if count>10:
            flag_checkpoint=0
    payload = {
        'fb_dtsg':fb_dtsg,
        'jazoest':jazoest,
        'nh': nh,
        'checkpoint_data': '',
        'name_action_selected': 'save_device',
        'submit[Continue]': 'Continue',
        'fb_dtsg':fb_dtsg,
        'jazoest':jazoest,
        }
    res = session.post('https://mbasic.facebook.com/login/checkpoint/', data=payload).text
    flag_logined = res.find('id="mbasic_logout_button"')
    if flag_logined>0:
        work.signal.emit({'stt': r, 'progress': 6})
        return session
    work.signal.emit({'stt': r, 'progress': 7})
    return

