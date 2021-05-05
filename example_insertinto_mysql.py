"""
Time:2021/4/26 10:28
Author:中庸猿
奋斗不止，赚钱不停    
"""
import pymysql


def execution_statement_mysql(mysql_sentence:str, b=None, host='127.0.0.1', port=3306, user='root', password='123456', database='tushare_for_ali', charset='utf8mb4'):
    # 第一步: 创建链接对象
    conn = pymysql.connect(host=host, port=port,
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
            row = cursor.fetchall()  # 抓取出来是一个二维元组
            return row

    except pymysql.MySQLError as err:
        print(err)
        conn.rollback()
        return 0
    finally:
        # 第五步: 关闭连接释放资源
        print('最后执行')
        conn.close()













