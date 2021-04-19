"""
Time:2021/4/17 12:45
Author:中庸猿
奋斗不止，赚钱不停    
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOST = 'localhost'
PORT = 3306
USER = 'root'
PASS = '123456'
DB = 'tushare'

SQLALCHEMY_DATABASE_URL = f"mysql://{USER}:{PASS}@{HOST}:{PORT}/tushare?charset=utf8mb4"
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:123456@localhost/tushare"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# 获取数据库会话工厂(通过调用该对象就可以获得数据库会话对象)
db_session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
