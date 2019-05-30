""" 专用函数 """
""" 排序函数
sort 返回排序后的数组
lexsort 根据键值的字典序进行排序
argsort 返回数组排序后的下标
ndarray.sort 进行原地排序
msort 沿着第一个轴排序
sort_complex 对复数按照先实部后虚部的顺序进行排序
"""
import numpy as np
import datetime
import matplotlib.pyplot as plt

def datestr2num(s):
    return datetime.datetime.strptime(str(s,encoding='utf8'), "%d-%m-%Y").toordinal()



def demo_sort():

    # 按字典进行排序
    dates, closes = np.loadtxt('NumPy_Beginner_Guide/BHP.csv',
                                delimiter=',',
                                usecols=(1,6),
                                converters={1:datestr2num},
                                unpack=True)
    # 优先按照收盘价排序：
    # lexsort返回数组的下标
    indices = np.lexsort((dates, closes))
    print(indices)
    print(["%s %s" % (datetime.date.fromordinal(int(dates[i])), closes[i]) for i in indices])



def sort_complex():
    """ 对复数排序 """
    # 生成5个随机数作为实部，5个随机数作为虚部，设置随机数种子为42
    np.random.seed(42)
    complex_numbers = np.random.random(5) + 1j * np.random.random(5)
    print(complex_numbers)
    print(np.sort_complex(complex_numbers))

def search_array():
    """ 搜索演示 
    
    np.argmax(A)  返回数组中最大值对应的下标
    np.nanargmax(A) 忽略NaN值
    np.argwhere(A <=4) 分组返回对应下标
    np.searchsorted()  为指定的插入值寻找维持数组排序的索引位置。
    np.extract()    返回满足指定条件的数组元素
    """
    A = np.array([2,4,8])
    print(np.argmax(A))
    print(np.nanargmax(A))
    print(np.argwhere(A <= 4))
    # 需要一个排序后的数组演示searchsorted()
    B = np.arange(5)
    indices = np.searchsorted(B, [-2, 7])
    print(indices,'\n',B)
    # 返回[0, 5] 表示维持数组排序的插入位置
    # 使用insert函数构建完整的数组
    print(np.insert(B, indices, [-2, 7]))

def extract_array():
    """ 按照条件从数组中抽取指定元素 """
    a = np.arange(7)
    # 生成偶数元素的条件变量：
    condition = (a % 2) == 0
    print(np.extract(condition, a))
    # 查看非零元素
    print(np.nonzero(a))

""" 金融类函数

fv 计算终值（future value),基于一些假设给出的某个金融资产在未来某一时间点的价值
pv 计算现值(present value)
npv 净现值(net present value) 按折现率计算净现金流之和
pmt 更具本金和利率计算每期需支付的金额
irr 计算内部收益率(internal rate of return) 内部收益率是净现值为0时的有效利率，不考虑通胀
mirr 计算修正后的内部收益率(modified internal rate of return)
nper 计算定期付款的期数
rate 计算利率(rate of interest)
"""
def demo_intervset():
    """ 金融类函数演示 """

    # 计算终值，终值取决于4个参数：利率、期数、每期支付金额及现值。
    # 利率3%，每季度支付金额10，存款周期5年及现值1000
    print(np.fv(0.03 / 4, 5 * 4,-10,-1000))
    
    # 计算现值
    print(np.pv(0.03/4, 5* 4, -10, 1376.096332)) 

    # 计算净现值
    cashflows = np.random.randint(100, size=5)
    cashflows = np.insert(cashflows, 0, -100)
    print(cashflows)
    # 根据上一步生成的现金流数据，按利率3% 计算净现值：
    print(np.npv(0.03, cashflows))

    # 计算内部收益率
    print(np.irr([-100, 79, 4, 94, 66, 44]))

    # 分期付款:假设贷款100万，年利率10%，30年还完，没用需支付？
    print(np.pmt(0.10/12, 12 * 30, 1000000))

    # 付款期数：贷款9000，年利率10%，每月固定还款100
    print(np.nper(0.10/12, -100, 9000))

    # 利率计算
    print(np.rate(167, -100, 9000, 0))

""" 窗函数

信号处理领域常用的数学函数，相关应用包括谱分析和滤波器设计等。
"""
def window_func():
    """ 绘制窗函数 """
    # 巴特利特窗(Bartlett window)是一种三角形平滑窗
    window = np.bartlett(42)
    plt.plot(window)
    plt.show()
    # 布莱克曼窗(Blackman window)形式上为三项余弦值的加和
    # 使用布莱克曼窗形平滑股价数据
    closes = np.loadtxt('NumPy_Beginner_Guide/BHP.csv', delimiter=',',usecols=(6,),unpack=True)
    N = 5
    window = np.blackman(N)
    smoothed = np.convolve(window/window.sum(), closes, mode='same')
    plt.plot(smoothed[N:-N], lw=2, label='smoothed')
    plt.plot(closes[N:-N], label='closes')
    plt.legend(loc='best')
    plt.show()
    # 汉明窗：一个加权的余弦函数，hamming唯一的参数是输出点的数量
    window = np.hamming(42)
    plt.plot(window)
    plt.show()
    # 凯泽窗：以贝塞尔函数(Bessel function)定义的。
    # 第一个参数为输出的点，第二个参数为贝塔值
    window = np.kaiser(42, 14)
    plt.plot(window)
    plt.show()


