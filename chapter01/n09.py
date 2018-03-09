# coding: utf-8

# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

words = s.split()

def typoglycemia(word):
	mid_chars = list(word)[1:-1]
	random.shuffle(mid_chars)
	return word[0] + "".join(mid_chars) + word[-1]

ans = " ".join(list(map(lambda word: typoglycemia(word) if len(word) > 4 else word, words)))

print(ans)
# I co'dnlut bielvee that I colud acaultly uednratsnd what I was rdienag : the pahemonenl pewor of the huamn mind .