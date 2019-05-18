""" 常用函数 """
# 创建一个单位矩阵并将其存到文件中
import numpy as np

def create_eye_save_txt(n):
    """ 创建单位矩阵并保存为eye.txt """

    # Numpy中提供 eye 创建单位矩阵，参数为 1 的个数
    i2 = np.eye(n)
    print(i2)
    # 保存文件
    np.savetxt('NumPy_Beginner_Guide/eye.txt', i2)


