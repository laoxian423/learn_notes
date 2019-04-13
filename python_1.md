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

* 