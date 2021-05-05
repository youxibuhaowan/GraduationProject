"""
Time:2021/4/17 12:45
Author:中庸猿
奋斗不止，赚钱不停    
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# HOST = '47.98.138.168'
# PORT = 3306
# USER = 'root'
# PASS = "Yupeixin.281513"
# DB = 'tushare'

HOST = 'localhost'
PORT = 3306
USER = 'root'
PASS = "123456"
DB = 'tushare_for_ali'
# DB = 'tushare'

SQLALCHEMY_DATABASE_URL = f"mysql://{USER}:{PASS}@{HOST}:{PORT}/{DB}?charset=utf8mb4"
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{USER}:{PASS}@{HOST}:{PORT}/tushare_for_ali?charset=utf8mb4"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# 获取数据库会话工厂(通过调用该对象就可以获得数据库会话对象)
db_session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
