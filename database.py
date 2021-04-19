"""
Time:2021/4/17 12:45
Author:中庸猿
奋斗不止，赚钱不停    
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "msyql://root:123456@localhost/tushare"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:123456@localhost/tushare"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)
# 获取数据库会话工厂(通过调用该对象就可以获得数据库会话对象)
db_session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session():
    session = db_session_factory()
    try:
        yield session
        session.commit()
    except SQLAlchemyError as err:
        print(err)
        session.rollback()
    finally:
        session.commit()


Base = declarative_base()