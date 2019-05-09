* pysnooper： 很好用的 debug 插件

  ```bash
  pip install pysnooper
  # 使用方式
  import pysnooper
  
  @pysnooper.snoop()   # 会详细输出每一行的执行情况
  def number_to_bits(number):
      if number:
          bits = []
          while number:
              number, remainder = divmod(number, 2)
              bits.insert(0, remainder)
          return bits
      else:
          return [0]
  
  number_to_bits(6)
  # 保存到文件
  @pysnooper.snoop('/my/log/file.log')
  ```

* pymysql   MySQL操作插件

  ```bash
  pip install pymysql
  # 依赖库 
  pip install cryptography
  ```

  