"""
Time:2021/4/17 11:59
Author:中庸猿
奋斗不止，赚钱不停
"""
from MySQLdb.constants.FIELD_TYPE import VARCHAR
from sqlalchemy import Column, String, DECIMAL, INT, Integer, DATE

from database import Base

"""
对应数据库中的数据模型。

对数据模型进行了预处理。
"""


class Daily(Base):
    __tablename__ = 'tb_daily'

    ts_code = Column('ts_code', String(255))
    trade_date = Column(DATE)
    open = Column(DECIMAL)
    high = Column(DECIMAL)
    low = Column(DECIMAL)
    close = Column(DECIMAL)
    change = Column(DECIMAL)
    pct_chg = Column(DECIMAL)
    vol = Column(DECIMAL)
    amount = Column(DECIMAL)


class DailyBasic(Base):
    __tablename__ = 'tb_daily_basic'

    ts_code = Column('ts_code', String(255))
    trade_date = Column('trade_date', DATE)
    close = Column('close', DECIMAL)
    volume_ratio = Column('volume_ratio', DECIMAL)
    pe = Column('pe', DECIMAL)
    pb = Column('pb', DECIMAL)
    total_share = Column('total_share', DECIMAL)
    total_mv = Column('total_mv', DECIMAL)


class IndexBasic(Base):
    __tablename__ = 'tb_index_basic'

    ts_code = Column('ts_code', String(255), primary_key=True)
    name = Column('name', String(50))
    market = Column('market', String(10))
    publisher = Column('publisher', String(20))
    category = Column('category', String(10))
    base_date = Column('base_date', DATE)
    base_point = Column('base_point', DECIMAL)


class IndexDaily(Base):
    __tablename__ = 'tb_index_daily'

    ts_code = Column('ts_code', String(255))
    trade_date = Column('trade_date', DATE)
    open = Column('open', DECIMAL)
    close = Column('close', DECIMAL)
    high = Column('high', DECIMAL)
    low = Column('low', DECIMAL)
    change = Column('change', DECIMAL)
    pct_chg = Column('pct_chg', DECIMAL)
    vol = Column('vol', DECIMAL)
    amount = Column('amount', DECIMAL)


class IndexDailybasic(Base):
    __tablename__ = 'tb_index_dailybasic'

    ts_code = Column('ts_code', String(255))
    trade_date = Column('trade_date', DATE)
    total_mv = Column('total_mv', DECIMAL)
    turnover_rate = Column('turnover_rate', DECIMAL)
    pe = Column('pe', DECIMAL)
    pb = Column('pb', DECIMAL)


class StockBase(Base):
    __tablename__ = 'tb_stock_base'

    ts_code = Column('ts_code', String(255), primary_key=True)
    symbol = Column('symbol', String(255))
    name = Column('name', String(255))
    area = Column('area', String(255))
    industry = Column('industry', String(255))

    def __repr__(self):
        return self.ts_code


class ThsDaily(Base):
    __tablename__ = 'tb_ths_daily'

    ts_code = Column('ts_code', String(255))
    trade_date = Column('trade_date', DATE)
    open = Column('open', DECIMAL)
    close = Column('close', DECIMAL)
    high = Column('high', DECIMAL)
    low = Column('low', DECIMAL)
    change = Column('change', DECIMAL)
    vol = Column('vol', DECIMAL)


class ThsIndex(Base):
    __tablename__ = 'tb_ths_index'

    ts_code = Column('ts_code', String(255), primary_key=True)
    name = Column('name', String(20))
    count = Column('count', DECIMAL)
    exchange = Column('exchange', String(10))
    list_date = Column('list_date', DATE)
    type = Column('type', String(20))