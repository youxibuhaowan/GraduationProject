"""
Time:2021/4/21 14:59
Author:中庸猿
奋斗不止，赚钱不停    
"""
from concurrent.futures.thread import ThreadPoolExecutor
from datetime import datetime
from time import time

import MySQLdb

import requests
from fastapi.params import Depends
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from database import db_session_factory
from main import get_db_session
from models import StockPool, StockBase

number = 0
token = 'c43d43d2f232eba8a6c58928cb248be964fb271fa3ab48d2b9a60d40'
url = 'http://api.waditu.com'

daily_api = "daily"
daily_fields = "ts_code, trade_date, open, high, low, close, change, pct_chg, vol, amount"
daily = {
            "ts_code": "",
            "start_date": "19990101",
            "end_date": datetime.now().strftime('%Y%m%d')
        }

stock_basic_api = "stock_basic"
stock_basic_fields = "ts_code, symbol, name, area, industry"
stock_basic = {
    "exchange": "",
    "list_status": "L"
}

daily_basic_api = "daily_basic"
daily_basic_fields = "ts_code, trade_date, close, volume_ratio, pe, pb, total_share, total_mv"
daily_basic = {
    "ts_code": "",
    "start_date": "",
    "end_date": ""
}

moneyflow_hsgt_api = "moneyflow_hsgt"
moneyflow_hsgt_fields = "trade_date, ggt_ss, ggt_sz, hgt, sgt, north_money, south_money"
moneyflow_hsgt = {
    "start_date": "",
    "end_date": ""
}


def get_data_from_tushare(apiname, params, fields):
    with ThreadPoolExecutor(max_workers=100) as pool:

        json = {
            "api_name": apiname,
            "token": token,
            "params": params,
            "fields": fields
        }
        response = requests.post(url=url, json=json)
        print(response.json()['data']['items'])
        return response.json()['data']['items']

def get_db_session():
    session = db_session_factory()
    try:
        yield session
        session.commit()
    except SQLAlchemyError as err:
        print(err)
        session.rollback()
    finally:
        session.close()

# 执行数据入tb_stockpool

# stock_data = get_data_from_tushare(stock_basic_api, stock_basic, stock_basic_fields)

def insert_stockpool(stockpool: StockPool):
    # 新增数据
    try:
        session = db_session_factory()
        session.add(stockpool)
        session.commit()
        return {'code': '成功'}
    except:
        session.rollback()
        return {'code': '失败'}


def save_stockpool(data):
        with ThreadPoolExecutor(max_workers=100) as pool:
            length = len(data)
            for j in range(length):
                d2 = StockPool(ts_code=data[j][0], symbol=data[j][1], name=data[j][2], area=data[j][3],
                                    industry=data[j][4])
                # function.insert_daily(daily=d1)
                pool.submit(insert_stockpool, d2)
            print('ok')


# 返回股票列表
def searchall_ts_code_from_stockpool(sql: str, host='47.98.138.168', port=3306, user='root', password='Yupeixin.281513',
                        database='tushare', charset='utf8mb4'):

    # 第一步: 创建链接对象
    conn = MySQLdb.connect(host=host, port=port,
                           user=user, password=password,
                           database=database, charset=charset)
    try:
        with conn.cursor() as cursor:
            affected_rows = cursor.execute(sql)
            row = cursor.fetchall()  # 抓取出来是一个二维元组
            conn.commit()
            ts_code = []
            for i in row:
                ts_code.append(i[0])
            return ts_code

    except MySQLdb.MySQLError as err:
        print(err)
        conn.rollback()
        return 0
    finally:
        conn.close()

    # ts_code = []
    # for code in result1.fetchall():
    #     ts_code.append(code)
    # return ts_code
sql_select_all_tscode = "select `ts_code` from tb_stockpool order by symbol asc;"






# save_data(stock_data)

# 执行数据入tb_stockbase
# daily_data = get_data_from_tushare(daily_api, daily, daily_fields)


def insert_stockbase(stockpool: StockPool):
    # 新增数据
    try:
        session = db_session_factory()
        session.add(stockpool)
        session.commit()
        return {'code': '成功'}
    except:
        session.rollback()
        return {'code': '失败'}


def save_stockbase(data):
    with ThreadPoolExecutor(max_workers=100) as pool:
        print(data)
        for j in data:
            d2 = StockBase(ts_code=j[0], trade_date=j[1], open=j[2], high=j[3],
                           low=j[4], close=j[5], change=j[6], pct_chg=j[7], vol=j[8], amount=j[9])
            pool.submit(insert_stockbase, d2)
        print('ok')


def getall_daily_data():
    tscode = searchall_ts_code_from_stockpool(sql_select_all_tscode)
    for i in tscode:
        time.sleep(1)
        daily['ts_code'] = i
        save_stockbase(get_data_from_tushare(daily_api, daily, daily_fields))


getall_daily_data()
