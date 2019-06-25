#
# Pandas 学习笔记整理
# 
# 描述 ：
#       对Pandas的学习资料整理
# 历史版本 ：
#       2019-06-21 ：创建 刘昕
#       2019-06-22 ：access_file()
#       2019-06-24 ：base_function_attribute() access_data()
#                    data_operation() observe_data()
#       2019-06-25 ：更新access_data()、observe_data（）

import pandas as pd

# 数据文件路径
path = 'data_analysis/main_packages/'
df = pd.read_csv(path+'titanic.csv')

def access_file():
    """ 文件访问

    关键字：读取csv 
    """
    df = pd.read_csv(path+'titanic.csv')
    print(1, df.head())

#access_file()

""" 总结
    1、归类：通用操作、数据结构
    2、关联：
        pandas 是对Numpy的一个封装，功能更为强大，使用也比较简洁。它的设计框架和Numpy非常像。
        比如，它的基本数据结构是DataFrame，DF本身也有大量的方法和属性。另外pandas提供了丰富
        的函数来处理数据。
    3、用途：
        Pandas可能是python数据分析领域中最耳熟能详的东西了，凡是接触python数据分析的都基本是从
        pandas开始。在量化交易方面尤其如此，基本都是围绕着Pandas做一些封装。
"""

def base_function_attribute():
    """ 基本属性和方法

    关键字：数据信息 索引 列名 类型 数据值
    """
    print(1, df.info())
    print(2, df.index)
    print(3, df.columns)   
    print(4, df.dtypes)
    print(5, df.values)



#base_function_attribute()
""" 总结
    1、归类：数据结构-方法和属性
    2、关联：
        可以参考numpy的方法和属性，pandas的使用更加简单，而且对于数据分析有很强的针对性。
    3、用途：
        一部分属性和方法可以帮助观察数据。
"""

def access_data():
    """ 访问数据
    
    关键字：切片 取列值 设置列名为索引
    """
    df = pd.read_csv(path+'titanic.csv')
    age = df['Age']
    print(1, age)
    print(2, age.index)
    print(3, age.values[:5])
    print(4, age[:5])
    # 将列设置为索引
    df = df.set_index('Name')
    age = df['Age']
    print(5, age[:5])
    print(6, age['Heikkinen, Miss. Laina'])

    # 读取多个列
    print(7,df[['Age','Fare']][:5])

    # 使用iloc（位置索引） 和 loc（标签索引） 访问数据
    print(8, df.iloc[0:5])
    print(9, df.iloc[0:5,1:3])

    print(10, df.loc['Braund, Mr. Owen Harris','Fare'])

    # 使用条件判断来选取数据
    print(11, df[ df['Fare'] > 40 ])
    print(12, df['Fare'] > 40 )

  
#access_data()
""" 总结:
    1、归类：数据访问
    2、关联：
        DataFrame中的每一行和列和Numpy中的ndarray操作差不多，支持python格式的切片操作，看来真是一脉相承
        每一列又继承了dataframe的一些方法和属性，因此可以多尝试一下。
        我记得python是不是也能用条件筛选索引？
    3、用途：
        要分析数据，首先要访问数据，而且需要很灵活、精确的访问数据，目前多数方法都用到了列名，看来在从
        数据库中导出.csv时，要将列名也一起导出。

"""


def observe_data():
    """ 观察数据
    
    关键字：最大值 最小值 平均数 统计信息 groupby
    """
    age = df['Age']
    print(1, age.max(), age.min(), age.mean())
    # 显示常用统计信息
    print(2, age.describe())
    print(3, '\n', df.describe())
    
    # 使用groupby()分组统计数据
    print(4, df.groupby('Age').sum())
    print(5, df.groupby('Age').mean())
    age_mean = df.groupby('Sex')['Age'].mean()
    print(6, df.groupby('Sex')['Age'].mean())
    

    

observe_data()

"""总结:
    1、归类：统计分析之观察数据
    2、关联：
        在学习pandas时，我感到和学习程序语言有很大的不同，我觉得我不是在学习python编程，而是学习Excel
        一类的工具软件，所以我不再按照numpy的分类来归类，而是按照应用软件的习惯来分类。比如，新增的这个
        观察数据的分类。我觉得我应该按照统计学的习惯去分类pandas。
    3、用途：
        这一部分主要归类一些概览数据的功能，可以在编写程序之前先对数据有一个大概的认识。这一部分学习的
        时候感觉很数学、很统计，就像我们要解一道题时，或者准备建模时，首先把数据大致了解一下。
        好吧，Pandas更像是一个 SQL + Excel。


"""

def data_operation():
    """ 数学运算

    关键字：加 减 乘 除 
    """
    age = df['Age'][:10]
    print(1, '\n', age * 10)

#data_operation()

""" 总结：
    1、归类：数学运算
    2、关联：
        和ndarray差不多，估计后面也能学到大量的矩阵、向量运算，这里有个不错的叫法“广播效果”
    3、用途：
        这个用处是基本的了，必须的。我发现numpy也好，pandas也好，设计它们的一个主要原因就是
        消灭循环。越学习数据分析，就越发现自己不像是个程序员了，没有了循环，没有了判断，没有
        了多线程，嗯，好吧，这不是我正想要的吗。
"""

