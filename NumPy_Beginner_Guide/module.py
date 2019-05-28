""" Numpy 模块 
    numpy.dual模块包含同时在numpy和SciPy中的定义的函数
    numpy.linalg 线性代数模块
"""

import numpy as np
import matplotlib.pyplot as plt

def calc_inverse_matrix():
    """ 计算逆矩阵 
    
    必须是方阵且可逆，否则会抛出LinAlgError异常
    """
    A = np.mat('0 1 2; 1 0 3; 4 -3 8')
    inverse = np.linalg.inv(A)
    print(inverse)
    # 矩阵和其逆矩阵的积是单位矩阵
    print( A * inverse)


def calc_linear_equations():
    """ 求解线性方程组 """
    A = np.mat('1 -2 1; 0 2 -8; -4 5 9')
    b = np.array([0, 8, -9])
    
    x = np.linalg.solve(A, b)
    print(x)
    # 验证结果
    print(np.dot(A, x))

def clac_eigenvalue():
    """ 特征值和特征向量

    特征值即方程Ax = ax的根，是一个标量。A是二维矩阵，x 是一个一维向量
    特征向量是关于特征值的向量。
    """
    A = np.mat('3 -2; 1 0')
    # 求解特征值
    print(np.linalg.eigvals(A))
    # 求解特征值和特征向量
    eigenvalues, eigenvectors = np.linalg.eig(A)
    print(eigenvalues)
    print(eigenvectors)
    # 验证
    for i in range(len(eigenvalues)):
        print('left:',np.dot(A, eigenvectors[:,i]))  # [:,i] 取出第i列数据
        print('right:', eigenvalues[i] * eigenvectors[:,i]) 
        print()

def clac_svd():
    """ 奇异值分解 
    
    Singular Value Decomposition,是一种因子分解运算，将一个矩阵分解为3个矩阵的乘积
    svd()函数返回3个矩阵，U Sigma V ,U V 是正交矩阵，Sigma包含矩阵的奇异值。
    """
    A = np.mat(" 4 11 14; 8 7 -2")
    U, Sigma, V = np.linalg.svd(A, full_matrices=False)
    print(U)
    # Sigma并不是奇异值矩阵，只是其对角线上的值，其他是0
    print(Sigma)
    print(V)
    print(U * np.diag(Sigma) * V)

def clac_pinv():
    """ 计算广义逆矩阵 """
    A = np.mat('4 11 14; 8 7 -2')
    pseudoinv = np.linalg.pinv(A)
    print(pseudoinv)
    # 与原矩阵相乘，等到一个近似的单位矩阵
    print(A * pseudoinv)


def clac_determinant():
    """ 行列式 

    行列式是与方阵相关的一个标量值，在数学中得到广泛应用。对于一个n * n的实数矩阵，行列式描述
    的是一个线性变化对”有向体积“所造成的影响，行列式的值为正标识保持了空间的定向（顺时针或逆时针）
    为负表示颠倒了空间的定向。
    """
    A = np.mat("3 4; 5 6")
    print(np.linalg.det(A))

""" 快速傅里叶变换
FFT(Fast Fourier Transform) 是一种高效的DFT（Discrete Fourier Transform 离散傅里叶变换）的算法。
DFT在信号处理、图像处理、求解偏微分方程等方面都有应用。
傅里叶变换的核心思想是所有的波都可以用多个正弦波表示，比如要去除声音文件中的某种声音，就是去除它的特征值
对应的sin值。
Numpy中有一个fft提供FFT的功能，许多函数都是成对存在的，也就是说许多函数存在队形的逆操作函数
"""
def clac_fourier():
    """ 计算傅里叶变换 """
    # 创建一个包含30个点的余弦波信号
    x = np.linspace(0, 2 * np.pi, 30)
    wave = np.cos(x)
    # 使用fft函数对余弦波信号进行傅里叶变换
    transformed = np.fft.fft(wave)
    # 对变换后的结果应用ifft函数，近似还原原始信号
    print(np.all(np.abs(np.fft.ifft(transformed)- wave) < 10 ** -9))
    plt.plot(transformed)
    plt.plot(wave)
    plt.show()


""" 移频
numpy.linalg模块中的fftshift函数可以将FFT输出中的直流分量移动到频谱的中央，ifftshift是其逆操作
"""
def clac_fftshift():
    """ 移频 """
    # 创建一个30个点的余弦波信号
    x = np.linspace(0, 2 * np.pi, 30)
    wave = np.cos(x)
    # 使用fft函数对余弦波信号进行傅里叶变换
    transformed = np.fft.fft(wave)
    # 使用fftshift函数进行移频操作
    shifted = np.fft.fftshift(transformed)
    # 还原移频前信号
    print(np.all(np.abs(np.fft.ifftshift(shifted)- transformed) < 10 ** -9))

    plt.plot(transformed, lw=2)
    plt.plot(shifted, lw=3)
    plt.show()
    

""" 随机数 """
""" 硬币赌博游戏
    设想你来到了一个17世纪的赌场，正在对一个硬币赌博游戏下8份赌注。每一轮抛9枚硬币，如果少于
    5枚硬币正面朝上，你将损失8份赌注中的一份；否则，赢得一份。下面来模拟这个过程，初始资本
    1000份赌注
"""
def demo_random():
    """ 通过一个赌博游戏演示随机数"""
    # 初始化一个全0的数组来存放剩余资本
    cash = np.zeros(10000)  # 玩1万轮游戏
    cash[0] = 1000
    # binomial 模拟随机游走
    outcome = np.random.binomial(9, 0.5, size=len(cash))
    print(outcome)
    # 模拟每一轮抛硬币的结果并更新cash数组
    for i in range(1, len(cash)):
        if outcome[i] < 5:
            cash[i] = cash[i - 1] - 1
        elif outcome[i] < 10:
            cash[i] = cash[i - 1] + 1
        else:
            raise AssertionError("Unexpected outcome " + outcome)
    print(outcome.min(), outcome.max())
    plt.plot(np.arange(len(cash)), cash)
    plt.show()

""" 超几何分布
（hypergeometric distribution）是一种离散概率分布，它描述的是一个管子里有两种物件，无放回地从中
抽取指定数量的物件后，抽出指定种类物件的数量。
"""
def demo_hypergeometric():
    """ 模拟游戏秀节目 
    
    有这样一个节目，每当参赛者回答对一个问题，他们可以从一个罐子里模出3个球并放回。罐子里有一个
    “倒霉球”，一旦被摸到，参赛者会被扣去6分。如果没摸到加1分。如果有100道问题被正确回答，得分怎样？
    """
    # 使用hypergeometric函数初始化游戏的结果矩阵。该函数第一个参数为罐中普通球的数量，
    # 第二个参数为“倒霉球”的数量，第三个参数为每次采样（摸球）的数量
    points = np.zeros(100)
    outcome = np.random.hypergeometric(25, 1, 3, size=len(points))
    # 根据上一步产生的游戏结果计算相应的得分
    for i in range(len(points)):
        if outcome[i] == 3:
            points[i] = points[i - 1] + 1
        elif outcome[i] == 2:
            points[i] = points[i -1] - 6
        else:
            print(outcome[i])
    plt.plot(np.arange(len(points)), points)   
    plt.show()

""" 连续分布
连续分布可以用PDF（Probability Density Function,概率密度函数）来描述。随机变量落在某一区间内的概率
等于概率密度函数在该区间的曲线下方的面积。
"""
def draw_normal():
    """ 绘制正态分布 """
    # 使用normal函数产生指定数量的随机数
    N = 10000
    normal_values = np.random.normal(size=N)
    # 绘制分布直方图和理论上的概率密度函数（均值为0，方差为1的正太分布）曲线。
    dummy, bins, dummy = plt.hist(normal_values, np.sqrt(N), normed=True, lw=1)
    sigma = 1
    mu =0
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu)**2 / (2 * sigma**2)), lw=2)
    plt.show()

def draw_log_distributtion():
    """ 对数正态分布 
    
    （lognormal distribution)是自然对数服从正太分布的任意随机变量的概率分布。
    """
    N = 10000
    lognormal_values =  np.random.lognormal(size=N)
    # 绘制分布直方图和理论上的概率密度函数（均值为0，方差为1的正太分布）曲线。
    dummy, bins, dummy = plt.hist(lognormal_values, np.sqrt(N), normed=True, lw=1)
    sigma = 1
    mu =0
    x = np.linspace(min(bins), max(bins), len(bins))
    pdf = np.exp(-(np.log(x) - mu)**2 / (2*sigma**2))/(x*sigma*np.sqrt(2*np.pi))

    plt.plot(x,pdf,lw=3)
    plt.show()

draw_log_distributtion()



