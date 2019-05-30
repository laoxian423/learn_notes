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

#### 0007 更换PIP源

> - 豆瓣：http://pypi.douban.com/simple/
> - 中科大：https://pypi.mirrors.ustc.edu.cn/simple/
> - 清华：https://pypi.tuna.tsinghua.edu.cn/simple

```bash
# 一次性使用
# 可以在使用pip的时候加参数-i https://pypi.tuna.tsinghua.edu.cn/simple

# 例如：
   pip install SomePackage -i https://pypi.tuna.tsinghua.edu.cn/simple
# 这样就会从清华这边的镜像去安装SomePackage库。
# 永久修改
# linux下，修改 ~/.pip/pip.conf (没有就创建一个)， 修改 index-url 为国内镜像地址，内容如下：
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple

#windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini，内容如下
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple 
```

#### 0008 pip 一次安装多个包

```bash
# 列出已经安装的包
pip freeze 
pip list
# 把已安装的包导出列表信息
pip freeze > require.txt
# 根据文件安装软件包
pip install -r require.txt
# 注，该文件中的版本号如果不写，就安装最新包
# 卸载包
pip uninstall PackageName
# 升级包
pip install -U PackageName
# 升级pip
pip install -U pip
# 打包，导出wheel文件
pip wheel PackageName
# 导出wheel文件，本地文件可能没有缓存，需要重新下载，使用命令下载requirements.txt中的包，然后在另一台机子上，使用pip3 install xxxxx.whl 进行安装
pip3 download -r requirements.txt 


```

#### 0009 ImportError 错误
```bash
# 使用pandas时报错：
ImportError: C extension: No module named 'pandas._libs.tslibs.nattype' not built.
# 想着，是不是安装有问题，于是卸载Pandas，准备重新安装，然而被拒绝。
PermissionError: [WinError 5] 拒绝访问。: 'd:\\programs\\python\\python37-32\\lib\\site-packages\\~andas\\_libs\\tslibs\\conversion.cp37-win32.pyd'
# 看到文件名，感觉有些熟悉，好像前面杀毒软件报病毒就是这个，估计被隔离了
# 于是，从隔离区恢复并信任
# 执行pandas还是有问题，就卸载然后重新安装。
# 问题解决
```

#### 0010 nose 测试框架

```python
'''
nose是python框架，使得（单元）测试更加容易。nose可以帮助你组织测试代码。任何匹配正则表达式
(?:^|[b_.-][Tt]est)的Python源代码文件、文件夹或库都将被收集用于测试。nose 充分利用了装饰器
'''
pip install nose
```

