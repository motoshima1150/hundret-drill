# coding: utf-8

# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

fname = 'hightemp.txt'
with open(fname) as f:
	lines = f.readlines()
	col1 = list(map(lambda line: line.split()[0] + '\n', lines))
	print(set(col1))

# {'静岡県\n', '埼玉県\n', '群馬県\n', '愛知県\n', '高知県\n', '愛媛県\n', '山梨県\n', '岐阜県\n', '和歌山県\n', '千葉県\n', '山形県\n', '大阪府\n'}

	
# By UNIX commands
# cut -f 1 hightemp.txt | sort | uniq
# 千葉県
# 埼玉県
# 大阪府
# 山形県
# 山梨県
# 岐阜県
# 愛媛県
# 愛知県
# 群馬県
# 静岡県
# 高知県
# 和歌山県
