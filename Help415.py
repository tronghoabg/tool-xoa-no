import requests
import base64

def main(work, r, session):
    data = init415(session)
    work.signal.emit({'stt': r, 'progress': 8})
    eav = data['eav']
    jazoest = data['jazoest']
    fb_dtsg = data['fb_dtsg']
    arrAds = data['arrAds']
    if len(arrAds) == 0:
        work.signal.emit({'stt': r, 'progress': 15})
        return
    for ads in arrAds:
        flag_result = "TRY"
        count=0
        while(flag_result == "TRY"):
            count+=1
            data = getLinkCaptcha(session, eav, jazoest, fb_dtsg)
            work.signal.emit({'stt': r, 'progress': 9})
            persist = data['persist']
            imgbase64 = data['imgbase64']
            #captcha = solveCaptcha(imgbase64)
            captcha = "test"
            work.signal.emit({'stt': r, 'progress': 10})
            content = work.txtContent.toPlainText()
            flag_result =  send415(session, eav, fb_dtsg, jazoest, ads , persist, captcha, content)
            if count>5:
                flag_result = "ERR"
            if flag_result == "TRY":
                work.signal.emit({'stt': r, 'progress': 11})
            elif flag_result == "PASS":
                work.signal.emit({'stt': r, 'progress': 12})
            else:
                work.signal.emit({'stt': r, 'progress': 13})

def init415(session):
    res  = session.get('https://mbasic.facebook.com/help/contact/211878790360415').text
    flag_eav = res.find('/a/help/contact_us/?eav=')
    if flag_eav < 0:
        obj = {
            'eav': 'No eav',
            'jazoest': 'jazoest',
            'fb_dtsg': 'fb_dtsg',
            'arrAds': []
        }
        return obj
    eav = res.split('/a/help/contact_us/?eav=')[1].split('&')[0]
    jazoest = res.split('name="jazoest" value="')[1].split('"')[0]
    fb_dtsg = res.split('name="fb_dtsg" value="')[1].split('"')[0]
    textAds = res.split('name="ad_account_selector">')[1].split('</select>')[0].split('<option value="')
    arrAds = []
    for ads in textAds:
        if ads != '':
            id = ads.split('"')[0]
            arrAds.append(id)
    obj = {
        'eav': eav,
        'jazoest': jazoest,
        'fb_dtsg': fb_dtsg,
        'arrAds': arrAds
    }
    return obj
def getLinkCaptcha(session,eav, jazoest, fb_dtsg):
    params = {
        'eav': eav,
        'paipv':'0'
    },
    payload = {
    'fb_dtsg':fb_dtsg,
    'jazoest': jazoest,
    'contact_form_id':'391647094929792',
    'ad_account_selector': 'test',
    'Field2287273754878414':'',
    'form_id':'211878790360415',
    'support_form_hidden_fields':'[]',
    'support_form_fact_false_fields':'[]'
    }
    get_link_captcha = session.post('https://mbasic.facebook.com/a/help/contact_us/', params=params , data=payload).text
    persist = get_link_captcha.split('name="captcha_persist_data" value="')[1].split('"')[0]

    payload = {
            'captcha_challenge_code':get_link_captcha.split('captcha_challenge_code=')[1].split('&')[0],
            'captcha_challenge_hash':get_link_captcha.split('captcha_challenge_hash')[1]
    }
    captcha_data = session.get('https://mbasic.facebook.com/captcha/tfbimage.php', params=payload).content
    imgbase64 = base64.b64encode(captcha_data).decode()
    obj = {
        'persist': persist,
        'imgbase64': imgbase64 
    }
    return obj

def solveCaptcha(base64):
    data = {
        'apikey':'1dde9936759641680fc259d636b26c28',
        'img':base64,
        'type':6
    }
    res = requests.post('https://anticaptcha.top/api/captcha',json=data).json()
    captcha = res['captcha']
    return captcha
                                
def send415(session, eav, fb_dtsg, jazoest, ads_acc, persist, captcha, content):
    params = {
        'eav': eav,
        'paipv':'0'
        }
    payload = {
        'fb_dtsg':fb_dtsg,
        'jazoest': jazoest,
        'captcha_persist_data': persist,
        'captcha_response': captcha,
        'contact_form_id':'391647094929792',
        'ad_account_selector': ads_acc,
        'Field2287273754878414': content,
        'Field329072362080467[0]':  'You traveled within the last 60 days',
        'form_id':'211878790360415',
        'support_form_hidden_fields':'[]',
        'support_form_fact_false_fields':'[]',
        '_orig_post_vars': 'jazoest,contact_form_id,ad_account_selector,Field2287273754878414,Field329072362080467,form_id,support_form_hidden_fields,support_form_fact_false_fields',
        'captcha_attempt': '1',
        'captcha_submit_text': 'Send'
    }
    res = session.post('https://mbasic.facebook.com/a/help/contact_us/', params=params, data=payload).text  
    flag_check_err = res.find('captcha_persist_data')
    if flag_check_err>0:
        return "TRY"
    else:
        flag_check_logined = res.find('FB4BResponsiveMain')
        if flag_check_logined > 0:
            return "PASS"
        else:
            return "ERR"