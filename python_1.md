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

> 1996年，计算机科学家证明了任何简单或复杂的算法，都可以有顺序结构，选择结构和循环结构组合而成。
>
> ```python
> # 所有对象都有布尔值。
> # False  数值零，None，空字符串，空列表，空元组，空字典,空集合的布尔值为>False
> bool(False)  
> bool(0)
> bool(None)
> bool('')
> bool([])
> bool(())
> bool(tuple())
> bool({})
> 
> 
> # 选择结构 if
> if score >= 60 :
> print('hello')
> else :
> print('world')
> 
> 
> # elif
> if score >=90 :
> print('90')
> elif score >=80:
> print('80')
> elif score >=60:
> print('60')
> [else] :
> print('<60')        
> 
> ```

* 条件表达式

> ```python
> score = 88
> result = '及格了' if score >= 60 else '没及格'
> ```

* 循环结构

> ```python
> i=1
> while i< 11:
> print(i)
> i += 1
> while True:
> print(i)
> i += 1
> if i >=100 :
>   break
>  
> for i in range(1,11):   # for i in 可迭代对象：列表，元组
> print(i)
> for _ in range(1,11):
> print('hello')
> 
> words = ['java','python','kotlin','swift']
> for word in words[:]: # 通过切片操作生成一份列表的拷贝
> if len(word)<5:
>   words.remove(word)
>   
> # 遍历集合和字典
> s = {2,3,1}
> for number in s:
> print(number)    # 打印出的顺序是没有顺序的
> 
> for number in sorted(s):
> print(number)
> 
> d = {'fruits':86,'books':88,'videos':83}
> for elem in d:
> print(elem)    # 会打印所有的key
> for elem in d:
> print(d[elem])
> for key in d.keys():
> print(key)
> for value in d.values():
> print(key)
> for key,value in d.items():
> print(key,values)
> 
> # 带索引的序列遍历
> L = ['java','python','swift','kotlin']
> index = 0
> for item in L:
>  print('L[{}]={}'.format(index,item))
>  index += 1
> 
> for index in range(len(L)):
>  print('L[{}]={}'.format(index,L[index]))
>  
> index=0
> while index < len(L):
>  print('L[{}]={}'.format(index,L[index]))
>  index += 1
> 
> # 将要遍历的对象转换为enumerate()对象    
> print(list(enumerate(L)))
> print(list(enumerate(L,1)))  # 索引从1开始
> 
> for index,item in list(enumerate(L)):
>  print('L[{}]={}'.format(index,item)   
>        
> for index,item in enumerate(L):
>  print('L[{}]={}'.format(index,item)   
>        
> # 循环中的break-else,
> isBreak = False
> n = 0
> while n<5:
> if n == 6:
>     isBreak = True
>     break
> n += 1
> if not isBreak:
> print('正常结束')
>  
> isBreak = False
> for n in range(5):
> if n == 6:
>     isBreak = True
>     break
> if not isBreak:
> print('正常结束')
>        
> n = 0
> while n<5:
> if n == 6:
>     break
> n += 1
> else:
> print('正常结束')          
> ```
>
> ```python
> # 循环中的break和continue
> for i in range(1,5):
>     if i == 3:
>         break
>     print('i=',i)
> 
> for i in range(1,5):
>     if i==3:
>         continue
>     print('i=',i)
> # 在嵌套的循环语句中，break和continue默认作用域当前循环
> for i in range(1,4):
>     for j in range(1,4):
>         if i == j:
>             break
>         print('i=',i,'j=',j)
> 
> ```
>
> ```python
> # 并行遍历。同时遍历多个可迭代对象
> names = ['jack','mike','tom']
> ages = [16,32,43]
> for in in range(len(names)):
>     print(names[i],'的年龄是:',ages[i])
>     
> # 使用zip打包多个可迭代对象为zip对象
> zip(names,ages)
> for name,age in list(zip(names,ages)):
>     print(name,'的年龄是:',age)
>     
> for name,age in zip(names,ages):
>     print(name,'的年龄是:',age)
> 
> # 如果多个可迭代对象长度不同，回向短的看齐
> # 可以使用*对zip对象解压缩
> x = [1,2,4]
> y = [4,5,6]
> print(list(zip(x,y)))
> 
> print(list(zip(*zip(x,y))))
> x2,y2 = zip(*zip(x,y))
> ```
>
> ```python
> # map 和 filter
> # map(函数名，可迭代对象）
> result = map(ord,'abcd')
> print(list(result))
> result = map(str.upper,'abcd')
> 
> # filter(函数名，可迭代对象）
> result = filter(str.isalpha,'123abc')
> # 屏蔽掉结果为假的结果
> 
> ```

* 列表生成式

> ```python
> # [元素表达式 for 变量  in  可迭代对象]
> L = [i * i for i in range(1,7)] 
> print(L)
> 
> # 满足条件才给元素表达式
> L = [i * i for i in range(1,7) if not i % 2]  
> print(L)
> 
> # 使用双重循环
> L = [(i,j) for i in range(1,4) for j in range(1,4)]
> # 相当于
> L = []
> for i in range(1,4):
>     for j in range(1,4):
>         L.append((i,j))
> 
> # 双重加if
> L = [(i,j) for i in range(1,4) for j in range(1,4) if i != j]
>  
>     
> # 列表生成式的嵌套
> matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
> L = [[row[i] for row in matrix] for i in range(4)]
> # 相当于
> L = []
> for i in range(4):
>     L.append([row[i] for row in matrix])
>     
> # 还相当于
> L = []
> for i in range(4):
>     l_row = []
>     for row in matrix:
>         l_row.append([row[i]])
>     L.append([l_row])
>     
> ```

* 集合生成式

> ```python
> # {元素表达式 for 变量  in  可迭代对象}
> s = {i * i for i in range(1,7)} 
> print(L)
> 
> # 和列表生成式基本一样，只是换成集合符号
> ```

* 字典生成式

> ```python
> items = ['Fruits','books','others']
> prices = [96,78,83]
> # ==> {'FRUITS':96,'BOOKs':78....}
> # {字典key的表达式:value的表达式 for key ,value in 可迭代对象}
> d = {item.upper():price for item,price in zip(items,prices)}
> 
> # if 从句
> d = {item.upper():price 
>   for item,price in zip(items,prices) 
>   if price > 80 }
> # 双重循环：
> {i:j for i in range(1,4) for j in range(1,4)}
> ```
>

* 函数

> ```python
> # 函数定义,推荐函数名命名规范动宾格式。
> def 函数名([形式参数1,形式参数2,...,形式阐述n]):
>  函数体
> ```
>
> ```python
> # 函数如果直接用return返回，也是有返回值的：None
> def decide_args(arg1,arg2):
>  if arg1 and arg2 :
>      return arg1,arg2
>  elif (not arg1) and (not arg2):
>      return
>  else:
>      result = arg1 or arg2
> print(decide_args)
> print(type(decide_args))
> ```
>
> ```python
> # 位置实参
> def f(a,b,c):
>  print('a=',a,'b=',b,'c=',c)
>  
> f(2,5,8) #实参对应相应形参    
> ```
>
> ```python
> # 关键字形参
> def f(a,b,c):
>  print('a=',a,'b=',b,'c=',c)
>  
> f(a=2,b=5,c=8) # 指定形参名称，
> f(2,5,c=8) # 位置实参和关键字实参，位置实参必须在关键字实参之前
> ```
>
> ```python
> #如果实参对象是可变类型，那么对形参的修改就是对实参的修改
> def f(arg1,arg2):
>  print('初始化形参后：arg1=',arg1,'arg2',arg2)
>  arg1 = arg1 * 2
>  arg2.append(4)
>  print('修改形参后：arg1=',arg1,'arg2',arg2)
> i = 10
> L = [1,2,3]
> print('调用函数前:i=',i,'L=',L)
> f(i,L)
> print('调用函数后:i=',i,'L=',L)
> 
> f(i,L[:])  # 利用切片仅仅把可变类型的值拷贝进去，变量相当于标签
> print('调用函数后:i=',i,'L=',L)
> ```
>
> ```python
> # 多个返回值，利用return元组
> def classify_numbers(numbers):
>  odds = []
>  evens = []
>  for number in numbers:
>      if number % 2 :
>          odds.append(number)
>      else:
>          evens.append(number)
>   return odds,evens
> classify_numbers([15,86,39,26,53,68])
> #([],[])
> 
> def lookup_min_max(numbers):
>  if len(numbers) == 0:
>      return
>  min_num = numbers[0]
>  max_num = numbers[0]
>  for number in numbers[1:len(numbers)]:
>      if number < min_num :
>          min_num = number
>      elif number > max_num:
>          max_num = number
>  return min_num,max_num
> ```
>
> ```python
> # 带默认值的形参
> def f1(a,b=5):
>  print('a=',a,'b=',b)
>  
> f1(2,6)
> f1(2)
> 
> def f2(a,b=5,c=8):
>  print(a,b,c)
> f2(2,6,9)
> f2(2)
> f2(2,c=9)
> 
> # 定义形参默认值时，如果使用了可变类型，并且在函数体中改变了这个值，那么
> # 下次调用函数时，默认值会变成改变后的值。变量就是标签
> # 要使用可变类型对象时要多考虑这些影响。
> 
> ```
>
> ```python
> # 定义关键字形参,只能接受关键字实参
> def f(a,b,*,c,d):
>     print('a=',a,'b=',b,'c=',c,'d',d)    
> f(1,2,c =3 ,d =4)    
> 
> ```
>
> ```python
> # 定义个数可变的位置形参,会将实参初始化为一个元组
> def f(*args):
>     print(args)
> f()
> f(1)
> f(1,2,3)
> # 通常*放到最后一个形参
> def f(a,b,*c):
>     print(a,b,c)
> # 如果个数可变的位置形参只能放在前面，那么后面的位置形参必须都是关键字形参
> def fun2(a,*b,c,d):
>     print(a,b,c,d)
> fun2(1,2,3,4,c=5,d=9)
> 
> ```
>
> ```python
> # 使用 * 将序列中的每个元素都转换为位置实参
> def f(a,b,c):
>     print(a,b,c)
> f(1,2,3)
> L = [1,2,3]
> f(*L)
> 
> def fun(*args):
>     print(args)
> fun(L) # ([1,2,3],)
> fun(*L) # (1,2,3)
> ```
>
> ```python
> # 使用 ** 定义个数可变的关键字形参
> def f(**kwargs):
>     print(kwargs)
> f()
> f(a=1)
> f(a=1,b=2,c=3)  #  {'a':1,'b':2,'c':3}
> 
> def fun(*args,**args): # 位置形参必须在关键字形参之前。
> ```
>
> ```python
> # 使用 ** 将字典中的每个k-value对转换为关键字形参
> D = {'a':1,'b':2,'c':3}
> def f(a,b,c):
>     print(a,b,c)
> f(**D)
> 
> def fun(**args):
>     print(args)
> fun(**D)  
> # 输出：{'a':1,'b':2,'c':3}
> 
> ```
>
> ```python
> # 函数参数总结
> def f1(a,b=5,*args,**kwargs):
>     print(a,b,args,kwargs)
>     
> f1(2,6,7,8,c=9)
> 
> def f2(a,b=5,*,c,**kwargs):
>     print(a,b,c,kwargs)
> f2(*(3,6),**{'c':8,'d':10})
> ```
>
> ```python
> # pass 占位符
> def f1():
>     pass
> 
> if a>0:
>     pass
> 
> for i in range(1,10):
>     pass
> ```
>
> ```python
> # 文档字符串，对函数、模块、类、或方法进行解释说明
> # 可以使用工具根据字符串自动生成文档
> # 通过属性__doc__可以访问文档字符串
> # 调用内置函数help()得到的信息中会包含文档字符串
> 文档、函数体、类的第一行：
> """函数的定义之文档字符串"""
> print(len.__doc__)
> print(help(len))
> # 格式约定
> 1.第一行是简明扼要的总结
> 2.第一行的首字母大写，第一行以句号结尾。
> 3.如果文档字符串包含多行，第二行是空行，从第三行开始是详细的描述
> def form_complex(real = 0.0,imag = 0.0):
>     """Form a complex number.
>     
>     Keyword arguments:
>     real  -- the real part(default 0.0)
>     imag  -- the imaginary part(default 0.0)
>     """
>     pass
> PEP 257
> 
> ```
>
> ```python
> # 函数注解
> # 说明形参或返回值的类型和作用，帮助函数文档化
> PEP 3107
> def f(a:'stirng type',b: int) -> 'join a with b':
>     return a + str(b)
> # 通过属性__annotations__可以访问函数注解
> print(f.__annotations__)
> # 通过help()包含函数注解
> ```
>
> ```python
> # 函数递归(递推 回归)
> # 递归函数包含一种隐式循环，因此，必须有一个明确的递归结束条件
> # 递归解决的问题必须满足两个条件：
> 1.可以通过递归调用来缩小问题的规模，且新问题与原问题有着相同的形式
> 2.存在一种简单情景，可以是递归在简单情景下退出
> # 递归计算阶乘
>    n! = 1*2*3.....*n=(n-1)! *n ,且1!=1
>    如果用函数fac(n)表示n!,那么fac(n) = fac(n-1) * n = n * fac(n-1)
> 且fac(1)=1
> def fac(n):
>     """使用递归结算阶乘"""
>     if n ==1 :
>         return 1
>     return n * fac(n-1)
> print(fac(6))
> 
> # 递归计算菲薄纳妾数列
> F0 = 0,F1=1,Fn=F(n-1)+F(n-2) (n>=2)
> 如果用函数fib(n)表示Fn，那么fib(n) = fib(n-1) + fib(n-2)
> 且fib(0) = 0,fib(1)=1
> def fib(n):
>     if n == 0:
>         return 0
>     if n ==1 :
>         return 1
>     return fib(n-1) + fib(n-2)
> print(fib(6))
> ```

* 舍含王赏麦：

```python
# 设计思路：
def shehanwang(n):
    t = 1  # 当前格子的麦子数
    s = 1  # 当前所有格子的麦子数之和
    for _ in range(2,n+1):
        t *= 2
        s += t
    return s
print(shehanwang(64))

print(sum([2 ** i for i in range(64)]))
```

* 不重复的三位数：

```python
# 设计思路
排列组合：0-9不重复的三位数 9 * 9 * 8 = 648
设百位、十位、个位分别是a,b,c，取值范围是[1,9][0,9][0,9]
通过三重循环穷举
counter = 0
for a in range(1,10):
    for b in range(10):
        for c in range(10):
            if a != b and b!=c and c!=a :
                counter += 1
print(counter) 
```



