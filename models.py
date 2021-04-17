"""
Time:2021/4/17 11:59
Author:中庸猿
奋斗不止，赚钱不停    
"""
from sqlalchemy import Column, String, DATETIME, DECIMAL, INT

from database import Base


# 模型类，对应数据库中的表
class Stock_basic(Base):
    __tablename__ = 'tb_stock_basic'

    ts_code = Column('ts_code', String(255), primary_key=True)
    symbol = Column('symbol', String(255))
    name = Column('name', String(255))
    area = Column('area', String(255))
    industry = Column('industry', String(255))
    market = Column('market', String(255))
    list_date = Column('list_date', DATETIME)


class Trade_cal(Base):
    __tablename__ = 'tb_trade_cal'

    exchange = Column('exchange', String(10))
    cal_date = Column('cal_date', DATETIME, primary_key=True)
    is_open = Column('is_open', String(255))


class Daily(Base):
    __tablename__ = 'tb_daily'

    ts_code = Column('ts_code', String(255), primary_key=True)
    stade_date = Column('stade_date', DATETIME)
    open = Column('open', DECIMAL)
    high = Column('high', DECIMAL)
    low = Column('low', DECIMAL)
    close = Column('close', DECIMAL)
    pre_close = Column('pre_close', DECIMAL)
    change = Column('change', DECIMAL)
    pct_chg= Column('pct_chg', DECIMAL)
    vol = Column('vol', DECIMAL)
    amount = Column('amount', DECIMAL)


class Daily_basic(Base):
    __tablename__ = 'tb_daily_basic'

    ts_code = Column('ts_code', String(255), primary_key=True)
    trade_date = Column('trade_date', DATETIME)
    colse = Column('colse', DECIMAL)
    turnover_rate = Column('turnover_rate', DECIMAL)
    turnover_rate_f = Column('turnover_rate_f', DECIMAL)
    volume_ratio = Column('volume_ratio', DECIMAL)
    pe = Column('pe', DECIMAL)
    pe_ttm = Column('pe_ttm', DECIMAL)
    pb = Column('pb', DECIMAL)
    ps = Column('ps', DECIMAL)
    ps_ttm = Column('ps_ttm', DECIMAL)
    dv_ratio = Column('dv_ratio', DECIMAL)
    dv_ttm = Column('dv_ttm', DECIMAL)
    total_share = Column('total_share', DECIMAL)
    float_share = Column('float_share', DECIMAL)
    free_share = Column('free_share', DECIMAL)
    total_mv = Column('total_mv', DECIMAL)
    circ_mv = Column('circ_mv', DECIMAL)

class Monthly(Base):
    __tablename__ = 'tb_monthly'

    ts_code = Column('ts_code', String(255), primary_key=True)
    trade_date = Column('trade_date', DATETIME)
    open = Column('open', DECIMAL)
    high = Column('high', DECIMAL)
    low = Column('low', DECIMAL)
    close = Column('close', DECIMAL)
    pre_close = Column('pre_close', DECIMAL)
    change = Column('change', DECIMAL)
    pct_chg= Column('pct_chg', DECIMAL)
    vol = Column('vol', DECIMAL)
    amount = Column('amount', DECIMAL)


class Weekly(Base):
    __tablename__ = 'tb_weekly'

    ts_code = Column('ts_code', String(255), primary_key=True)
    trade_date = Column('trade_date', DATETIME)
    open = Column('open', DECIMAL)
    high = Column('high', DECIMAL)
    low = Column('low', DECIMAL)
    close = Column('close', DECIMAL)
    pre_close = Column('pre_close', DECIMAL)
    change = Column('change', DECIMAL)
    pct_chg= Column('pct_chg', DECIMAL)
    vol = Column('vol', DECIMAL)
    amount = Column('amount', DECIMAL)


class Moneyflow(Base):
    __tablename__ = 'tb_moneyflow'

    ts_code = Column('ts_code', String(255), primary_key=True)
    trade_date = Column('trade_date', DATETIME)
    buy_sm_vol = Column('buy_sm_vol', INT)
    buy_sm_amount = Column('buy_sm_amount', DECIMAL)
    sell_sm_vol = Column('sell_sm_vol', INT)
    sell_sm_amount = Column('sell_sm_amount', DECIMAL)
    buy_md_vol = Column('buy_md_vol', INT)
    buy_md_amount = Column('buy_md_amount', DECIMAL)
    sell_md_amount = Column('sell_md_amount', DECIMAL)
    buy_lg_vol = Column('buy_lg_vol', INT)
    buy_lg_amount = Column('buy_lg_amount', DECIMAL)
    sell_lg_vol = Column('sell_lg_vol', INT)
    sell_lg_amount = Column('sell_lg_amount', DECIMAL)
    but_elg_vol = Column('but_elg_vol', INT)
    buy_elg_amount = Column('buy_elg_amount', DECIMAL)
    sell_elg_vol = Column('sell_elg_vol', INT)
    sell_elg_amount = Column('sell_elg_amount', DECIMAL)
    net_mf_vol = Column('net_mf_vol', INT)
    net_mf_amount = Column('net_mf_amount', DECIMAL)
    sell_md_vol = Column('sell_md_vol', INT)
