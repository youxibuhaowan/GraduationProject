"""
Time:2021/4/22 19:26
Author:中庸猿
奋斗不止，赚钱不停    
"""
from concurrent.futures.thread import ThreadPoolExecutor


def asd(a):
    a += a
    return {'a': a}
with ThreadPoolExecutor(max_workers=32) as pool:
    f1 = pool.submit(asd, 12)

    print(f1.result())



