* 不可变类型对象的is比较。不可变内存对象的内存可能会被重用

* id 内置函数可以返回对象的内存地址

* `age=18 , print( 0< age < 100  )`链式比较

* help()    

  help>keywords

* 通过倒入模块keywork查看关键字

  ```python
  >>>import keyword
  >>>keyword.kwlist
  ```

* 计算机科学中最难的两件事，一个是命名，一个是缓存失效。

* None ，表示数据直不存在，它在内存中分配了一定的内存空间，不意味着空，是something,而不是nothing

* and 比 or 优先级高，or 是左运算

* range  返回整数序列，默认起始是0，不包含stop本身，返回值是一个迭代器对象。

  ```python
  range()
  range(stop)
  range(start,stop)
  range(start,stop,step)
  >>>print(list(range(10,20,2)))
  >>>print(3 in range(5))   # True
  >>>print(8 not in range(5)) # True
  ```

  range 占用的内存空间都是相同的。

* 列表 list：

  > 列表是一个有序数列。
  >
  > 每一个列表元素都有两个整数索引指明它的位置，比如第一个元素位置是0 ,最后一个是6,那么最后一个元素还有一个位置标识就是-1,而第一个就是-7.
  >
  > 列表中可以有重复的数据
  >
  > 列表中可保存任何数据，也可混合存储在一个列表。
  >
  > 系统可根据需要自动分配和收回列表内存。
  >
  > 列表的创建：L = ['python',18,True ]      list(rang(1,6))
  >
  > 索引：2个索引，
  >
  > index()放回2个索引大于0那个。
  >
  > ```python
  > L=[2,3,56,3,7,5,3,2,4,65]
  > print(L.index(56))   # 2 ，有多个只放回第一个，没有抛出异常valueError
  > print(L.index(7,3))  # (value,start) ,从3往后找7这个值的索引
  > print(L.index(7,3,7)) # (value,start,stop)
  > 
  > L[0] # 2
  > L[-10]  # 2
  > L[-1] # 65
  > ```
  >
  > * 切片
  >
  > ```python
  > # [start:stop:step] ，不包括stop，好像python的stop都不包含
  > # 默认 start=0 stop=-1 step=1  [::] all
  > # [start:stop]
  > # step 可以是负数
  > [::-1]   # 相当于反转了列表。
  > [0:6:-2] # 空列表
  > # 切片操作是允许索引越界的
  > print(L[:100]) # 不会报索引越界错误
  > 
  > 内置函数slice
  > slice(stop)
  > slice(start,stop)
  > slice(start,stop,step)  # 默认值都是None
  > L=[2,3,56,3,7,5,3,2,4,65]
  > print(L[slice(1,7,2)])
  > print(L[slice(None,None,None)]) #[::]
  > 
  > ```
  >
  > * in 和 not in  检查列表中存在某元素
  >
  > ```python
  > L=[2,3,56,3,7,5,3,2,4,65]
  > 5 in L  
  > 5 not in L
  > ```
  >
  > * 改
  >
  > ```python
  > L=[2,3,56,3,7,5,3,2,4,65]
  > L[2] = 8
  > L[1:4] = [1,9,2]
  > L[1:4] = [5] # 等号左右元素个数可以不同,列表长度会改变
  > ```
  >
  > * 增
  >
  > ```python
  > # 追加一个
  > L=[2,3,7,5,3,4]
  > L.append(9)
  > L.append(9,10)  # [2,3,7,5,3,4,[9,10]]
  > # 扩展
  > L =[3,4,5,6,7,8]
  > L.extend([9,10]) #  [3,4,5,6,7,8,9,10]
  > # 插入
  > L =[3,4,5,6,7,8]
  > L.insert(3,8)  # L =[3,4,5,8,6,7,8] 插在index之后
  > # 切片
  > L=[3,4,5,6]
  > L[2:2] = [8,9] # [3,4,8,9,5,6] ,变成在索引2后插入8,9
  > L[len(l):] = [1,2] # 在末尾添加2个元素
  > ```
  >
  > * 删除
  >
  > ```python
  > L =[3,4,5,4,6,7,8]
  > L.remove(4)  # [3,5,4,6,7,8] ,存在多个指定元素，只删除第一个
  > L.remove(10) # 不存在，抛出ValueError
  > 
  > L = [1,2,3,4]
  > L.pop(2) #  返回被删除的元素，[1,2,4]
  > L.pot(6)  # IndexError:index out of range
  > L.pop()  # 默认删除最后一个
  > 
  > L = [1,2,3,4,5,6]
  > del L[2]  # 删除索引为2的元素
  > del L[1:4]  # 按照切片删除
  > 
  > L = [1,2,3,4,5,6]
  > L[2:3]=[]   # 指定切片赋值空列表
  > L[:]=[] # 列表清空
  > 
  > L = [1,2,3,4,5,6]
  > L.clear()  # 清空列表
  > ```
  >
  > * 加法和乘法操作列表
  >
  > ```python
  > L1 = [1,2,3]
  > L2 = [4,5,6]
  > L3 = L1 + L3  # print(L3)==>[1,2,3,4,5,6],列表的合并
  > 
  > L1=L2=[1,2]
  > L1=L1+[3,4]
  > print(L1,L2) # [1,2,3,4] [1,2]
  > 
  > L1=L2=[1,2]
  > L1 += [3,4]
  > print(L1,L2) # [1,2,3,4] [1,2,3,4] 参数赋值运算符会对列表本身进行修改
  > 
  > L1=[1,2,3]
  > L = L1 * 3
  > print(L)  # [1,2,3,1,2,3,1,2,3]
  > print(L1) # [1,2,3]
  > 
  > L = [0] * 5  # [0,0,0,0,0]
  > 
  > L1=L2=[1,2,3]
  > L1 *= 3
  > print(L1,L2)  # [1,2,3,1,2,3,1,2,3] [1,2,3,1,2,3,1,2,3]
  > ```
  >
  > * 比较列表
  >
  > ```python
  > print([2,3,4]<[2,3,5]) # True
  > print([7,[2,6]] > [7,[2,5]]) # True
  > 
  > a=b=[1,2,3]
  > c=[1,2,3]
  > print(a == b)  # True
  > print(a == c)  # True
  > 
  > print(a is b)  # True 是不是同一个列表
  > print(a is c)  # False
  > 
  > 
  > ```
  >
  > * 列表的反转
  >
  > ```python
  > L = [1,2,3,4,5]
  > L.reverse()
  > print(L) # [5,4,3,2,1]
  > 
  > L = [1,2,3,4,5]
  > iterator = reversed(L) # 返回一个迭代器对象
  > print(list(iterator)) # [5,4,3,2,1],L 没有受到影响
  > ```
  >
  > * 列表的排序
  >
  > ```python
  > L = [3,2,5,1,9,5]
  > L.sort() #L.sort(reverse = True) 逆序排序
  > print(L) # [从小到大]
  > 
  > L = [3,2,5,1,9,5]
  > sorted(L)  # 返回一个排好序的新列表，sorted(L,reverse = True)
  > 
  > ```
  >
  > * 多维列表
  >
  > ```python
  > L = [[3,4],[1,5,3],[6,8,9,7]]
  > print(L[2][1])  # 8
  > 
  > print([[0]*3]*4)  # [[0,0,0],[0,0,0],[0,0,0],[0,0,0],]
  > 
  > print([[0 for i in range(3)] for j in range(4)])  # 列表生成式
  > ```
  >
  > 