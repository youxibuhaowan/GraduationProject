"""
Time:2021/4/15 19:28
Author:中庸猿
奋斗不止，赚钱不停    
"""
import MySQLdb
from models import Daily
from database import db_session_factory
from models import Daily, DailyBasic, IndexDaily, IndexBasic, IndexDailybasic, StockBase, ThsDaily, ThsIndex


def print_mysql_data(class_tb):
    # 查询数据
    session = db_session_factory()
    depts = session.query(class_tb).all()
    return {'ts_code': '10000', 'depts': depts}


def insert_mysql_data(class_tb):
    # 新增数据
    try:
        session = db_session_factory()
        session.add(class_tb)
        session.commit()
        return {'code': '成功'}
    except:
        session.rollback()
        return {'code': '失败'}


# 连接数据库的函数,执行SQL语句， 执行新增数据库数据
def execution_mysql(mysql_sentence: str, b=None, host='127.0.0.1', port=3306, user='root', password='123456',
                    database='tushare', charset='utf8mb4'):
    # 第一步: 创建链接对象
    conn = MySQLdb.connect(host=host, port=port,
                           user=user, password=password,
                           database=database, charset=charset)
    try:
        # 第二步: 获取游标对象
        with conn.cursor() as cursor:

            affected_rows = cursor.execute(mysql_sentence, b)

            conn.commit()
            print('执行成功')


    except MySQLdb.MySQLError as err:
        print(err)
        conn.rollback()
        return 0
    finally:
        conn.close()


def interface_mysql(table='tb_daily', ts_code='600000.SH', page=1, host='127.0.0.1', port=3306, user='root',
                    password='123456',
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

