"""
Time:2021/4/17 13:28
Author:中庸猿
奋斗不止，赚钱不停    
"""
import function
import requests
import models
import time
from concurrent.futures.thread import ThreadPoolExecutor

number = 0
token = 'c43d43d2f232eba8a6c58928cb248be964fb271fa3ab48d2b9a60d40'
url = 'http://api.waditu.com'

SSE_50 = function.print_stock_basic()
length = len(SSE_50['depts'])
SSE_50 = SSE_50['depts']


# print(SSE_50['depts'])

def save_monthly(SSE_50):
    number = 0
    with ThreadPoolExecutor(max_workers=100) as pool:

        for i in SSE_50:
            # time.sleep(2)
            # time.sleep(1)
            params_monthly = {
                "ts_code": str(i),
                "start_date": "20200101",
                "end_date": "20210416"
            }
            json_daily_basic = {
                "api_name": "monthly",
                "token": token,
                "params": params_monthly,
                "fields": ""
            }
            response = requests.post(url=url, json=json_daily_basic)
            print(response.text)
            data = response.json()['data']['items']
            print(data, type(data))
            lensth2 = len(data)

            for j in range(lensth2):
                d2 = models.Monthly(ts_code=data[j][0], trade_date=data[j][1], close=data[j][2], open=data[j][3],
                                    high=data[j][4],
                                    low=data[j][5], pre_close=data[j][6], change=data[j][7],
                                    pct_chg=data[j][8], vol=data[j][9], amount=data[j][10])
                # function.insert_daily(daily=d1)
                pool.submit(function.insert_monthly, d2)
                number += 1
                print(number)
    print('完成')


# save_monthly(SSE_50)

def save_weekly(SSE_50):
    number = 0
    with ThreadPoolExecutor(max_workers=100) as pool:

        for i in SSE_50:
            # time.sleep(2)
            # time.sleep(1)
            params_weekly = {
                "ts_code": str(i),
                "start_date": "20200101",
                "end_date": "20210416"
            }
            json_daily_basic = {
                "api_name": "weekly",
                "token": token,
                "params": params_weekly,
                "fields": ""
            }
            response = requests.post(url=url, json=json_daily_basic)
            print(response.text)
            data = response.json()['data']['items']
            print(data, type(data))
            lensth2 = len(data)

            for j in range(lensth2):
                d2 = models.Weekly(ts_code=data[j][0], trade_date=data[j][1], close=data[j][2], open=data[j][3],
                                   high=data[j][4],
                                   low=data[j][5], pre_close=data[j][6], change=data[j][7],
                                   pct_chg=data[j][8], vol=data[j][9], amount=data[j][10])
                # function.insert_daily(daily=d1)
                pool.submit(function.insert_weekly, d2)
                number += 1
                print(number)
    print('完成')


# save_weekly(SSE_50)

# 需要传一个股票名进去
def save_daily_basic(SSE_50):
    number = 0
    with ThreadPoolExecutor(max_workers=100) as pool:

        for i in SSE_50:
            # time.sleep(2)
            # time.sleep(1)
            params_daily_basic = {
                "ts_code": str(i),
                "start_date": "20200101",
                "end_date": "20210416"
            }
            json_daily_basic = {
                "api_name": "daily_basic",
                "token": token,
                "params": params_daily_basic,
                "fields": ""
            }
            response = requests.post(url=url, json=json_daily_basic)
            # print(response.text)
            data = response.json()['data']['items']
            # print(data, type(data))
            lensth2 = len(data)

            for j in range(lensth2):
                d2 = models.Daily_basic(ts_code=data[j][0], trade_date=data[j][1], close=data[j][2],
                                        turnover_rate=data[j][3], turnover_rate_f=data[j][4], volume_ratio=data[j][5],
                                        pe=data[j][6], pe_ttm=data[j][7], pb=data[j][8], ps=data[j][9],
                                        ps_ttm=data[j][10], dv_ratio=data[j][11], dv_ttm=data[j][12],
                                        total_share=data[j][13],
                                        float_share=data[j][14], free_share=data[j][15], total_mv=data[j][16],
                                        circ_mv=data[j][17])
                # function.insert_daily(daily=d1)
                pool.submit(function.insert_daily_basic, d2)
                # number += 1
                # print(number)
    print('完成')


# save_daily_basic(SSE_50)


# 需要传输一个股票名进去
def save_daily_SSE_50(SSE_50):
    with ThreadPoolExecutor(max_workers=100) as pool:
        for i in SSE_50:
            # time.sleep(1)
            params_daily = {
                "ts_code": str(i),
                "start_date": "20200101",
                "end_date": "20210416"
            }
            json_daily = {
                "api_name": "daily",
                "token": token,
                "params": params_daily,
                "fields": ""
            }
            response = requests.post(url=url, json=json_daily)

            # number += 1
            # print(number)
            # print(response.text)
            # if not number % 499:
            #     time.sleep(100)

            data = response.json()['data']['items']
            # print(data)
            lensth2 = len(data)

            for j in range(lensth2):
                d1 = models.Daily(ts_code=data[j][0], stade_date=data[j][1], open=data[j][2], high=data[j][3],
                                  low=data[j][4], close=data[j][5], pre_close=data[j][6], change=data[j][7],
                                  pct_chg=data[j][8], vol=data[j][9], amount=data[j][10])
                # function.insert_daily(daily=d1)
                pool.submit(function.insert_daily, d1)

    print('完成')

    # "ts_code", "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount"
# save_daily_SSE_50(SSE_50)
