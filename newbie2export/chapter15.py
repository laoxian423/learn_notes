# LOOK 文件操作与管理
""" 
* python的文件对象类似于Linux的文件对象
"""

""" 打开文件操作
    open() 是python的内置函数
    open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None,
        closefd=True, opener=None)
    file 可以是字符串或者整数，字符串表示文件名；整数表示文件描述符，指向一个已经打开的文件
    mode 如果是二进制文件需要设置 rb wb xb ab 如果是文本文件需要设置 rt wt xt at
        r 只读 ； w 覆盖写入 ；x 独占模式，文件不存在时创建并写入，存在抛出异常FileExistsError
        a 追加 ； b 二进制模式 ；t 文本模式（默认）； + 更新模式，必须和r w x a组合使用
    buffering 缓冲区策略，默认-1，表示系统自动设置缓冲区；0 时关闭缓冲，直接写入文件，主要用于
        二进制文件的写入；>0 时，用来设置缓冲区字节大小。
    encoding 打开文件时的文件编码。
    errors 文件编码错误时该如何处理
    newline 设置换行模式
    closefd 文件描述符时使用，为True时，文件对象调用close()关闭文件，同时关闭描述符对应的文件
        ，为False时，调用close()关闭文件，但不关闭描述符对应的文件
    opener 打开文件时执行一些加工操作，opener指向一个函数，改函数返回一个文件描述符

    文件描述对应一个打开的文件，如标准输入是0 ，标准输出是1，标准错误是2
"""
f = open(r'f:\temp\test.txt','w+')
f.write('world')
f.close()

with open(r'f:\temp\test.txt','a+') as f:
    f.write('\nhello')

with open(r'f:\temp\test.txt','r') as f:
    file_context = f.read()

print(file_context)
print(type(file_context))


""" 文本文件读写
    read(size=-1)       读取字符串，size限制读取的字节数，-1 时没有限制
    readlines(size=-1)  读取单行字符串，如果到文件尾，则返回空
    readlines(hint=-1)  读取到列表中，-1 行数不限制
    write(s)            将字符串 s 写入到文件中，返回写入的字符数
    writelines(lines)   写入一个列表
    flush()             刷新写缓冲区，将数据写入文件
"""
f_name = r'f:\temp\test01.txt'

with open(f_name, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)
    copy_f_name = r'f:\temp\copy.txt'
    with open(copy_f_name, 'w', encoding='utf-8') as copy_f:
        copy_f.writelines(lines)
        print('文件复制成功')

""" 二进制文件读取
    read(size=-1)       读取字节，size限制最多读取的字节数，-1读取全部
    readline(size=-1)   读取并返回一行
    readlines(hint=-1)  读取到列表中，每一行是列表的元素
    write(b)            写入b字节，返回写入的字节数
    writelines(lines)   写入一个列表
    flush()             刷新缓冲区，数据写入到文件中
"""
f_name = r'f:\temp\Markdown.pdf'

with open(f_name, 'rb') as f:
    b = f.read()
    copy_f_name = r'f:\temp\copy01.pdf'
    with open(copy_f_name, 'wb') as copy_f:
        copy_f.write(b)
        print('文件复制成功')

""" os 模块
    删除文件、修改文件名、创建目录、管理目录
    os.rename(src, dst)     修改文件名
    os.remove(path)         删除文件
    os.mkdir(path)          创建目录
    os.rmdir(path)          删除空目录
    os.walk(top)            遍历top所指的目录树，返回一个三元组(目录路径，目录名列表，文件名列表)
    os.listdir(dir)         列出指定目录中文件和子目录
    os.curdir 属性          当前目录
    os.pardir 属性          当前父目录
"""
"""
import os

f_name = r'f:\temp\copy01.pdf'

try:
    os.rename(f_name, 'f:/temp/md.pdf')  # 不指定目录的话，会修改到当前目录
except OSError:
    print('无法改名....')

try:
    os.mkdir('f:/temp/test')
except OSError:
    print('无法创建目录....')

"""

""" os.path 模块
    os.path.abspath(path)       返回path的绝对路径
    os.path.basename(path)      返回path中最右侧的文件名或目录名
    os.path.dirname(path)       返回path中的目录部分
    os.path.exists(path)        path是否存在
    os.path.isfile(path)        path是否是个文件
    os.path.isdir(path)         path是否是个目录
    os.path.getatime(path)      返回最后一次访问时间，如不存在文件抛出异常
    os.path.getmtime(path)      返回最后一次修改时间，如不存在文件抛出异常
    os.path.getctime(path)      返回创建时间，如不存在文件抛出异常
    os.path.getsize(path)       返回文件大小，如不存在文件抛出异常
"""
