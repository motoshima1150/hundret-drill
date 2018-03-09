# coding: utf-8

# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

fname = 'hightemp.txt'
with open(fname) as f:
	lines = f.readlines()
	while True:
		input_str = input('Please Enter Number(max: ' + str(len(lines)) + '): ')
		if input_str.isdigit():
			for line in lines[:int(input_str)]:
				print(line, end='')
			break

		print(input_str + ' is invalid data.')
# Please Enter Number(max: 24): 5
# 高知県	江川崎	41	2013-08-12
# 埼玉県	熊谷	40.9	2007-08-16
# 岐阜県	多治見	40.9	2007-08-16
# 山形県	山形	40.8	1933-07-25
# 山梨県	甲府	40.7	2013-08-10


# By UNIX commands
# $ head -n 5 hightemp.txt
# 高知県	江川崎	41	2013-08-12
# 埼玉県	熊谷	40.9	2007-08-16
# 岐阜県	多治見	40.9	2007-08-16
# 山形県	山形	40.8	1933-07-25
# 山梨県	甲府	40.7	2013-08-10
