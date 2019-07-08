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
#       2019-06-26 ：create_df(),更新observe_data（）
#       2019-07-01 : 更新create_df()、access_data()
#       2019-07-02 : merge_df()
#       2019-07-05 ： data_pivot()

import pandas as pd

# 数据文件路径
path = 'data_analysis/main_packages/'
df = pd.read_csv(path+'titanic.csv')

def create_df():
    """ 创建数据结构DataFrame series

    关键字：DataFrame 数据结构  series
    """
    # 方式一：自动生成
    df = pd.read_csv(path+'titanic.csv')
    # 方式二：手动创建
    df1 = pd.DataFrame([[1, 2, 3],[4, 5, 6]],
                         index=['a','b'],
                         columns=['A','B','C'])
    print(1, '\n', df1)
    
    # 创建series
    data = [1, 2, 3]
    index = ['a', 'b', 'c']
    s = pd.Series(data=data, index=index)
    print(2, s)

#create_df()

""" 总结
    1、分类：
        数据结构
    2、关联：
        pandas和Numpy一样，有自己的数据结构类:DataFrame和Series,DataFrame中的每一行
        就是一个Series。他们具有基本相同的方法和属性。
    4、用途：
        每一种语言，或者大的工具包，都有自己的数据结构。所有的方法和属性都是围绕着数据结构
        展开。无论是BASIC、C、C++都是如此，最先设计的就是数据结构，整数、浮点数、布尔、文件
        ，在加上控制语句循环、判断等就成了一个完整的处理系统。其实现在想起来，应用系统也是如
        此，操作系统也是如此。都是在处理广义的或者狭义的数据结构，然后形成了一门编程语言、一个
        操作系统、一个应用系统。有时候觉得很诡异，比如我们证券，整个行业起码有上千亿的IT投资，
        都是围绕着那几个很小的表，行情库以及委托成交清算，这几个基础库可能不到10M，但是围绕着
        这几个库形成了上千亿的IT投入，人类不知道在干什么。
"""
#----------------------------------------------------------------------------------

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
#----------------------------------------------------------------------------------
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
#----------------------------------------------------------------------------------
def access_data():
    """ 访问数据
    
    关键字：切片 取列值 设置列名为索引 查找 修改 增加 删除
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

    # Series的操作
    # 创建一个Series数据
    data = [1, 2, 3]
    index = ['a', 'b', 'c']
    s = pd.Series(data=data, index=index)
    # Series 的查找
    print(15, s.loc['b'])
    print(16, s.iloc[1])
    # Series 的修改
    s1 = s.copy()
    s1['a'] = 100
    print(17, s1)
    # Series的增加
    s1['d'] = 200
    print(18,'\n', s1)
    s.append(s1, ignore_index=True)
    print(19,'\n', s)
    # Series的删除
    del s1['d']
    print(20,'\n', s1)
    s1.drop(['b', 'c'],inplace=True)
    print(21,'\n', s1)

    # DataFrame的操作
    # 创建一个DF
    data = [[1, 2, 3], [4, 5, 6]]
    index = ['a', 'b']
    columns = ['A','B','C']
    df = pd.DataFrame(data=data, index=index, columns=columns)
    print(22, '\n', df)
    # DF 查找
    print(23, df.loc['a'])
    print(24, df['A'])
    # DF 增加
    df['D'] = [ 7,8]
    print(25, '\n', df)
    # DF 修改
    df.loc['a']['A'] = 150
    print(26, '\n', df)
    # DF 删除
    df.drop(['b'],inplace=True)
    del df['D']
    print(27, '\n', df)
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
#----------------------------------------------------------------------------------

def observe_data():
    """ 观察数据
    
    关键字：最大值 最小值 平均数 统计信息 groupby 二元统计 协方差 相关系数 分值统计
            count 计数 中位数
    """
    df = pd.read_csv(path+'/titanic.csv')
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
    
    # 基本统计指标
    print(7, df.sum())
    print(8, df.sum(axis=1))
    print(9, df.sum(axis='columns'))
    print(10, df.median())

    # 二元统计
    # 协方差
    print(11, df.cov())
    # 相关系数
    print(12, df.corr())
    # 分值统计
    print(13, df['Age'].value_counts())
    # 计数
    print(14, df['Age'].count())

  


#observe_data()

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
#----------------------------------------------------------------------------------
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
        了多线程，嗯，好吧。
"""
#----------------------------------------------------------------------------------


def merge_df():
    """合并两个DF

    关键字：merge 合并DtaaFrame
    """
    left = pd.DataFrame({'key':['K0', 'K1', 'K2', 'K3'],
                         'A':['A0', 'A1', 'A2', 'A3'],
                         'B':['B0', 'B1', 'B2', 'B3'],
                         'C':['C0', 'C1', 'C2', 'C3']
                         })
    right = pd.DataFrame({'key':['K0', 'K1', 'K2', 'K3'],
                        'D':['D0', 'D1', 'D2', 'D3'],
                        'E':['E0', 'E1', 'E2', 'E3'],
                        'F':['F0', 'F1', 'F2', 'F3']
                        })

    print(1, '\n', left) 
    print(2, '\n', right) 
    
    # 合并两个DF,默认按照key值合并，两个表共同拥有的字段
    print(3, '\n', pd.merge(left, right, on='key'))
    
    # 合并,按照两个关键值,相当于交集
    left1 = pd.DataFrame({'key1':['K0', 'K1', 'K2', 'K3'],
                         'key2':['K0', 'K1', 'K2', 'K3'],
                         'A':['A0', 'A1', 'A2', 'A3'],
                         'B':['B0', 'B1', 'B2', 'B3'],
                         'C':['C0', 'C1', 'C2', 'C3']
                         })
    right1 = pd.DataFrame({'key1':['K0', 'K1', 'K2', 'K3'],
                          'key2':['K0', 'K1', 'K2', 'K3'],
                          'D':['D0', 'D1', 'D2', 'D3'],
                          'E':['E0', 'E1', 'E2', 'E3'],
                          'F':['F0', 'F1', 'F2', 'F3']
                         })
    print(4, '\n', pd.merge(left1, right1, on=['key1','key2']))
    # 合并,按照两个关键值,相当于并集
    right1 = pd.DataFrame({'key1':['K0', 'K1', 'K2', 'K3'],
                          'key2':['K0', 'K1', 'K2', 'K4'],
                          'D':['D0', 'D1', 'D2', 'D3'],
                          'E':['E0', 'E1', 'E2', 'E3'],
                          'F':['F0', 'F1', 'F2', 'F3']
                         })

    print(5, '\n', pd.merge(left1, right1, on=['key1','key2'], how='outer', indicator=True))
    # 合并，以'left'或者'right'为基准
    print(6, '\n', pd.merge(left1, right1, on=['key1','key2'], how='left'))
    print(7, '\n', pd.merge(left1, right1, on=['key1','key2'], how='right'))

#merge_df()

"""总结
    1、归类：通用操作-合并数据
    2、关联：
        基础语言中可以用编程手段解决两个表的按关键字合并，Numpy中也有这样的函数，虽然我在漫长的编程生涯中
        很少合并两个数据集，不过看来这是数据分析中常用手段了。似乎可以通过Merge函数来进行集合的运算，下次
        试试。
    3、用途：
        按教材的说法，可以合并特征值。
"""

def data_pivot():
    """ 数据透视表

    关键字： pivot_table
    """ 
    # 准备示例数据
    excel_sample = pd.DataFrame({'Month':['January','January','January','January',
                                          'February','February','February','February',
                                          'March','March','March','March'],
                                 'Category':["Transportation","Grocery","HouseHold","Entertainment",
                                             "Transportation","Grocery","HouseHold","Entertainment",
                                             "Transportation","Grocery","HouseHold","Entertainment"],
                                 'Amount':[74,235,175,100,115,240,225,125,90,260,200,120]})
    print(1, '\n', excel_sample)
    pivot1 = excel_sample.pivot_table(index='Category',columns='Month',values='Amount')
    print(2, '\n\n', pivot1)
    pivot1 = excel_sample.pivot_table(index='Category',columns='Month',values='Amount',aggfunc='sum')
    print(3, '\n\n', pivot1)

#data_pivot()       

""" 总结：
    1、归类：统计分析
    2、关联：Pandas 和 numpy 都有大量的重复的方法和属性实现同一功能，也不知道这些方法之间有什么不同，也可能相互继承。
    3、用途：数据透视表的用途很广，尤其对一堆数据进行观察时，可以从各个维度来对数据有个整体映像。
"""