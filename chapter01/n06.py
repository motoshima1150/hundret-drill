# coding: utf-8

# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

from n005 import ngram

s1 = "paraparaparadise"
s2 = "paragraph"
check_str = 'se'

x = set(ngram(s1, 2))
y = set(ngram(s2, 2))

# 和集合
print(x | y)
{'se', 'ad', 'ar', 'di', 'gr', 'ap', 'ag', 'pa', 'is', 'ph', 'ra'}

# 積集合
print(x & y)
{'pa', 'ap', 'ar', 'ra'}

# 差集合
print(x - y)
{'se', 'ad', 'is', 'di'}

# 'se'というbi-gramがXに含まれるかどうか
print(check_str in x)
True

# 'se'というbi-gramがYに含まれるかどうか
print(check_str in y)
False
