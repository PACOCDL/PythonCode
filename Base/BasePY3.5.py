# -*- coding: UTF-8 -*-
import time

import re

print("Hello World!")
# 所有标识符可以包括英文、数字以及下划线（_），但不能以数字开头
_abc = 2.1
print(_abc)

"""
数据类型
Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）
"""
# 数据类型
a = b = c = 1
a, b, c = 1, 1.2, "string"
print()
# 字符串
str = 'Hello World!'
print(str)  # 输出完整字符串
print(str[0])  # 输出字符串中的第一个字符
print(str[2:5])  # 输出字符串中第三个至第五个之间的字符串
print(str[2:])  # 输出从第三个字符开始的字符串
print(str * 2)  # 输出字符串两次
print(str + " TEST")  # 输出连接的字符串
print(str[-1:5])
print()
# 列表
s = [a, b, 123, "list"]
print(s)
print(s[0:])
print(s[1:2])
print(s * 3)
print()
# 元祖 元组不能二次赋值，相当于只读列表
tuple = (a, b, "abc", 123)
print(tuple)
print(tuple[2:3])
print()
# 元字典

dict = {'a':1,'c':2,a:3}

print('dict',dict)

print(           )
# 运算符
num=2
print(num//1.1)
print(num**2)
print(            )
# 身份运算符 in/not in
list=[1,2,3,4,5]
if(a not in list):
    print(True)
else:
    print(False)
print(            )
# 条件判断

a=2
b=3
c=4
if a>b:
    print(a)
elif a<b:
    print(b)
else:
    print("a=b")

print(            )
# while
a=1
while a<3:
    print("a=",a)
    a=a+1

print(            )

# for in 循环
name=['ali','baidu','google']
for n in name:
    print(n)

print(            )
# 输入语句，输入的类型为String
#a=input('请输入：')
#print(a)

# 函数
print(            )
def def_pow(a,b):
    return a*b
a=def_pow(2,4)
print('a=',a)

print(abs(-10))
print(            )
# 递归函数
def digui(a):
    if a<5:
        a=a+1
        print(a)
        digui(a)
    else:
        print('ok')
a=3
digui(a)
# TODU
print('时间')

# 时间
a=time.time();
print('time=',a)
print('高级函数')

# 高级函数

a=abs(-10)
print('-10的绝对数是',a)
a=abs(10)
print('a的绝对数是',a)
def add(x,y,f):
   return f(x)+f(b)
a=2
b=3
f=abs
print("add is",add(a,b,f))
print(            )
def powe(x):
    return x*x
a=map(pow,[1,2,3,4])



print(            )
# 正则表达式
test='somew2on@egmail.com'
if re.match(r'\w*\@\w{1,10}\.\?{1}\w*',test):
    print('ok')
else:
    print('no')
print(    '模块'        )

print(            )



print(            )
