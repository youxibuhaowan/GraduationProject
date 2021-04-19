"""
Time:2021/4/15 19:28
Author:中庸猿
奋斗不止，赚钱不停    
"""
import MySQLdb
import uvicorn
from datetime import datetime, date
import json
import database
from database import db_session_factory
from models import Stock_basic, Trade_cal, Daily, Daily_basic, Monthly, Weekly, Moneyflow

def print_stock_basic():
    #
    session = db_session_factory()
    depts = session.query(Stock_basic).all()
    return {'ts_code': '10000', 'depts': depts}


def print_trade_cal():
    #
    session = db_session_factory()
    depts = session.query(Trade_cal).all()
    return {'ts_code': '10000', 'depts': depts}


def print_daily():
    #
    session = db_session_factory()
    depts = session.query(Daily).all()
    return {'ts_code': '10000', 'depts': depts}


def print_daily_basic():
    #
    session = db_session_factory()
    depts = session.query(Daily_basic).all()
    return {'ts_code': '10000', 'depts': depts}


def print_monthly():
    #
    session = db_session_factory()
    depts = session.query(Monthly).all()
    return {'ts_code': '10000', 'depts': depts}


def print_weekly():
    #
    session = db_session_factory()
    depts = session.query(Weekly).all()
    return {'ts_code': '10000', 'depts': depts}


def print_moneyflow():
    #
    session = db_session_factory()
    depts = session.query(Moneyflow).all()
    return {'ts_code': '10000', 'depts': depts}


def insert_stock_basic(stock_basic: Stock_basic):
    # 新增数据
    try:
        session = db_session_factory()
        session.add(stock_basic)
        session.commit()
        return {'code': '成功'}
    except:
        session.rollback()
        return {'code': '失败'}


def insert_trade_cal(trade_cal: Trade_cal):
    # 新增数据
    try:
        session = db_session_factory()
        session.add(trade_cal)
        session.commit()
        return {'code': '成功'}
    except:
        session.rollback()
        return {'code': '失败'}


def insert_daily(daily: Daily):
    # 新增数据
    try:
        session = db_session_factory()
        session.add(daily)
        session.commit()
        return {'code': '成功'}
    except:
        session.rollback()
        return {'code': '失败'}


def insert_daily_basic(daily_basic: Daily_basic):
    # 新增数据
    try:
        session = db_session_factory()
        session.add(daily_basic)
        session.commit()
        return {'code': '成功'}
    except Exception as err:
        print(err)
        # raise err
        session.rollback()
        return {'code': '失败'}


def insert_monthly(monthly: Monthly):
    # 新增数据
    try:
        session = db_session_factory()
        session.add(monthly)
        session.commit()
        return {'code': '成功'}
    except:
        session.rollback()
        return {'code': '失败'}


def insert_weekly(weekly: Weekly):
    # 新增数据
    try:
        session = db_session_factory()
        session.add(weekly)
        session.commit()
        return {'code': '成功'}
    except Exception as err:
        print(err)
        session.rollback()
        return {'code': '失败'}


def insert_moneyflow(moneyflow: Moneyflow):
    # 新增数据
    try:
        session = db_session_factory()
        session.add(moneyflow)
        session.commit()
        return {'code': '成功'}
    except:
        session.rollback()
        return {'code': '失败'}


# 连接数据库的函数,执行SQL语句
def execution_mysql(mysql_sentence: str, b=None, host='127.0.0.1', port=3306, user='root', password='123456',
                              database='tushare', charset='utf8mb4'):
    # 第一步: 创建链接对象
    conn = MySQLdb.connect(host=host, port=port,
                           user=user, password=password,
                           database=database, charset=charset)
    try:
        # 第二步: 获取游标对象
        with conn.cursor() as cursor:
            # 第三步: 通过游标对象向数据库服务器发出SQL语句
            # cursor.execute('SQL语句')
            affected_rows = cursor.execute(mysql_sentence, b)
            # 第四步: 获取查询结果（通过游标抓取数据）
            # fetchone() ---> 抓取一条数据
            # fetchall() ---> 抓取所有数据，嵌套元组
            # fetchmany(n) ---> 抓取n个数据，嵌套元组
            # row = cursor.fetchall()  # 抓取出来是一个二维元组
            # return row
            conn.commit()
            print('执行成功')


    except MySQLdb.MySQLError as err:
        print(err)
        conn.rollback()
        return 0
    finally:
        # 第五步: 关闭连接释放资源
        conn.close()


def interface_mysql(table='tb_daily', ts_code='600000.SH', page = 1, host='127.0.0.1', port=3306, user='root', password='123456',
                    database='tushare', charset='utf8mb4'):
    index = 0
    list_index = []
    if page == 1:
        sql = "select `trade_date` from " + table + " where ts_code = '" + ts_code + "';"
        list_index.append(sql)
        sql = "select `vol`, `amount` from " + table + " where ts_code = '" + ts_code + "';"
        list_index.append(sql)
        index = 2
    elif page == 2:
        sql = "select `ts_code`, `trade_date`, `open`, `close`, `high`, `low` from " + table + " where ts_code = '" + ts_code + "';"
    elif page == 3:
        pass
    elif page == 4:
        sql = "select `ts_code`, `trade_date`, `pe`, `pb` `ps` `dv_ttm` from " + table + " where ts_code = '" + ts_code + "';"
    else:
        print('我啥也不知道，这页面超了')


    # sql = "select `stade_date`, `open`, `close`, `high`, `low` from `tb_daily` where ts_code = '600000.SH' and  `index` < '10';"
    # vw = "vw_" + vw_date + "_" + vw
    conn = MySQLdb.connect(host=host, port=port,
                           user=user, password=password,
                           database=database, charset=charset)
    try:
        with conn.cursor() as cursor:

            cursor.execute(sql)
            conn.commit()
            result = cursor.fetchall()
            # result = json.dumps(result)
            print(result)
            print('执行成功')
            return result
    except MySQLdb.MySQLError as err:
        print(err)
        conn.rollback()
        return 0
    finally:
        conn.close()

# interface_mysql()