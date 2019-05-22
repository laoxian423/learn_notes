""" 便捷函数 """
""" 股票相关性分析
    协方差描述的是两个变量共同变化的趋势，其实就是归一化前的相关系数，使用cov函数
    计算股票收益率的协方差矩阵
"""
import numpy as np
import matplotlib.pyplot as plt

def get_close(csv_filepath, default_fild=6):
    """ 从数据文件中得到股票的收盘价 """
    C = np.loadtxt(csv_filepath, 
                    delimiter=',', 
                    usecols=(default_fild), 
                    unpack=True)
    return C


def rate_of_return(csv_filepath):
    """ 根据数据文件计算股票收益率 
    
    简单收益率：指相邻两个价格之间的变化率。
    对数收益率：指所有价格取对数后两两之间的差值。
    """
    # 计算简单收益率
    # NumPy的diff函数可以返回一个由相邻数组元素的差值构成的数组，类似于微分。
    # 我们还需要用差值除以前一天的价格。
    # diff返回的数组比收盘价少一个元素。
    C =get_close(csv_filepath)
    returns = np.diff(C) / C[:-1]
    # print(returns)
    # 计算标准差
    # print("Standard deviation",np.std(returns))

    # 计算对数收益率
    # logreturns = np.diff(np.log(C))

    return returns

def get_close(csv_filepath):
    """ 从数据文件中得到股票的收盘价 """
    C = np.loadtxt(csv_filepath, 
                    delimiter=',', 
                    usecols=(6), 
                    unpack=True)
    return C
    



def rate_related():
    """ 计算两只股票的收益率相关性 """
    csv_bhp = 'NumPy_Beginner_Guide/BHP.csv' 
    csv_vale = 'NumPy_Beginner_Guide/vale.csv'
    bhp_returns = rate_of_return(csv_bhp)
    vale_returns = rate_of_return(csv_vale)

    # 1.协方差描述两个变量共同变化的趋势,得到协方差矩阵
    covariance = np.cov(bhp_returns, vale_returns)
    print(covariance)
    # 2.使用diagonal函数查看对角线上的元素
    # 协方差矩阵的对角线元素并不相等，这与相关系数矩阵不同
    print(covariance.diagonal())
    # 3.使用trace函数计算矩阵的迹，即对角线上元素之和
    print(covariance.trace())
    # 4.两个向量的相关系数被定义为协方差除以各自标准差的乘积。计算向量a和b的相关系数公式如下：
    # corr(a,b)=cov(a,b)/（a的标注差 * b的标准差）
    print(covariance/(bhp_returns.std() * vale_returns.std()))
    # 用相关系数来度量这两只股票的相关程度，相关系数的取值范围在-1到1之间，与自身相关系数是1
    # 相关系数矩阵是关于对角线对称的。
    print(np.corrcoef(bhp_returns, vale_returns))
    
    # 判断两只股票价格是否同步,如果他们收盘价差值偏离了平均差值2倍于标准差的距离，则不同步
    bhp_close = get_close(csv_bhp)
    vale_close = get_close(csv_vale)

    difference = bhp_close - vale_close
    avg = np.mean(difference)
    dev = np.std(difference)
    print(np.abs(difference[-1] - avg) > 2 * dev)

    # 绘图
    t = np.arange(len(bhp_returns))
    plt.plot(t, bhp_returns, lw=1)
    plt.plot(t, vale_returns, lw=2)
    plt.show()



