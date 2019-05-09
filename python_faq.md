#### 0001    pylint 是什么：

> Pylint 是一个 Python 代码分析工具，它分析 Python 代码中的错误，查找不符合代码风格标准（Pylint 默认使用的代码风格是 PEP 8，具体信息，请参阅参考资料）和有潜在问题的代码。目前 Pylint 的最新版本是 pylint-0.18.1。
>
> * Pylint 是一个 Python 工具，除了平常代码分析工具的作用之外，它提供了更多的功能：如检查一行代码的长度，变量名是否符合命名标准，一个声明过的接口是否被真正实现等等。
> * Pylint 的一个很大的好处是它的高可配置性，高可定制性，并且可以很容易写小插件来添加功能。
> * 如果运行两次 Pylint，它会同时显示出当前和上次的运行结果，从而可以看出代码质量是否得到了改进。

#### 0002 pysnooper： 很好用的 debug 插件

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

#### 0003 pymysql   MySQL操作插件

```bash
pip install pymysql
# 依赖库 
pip install cryptography
```

