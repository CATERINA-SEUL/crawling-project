tv_channels = {
    
    '1':'지상파',
    '2':'종편',
    '3':'케이블',
}

from datetime import datetime, timedelta

def program_percentage(tv_channel,days_):

    url = f'http://nielsenkorea.co.kr/tv_terrestrial_day.asp?menu=Tit_1&sub_menu={tv_channel}_1&area=01&begin_date={days_}'

    params = {
        'sYear': '2020',
        'sMonth': '03',
        'sDay': '08',
    }
    resp = requests.post(url, headers=params)
    soup = BeautifulSoup(resp.content, 'html.parser')

    days_range = []
    rank_list = []
    pg_list = []
    bs_list = []
    rate_list = []
    ch_list = []
    datas = []
    
    # 날짜
    start = (now+timedelta(days = -14))
    end = datetime.now()
    date_generated = [start + timedelta(days=x) for x in range(0, (end-start).days)]
    days_range = [date_.strftime("%Y%m%d") for date_ in date_generated] 
    
    # columns
    ranks = soup.select('.tb_txt_center')
    broadcasts = soup.select('.tb_txt_center')
    programs = soup.select('table.ranking_tb .tb_txt')
    rates_10 = soup.select('table.ranking_tb .percent')
    rates_20 = soup.select('table.ranking_tb .percent_g')
    rates_all = rates_10[:10]+rates_20[:10]

    rank_list = [rank.text.split('\t')[0] for rank in ranks[0:40:2]]
    bs_list = [broadcast.text.split('\t')[0]
               for broadcast in broadcasts[1:40:2]]
    pg_list = [program.text.split('\t')[0] for program in programs[0:20]]
    rate_list = [rate.text.strip() for rate in rates_all]
        
    datas = pd.DataFrame({'rank': rank_list,
                       'program': pg_list,
                       'broadcast': bs_list,
                       'rate': rate_list,})

    return datas