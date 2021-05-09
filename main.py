"""
Time:2021/4/17 12:51
Author:中庸猿
奋斗不止，赚钱不停    
"""

from re import findall
import uvicorn
from concurrent.futures.thread import ThreadPoolExecutor
from fastapi import FastAPI, Depends
from fastapi.params import Query
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
import function
from database import db_session_factory
from models import Daily
import reptile
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

# 判断接受到的参数是一个股票代码还是一个股票的名字
def ts_code_or_name(key, session: Session = Depends(get_db_session)):
    if function.is_number(key):
        pass
    else:
        sql = "select symbol from `tb_stock_base` where name = '" + key + "';"
        key = str(function.interface_mysql(sql=sql, page=99)[0][0])

    b = int(key)
    if b > 300983:
        key += '.SH'
    else:
        key += '.SZ'
    print("key", key)
    return key






# 图一，日期和量
@app.get('/tushare/pageone')
def for_one_page(

        keyword: str = Query('600050'),
        session: Session = Depends(get_db_session)
):
    print(keyword)
    key = ts_code_or_name(keyword)
    result1 = session.execute(
        "select `trade_date` as date, volume_ratio  from `tb_daily_basic` where `ts_code` = '" + key + "' order by `date` asc;"
    )

    day_x_data, day_y_data, week_x_data, week_y_data, month_x_data, month_y_data = [], [], [], [], [], []
    for date, volume_ratio in result1.fetchall():
        day_x_data.append(date)
        day_y_data.append(volume_ratio)

    return {'dayxData': day_x_data, 'dayyData': day_y_data}
    # , 'weekxData': week_x_data, 'weekyData': week_y_data, 'monthxData': month_x_data, 'monthyData': month_y_data}


# 返回一个日期和一个 股票代码，日期，开盘价，收盘价，最高价，最低价 ---> 日线，周线，月线 ---> 通过前端页面传递参数，页面的点击传递参数
@app.get('/tushare/pagetwo')
def for_two_page(
        keyword: str = Query('600050'),
        session: Session = Depends(get_db_session)):
    key = ts_code_or_name(keyword)
    result1 = session.execute(
        "select `trade_date` as date, open, high, low, close, vol from `tb_daily` where `ts_code` = '" + key + "' order by `date` asc;"
    )


    day_x_data, day_y_open, day_y_high, day_y_low, day_y_close, day_vol = [], [], [], [], [], []

    for date, open, high, low, close, vol in result1.fetchall():
        day_x_data.append(date)
        day_y_open.append(open)
        day_y_high.append(high)
        day_y_low.append(low)
        day_y_close.append(close)
        day_vol.append(vol)

    result = zip(day_x_data, day_y_open, day_y_close, day_y_low, day_y_high, day_vol)
    list_result = []
    for i in result:
        list_result.append(list(i))

    return list_result


# 图三，股票的基础属性
@app.get('/tushare/pagethree')
def for_three_page(
        keyword: str = Query('600050'),
        session: Session = Depends(get_db_session)
):
    key = ts_code_or_name(keyword)
    # todaytime = function.getYesterday()
    todaytime = '20200102'
    result1 = session.execute(
        "select `volume_ratio`, `pe`, `pb`, `total_share`, `total_mv` from `tb_daily_basic` where `ts_code` = '" + key + "' and trade_date = '" + todaytime + "';"
    )

    # result2 = session.execute(
    #     "select max(`total_share`), max(`total_mv`) from `tb_daily_basic` group by `ts_code` = '" + key + "' ;"                                                                                                                                                          "selsect max(total_share), max(totsl_mv) from `tb_daily_basic` ;"
    # )
    # max_ts, max_tm = result2.fetchall()

    vr, pe, pb, ts, tm = [], [], [], [], []
    for data_vr, data_pe, data_pb, data_ts, data_tm in result1.fetchall():
        vr.append(data_vr)
        pe.append(data_pe)
        pb.append(data_pb)
        ts.append(data_ts)
        tm.append(data_tm)
    # ts_ratio = ts / max_ts * 100
    # tm_ratio = tm / max_tm * 100

    return {'vr': vr, 'pe': pe, 'pb': pb, 'ts': ts, 'tm': tm}





# 返回一个日期和一个 股票代码，日期，开盘价，收盘价，最高价，最低价 ---> 日线，周线，月线 ---> 通过前端页面传递参数，页面的点击传递参数
@app.get('/tushare/pagefour')
def for_two_page(table='tb_daily_basic', ts_code='600000.SH'):
    result = function.interface_mysql(table, ts_code, page=4)
    return {'ts_code': '10000', 'depts': result}


@app.get('/tushare/pagefive')
def for_five_page(
        keyword: str = Query('600050')
):
    key = ts_code_or_name(keyword)
    re_str = r'(\d*).\D\D'
    result = findall(re_str, key)
    # print("result:", result, type(result))
    list1 = reptile.public_opinion(result[0])
    # print("list1:", list1, type(list1))

    return {'list': list1}












@app.get('/tushare/tradingstock')
def for_trading_stock(session: Session = Depends(get_db_session)):
    result1 = session.execute(
        "select tb_stock_basic.ts_code,  `name`, `industry`, `pre_close`, `up_limit`, `down_limit`  from `tb_stock_basic` left join `tb_trading_limit` on tb_stock_basic.ts_code = tb_trading_limit.ts_code  where trade_date = '2021-04-09 00:00:00' ;"
    )

    ts_code1, name1, industry1, pre_close1, up_limit1, down_limit1 = [], [], [], [], [], []

    for ts_code, name, industry, pre_close, up_limit, down_limit in result1.fetchall():
        ts_code1.append(ts_code)
        name1.append(name)
        industry1.append(industry)
        pre_close1.append(pre_close)
        up_limit1.append(up_limit)
        down_limit1.append(down_limit)

    result2 = session.execute(
        "select `ts_code`, `total_mv` from tb_daily_basic where trade_date = '2021-04-09 00:00:00' ;"
    )
    ts_code2, total_mv2 = [], []
    for ts_code, total_mv in result2.fetchall():
        ts_code2.append(ts_code)
        total_mv2.append(total_mv)
    result3 = zip(ts_code1, name1, industry1, pre_close1, up_limit1, down_limit1)
    result4 = zip(ts_code2, total_mv2)
    listend = []
    listresult4 = []
    for asd in result4:
        asd = list(asd)
        listresult4.append(asd)
    for i in result3:
        i = list(i)
        for j in listresult4:
            if i[0] == j[0]:
                i.append(j[1])
        listend.append(i)
    return listend










if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
