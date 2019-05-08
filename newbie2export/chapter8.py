# LOOK 控制语句
"""控制语句
分支语句： if
循环语句：while 和 for
跳转语句：break  continue return
"""

""" if 语句的三种模式：
if 条件：
    pass
------------
if  条件：
    pass
else :
    pass
------------
if  条件：
    pass
elif 条件:
    pass
elif 条件：
    pass
else:
    pass
------------
"""

"""三元运算符：条件表达式
表达式1  if  条件  else  表达式2  
条件为真时返回表达式1，否则返回表达式2
"""
a = 10
b = 11
c = a*a if a<b else b*b
print(c)

"""循环语句 while
while 循环条件：
    pass
[else]:
    pass

在循环 break,return 或者 异常后执行else
"""

"""循环语句 for
for 迭代变量 in 序列：
    pass
[else:]
    pass

在循环 break,return 或者 异常后执行else
"""

"""跳转语句
break 强行退出循环
continue 结束本次循环
"""

""" range()的使用
range(start,stop,step)
