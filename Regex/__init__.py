import re

# 正则拼配match用法
m = re.match('foo', 'food').group()
print('m的match匹配结果为', m)

# search的用法
n = re.search('foo', 'goodfoofoodd').group()
print('n的search结果是', n)

# 匹配多个字符
bt = 'bat|bet|bit'
b = re.match(bt, 'bat').group()
print('b的多字符bat的match结果是', b)
b = re.match(bt, 'bit').group()
print('b的多字符bit的match结果是', b)
b = re.search(bt, 'bbtbet').group()
print('b的多字符bet的search结果是', b)

# 匹配任何单字符
'''
单字符无法匹配\n
'''

anyend = '.end'

end = re.match(anyend, 'bend').group()
print('anyend的bend的match结果是', end)

end = re.match(anyend, 'end')
if end is not None:
    print('end的match的结果是', end.group())
else:
    print('end匹配失败')

end = re.match(anyend, '\nend')
if end is not None:
    print('end的match的结果是', end.group())
else:
    print('end匹配失败')

end = re.search(anyend, 'the game is end')
if end is not None:
    print('end的search的结果是', end.group())
else:
    print('end匹配失败')

# 创建字符集 []

'''
比较[]与|的差异
[cr][23][dp][o2]和r2d2|c3po
'''

str1 = re.match('[cr][23][dp][o2]', 'c2do').group()
print('str的match c2do结果为', str1)
str2 = re.match('r2d2|c3po', 'c2do')
if str2 is not None:
    print('str2的match结果为', str2)
else:
    print('匹配失败')

