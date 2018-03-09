# coding: utf-8

# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

col1fname = 'col1.txt'
col2fname = 'col2.txt'
mergefname = 'merge.txt'
with open(col1fname) as col1f, open(col2fname) as col2f:
	merge = list(map(lambda col1, col2: col1.strip() + '\t' + col2.strip() + '\n', col1f, col2f))

	with open(mergefname, 'w') as wf:
		wf.writelines(merge)


# By UNIX commands
# $ paste col1.txt col2.txt 
# 高知県	江川崎
# 埼玉県	熊谷
# 岐阜県	多治見
# 山形県	山形
# 山梨県	甲府
# 和歌山県	かつらぎ
# 静岡県	天竜
# 山梨県	勝沼
# 埼玉県	越谷
# 群馬県	館林
# 群馬県	上里見
# 愛知県	愛西
# 千葉県	牛久
# 静岡県	佐久間
# 愛媛県	宇和島
# 山形県	酒田
# 岐阜県	美濃
# 群馬県	前橋
# 千葉県	茂原
# 埼玉県	鳩山
# 大阪府	豊中
# 山梨県	大月
# 山形県	鶴岡
# 愛知県	名古屋