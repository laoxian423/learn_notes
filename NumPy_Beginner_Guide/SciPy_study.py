""" SciPy 
    著名的开源科学计算库，建立在NumPy之上，它增加的功能包括数值积分、最优化、统计和一些专用函数
"""
""" Summary 
    .mat(MATLAB,Octave)  
    统计模块scipy.stats  离散分布 连续分布 统计检验
    正态分布 偏度 峰度 正态性检验
"""

import numpy as np
from scipy import io
from scipy import stats
import matplotlib.pyplot as plt

currentDir = "NumPy_Beginner_Guide/"

def demo_mat():
    """ 保存和加载.mat文件 """
    a = np.arange(7)
    io.savemat(currentDir+"a.mat", {"array":a})

#demo_mat()
""" What do
    生成的mat文件是一个二进制文件，与MATLAB交互使用。
"""

def demo_stats_normal():
    """ 按正态分布生成随机数，并分析绘图 """
    # 按正太分布生成随机数
    generated = stats.norm.rvs(size=900)
    # 用正态分布去拟合生成的数据，得到其均值和标准差
    print(stats.norm.fit(generated))
    # 偏度(skewness)描述的是概率分布的偏斜（非对称）程度，做一个偏度检验，数据集是否
    # 服从正态分布，取值范围0-1
    print(stats.skewtest(generated))  #pvalue=0.9195164327603584 91% 服从正态分布
    # 峰度(kurtosis)是概率分布曲线的陡峭程度
    print(stats.kurtosistest(generated))
    # 正态性检验(normality test)检查数据集服从正态分布的程度。
    print(stats.normaltest(generated))
    # 得到数据所在的区段中某一百分比处的数值：
    print(stats.scoreatpercentile(generated, 95))
    # 反过来，从数值1出发找到对应的百分比
    print(stats.percentileofscore(generated, 1))

    plt.hist(generated)
    plt.show()

#demo_stats_normal()
"""what do
    检验一个数据集是否服从正态分布，判断峰度、偏度、正态性
"""

