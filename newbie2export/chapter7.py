# LOOK 运算符
"""
算术运算符
    一元运算符： 只有一个，- ，取反运算符  a = 12 ,-a 
    二元运算符：
        加 +   减 -    乘 *   除/   取余 %     冥 **    
        地板除法 // ： 求小于 a 除以 b 商的最大整数
"""
print(3 // 2)
print(-3 // 2)

# 关系运算符

# 逻辑运算符：and not or 

"""位运算符
~       位反
&       位与
|       位或
^       位异或
>>      右移
<<      左移
"""
a = 0b10110010
b = 0b01011110
print('{0:b}'.format(a | b))  # 11111110
print('{0:b}'.format(a & b))  # 00010010
print('{0:b}'.format(a ^ b))  # 11101100
print('{0:b}'.format( ~a ))   # -10110011
print('{0:b}'.format(a >> 2)) # 00101100

"""其他运算符
同一性测试运算符： is   not is
成员测试运算符：  in    not in
