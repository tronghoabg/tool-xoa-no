import requests

def main(work, r, session):

    user_id = work.user_id
    work.signal.emit({'stt': r, 'progress': 16})
    url = 'https://mbasic.facebook.com'
    res = session.get(url + '/'  + user_id).text
    flag_add_friead = res.find('/a/friends')
    if flag_add_friead > 0:
        link = res.split('/a/friends')[1].split('"')[0]
        link = url + '/a/friends' + link
        link = link.replace('amp;', '')
        id_me = res.split('lst=')[1].split('%')[0]
        res = session.get(link).text
        print(res)
        work.signal.emit({'stt': r, 'progress': 17})
        x = appcept_friend(work.ssViaShare, id_me)
        return
    flag_add_friead = res.find('/removefriend.php')
    if flag_add_friead>0:
        work.signal.emit({'stt': r, 'progress': 19})
        return
    work.signal.emit({'stt': r, 'progress': 18})
    return

def appcept_friend(ssViaShare, id_via_clone):
    url = 'https://mbasic.facebook.com'
    res = ssViaShare.get(url + '/'  + id_via_clone).text
    print(1)
