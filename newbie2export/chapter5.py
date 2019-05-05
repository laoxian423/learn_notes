# coding=utf-8

# Python 编码规范
"""
   常用规范：PEP8 和 谷歌python编码规范
   https://www.python.org/dev/peps/pep-0008
   https://google.github.io/styleguide/pyguide.html
   1、命名规范：
   * 包名：小写，推荐域名倒置，com.apple.quicktime.v2
   * 模块名: dummy_threading
   * 类名：驼峰，SplitViewController
   * 异常名：同类，用Error结尾，FileNotFoundError
   * 变量名：和模块名差不多，如果变量只在模块内部或函数内部，有单下划线开头，如果是私有
     变量，有双下划线开头。
   * 函数和方法名：同变量名
   * 常量名：全部大写。多单词用下划线链接。
   2、注释规范：
   2.1 文件注释：
      #
      ＃ 版权所有 2015 北京智捷东方科技有限公司
      ＃ 许可信息查看 LICENSE . txt 文件
      ＃ 描述 ：
      #       实现日期基本功能
      ＃ 历史版本 ：
      #       2015 7 22 ：创建关东升
      #       2015 - 8 - 20 ： 添加 socket 库
      #       2015 - 8 - 22 ：添加 math 库
      #
      2.2 文档注释：
      * 注释内容能够生成 API 帮助文档 ，可以使用官方 pydoc工具
      * 文档注释位于被注释的模块、函数、类和方法内部的第一条
      * 文档注释用三重双引号包裹起来
      2.3 TODO注释：
      * pycharm等IDE提供的一种特殊注释。主流IDE 一般都支持TODO
      * 有TODO 注释说明此处有待处理的任务或代码未完成。
      * 从pycharm的左下角todo菜单可以看到当前项目的todo注释
      3.导入规范：
      * 放置文件顶部，位于模块注释和文档注释之后
      * 每一个导入语句只能导入一个模块：
         import re
         import struct
         from codeop import CommandCompiler,compile_command
      * 导入顺序按照从通用到特殊：标准库-》第三方库-》自己模块，每一组中间有空行
      4、代码排版
      * import 语句前后保留两个空行
      * 函数声明前保留两个空行
      * 类声明之前保留两个空行
      * 类方法声明之前保留一个空行
      * 两个逻辑代码块之间保留一个空行
      * 等号 = 左右一个空格
      * 二元运算使用空格与操作数分开: a += c + d
      * 括号内不要有空格
      * 逗号、分号、冒号后面有一个空格 ：x, y = y, x
      * 参数列表、索引或切片的左括号前不要空格：doque(1)  不要doque (1)
      * 一行代码最多79个字符，注释最多72个字符。
      * 断行：在逗号，运算符后面断开，尽量不使用续行符“\”
"""
y = 20
# TODO 声明函数
print(y)