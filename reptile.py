"""
Time:2021/5/6 12:07
Author:中庸猿
奋斗不止，赚钱不停
"""
from datetime import datetime
import requests
from re import findall
import os


def public_opinion(stock=''):
    today = datetime.now().strftime('%Y%m%d')
    print(today)
    if not os.path.exists("./option_data/" + today + stock + ".csv"):
        url = 'http://guba.eastmoney.com/list,' + stock + ',99.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
            'Cookie': 'intellpositionL=1215.35px; HAList=a-sh-600016-%u6C11%u751F%u94F6%u884C; em_hq_fls=js; emshistory=%5B%22600016%22%5D; intellpositionT=985.4px; qgqp_b_id=e3079f6f91e0549994ee953c115a52ac; st_si=44583305646846; st_asi=delete; st_pvi=33164132190652; st_sp=2020-12-29%2022%3A03%3A33; st_inirUrl=https%3A%2F%2Fwww.eastmoney.com%2F; st_sn=15; st_psi=20210509134619451-117001300541-4431745685'
        }

        response = requests.get(url, headers=headers)
        print(response)
        if response.status_code == 200:
            re_str = r'<span class="l3 a3"><a href=".*" title="(.*)">'
            result = findall(re_str, response.text)
            with open("./option_data/" + today + stock + ".csv", mode='w', encoding='utf8') as f:
                f.write(str(result))
        else:
            return 0

    with open("./option_data/" + today + stock + ".csv", encoding='utf8') as f:
        result = eval(f.read())
        str_result = '\n'.join([i for i in result])

    return str_result




