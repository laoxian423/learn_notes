* 通用函数和操作

```python
# 常用库的导入
import numpy as np
import matplotlib.plyplot as plt

# 条件选择
np.where( vals > 0)
# 判断两个数组是否相等
np.array_equal(signs, pieces)

"""向量化函数"""
def myfunc(a, b): 
    "Return a-b if a>b, otherwise return a+b"
    if a > b:
        return a - b 
    else: 
        return a + b 
vfunc = np.vectorize(myfunc) 
vfunc([1, 2, 3, 4], 2) 
Out[87]: array([3, 4, 1, 2])
    
# 创建通用函数
# ultimate_anser是一个python函数，两个1表示输入参数个数是1个，输出参数个数是1个
ufunc = np.frompyfunc(ultimate_answer, 1, 1)
ufunc(np.arange(4))

# 优先按照股价排序，返回索引
indices = np.lexsort((dates, closes))
# 搜索：返回数组中最大值对应的下标
np.argmax(A)  
# 忽略NaN值
np.nanargmax(A) 
# 分组返回对应下标
np.argwhere(A <=4) 
# 抽取：按照条件抽取指定元素
condition = (a % 2) == 0
print(np.extract(condition, a))
# 查看非零元素
print(np.nonzero(a))

```

* 数学操作

```python
# 创建单位矩阵，n 为 1的个数
np.eye(n)
# 计算对数
np.log(c)
# 开方,python中整数和浮点数的除法运算机制不同，要注意。
np.sqrt(1./252.)
# 转置矩阵
ndarray.transpose()
ndarray.T

# 生成 N 个数据，所有元素值都为 1
np.ones(N)
# 用 1 填充数组，不管是一维还是多维
np.ones_like(arr1)

# 指数运算
np.exp(arr1)

# 线性代数相关
np.linalg.lstsq(A, b)
np.dot(b, x)

# 计算阶乘
arr1 = np.arange(1, 9)
arr1.prod()
# 计算所有阶乘
arr1.cumprod()

# 求矩阵的逆矩阵
np.linalg.inv(A)
# 求两个数组的协方差矩阵
covariance = np.cov(returns1, returns2)
# 查看矩阵的对角线元素
covariance.diagonal()
# 求矩阵对角线元素之和
covariance.trace()
# 求两个数组的相关系数
np.corrcoef(returns1, returns2)
# 求解线性方程组
A = np.mat('1 -2 1; 0 2 -8; -4 5 9')
b = np.array([0, 8, -9])
x = np.linalg.solve(A, b)
np.dot(A, x) # 验证结果
""" 特征值和特征向量
特征值即方程Ax = ax的根，是一个标量。A是二维矩阵，x 是一个一维向量
特征向量是关于特征值的向量。
"""
A = np.mat('3 -2; 1 0')
# 求解特征值
print(np.linalg.eigvals(A))
# 求解特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(A)
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
# np.diag(Sigma) 将Sigma补充为一个完整矩阵
print(U * np.diag(Sigma) * V)

""" 计算广义逆矩阵 """
A = np.mat('4 11 14; 8 7 -2')
pseudoinv = np.linalg.pinv(A)
print(pseudoinv)
# 与原矩阵相乘，等到一个近似的单位矩阵
print(A * pseudoinv)

""" 计算傅里叶变换 """
# 创建一个包含30个点的余弦波信号
x = np.linspace(0, 2 * np.pi, 30)
wave = np.cos(x)
# 使用fft函数对余弦波信号进行傅里叶变换
transformed = np.fft.fft(wave)
# 对变换后的结果应用ifft函数，近似还原原始信号
print(np.all(np.abs(np.fft.ifft(transformed)- wave) < 10 ** -9))

"""   随机数   """
cash = np.zeros(10000)  # 玩1万轮游戏
cash[0] = 1000
# binomial 模拟随机游走,
outcome = np.random.binomial(9, 0.5, size=len(cash))
# 返回一个结果矩阵，比如从25个红球和1篮球中每次采样3个，每次拿到红球的数量，100次的情况
outcome = np.random.hypergeometric(25, 1, 3, size=100)

# 绝对值
np.abs(arr1)
# 三角函数
np.sin(arr1)

# 返回元素的正负符号
np.sign(arr1)
# 根据正负符号自定义返回值
np.piecewise(arr1, [arr1 < 0, arr1 > 0])

# 加权余弦窗函数 np.hanning(N)
np.hanning(5)
out:array([0. , 0.5, 1. , 0.5, 0. ])
    
# 创建矩阵
A = np.mat('1 2 3; 4 5 6; 7 8 9')
B = np.mat(np.range(9).reshape(3, 3))
ab = np.bmat('A B; A B')
C = np.matrix([1, 1], [1, 0])

# 算术运算
a = np.array([2, 6, 5])
b = np.array([1, 2, 3])
# 除法,截断小数
np.divide(a, b)
np.true_divide(a, b)
# 除法，返回整数
np.floor_divide(a, b)
# 模运算
# 返回两个数组中元素相除后的余数
a = np.arange(-4, 4)
np.remainder(a, 2)
np.mod(a, 2)
np.fmod(a, 2) # 对负数的处理有所不同

# 二进制逻辑运算符
np.less(a, 0)
np.bitwise_xor(x, y)
np.bitwise_and(x, y)
```

* 文件操作类

```python
""" 读取csv文件中的数据

filePath  csv文件全路径
delimiter	分隔符
usecols	字段位置，从0开始
unpack 	True 分拆存储不同列的数据
"""
o, c = np.loadtxt(filePath, delimiter=',' usecols=(2,5), unpack=True)
# 指定转换器。在读取的同时，指定自定义函数同步处理 2 表示应用在第2个字段上
o, c = np.loadtxt(filePath, delimiter=',' usecols=(2,5), converters={2:functionName} unpack=True)
"""将一个ndarray 存储到文件中"""
np.savetxt(filePath, ndarray)
np.savetxt(filePath, ndarray, delimiter=',', fmt='%s')


```

* 统计类函数

```python
"""计算平均值（加权平均）
   
以 V 为权重计算 C 的平均值
"""
vwap = np.average(C, weights=V)

# 简单平均
m = np.mean(c)
# 中位数
np.median(c)
# 方差
np.var(c)
# 标准差
np.std(returns)

""" diff
返回相邻数组元素之间的差额，通常可用于计算收益率
"""
returns = np.diff(c) / c[:-1]
# 对数收益率
returns = np.diff(np.log(c))

""" np.apply_along_axis

numpy.apply_along_axis(func, axis, arr, *args, **kwargs)
将arr数组的每一个元素经过func函数变换形成一个新的数组
axis 轴，表示func对arr是作用于行还是列
*args,**kwargs 都是函数func()需要的参数
"""
def func(a):
    return a[0]+a[1]
b =np.array([[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12]])
np.apply_along_axis(func,0,b)
out: array([ 6,  8, 10, 12])
np.apply_along_axis(func,1,b)
out: array([ 3, 11, 19])

# maximum() 函数
# 对多个数组进行运算，返回结果中的最大值
np.maximum(arr1 - arr2, arr3- arr4, arr5 - arr6)

# convolve() 卷积操作，可用来计算移动平均线
# weights 是窗口权重，计算close的移动平均
N = 5
weights = np.ones(N) / N
np.convolve(weights, close)
```

* array数组操作函数

```python
# 数组的一些属性
a.dtype  # 数据类型
a.shape  # 数组的维度
a.ndim 	 # 数组的维数
a.size   # 元素个数
b.itemsize # 元素的内存大小
b.nbytes   # 字节大小
b.flat   # 返回一个扁平迭代器

# 生成一个ndarray数组
np.arange(start:stop:step)

# 返回最大值
np.max(c)
# 返回最小值
np.min(c)
# 返回最大值和最小值的差值
np.ptp(c)

# 数组排序
np.msort(c)
# 初始化一个全为0的数组
np.zeros(5)
np.zeros((5,5),float)

# 条件选择
np.where( vals > 0)
# 只保留满足条件的元素
arr1.compress(arr1 > 2)
# 根据索引取出对应的值
np.take(array, indexs)

# 创建自定义数据类型
t = np.dtype([('name', np.str_, 40),
              ('numitems', np.int32),
              ('price', np.float32)])
itemz = np.array([('Meaning of life DVD', 42, 3.14),
              ('Butter', 13, 2.72)],
              dtype=t)

# 改变数组的维度
# 包含2个3行4列的数组
b = np.arange(24).reshape(2, 3, 4)

# 将数组展平为一个一维数组(视图)
b.ravel()
b.flatten()
# 修改数组维度,把b 改成6行4列
b.shape=(6,4)
b.resize((2,12))

# 数组的水平组合
np.hstack((arr1,arr2))
# 水平组合2
np.concatenate((a,b), axis=1)
# 垂直组合1
np.vstack((a,b))
np.concatenate((a,b), axis=0)
# 深度组合
np.dstack((a,b))
# 列组合,同水平组合
np.column_stack((a,b))
# 行组合，同垂直组合
np.row_stack((a,b))

#数组的水平分割
np.hsplit(a, 3)
np.split(a, 3, axis=1)
# 数组的垂直分割
np.vsplit(a, 3)
np.split(a, 3, axis=0)
# 数组的深度分割
np.dsplit(c, 3)

# 数组的转换
b.tolist()  # 转换成list
b.astype(int) # 指定转换类型

# linspace :返回一个元素值在指定范围内均匀分布的数组
# linspace(start, stop, 元素个数)
np.linspace(-1., 0., 5)

# 数组元素的和
arr1.sum()
# 数组填充,用指定值填充数组
arr1.fill(1)
# clip() 把数组中所有比给定值大和小的值修改为最大值和最小值
# 比 1 小的都改为1，比2 大的都改为2
arr1.clip(1,2)

```

* 金融类函数

```bash
fv 计算终值（future value),基于一些假设给出的某个金融资产在未来某一时间点的价值
pv 计算现值(present value)
npv 净现值(net present value) 按折现率计算净现金流之和
pmt 更具本金和利率计算每期需支付的金额
irr 计算内部收益率(internal rate of return) 内部收益率是净现值为0时的有效利率，不考虑通胀
mirr 计算修正后的内部收益率(modified internal rate of return)
nper 计算定期付款的期数
rate 计算利率(rate of interest)
```



