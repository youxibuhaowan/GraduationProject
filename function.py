"""
Time:2021/4/15 19:28
Author:中庸猿
奋斗不止，赚钱不停    
"""
import uvicorn
import pymysql
import database
from database import db_session_factory
from models import Stock_basic, Trade_cal, Daily, Daily_basic, Monthly, Weekly, Moneyflow


def print_stock_company():
    # 获取所有部门信息
    session = db_session_factory()
    depts = session.query(Stock_basic).all()
    return {'ts_code': '10000', 'depts': depts}


def print_trade_cal():
    # 获取所有部门信息
    session = db_session_factory()
    depts = session.query(Trade_cal).all()
    return {'ts_code': '10000', 'depts': depts}


def print_daily():
    # 获取所有部门信息
    session = db_session_factory()
    depts = session.query(Daily).all()
    return {'ts_code': '10000', 'depts': depts}


# @app.get('/tushare/daily_basic')
def print_daily_basic():
    # 获取所有部门信息
    session = db_session_factory()
    depts = session.query(Daily_basic).all()
    return {'ts_code': '10000', 'depts': depts}


# @app.get('/tushare/monthly')
def print_monthly():
    # 获取所有部门信息
    session = db_session_factory()
    depts = session.query(Monthly).all()
    return {'ts_code': '10000', 'depts': depts}


# @app.get('/tushare/weekly')
def print_weekly():
    # 获取所有部门信息
    session = db_session_factory()
    depts = session.query(Weekly).all()
    return {'ts_code': '10000', 'depts': depts}


# @app.get('/tushare/moneyflow')
def print_moneyflow():
    # 获取所有部门信息
    session = db_session_factory()
    depts = session.query(Moneyflow).all()
    return {'ts_code': '10000', 'depts': depts}


def insert_stock_company(stock_basic: Stock_basic):
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
    except:
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
    except:
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
