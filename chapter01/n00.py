# coding: utf-8

# 00. 文字列の逆順
# 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

s = "stressed"

# Ans 1
ans = "".join(reversed(s))
print(ans)

# Ans 2
print(s[::-1])
#desserts
