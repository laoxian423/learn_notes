""" 爬虫工作计划任务 """
import datetime
import hashlib
import logging
import os
import re 
import threading
import time
import urllib.request

from bs4 import BeautifulSoup
from db_access import insert_hisq_data

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s-%(threadName)s-'
                            '%(name)s-%(funcName)s-%(levelname)s-%(message)s')
logger = logging.getLogger(__name__)

# 线程运行标志
isrunning = True
# 爬虫工作间隔
interval = 5

def controlthread_body():
    """控制线程体函数"""

    global interval, isrunning

    while isrunning:
        # 控制爬虫计划
        i = input('输入bye终止爬虫，输入数字改变爬虫工作间隔（秒）:')
        logger.info('控制输入{0}'.format(i))
        try:
            interval = int(i)
        except ValueError:
            if i.lower() == 'bye':
                isrunning = False

def istradtime():
    """ 判断交易时间 """
    now = datetime.datetime.now()
    df = "%H%M%S"
    strnow = now.strftime(df)
    starttime = datetime.time(9,30).strftime(df)
    endtime = datetime.time(15,30).strftime(df)

    if now.weekday() == 5 \
        or now.weekday() == 6 \
            or (strnow < starttime or strnow > endtime):
        return False
    return True 

def workthread_body():
    """ 工作线程体函数 """
    global interval, isrunning 

    while isrunning:
        if istradtime():
            logger.info('交易时间，休眠1小时')
            time.sleep(60 * 60)
            continue
        logger.info('爬虫开始工作...')
        print('这里是分析数据和保存到数据库的代码。。。')
        logger.info('爬虫休眠{0}'.format(interval))
        time.sleep(interval)    

def main():
    global interval, isrunning
    workthread = threading.Thread(target=workthread_body,name='WorkThread')
    workthread.start()

    controlthread = threading.Thread(target=controlthread_body,name='ControlThread')
    controlthread.start()

if __name__ == "__main__":
    main()