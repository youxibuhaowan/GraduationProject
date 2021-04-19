"""
Time:2021/4/17 12:51
Author:中庸猿
奋斗不止，赚钱不停    
"""
import uvicorn
from fastapi import FastAPI, Depends
from fastapi.params import Query
from sqlalchemy.sql.elements import or_

from database import  get_db_session, db_session_factory
from sqlalchemy.orm import Session
from models import Stock_basic, Trade_cal, Daily, Daily_basic, Monthly, Weekly, Moneyflow

import function

from database import db_session_factory

app = FastAPI()

@app.get('/tushareone')
def search(
        page: int = Query(1, gt=0),
        size: int = Query(50, ge=5, le=50),
        keyword: str = Query(None),
        session: Session = Depends(get_db_session)
):
    query = session.query(Daily)\
        .filter(Daily.index)\
        .order_by(Daily.index.desc())
    if keyword:
        print('none')
        # query = query.filter(or_(
        #     Daily.ts_code.contains
        # ))
    return {'code': 10000, 'result': query}



# 返回一个日期和一个成交额和成交量 ---> 日线，周线，月线 ---> 通过前端页面传递参数，页面的点击传递参数
@app.get('/tushare/pageone')
def for_one_page(table='tb_daily', ts_code='600000.SH'):
    result = function.interface_mysql(table, ts_code, page = 1)
    return {'ts_code': 10000, 'depts': result}


# 返回一个日期和一个 股票代码，日期，开盘价，收盘价，最高价，最低价 ---> 日线，周线，月线 ---> 通过前端页面传递参数，页面的点击传递参数
@app.get('/tushare/pagetwo')
def for_two_page(table='tb_daily', ts_code='600000.SH'):
    result = function.interface_mysql(table, ts_code, page = 2)
    return{'ts_code': '10000', 'depts': result}


# 返回一个日期和一个 股票代码，日期，开盘价，收盘价，最高价，最低价 ---> 日线，周线，月线 ---> 通过前端页面传递参数，页面的点击传递参数
@app.get('/tushare/pagefour')
def for_two_page(table='tb_daily_basic', ts_code='600000.SH'):
    result = function.interface_mysql(table, ts_code, page = 4)
    return{'ts_code': '10000', 'depts': result}




if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', reload=True)
