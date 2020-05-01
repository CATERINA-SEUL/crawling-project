genres = {
    'all': '전체',
    '01': "드라마",
    '02': "예능",
}

def wavve(genre, offset, page):

    url = f'https://apis.pooq.co.kr/cf/vod/popularcontents?\
    WeekDay=all&broadcastid=6339&came=broadcast&contenttype=vod&genre={genre}&limit=20&offset={offset}&\
    orderby=viewtime&page={page}&uiparent=GN2-VN2&\
    uirank=2&uitype=VN2&apikey=E5F3E0D30947AA5440556471321BB6D9&credential=none&device=pc&\
    drm=wm&partner=pooq&pooqzone=none&region=kor&targetage=auto'

    resp = requests.get(url)
    datas = resp.json()['cell_toplist']['celllist']

    wavve_list = []

    for data in datas:

        title = data['title_list'][0]['text']
        count = data['title_list'][1]['text'].split('$')[0]
        print(data['title_list'][1]['text'])
        try :
                
            date = data['title_list'][1]['text'].split('$')[2]
        
        except:
            
            count = 0
            date = data['title_list'][1]['text'].split('$')[0]
            

        wavve_list.append({

            'title': title,
            'episode': count,
            'date': date,
            'category': genre,
            'page': page,
        })

    return pd.DataFrame(wavve_list)