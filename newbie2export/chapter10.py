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


