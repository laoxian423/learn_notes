import pymysql

def insert_hisq_data(row):
    """ 在股票历史价格表中传入数据 """
    connection = pymysql.connect(host='192.168.0.21',
                                 user='root',
                                 password='root',
                                 database='NASDAQ',
                                 charset='utf8'
                                )

    try:
        # 创建游标对象
        with connection.cursor() as cursor:
            # 执行SQL操作
            sql = 'insert into HistoricalQuote ' \
                '(HDate,Open,High,Low,Close,Volume,Symbol) '\
                'values (%(Date)s,%(Open)s,%(High)s,%(Low)s,%(Close)s,%(Volume)s,%(Symbol)s)'
            print(sql % row)
            affectedcount = cursor.execute(sql, row)
            
            print('影响的数据行数：{0}'.format(affectedcount))
            connection.commit()
    except pymysql.DatabaseError as error:
        connection.rollback()
        print(error)
    finally:
        connection.close
