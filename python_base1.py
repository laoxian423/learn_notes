from datetime import datetime
from string import Template

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
    
    print('\n\n-列表的加法和乘法操作')
    L1 = [1,2,3]
    L2 = [4,5,6]
    print('L1 = ',L1)
    print('L2 = ',L2)
    print('L1 + L2 = ',L1 + L2)

    print('\n\n-列表的加法不会对原有的值进行修改')
    L1 = L2 = [1,2,3]
    L1 = L1 + [4,5,6]
    print('L1 = L2 = [1,2,3]')
    print('L1 = L1 + [4,5,6]')
    print('L1 , L2 ：',L1,L2)   
    print('L1 的值发生了变化，而 L2 还是原有的值')

    print('\n\n-参数赋值运算符会对列表本身进行修改')
    L1 = L2 = [1,2,3]
    L1 += [4,5,6]
    print('L1 = L2 = [1,2,3]')
    print('L1 += [4,5,6]')
    print('L1 , L2 ：',L1,L2)   
    print('L1 和 L2 的值都发生了变化')

    print('\n\n-列表的乘法')
    L1 = [1,2,3]
    L1 = L1 * 3
    print('L1 = [1,2,3] ;L1 = L1 * 3 =>',L1)
    
    print('\n\n-列表的比较')
    print('[2,3,4]<[2,3,5] =>',[2,3,4]<[2,3,5])
    print('[7,[2,6]] > [7,[2,5]]',[7,[2,6]] > [7,[2,5]])
    a = b = [1,2,3]
    c = [1,2,3]
    print('a = b = [1,2,3];c = [1,2,3]:')
    print('a == b ?:',a == b)
    print('a == c ?:',a == c)
    print('a is b ?:',a is b)
    print('a is c ?:',a is c)

    print('\n\n-列表的反转')
    L = [1,2,3,4,5]
    L.reverse()
    print('L = ',L)
    print('列表的类方法 L.reverse() = >',L)
    L = [1,2,3,4,5]
    iterator = reversed(L)
    print('内置函数(返回一个迭代器)  reversed(L) = >',list(iterator))

    print('\n\n-列表的排序 ')
    L = [3,5,1,2,3,9,10]
    L.sort()
    print('列表的类方法 L.sort(),L.sort(reverse = True) ',L)
    L = [3,5,1,2,3,9,10]
    print('内置的排序函数 sorted(),sorted(reverse = True) ',sorted(L))
    
def t_tuple():
  """元组的使用

  元组是不可变类型，不可在运行时修改
  元组中至少有一个逗号(18,)
  """
  print('\n\n-元组赋值时可以省略小括号：')
  t = "python",18,True
  print('t = "python",18,True =>',t)    
  
  t = (5,[1,3],8)
  print('元组不可修改，但是元组中的可变类型数据是可以修改的：')  
  print('t = (5,[1,3],8) \nt[1][0] = 10 ')
  t[1][0] = 10
  print('t = ',t)

def t_string():
  """字符串就是字符的列表

  python 没有字符数据，字符就是长度1的字符串
  转义字符： 
     换行：\n  回车:\r  制表符:\t  退格:\t
  """
  print('\n\n-原始字符串,python会忽略转义：')
  print("s = r'c:\dos' =>",r'c:\dos')
  s1 ="Hello"
  s2 = "world"
  print('s1 = "Hello" ;s2 = "world";print(s1+s2) =>',(s1+s2))

  print('\n\n-字符串乘法:')
  s1 = "A"
  # 因为字符串就是列表，所以列表能用的方法字符串也能用
  print('s1 = "A";print(s1*3) => ' ,s1 * 3) 

  print('\n\n-字符串的查找：')
  s = '18*18*18*'
  print('s ="18*18*18*"')
  print('s.index("18"),返回第一个18的索引 =>',s.index('18'))
  print('s.find("18"),返回第一个18的索引 =>',s.find('18')) 
  print('s.rindex("18"),从右查找，返回第一个18的索引 =>',s.rindex('18'))
  print('注：子串不存时，index,rindex会抛出异常，find,rfind返回-1')
  print('字符串是不可变类型，无改，增，删操作')
  
  print('\n\n-字符串的几个常用函数：')
  print('字符串的 ordinal value: ord("A") =>',ord('A'))
  print('根据 ordinal value 求对应字符：chr(65) =>',chr(65))

  print('\n\n-字符串常量和常数常量通常会被缓存：')
  print('a=b="Hello" ; c="Hello" ;')
  a = b = "Hello"
  c = "Hello"
  print("a is c ? =>" ,a is c)

  print('\n\n-字符串的反转：')
  s = 'Hello World'
  iterator = reversed(s)
  print("s = 'Hello World' ; iterator = reversed(s) =>",list(iterator))
  
  print('\n\n-字符串的排序（按照ordinal value)：')
  sort_s = sorted(s,reverse=True)
  print('sort_s = sorted(s,reverse=True) =>',sort_s) 
  print('sorted(s,key = 函数名或类名.方法)')
  sort_s_f = sorted(s,key = str.lower)
  print('key 转换成小写后比较，然后按照原值返回结果')
  print('sort_s_f = sorted(s,key = str.lower)',sort_s_f)
  print('元组和列表也可以使用 key ')

def t_format_string():
  """格式化字符串的方法一般有三种：

  1、 % 百分号占位符
  2、 {} 花括号占位符
  3、 $ 美元占位符
  """
  print('\n\n-格式化时间字符串，需导入 datetime')
  s1 = datetime(2018,8,18,18,18,18).strftime('%Y-%m-%d %H:%M:%S')
  print("datetime(2018,8,18,18,18,18).strftime('%Y-%m-%d %H:%M:%S')=>",s1)
  # %s 字符串；  %i or %d  整数；  %f 浮点数 ；
  book = '《数据结构》'
  s = '完成了一本书: %s' % book
  print("book = '《数据结构》';s = '完成了一本书: %s' % book =>",s)
  price = 68.99
  # 超过一个变量，需要放到元组里
  s1 = '花了%6.2f,买了一本书：%s' % (price,book)
  print(s1)
   
  print('\n\n-{}占位符')
  book = '《数据结构解析》'
  s = '买了一本书:{}'.format(book)
  print(s)
  price = 68.99
  s1 = '花了{},买了一本书:{}'.format(price,book)
  s2 = '花了{0},买了一本书:{1},只花了{0}'.format(price,book)
  s3 = '花了{p},买了一本书:{b},只花了{p}'.format(p=price,b=book)
  print("'花了{},买了一本书:{}'.format(price,book)",s1)
  print("'花了{0},买了一本书:{1},只花了{0}'.format(price,book)",s2)
  print("'花了{p},买了一本书:{b},只花了{p}'.format(p=price,b=book)",s3)
  print("\n花括号的一些格式：")
  print('10进制整数 {{:d}} :{:d}'.format(58)) 
  print('二进制 {{:b}} :{:b}'.format(58))  
  print('小写16进制 {{:x}} :{:x}'.format(58))
  print('大写16进制 {{:X}} :{:X}'.format(58))
  print('浮点数 {{:f}} :{:f}'.format(58)) 
  print('千位分割 {{:,}} :{:,}'.format(12345678))  
  print('二进制 {{0:b}} :{0:b}'.format(58))  
  print('二进制 {{num:b}} :{num:b}'.format(num=58)) 
  print('宽度10,右对齐 {{:10}} :{:10}'.format(58)) 
  print('宽度10,左对齐 {{:10}}:{:10}'.format('58')) 
  print('宽度10,包含小数共占3位 {{:10.3}} :{:10.3}'.format(58.00))  
  print('宽度10,精度小数位3位 {{:10.3f}}:{:10.3f}'.format(58)) 
  print('注：内置函数format(),s1 = format(3.13433,"8.3f"')

  print('\n\n- $ 占位符 ，String包中的Template类：')
  price = 88.88
  book = '《不高兴就去看大海》'
  tmpl = Template('花了 $p, 买了一本书：$b')
  s1 = tmpl.substitute(p=price,b=book)
  print(s1)
  s1 = tmpl.substitute({'p':price,'b':book})
  print(s1)
  # 参数不足时，不会抛出错误
  s1 = tmpl.safe_substitute(p=price)
  print(s1)



if __name__ == '__main__' :
    #t_is()            # 用is查看不可变数据类型
    #t_id()            # 用id查看对象的内存地址
    #t_lianshi()       # 链式比较
    #t_logic()         # and 和 or 的优先级
    #t_range()         # range()的用法
    #t_list()          # list列表的用法
    #t_tuple()         # tuple元组的用法
    #t_string()        # 字符串的用法
    t_format_string()  # 格式化字符串 
    #pass
    