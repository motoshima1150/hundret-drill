# coding: utf-8

# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

s = "I am an NLPer"

def ngram(input, n) :
	last = len(input) - n + 1
	ret = []
	for i in range(last):
		ret.append(input[i:i+n])
	return ret

# 文字bi-gram
print(ngram(s, 2))
# ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']

# 単語bi-gram
print(ngram(s.split(), 2))
# [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
