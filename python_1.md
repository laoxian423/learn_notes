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

  * 元组：

  > * 元组用小括号表示（）
  > * t = ('python',18,True)
  > * 小括号可以省略：t = 'python',18,True
  > * 空元组：()    tuple()
  > * 元组是不可变类型，不可在运行时修改
  > * t = (5,[1,3],8)    `t[1][0]=7`  引用所指向的可变数据的值是可以改变的
  > * 一个元素的元组
  > * t =(18)
  > * print(t)   # 18
  > * print(type(t))  # class int
  > * 元组中至少要有一个逗号，`(18,)  18,`
  > * a,b=[5,8]  # a=5  b=8
  > * [a,b] = [5,8]  
  > * a,b = 5, 8
  > * a, *b ,c =,1,2,3,4   # 1  [2,3]   4
  > * a = 5    b= 8
  > * 交换a,b：  a,b = b,a
  > * 赋值运算符的左右两边都是元组，左变量元组，右表达式元组

  * 字符串

  > 字符的列表，列表的操作对于字符床也是适用的。
  >
  > python没有字符型数据，字符就是包含1个元素的字符串
  >
  > str()
  >
  > 转义字符：
  >
  > 换行：\n  回车:\r  水平制表符：\t  退格：\t
  >
  > r'\tC:\\Program Files'     原始字符串 R大写也可以 ，最后不能是一个反斜杠\
  >
  > 跨多行：三个引号 print("""  zhangsan 
  >
  > lisi 
  >
  > wangwu  """)
  >
  > 断句：末尾\
  >
  > 字符串加法：print('hello' + 'world')   # hello world
  >
  > s = 'hellow' ', ' 'world'
  >
  > print(s)  # hellow world
  >
  > print('hello' * 3)  # 重复3遍
  >
  > 查：可看作列表
  >
  > index find  rfind  rindex
  >
  > s ='5739182186'
  >
  > s.index('18')  # 4  返回第一个
  >
  > s.find('18')  # 4 返回第一个
  >
  > s.rindex('18') # 7   从右查找
  >
  > s.rfind('18') # 7  从右查找
  >
  > s.index('18',1,5)   valueError
  >
  > s.rindex('18',1,5)
  >
  > 子串不存在时，index,rindex抛出错误，find,rfind返回-1
  >
  > 字符串是不可变类型，无改、增、删操作
  >
  > * 字符串比较：
  >
  > 与列表比较规则差不多
  >
  > 比较的是字符的ordinal vlaue,内置ord()
  >
  > 对应的是chr()
  >
  > is 类型判断
  >
  > a=b='Hello'
  >
  > c='Hello'
  >
  > a is c      True    字符串常量和常数会被缓存
  >
  > * 字符串的反转
  >
  > reversed() 内置函数，没有reverse方法，字符串不可变
  >
  > s = 'Hello World'
  >
  > iterator =reversed(s) # reversed object
  >
  > print(list(iterator))
  >
  > * 排序
  >
  > sorted(s,reverse = True)  返回字符串
  >
  > sorted(s,key = 函数名或类名.方法)  key 自定义排序方法
  >
  > stored(s,key = str.lower) ,对字符串中的每一个字符调用str.lower,全部转成小写后，进行排序，只是排序规则变了，字符串该是大写还是大写
  >
  > 元组和列表也可以使用key
  >
  > 不止是内置函数可以使用key,方法也可以
  >
  > * 格式化字符串：
  >
  > `‘2018-08-18 18:18:18'  '%Y-%m-%d %H​:%M:%​S'`
  >
  > 常见方式有三种：
  >
  > %  占位符  `%Y-%m-%d %H:%M:%S`  
  >
  > `from datetime import datetime`
  >
  > `print(datetime(2018,8,18,18,18,18).strftime('%Y-%m-%d %H:%M:%S'))`
  >
  > %s   字符串  会把任何类型转换为字符串
  >
  > %i 或 %d   整数
  >
  > %f   浮点数
  >
  > %使用百分号进行转义：`'完成了%d%%'` % 80
  >
  > ```python
  > book = '《数据结构》'
  > s = 'a book: %s ' %  book
  > print (s)
  > 
  > price = 68.99
  > '花了%f,买了一本书:%s' % (price,book) # 超过一个变量，需要放在一个元组中 
  > """
  > %中可以指定宽度  %10d  数字右对齐  字符串也是右对齐
  > %中可以指定精度  %.3f  三位小数
  >          %.5s  只显示前5个字符
  >          %8.3f  宽度8小数3位
  > """
  > ```
  >
  > {}   占位符  
  >
  > format
  >
  > ```python
  > book = '《数据结构》'
  > s = '买了一本书:{}'.format(book)
  > print(s)
  > price = 68.88
  > s = '花了{},买了一本书:{}'.format(price,book)
  > s = '花了{0},买了一本书:{1},只花了{0}'.format(price,book)
  > s = '花了{p},买了一本书:{b},只花了{p}'.format(p=price,b=book)
  > s = '花了{0},买了一本书:{1},只花了{0}'.format(price,book)
  > 
  > print('{:d}'.format(58))  # 10进制整数
  > print('{:b}'.format(58))  # 二进制
  > print('{:x}'.format(58))  # 小写16进制
  > print('{:X}'.format(58))  # 大写16进制
  > print('{:f}'.format(58))  # 浮点数
  > print('{:,}'.format(12345678))  # 千位分割
  > print('{0:b}'.format(58))  # 二进制
  > print('{num:b}'.format(num=58))  # 二进制
  > print('{:10}'.format(58))  # 宽度  右对齐
  > print('{:10}'.format(’58‘))  # 宽度 左对齐
  > print('{:10.3}'.format(58))  # 宽度,总共3位
  > print('{:10.3f}'.format(58))  # 宽度,精度小数位3位
  > from datetime import datetime
  > print('{:%Y-%m-%d %H:%M:%S}'.format(datetime(2018,8,18,18,18,18))) 
  > # 内置函数format()
  > format(58,'b')
  > format(3.1415926,'8.3f')
  > ```
  >
  > $   占位符  
  >
  > string类Template
  >
  > ```python
  > from string import Template
  > price = 68.88
  > book = '<<data struct>>'
  > tmpl=Template('cost $p,buy a book:$b')
  > s = tmpl.substitute(p=price,b=book)
  > s = tmpl.substitute({'p':price,'b':book})
  > s = tmpl.safe_substitute(p=price) # 参数不足时不会抛出错误
  > 
  > 
  > ```
  >
  > * 大小写转换
  >
  > ```python
  > # upper 大写
  > # lower  小写
  > # swapcase: 交换大小写
  > # capitalize:首字母大写
  > # title : 每个单词首字母大写，剩余小写
  > 
  > ```
  >
  > 
  >
  > 
  >
  > 
  >
  > 