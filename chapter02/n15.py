# coding: utf-8

# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

fname = 'hightemp.txt'
with open(fname) as f:
	lines = f.readlines()
	while True:
		input_str = input('Please Enter Number(max: ' + str(len(lines)) + '): ')
		if input_str.isdigit():
			for line in lines[-int(input_str):]:
				print(line, end='')
			break

		print(input_str + ' is invalid data.')
# Please Enter Number(max: 24): 5
# 埼玉県	鳩山	39.9	1997-07-05
# 大阪府	豊中	39.9	1994-08-08
# 山梨県	大月	39.9	1990-07-19
# 山形県	鶴岡	39.9	1978-08-03
# 愛知県	名古屋	39.9	1942-08-02


# By UNIX commands
# $ tail -n 5 hightemp.txt
# 埼玉県	鳩山	39.9	1997-07-05
# 大阪府	豊中	39.9	1994-08-08
# 山梨県	大月	39.9	1990-07-19
# 山形県	鶴岡	39.9	1978-08-03
# 愛知県	名古屋	39.9	1942-08-02
