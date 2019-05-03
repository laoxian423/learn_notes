def t_is():
    """ 对不可变数据类型使用 is 比较 """
    int1 = 188
    tuple1 =  (1,2,3)

    int2 = int1
    tuple2 = tuple1

    print(int1 is int2)
    print(tuple1 is tuple2)


def t_id():
    """ 使用id 查看对象的内存地址 """
    int1 = 19
    tuple2 = (2,3,4)
    print(id(int1))
    print(id(tuple2))

def t_lianshi():
    """ python 的链式比较 """
    age = 18
    print(0 < age < 100)

def t_logic():
    """ 测试逻辑运算符的优先级 
    
    and 比 or 优先级高，且 or 是左运算
    """
    arg1 = True
    arg2 = False
    arg3 = True
    # and 的优先级高于or,所以先计算 arg2 and arg3,
    # 结果和arg1进行or运算
    and1 = arg1 or arg2 and arg3
    print(and1)

def t_range():
    """ 测试range的一些用法

    range返回整数序列，默认起始是0,不包含stop，返回一个迭代对象。
    range(start,stop,step)
    """
    print('range(10):',list(range(10)))
    print('range(1,5):',list(range(1,5)))
    print('range(1,10,2):',list(range(1,10,2)))
    print('3 in range(1,5)?:',3 in range(1,5))
    print('8 not in range(1,5)?:',8 not in range(1,5))

def t_list():
    """ list 的用法和说明：
        * 列表是一个有序数列
        * 列表中的每一个元素都有两个下标，比如一个6个元素的列表
          其中第一个除了是下标0外，还有一个下标-7,最后一个除了
          下标是6以外，还有一个下标-1。
        * 列表中可以有重复的数据
        * index(value,start,stop)类方法返回某个元素大于0的索引
    """
    L = [1,2,3,4,5,6,7,8,7,8]
    print('L = [1,2,3,4,5,6,7,8,7,8]')
    # index(value) 有多个值时只返回第一个
    print('元素值4的索引，L.index(4):',L.index(4))
    print('从下标4往后找元素7的下标，L.index(7,4):',L.index(7,4))
    print('从下标3至8找元素值7的下标，L.index(7,3,8):',L.index(7,3,8))
    print('L[0]:',L[0])
    print('L[-7]:',L[-7])
    print('L[-1]:',L[-1])

    # 切片操作：
    # [start:stop:step] 从start到stop,不包括stop,python几乎所有的stop参数都不含
    # stop。
    print('切片操作：')
    print('L[:] 显示全部，创建了一个拷贝:',L[:])  
    # 列表拷贝
    arg1 = L[:]
    print('arg1 = L[:],print(arg1):',arg1)
    print('arg1 is L ?:',arg1 is L)
    # 列表反转
    arg1 = L[::-1]  
    print('arg1=L[::-1],反转列表：',arg1)    
    # 切片操作是允许索引越界的，不会抛出异常
    print('print(L[:100]),不会越界错误',L[:100])
    # 内置函数slice()
    print('\n\n')
    print('内置切片函数：slice(start,stop,step)')
    print('L[slice(1,7,2)]:',L[slice(1,7,2)])
    print('L[slice(None,None,None)]:',L[slice(None,None,None)])
    # 使用in 和 not in 检查列表中存在的元素
    print('\n\n-使用in 和 not in 检查列表中存在的元素 ')
    print('print(5 in L):',5 in L)
    print('print(5 not in L):',5 not in L)
    
    print('\n\n-列表的修改操作：')
    print('修改前 L :',L)
    L[2] = 10
    print('直接赋值，L[2]=10 :',L)
    L[1:4] = [12,13,14]
    print('区段赋值 L[1:4] = [12,13,14] :',L)
    L[1:4] = [5]
    print('减少列表长度的赋值 L[1:4] = [5]',L)

    print('\n\n-列表的增加操作：')
    L.append(88)
    print('追加元素 L.append(88):',L)
    L.append([8.8,9.9])
    print('追加子列表元素 L.append([8.8,9.9]):',L)
    L.extend([99,100])
    print('扩展列表 L.extend(99,100):',L)
    L.insert(3,888)
    print('插入元素 L.insert(index,value) L.insert(3,888):',L)
    
    print('\n\n-列表的删除操作：')
    L.remove(888)
    print('L.remove(value)  L.remove(888):',L)
    L.pop(2)
    print('L.pop(index)  l.pop(2):',L)
    del L[5]
    print('del L[5]:',L)
    del L[6:]
    print('del L[6:] :',L)
    L[:] = [] 
    print('L[:] = [] or L.clear(),列表清空 :',L)
    







if __name__ == '__main__' :
    #t_is()            # 用is查看不可变数据类型
    #t_id()            # 用id查看对象的内存地址
    #t_lianshi()       # 链式比较
    #t_logic()         # and 和 or 的优先级
    #t_range()         # range()的用法
    t_list()          # list的用法
    #pass
    