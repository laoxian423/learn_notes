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
  >       %.5s  只显示前5个字符
  >       %8.3f  宽度8小数3位
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
  > # s.upper() 大写
  > # s.lower()  小写
  > # s.swapcase(): 交换大小写
  > # s.capitalize():首字母大写
  > # s.title() : 每个单词首字母大写，剩余小写
  > 
  > # s.isupper(): 是否都是大写
  > # s.islower(): 是否都是小写
  > # s.istitle(): 是否每一个单词首字母是大写，剩余是小写
  > 
  > ```
  >
  > * 字符串对齐
  >
  > ```python
  > # s.center(18,'*')   第一个参数是宽度，第二个是填充字符,第二个省略是空格填充
  > # s.ljust(18,'*')
  > # s.rjust(18,'*')
  > # s.zfill(6)  右对齐，左边用零对齐，只接受一个宽度参数
  > 
  > ```
  >
  > * 字符串的子串替换
  >
  > ```python
  > s = 'Hello-Hello-Hello'
  > # s.replace(‘hello',‘hi’)   第一个参数是被替换的子串，第二个是替换后的子串，返回替换后的字符串,
  > # s.replace(‘hello',‘hi’,1)   第一个参数是被替换的子串，第二个是替换后的子串，返回替换后的字符串,第三个最大替换次数
  > 
  > ```
  >
  > * 字符串字符转换
  >
  > ```python
  > # maketrans  translate      对字符串的某些字符进行转换
  > # 先用maketrans 创建转换表
  > table = str.maketrans('bcd','234')  # 静态方法,对应转换，b->2,c_3
  > print(table) # {98:50,99:51,100:52}
  > table = str.maketrans({'b':2,'c':3,'d':4})
  > table = str.maketrans({98:50,99:51,100:52})
  > s.translate(table)
  > table = str.maketrans('bcd','234','ie') # 把i和e都删掉
  > s.translate(table)
  > table = str.maketrans('','','ie') # 把i和e都删掉
  > 
  > ```
  >
  > * 字符串的劈分和合并
  >
  > ```python
  > # s.split()  从左劈分,默认分隔符是空格，返回值都是list
  > # s.rplit()  从右劈分,默认分隔符是空格，返回值都是list
  > s = 'Python  Swift  kotlin'
  > s.split()  # ['Python','swift','kotlin']
  > s = 'python|swift|kotlin'
  > s.split(sep='|')
  > s = 'Python  Swift  kotlin java'
  > s.split(maxsplit = 2) # 最大劈分次数
  > 
  > # partition  劈分，必须指定劈分符
  > # rpartition 将字符串分为三部分
  > 第一部分：劈分符前
  > 第二部分：劈分符
  > 第三部分：劈分符后面
  > s='hello-world-'
  > s.partition('-')  # ('hello','-','world-)
  > 
  > # join 合并，列表和元组都可以
  > s = '|'.join(['python','swift','kotlin']) 合并用’|‘分隔
  > s = '|'.join('python') # p|y|t|h|o|n
  > 
  > ```
  >
  > * 以is开头的方法
  >
  > ```python
  > """
  > ’123'.isidentifier():是否是合法的标识符
  > ‘\t \r \n’.isspace()：是否由空白字符组成，指标符、回车、换行等
  > 'abcd'.isalpha():是否全部是字母
  > '123'.isdecimal():是否全部是十进制数组成
  > '233'.isnumeric():是否全部是数字,汉字数字和罗马数字都是数字
  > '111abc'.isalnum():是否全部有字母和数字组成
  > """
  > """
  >   keyword 关键字检查模块
  > """
  > import keyword
  > print(keyword.iskeyword('if'))
  > ```
  >
  > * 取出前导字符串或后续字符串
  >
  > ```python
  > # s.lstrip()  默认都是取空格
  > # s.rstrip()
  > # s.strip()
  > s='    hello  world    '
  > s='www.example.com'
  > s.lstrip('cmowz.')  # example.com
  > s.rstrip('cmowz.')  # www.example
  > s.strip('cmowz.') # example
  > ```

  * 字典

  > ```python
  > pbook={'zhangsan':'122222222','lisi':'133333333','wangwu':'144444444'}
  > print(pbook['zhangsan'])
  > ```
  >
  > * 字典元素都是key-value对
  > * key是唯一的
  > * 元素是无序存放的
  > * key必须是不可变对象
  > * 字典是空间换时间，比较占内存。
  >
  > ```python
  > # 字典的创建
  > dict1 = {'key1':'value1','key2':'value2'}
  > dict2 = {} # 空字典 
  > 
  > dict({'key1':'value1','key2':'value2'})
  > dict(name='jack',age='18')
  > dict([('name','jack'),('age',18)])
  > dict(zip(range(3),'ABC'))
  > 
  > dict.fromKeys(['name','age']) #{'name':None,'age':None}
  > dict.fromKeys(['name','age'],'N/A') # 指定一个默认值
  > 
  > ```
  >
  > ```python
  > # 查
  > d = {'name':'jack','age':18}
  > print(d['name'])
  > 
  > print(d.get('name'))
  > print(d.get('zhangsan','nan'))  # 设置不存在的key时返回的value
  > 
  > print('age' in d)  # 有这个key吗
  > print('age' not in d)
  > ```
  >
  > ```python
  > # 改
  > d = {'name':'jack','age':18,'gender':'man'}
  > d['age'] = 20
  > 
  > d.update({'name':'tom','age':20})
  > d.update([('name','mike'),('age',20)])
  > d.update(name='mike',age=20)
  > 
  > ```
  >
  > ```python
  > # 增
  > d = {'name':'jack','age':18}
  > d['gender']='man'   # 新增一个key-value
  > 
  > d.update({'gender':'man','score':90})
  > d.update([('gender','man'),('score',90)])
  > d.update(gender='man',score=90)
  > ```
  >
  > ```python
  > # 删
  > d = {'name':'jack','age':18,'gender':'man'}
  > value = d.pop('age') # 返回key对应value的值
  > value = d.pop('score',90) # key 不存在时，可以返回一个设定值
  > 
  > del d['age']
  > 
  > key_value = d.popitem()   # 删除任意一个k-value对
  > d.clear()  # 清空字典
  > ```
  >
  > ```python
  > # 为key设置默认value值
  > d = {}
  > print(d.setdefault('name','defaultName'))
  > >>>defaultName
  > d==>{'name':'defaultName'}
  > ```
  >
  > ```python
  > # 字典的视图，视图会随着字典变化
  > # keys  返回所有的key
  > # values  返回所有的value
  > # items  返回所有的key-value对
  > d = {'name':'jack','age':18,'gender':'man'}
  > keys = d.keys()
  > print(list(keys))
  > # d.items  返回一个列表，元素是列表
  > ```
  >
  > ```python
  > # 借助字典格式化字符串
  > pbook={'zhangsan':'1111111','lisi':'22222222','wangwu':'3333333'}
  > print('wangwu number:%s,zhangsan number:%s' %(pbook['wangwu'],pbook['zhangsan']))
  > # %(key)s
  > print('wangwu number:%(wangwu)s,zhangsan number:%()zhangsan' % pbook )
  > 
  > print('wangwu number:{},zhangsan number:{}'.format(pbook['wangwu'],pbook['zhangsan']))
  > # {key}
  > print('wangwu number:{wangwu},zhangsan number:{zhangsan}'.format_map(pbook))
  > 
  > ```

  * 集合

  > 只有key的字典：
  >
  > 集合中不可以有重复数据,重复的数据会被去除掉
  >
  > 数据是无序的
  >
  > 可以是任何不可变类型，可混合存放
  >
  > 可以动态伸缩，系统可动态分配内存
  >
  > 集合会浪费较大的内存，与list相比
  >
  > 不能使用{}创建空集合，`print(type({}))`
  >
  > ```python
  > # 集合的创建
  > s = {3,5,9,2,6}
  > 
  > set(range(1,6))  # range(start,stop)
  > set([3,4,5,6])
  > set((3,7,5,45,6))
  > set('3567898')
  > set({3,4,5,6,7})
  > set() # 空集合
  > ```
  >
  > * 集合间的关系
  >
  > ```python
  > # 两个集合是否相等
  > s1 = {1,3,5,7,9}
  > s2 = {3,7,9,5,1}
  > s1 == s2  # True
  > s1 != s2  # False
  > 
  > # 判断一个集合是否是另一个集合的子集
  > s1 = {1,3,5,7,9}
  > s2 = {2,3,6,7,10}
  > s2 = {1,3,5,6,7,9}
  > s1.issubset(s2)  # False
  > s1.issubset(s3)  # True
  > 
  > # 一个集合是否是另一个集合的超集
  > print(s2.issuperset(s1)) # False
  > print(s3.issuperset(s1)) # True
  > 
  > # 两个集合是否没有交集
  > s1 = {1,3,5,7,9}
  > s2 = {2,3,6,7,10}
  > s3 = {2,4,6,8,10}
  > s1.isdisjoint(s2)   # False
  > s1.isdisjoint(s3)   # True
  > 
  > ```
  >
  > * 集合的数学操作
  > * ![1556023210423](/home/morgan/myRepositray/learn_notes/pic/1556023210423.png)
  >
  > ```python
  > # 交集
  > s1 = {1,3,5,7,9}
  > s2 = {2,3,6,7,10}
  > print(s1.intersection(s2))
  > print(s1 & s2)
  > # 计算交集并更新值
  > s1.intersection_update(s2)  # s1 ={3,7}
  > 
  > # 并集
  > s1 = {1,3,5,7,9}
  > s2 = {2,3,6,7,10}
  > s1.union(s2)
  > print(s1 | s2)
  > 
  > # 差集
  > s1 = {1,3,5,7,9}
  > s2 = {2,3,6,7,10}
  > print(s1.difference(s2))
  > print(s1 -s2)
  > print(s1.difference_update(s2))
  > 
  > # 对称差集（并集-交集）
  > s1 = {1,3,5,7,9}
  > s2 = {2,3,6,7,10}
  > s1.symmetric_difference(s2)
  > s1.symmetric_difference_update(s2)
  > print(s1 ^ s2)
  > ```
  >
  > * 集合的查操作
  >
  > ```python
  > s = {3,4,5,6,7}
  > print(5 in s)
  > ```
  >
  > * 集合的增操作
  >
  > ```python
  > s = {3,4,5,6,7}
  > s.add(8)
  > 
  > s.update({2,8})
  > s.update([2,8])
  > s.update((2,8))
  > ```
  >
  > * 集合的删操作
  >
  > ```python
  > s = {3,4,5,6,7}
  > s.remove(5)  # key不存在，抛出keyError
  > s.discard(5) # key不存在，不抛出错误
  > s.pop(5) # 有返回值5
  > s.pop() # 任意一个被删除
  > s.clear() #清空集合
  > ```
  >
  > * 不可变集合frozenset
  >
  > ```python
  > # 存在hash值
  > # 可以作为字典的key
  > # 可以作为set中的元素
  > print(frozenset())
  > print(frozenset(range(1,6)))
  > print(frozenset([2,3,5,7,6]))
  > print(frozenset((3,5,6,7,8)))
  > print(frozenset('abcdef'))
  > print(frozenset({3,5,6,7,8,9}))
  > 
  > ```

* 流程控制

