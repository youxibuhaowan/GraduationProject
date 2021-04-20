"""
Time:2021/4/17 12:51
Author:中庸猿
奋斗不止，赚钱不停    
"""
import uvicorn
from fastapi import FastAPI, Depends
from fastapi.params import Query
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

import function
from database import db_session_factory
from models import Daily

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


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

# 图一，日期和量
@app.get('/tushareone')
def search(
        page: int = Query(1, gt=0),
        size: int = Query(50, ge=5, le=50),
        keyword: str = Query(None),
        session: Session = Depends(get_db_session)
):
    result1 = session.execute(
        "select `trade_date` as date, vol  from `tb_daily` where `ts_code` = '600000.SH' order by `date` asc;"
    )
    result2 = session.execute(
        "select `trade_date` as date, vol  from `tb_weekly` where `ts_code` = '600000.SH' order by `date` asc;"
    )
    result3 = session.execute(
        "select `trade_date` as date, vol  from `tb_monthly` where `ts_code` = '600000.SH' order by `date` asc;"
    )
    day_x_data, day_y_data, week_x_data, week_y_data, month_x_data, month_y_data = [], [], [], [], [], []
    for date, vol in result1.fetchall():
        day_x_data.append(date)
        day_y_data.append(vol)
    for date, vol in result2.fetchall():
        week_x_data.append(date)
        week_y_data.append(vol)
    for date, vol in result3.fetchall():
        month_x_data.append(date)
        month_y_data.append(vol)
        # z_data.append(amount)
    # query = session.query(Daily)\
    #     .order_by(Daily.index.desc()).all()
    # if keyword:
    #     # print('none')
    #     # query = query.filter(or_(
    #     #     Daily.ts_code.contains
    #     # ))
    #     pass
    return {'dayxData': day_x_data, 'dayyData': day_y_data, 'weekxData': week_x_data, 'weekyData': week_y_data, 'monthxData': month_x_data, 'monthyData': month_y_data}


# 返回一个日期和一个成交额和成交量 ---> 日线，周线，月线 ---> 通过前端页面传递参数，页面的点击传递参数
@app.get('/tushare/pageone')
def for_one_page(table='tb_daily', ts_code='600000.SH'):
    result = function.interface_mysql(table, ts_code, page = 1)
    return {'ts_code': 10000, 'depts': result}


# 返回一个日期和一个 股票代码，日期，开盘价，收盘价，最高价，最低价 ---> 日线，周线，月线 ---> 通过前端页面传递参数，页面的点击传递参数
@app.get('/tushare/pagetwo')
def for_two_page(session: Session = Depends(get_db_session)):
    result1 = session.execute(
        "select `trade_date` as date, open, high, low, close, vol from `tb_daily` where `ts_code` = '600000.SH' order by `date` asc;"
    )
    # result2 = session.execute(
    #     "select `trade_date` as date, open, high, low, close  from `tb_weekly` where `ts_code` = '600000.SH' order by `date` asc;"
    # )
    # result3 = session.execute(
    #     "select `trade_date` as date,  open, high, low, close  from `tb_monthly` where `ts_code` = '600000.SH' order by `date` asc;"
    # )
    day_x_data, day_y_open, day_y_high, day_y_low, day_y_close, day_vol = [], [], [], [], [], []
    # week_x_data, week_y_open, week_y_high, week_y_low, week_y_close = [], [], [], [], []
    # month_x_data, month_y_open, month_y_high, month_y_low, month_y_close = [], [], [], [], []

    for date, open, high, low, close, vol in result1.fetchall():
        day_x_data.append(date)
        day_y_open.append(open)
        day_y_high.append(high)
        day_y_low.append(low)
        day_y_close.append(close)
        day_vol.append(vol)
    # for date, open, high, low, close in result2.fetchall():
    #     week_x_data.append(date)
    #     week_y_open.append(open)
    #     week_y_high.append(high)
    #     week_y_low.append(low)
    #     week_y_close.append(close)
    # for date, open, high, low, close in result3.fetchall():
    #     month_x_data.append(date)
    #     month_y_open.append(open)
    #     month_y_high.append(high)
    #     month_y_low.append(low)
    #     month_y_close.append(close)

    result = zip(day_x_data, day_y_open, day_y_close, day_y_low, day_y_high, day_vol)
    list_result = []
    for i in result:
        list_result.append(list(i))

    return list_result
    # return {'dayxdata': day_x_data, 'dayyopen': day_y_open, 'dayyhigh': day_y_high, 'dayylow': day_y_low,
    #         'dayyclose': day_y_close,
    #         'weekxdata': week_x_data, 'weekyopen': week_y_open, 'weekyhigh': week_y_high, 'weekylow': week_y_low,
    #         'weekyclose': week_y_close,
    #         'monthxdata': month_x_data, 'monthyopen': month_y_open, 'monthyhigh': month_y_high, 'monthylow': month_y_low,
    #         'monthyclose': month_y_close}


# 返回一个日期和一个 股票代码，日期，开盘价，收盘价，最高价，最低价 ---> 日线，周线，月线 ---> 通过前端页面传递参数，页面的点击传递参数
@app.get('/tushare/pagefour')
def for_two_page(table='tb_daily_basic', ts_code='600000.SH'):
    result = function.interface_mysql(table, ts_code, page = 4)
    return{'ts_code': '10000', 'depts': result}




if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
