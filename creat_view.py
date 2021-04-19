"""
Time:2021/4/18 15:31
Author:中庸猿
奋斗不止，赚钱不停    
"""

import models
import function
import pymysql

stock_list = function.print_stock_basic()['depts']
# 拿取每个股票的日线，周线，月线 ---> 开盘价，收盘价，最高价，最低价 ---> 创建成视图
def creat_vw_for_Kline():
    sql = "create view `%s` (trade_date, open, close, high, low, vol, amount) " \
                                "AS SELECT trade_date, open, close, high, low, vol, amount" \
                                " FROM tb_monthly where ts_code=%s;"
    for i in stock_list:
        function.execution_mysql(sql, b=(f"vw_monthly_{i}", i))






# 拿取每个股票的日线，周线，月线 ---> 交易量



