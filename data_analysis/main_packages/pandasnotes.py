#
# Pandas 学习笔记整理
# 
# 描述 ：
#       对Pandas的学习资料整理
# 历史版本 ：
#       2019-06-21 ：创建 刘昕

import pandas as pd

# 数据文件路径
path = 'data_analysis/main_packages/'


def access_file():
    """ 文件访问

    关键字：读取csv 
    """
    df = pd.read_csv(path+'titanic.csv')
    print(1, df.head())
    print(2, df.info())
    print(3, df.index)
    print(4, df.columns)   
    print(5, df.dtypes)
    print(6, df.values)

access_file()