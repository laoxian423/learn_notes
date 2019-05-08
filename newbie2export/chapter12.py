# LOOK 异常
"""异常处理
   异常根类是 BaseException
   Exception子类是非系统退出的异常，自定义异常可以继承它及其子类，不要直接继承根类
   Warning子类是警告，提示潜在问题
"""

"""捕获异常
    异常是向上传递，直到有人处理它，否则退出程序
    try:
        <可能会抛出异常的语句>
    except [异常类型1]:
        <处理异常>
    except [异常类型2]:
        <处理异常>
    except [异常类型n]:
        <处理异常>


    except如果省略具体异常，则捕获所有异常
    多个except时，只捕获一个就返回
    多个捕获异常类之间存在父子关系时，从上到下先捕获子类，后捕获父类，否则子类捕获不到
    就是说如果父类在上，子类在下面，那么子类永远不会被捕获到。
"""
import datetime as dt

def read_date(in_date):
    try:
        date = dt.datetime.strptime(in_date,'%Y-%m-%d')
        return date
    except ValueError as e:
        print('处理 ValueError异常')
        print(e)
        return 'Error'

str_date = '20ab-8-18'
print('date = {0}'.format(read_date(str_date)))


""" try-except 语句嵌套

try:
    file = open(filename)
    try:
        in_date = file.read()
    except ValueError as e:
        pass
except FileNotFoundError as e:
    pass

如果内层捕获不到异常，那么外层来捕获
尽量不要使用嵌套
"""


""" 多重异常捕获

except (ValueError, OSError) as e:
    print(e)

"""

"""异常堆栈跟踪
    traceback.print_exc(limit=None, file=None, chain=True)
    limit 限制堆栈跟踪的个数，默认不限制
    file 判断是否输出堆栈信息到文件，默认不输出
    chain 为True ，则将 __casue__ 和 __context__ 串联起来。
"""
import traceback as tb

def read_date_from_file(filename):
    try:
        file = open(filename)
        in_date = file.read()
        in_date = in_date.strip()
        date = dt.datetime.strptime(in_date, '%Y-%m-%d')
        return date
    except (ValueError,OSError) as e:
        print('处理.....')
        tb.print_exc()

date = read_date_from_file('readme.txt')
print('date = {0}'.format(date))



"""释放资源
    有时try-except会占用一些资源，如打开文件，网络连接，打开数据库连接等
    这些不能通过Python的垃圾收集器回收，需要程序员释放
    通过finally 或者 with as管理
"""

"""finally 代码块
    try:
        <.....>
    except [exception1]:
        <.....>
    finally:
        <释放资源>

    无论try 还是 except，finally 都会被执行
"""

""" else 代码块：
    try:
        file = open(filename)
    except OSError as e:
        print(e)
    else:
        print('file is open')
        try:
            in_date = file.read()
        except ValueError as e:
            print(e)
        finally:
            file.close()
"""

""" with as 代码块自动管理资源
    with as 提供了一个代码块，在 as 后面声明了一个资源变量，代码块结束后释放资源

    try:
        with open(filename) as file:
            in_date = file.read()

        in_date = in_date.strip()
    except ValueError as e:
        pass
    
"""  

""" 自定义异常

class MyException(Exception):
    def __init__(self,message):
        super().__init__(message)

"""

"""显示抛出异常,raise
   不想某些异常传给上层调用者，可以捕获之后重新显示抛出另外一种异常给调用者

   except ValueErro as e:
       raise MyException('不是有效日期')



