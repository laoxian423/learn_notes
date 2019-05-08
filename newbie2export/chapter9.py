# LOOK 数据结构
"""数据结构
序列结构：
    有序、可迭代、可重复出现。
    元组touple、列表list、字符串str、字节序列bypes
    序列可进行分片、索引、加和乘
    序列中的元素通过下标访问
    max(t)  返回最后一个元素
    min(t)  返回第一个元素
    + 链接两个序列
    * 将序列重复多少次
    序列都支持分片：
      [start:stop:step]
"""

"""元组 touple： 
元组是一种序列结构,不可变序列
元组的创建有三种方式：
    t = 1,2,3,4
    t = (1,2,3,4)
    t = touple([1,2,3,4])
    t = (1,)
元组的访问：
    下表、分片
"""
a =  ('hello','world',1,2,3)
print(a[1])
print(a[1:])

# 元组的拆分
str1,str2,aa,bb,cc = a
print(str1,str2,aa,bb,cc)
str1,str2,*n = a
print(str1,str2,n)

# 元组的遍历
a =  ('hello','world',1,2,3)
for item in a:
    print(item)
for i , item in enumerate(a):
    print(i,item)
    
"""列表 list
    列表是一种可变序列，可追加、插入、删除、扩展、替换
    列表的元素可以是混合元素
列表的创建：
"""
L = [1,2,3,4]
L = []
# list() 可以将任何可迭代对象转变为列表。
L = list((1,2,3,4))

# 列表的追加
L.append('append')
L.extend([6,7,8,9])
print(L)

# 列表的插入
L.insert(3,"insert")
print(L)

# 列表的删除
L.remove('append')
popvalue = L.pop(3)
print(popvalue, L)

""" 列表的其他方法
L.reverse()  # 倒置
L.copy()     # 拷贝，拷贝后的列表与原有列表没有关系
L.clear()    # 清除
L.count(2)   # 统计列表中2的个数
L.index(value [,start[,stop]]) # 返回 value 的索引
"""

"""推导式
   列表推导式
   集合推导式
   字典推导式
"""
n_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(n_list)

""" 集合 set
    非序列数据结构。可迭代的、无序的、不能包含重复元素的数据结构。
    可变集合（set），不可变集合（frozenset）
    没有 key 的 字典
"""
a = {'tom','jack','mark'}
print(a)
print(len(a))
b = set((20,10,50))
print(b)

""" 集合的修改
    add(elem)       添加元素，如果已经存在，不会抛出异常
    remove(elem)    删除元素，不存在会抛出异常
    discard(elem)   删除元素，不存在不会抛出异常
    pop()           删除任意一个元素，返回该元素
    clear()         清空集合
"""
print(a)
a.add('eggstone')
print(a)
a.remove('mark')
print(a)
a.pop()
print(a)

# 集合的遍历：集合不可通过索引访问，但是它是一个可迭代对象
for item in b:
    print(item)

# 集合推导式
n_list = {x for x in range(100) if x % 5 ==0}
print(n_list)


""" 字典 dict
    可迭代的，无序的，可变的
"""
dict1 = {102:'tom',121:'jack',134:'mark'}
print(dict1)
print(len(dict1))

dict2 = dict(zip([102,111,222],['tong','li','wang']))
print(dict2)

"""字典的访问
    get(key[,default])  通过key返回值，没有返回default
    items()  返回所有键值对
    keys()  返回key视图
    values() 返回value视图
"""

# 字典的遍历
for id in dict2.keys():
    print(id,dict2[id])

# 字典推导式
input_d = {'one':1,'two':2,'three':3,'four':4}
output_d = {k:v  for k, v in input_d.items() if v % 2 ==0 }
print(output_d)