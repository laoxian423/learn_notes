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

