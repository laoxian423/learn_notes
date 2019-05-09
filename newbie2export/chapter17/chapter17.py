# LOOK 数据库编程
""" 数据持久化
    凡是把数据保存到介质上，需要的时候能读取出来，都属于持久化技术
    1）文本文件：XML JSON CSV 等
    2）数据库：
    主要分两类，遵循Python DB-API规范和ORM技术。
    python DB-API: PEP 249 ，通过python中编写SQL访问数据
    ORM:Object-Relational mapping，对象隐射关系，通过对象访问数据，不需要SQL
"""

"""MySQL 数据库管理系统
    常用MySQL命令：
    show databases;             查看数据库
    create database testdb;     创建数据库testdb
    drop database testdb;       删除数据库testdb
    use testdb;                 选择数据库
    show tables;                查看有多个表
    desc city;                  查看city这张表的表结构
"""

"""Python DB-API 管理MySQL数据库
    库：pymysql    如果没有需要安装：pip install pymysql
    需要安装依赖库: pip install cryptography
    http://pymysql.readthedocs.io/en/latest/modules/connecitons.html
    connection = pymysql.connect(...)
    connection.close() 关闭连接
    connection.commit() 提交事物
    connection.rollback() 回滚事物
    connection.cursor() 获得Cursor游标对象
"""
import pymysql

def query_db_have_condition():
    """ 有条件查询 """

    # 1.建立数据库连接
    connection = pymysql.connect(host='192.168.159.132',
                            port=3306,
                            user='root', 
                            password='root',
                            database='testdb',
                            charset='utf8')

    try:
        # 2.创建游标对象
        with connection.cursor() as cursor:

            # 3.执行SQL查询
            # %(id)s 是命名占位符，
            sql = 'select name, userid from user where userid >%(id)s' 
            cursor.execute(sql,{'id':0})

            # 4.提取结果集
            result_set =  cursor.fetchall()

            for row in result_set:
                print('id:{0} - name:{1}'.format(row[1], row[0]))
        # with 代码块结束，自动关闭游标
    finally:
        # 6. 关闭数据库连接
        connection.close()

def query_db_not_condition():
    """ 无条件查询 """
    maxid = 0

    # 1.建立数据库连接
    connection = pymysql.connect(host='192.168.159.132',
                            port=3306,
                            user='root', 
                            password='root',
                            database='testdb',
                            charset='utf8')

    try:
        # 2.创建游标对象
        with connection.cursor() as cursor:

            # 3.执行SQL查询
            sql = 'select max(userid) from user' 
            cursor.execute(sql)

            # 4.提取结果集
            row =  cursor.fetchone()

            if row is not None:
                print('最大用户id:{0}'.format(row[0]))
                maxid = int(row[0])
        # with 代码块结束，自动关闭游标
    finally:
        # 6. 关闭数据库连接
        connection.close()
    return maxid

def insert_db_user():
    """ 数据库插入操作"""
    maxid = query_db_not_condition()

    connection = pymysql.connect(host='192.168.159.132',
                            port=3306,
                            user='root', 
                            password='root',
                            database='testdb',
                            charset='utf8')
    try:
        with connection.cursor() as cursor:
            sql = 'insert into user (userid, name) values (%s,%s)'
            nextid = maxid + 1
            name = 'Alexanda'
            affect = cursor.execute(sql, (nextid, name))
            print('影响的行数:{0}'.format(affect))
            connection.commit()
    except pymysql.DatabaseError:
        connection.rollback()
    finally:
        connection.close()


def update_db():
    """ 数据库更新操作 """
    connection = pymysql.connect(host='192.168.159.132',
                            port=3306,
                            user='root', 
                            password='root',
                            database='testdb',
                            charset='utf8')
    try:
        with connection.cursor() as cursor:
            sql = 'update user set name = %s where userid > %s'
            affect = cursor.execute(sql, ('Mark Antony', 2))
            print('影响的行数:{0}'.format(affect))
            connection.commit()
    except pymysql.DatabaseError as e:
        connection.rollback()
        print(e)
    finally:
        connection.close()


def delete_dbdata():
    """ 删除数据 """
    connection = pymysql.connect(host='192.168.159.132',
                            port=3306,
                            user='root', 
                            password='root',
                            database='testdb',
                            charset='utf8')
    try:
        with connection.cursor() as cursor:
            sql = 'delete from user where userid = %s'
            affect = cursor.execute(sql, (2))
            print('影响的行数:{0}'.format(affect))
            connection.commit()
    except pymysql.DatabaseError as e:
        connection.rollback()
        print(e)
    finally:
        connection.close()

""" NoSQL 数据存储
    dbm (DataBase Manager) 是最简单的NoSQL。
    NoSQL 不通过SQL语句操作数据库
    dbm 类似字典数据结构
    dbm 保存的数据是字符串类型或者是字节序列
"""

"""dbm 数据库的打开和关闭、写入、读取
打开：  dbm.open(file, flag='r')    
        r 只读打开
        w 读写方式
        c 读写，如果不存在则创建
        n 始终创建一个空数据库，读写
关闭：  dbm.close() 
        使用with dbm.open(DB_NAME, 'c') as db:
                pass
        自动关闭。
写入：  d[key] = data
读取：  data = d[key] 或 data = d.get(key, defaultvalue)
删除:   del d[key]
查找:   flag = key in d
"""
#import pysnooper

#@pysnooper.snoop()
def dbm_operate():
    import dbm

    with dbm.open('f:/temp/mydb', 'c') as db:
        db['name'] = 'Tony'
        print(db['name'].decode())  # db['name'] 取出的是字节序列，decode()转成字符串

        age = int(db.get('age', b'18').decode())
        print(age)

        if 'age' in db:
            db['age'] = '20'
        del db['name']



    
if __name__ == '__main__' :
    # query_db_have_condition()  # 有条件查询  R
    # query_db_not_condition()   # 无条件查询  R
    # insert_db_user()           # 插入一条数据 I
    # update_db()                # 更新数据 U
    # delete_dbdata()            # 删除数据 D
    dbm_operate()              # dbm 的操作
    pass
