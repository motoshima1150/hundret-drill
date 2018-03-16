# coding: utf-8

# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

fname = 'hightemp.txt'
with open(fname) as f:
	lines = f.readlines()

	frequency = dict(map(lambda line: [line.split()[0], 0], lines))

	for keyword in map(lambda line: line.split()[0], lines):
			frequency[keyword] += 1

	result = list(frequency.items())
	result.sort(key=lambda item: item[1], reverse=True)
	print(result)

# [('埼玉県', 3), ('山形県', 3), ('山梨県', 3), ('群馬県', 3), ('岐阜県', 2), ('静岡県', 2), ('愛知県', 2), ('千葉県', 2), ('高知県', 1), ('和歌山県', 1), ('愛媛県', 1), ('大阪府', 1)]

# By UNIX commands
# $ cut --fields=1 hightemp.txt | sort | uniq --count | sort --reverse
# 群馬県
# 山梨県
# 山形県
# 埼玉県
# 静岡県
# 愛知県
# 岐阜県
# 千葉県
# 和歌山県
# 高知県
# 愛媛県
# 大阪府


