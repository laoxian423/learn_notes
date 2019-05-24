""" Numpy 模块 
    numpy.dual模块包含同时在numpy和SciPy中的定义的函数
    numpy.linalg 线性代数模块
"""

import numpy as np

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


