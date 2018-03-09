# coding: utf-8

# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

fname = 'hightemp.txt'
with open(fname) as f:
	lines = f.readlines()
	while True:
		input_str = input('Please Enter Number(max: ' + str(len(lines)) + '): ')
		if input_str.isdigit():
			num = int(input_str)
			number_of_lines = int(len(lines) / num)
			remainder = int(len(lines) % num)

			start_index = 0
			for count in range(num):
				row_count = number_of_lines if remainder <= count else number_of_lines+1
				with open('split' + str(count + 1) + '.txt', 'w') as wf:
					wf.writelines(lines[start_index:start_index+row_count])
					print(lines[start_index:start_index+row_count])
				start_index += row_count
			break

		print(input_str + ' is invalid data.')
# Please Enter Number(max: 24): 7
# ['高知県\t江川崎\t41\t2013-08-12\n', '埼玉県\t熊谷\t40.9\t2007-08-16\n', '岐阜県\t多治見\t40.9\t2007-08-16\n', '山形県\t山形\t40.8\t1933-07-25\n']
# ['山梨県\t甲府\t40.7\t2013-08-10\n', '和歌山県\tかつらぎ\t40.6\t1994-08-08\n', '静岡県\t天竜\t40.6\t1994-08-04\n', '山梨県\t勝沼\t40.5\t2013-08-10\n']
# ['埼玉県\t越谷\t40.4\t2007-08-16\n', '群馬県\t館林\t40.3\t2007-08-16\n', '群馬県\t上里見\t40.3\t1998-07-04\n', '愛知県\t愛西\t40.3\t1994-08-05\n']
# ['千葉県\t牛久\t40.2\t2004-07-20\n', '静岡県\t佐久間\t40.2\t2001-07-24\n', '愛媛県\t宇和島\t40.2\t1927-07-22\n']
# ['山形県\t酒田\t40.1\t1978-08-03\n', '岐阜県\t美濃\t40\t2007-08-16\n', '群馬県\t前橋\t40\t2001-07-24\n']
# ['千葉県\t茂原\t39.9\t2013-08-11\n', '埼玉県\t鳩山\t39.9\t1997-07-05\n', '大阪府\t豊中\t39.9\t1994-08-08\n']
# ['山梨県\t大月\t39.9\t1990-07-19\n', '山形県\t鶴岡\t39.9\t1978-08-03\n', '愛知県\t名古屋\t39.9\t1942-08-02\n']

# By UNIX commands
# $ split -l 7 hightemp.txt 
