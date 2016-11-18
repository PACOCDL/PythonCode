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
