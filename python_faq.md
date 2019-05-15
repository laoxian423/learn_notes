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

#### 0004 wxPython install on ubuntu 18
```bash
sudo apt install make gcc libgtk-3-dev libwebkitgtk-dev 
     libwebkitgtk-3.0-dev libgstreamer-gl1.0-0 freeglut3 
     freeglut3-dev python-gst-1.0 python3-gst-1.0 libglib2.0-dev 
     ubuntu-restricted-extras libgstreamer-plugins-base1.0-dev

sudo pip3 install wxPython
# 安装了好长时间，一个setup.py执行了差不多30分钟，可能我的笔记本太差
```

#### 0005 动态页面数据抓取的方法

```bash
1）无浏览器界面抓取方法
# selenium   一个web自动化测试工具，可以按指令自动化操作，可以直接运行在浏览器上，可以让浏览器自动加载页面，获取页面，甚至页面截屏，或者判断动作是否发生，它自己不带浏览器，需要与第三方浏览器结合才能使用。
# http://pypi.python.org/simple/sulenium
# 参考文档:http://selenium-python.readthedocs.io/index.html
pip intall selenium

# PhantomJS  一个无界面浏览器，会把网页加载到内存中并执行上面的JS。
# PhantomJS 只能下载（http://phantomjs.org/download.html。它是一个浏览器而非python库，但是它可以通过selenium调用来使用
# 官方文档:http://phantomjs.org/documention
2）调用真实浏览器抓取方法
# 用 selenium 操作 firfox 浏览器打开页面，抓取动态数据
# 解决版本兼容问题 https://github.com/mozilla/geckodriver/releases，不需要安装，解压即可。
# 在windows环境变量中增加firefox 和 geckodriver的路径

```

#### 0006 BeautifulSoup 网页结构解析工具：

> * 可以根据HTML标签及CSS选择器进行查找的工具包
>
> * https://www.crummy.com/software/BeautifulSoup/
>
> * BeautifulSoup类的常用API:
>       .find_all(tagname): 根据标签返回所有符合条件的元素列表
>       .find(tagname): 根据标签返回符合条件的第一个元素
>       .select(selector):通过css中选择器查找符合条件的所有元素
>       .get(key, default=None): 获取标签属性值
>       .title: 获得当前HTML页面的title属性值
>       .text:放回标签中的文本内容。

```bash
pip install beautifulsoup4
```

