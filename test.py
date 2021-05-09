"""
Time:2021/5/8 13:43
Author:中庸猿
奋斗不止，赚钱不停    
"""
import datetime

# todaytime = datetime.now().strftime('%Y%m%d')

def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday


# 输出
print(getYesterday())




