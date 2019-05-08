# LOOK 函数式编程
""" 函数式编程
def 函数名([参数列表])：
    pass
    [return 返回值]

关键字参数
*可变参数 ，组装成一个元组
**可变参数，组装成一个字典

利用元组返回多个函数值是安全的。
"""

""" yield 
在函数中使用return返回数据，有时候会用yield返回一个生成器
生成器是一种可迭代对象。
隐式的调用了__next__()方法。
"""
def square(num):
    n_list = []
    
    for i in range(1,num+1):
        n_list.append(i*i)

    return n_list

n_list =  square(10)
print(n_list)

def square_yield(num):

    for i in range(1,num +1):
        yield i * i
    
for i in square_yield(10):
    print(i)

""" 函数的嵌套
作用域只在被嵌套的函数内部
"""

"""函数类型
    python提供了一种函数类型function。
    函数调用时，就创建了函数类型实例，既函数对象
    函数类型实例和其他类型实例没有区别，可以赋值给一个变量，也可以作为参数传递给一个函数
    还可以作为函数返回值使用。
"""
def calculate_fun(opr):
    # 定义相加函数
    def add(a,b):
        return a + b

    # 定义相减函数
    def sub(a,b):
        return a -b 
    
    if opr == '+':
        return add
    else:
        return sub
    
f1 = calculate_fun('+')
f2 = calculate_fun('-')
print(type(f1))
print("10 + 5 = {0} ".format(f1(10,5)))
print("10 - 5 = {0} ".format(f2(10,5)))

""" Lambda 表达式
Lambda 本质上是一种匿名函数
lambda 参数列表 : lambda 体
参数列表类似于函数声明中的小括号里的参数，只是省略了小括号
lambda体只能有一条语句，语句计算结果返回给lambda表达式，不需要return
"""
def calculate_fun_lambda(opr):
    if opr == '+':
        return lambda a,b: (a + b)
    else:
        return lambda a,b: (a - b)

f1 = calculate_fun_lambda('+')
f2 = calculate_fun_lambda('-')
print(type(f1))
print("10 + 5 = {0} ".format(f1(10,5)))
print("10 - 5 = {0} ".format(f2(10,5)))

"""函数式编程的三大基础函数
函数式编程的本质是通过函数处理数据
过滤、隐射和聚合是三大基本操作
filter() map() reduce()
"""

"""filter() : 对 可迭代对象 的元素进行过滤
    filter(function,iterable)
    filter函数调用时iterable会被遍历，它的元素逐一传入function中，function返回布尔值。
    True的元素被保留，False的元素被过滤掉
    满足条件的留下，不满足的丢掉
    filter 返回一个 filter类型的可迭代器
"""
users = ['tony','tom','ben','alex']
users_filter = filter(lambda u: u.startswith('t'), users)
print(type(users_filter))
print(list(users_filter))


number_list = range(1, 11)
number_filter = filter(lambda it: it % 2 == 0 ,number_list)
print(list(number_filter))

"""map()
    对 可迭代对象 的元素进行变换
    map(function, iterable)
"""
users = ['TONY','tom','BEN','alex']
users_map = map(lambda u: u.lower(), users)
print(type(users_map))
print(list(users_map))

users = ['Tony','Tom','Ben','alex']
users_map = map(lambda u: u.lower(), filter(lambda u: u.startswith('T'),users))
print(list(users_map))

"""reduce()
    将多个数据聚合起来输出单个数据
    reduce(function, iterable[, initializer])
    initializer 是初始值
"""
from functools import reduce
a = (1,2,3,4)
a_reduce = reduce(lambda acc, i: acc + i, a)
print(a_reduce)
a_reduce = reduce(lambda acc, i: acc + i, a, 2)
# acc对应的应该就是initializer，如果没有初始值，acc就是0
print(a_reduce)
