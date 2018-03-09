# coding: utf-8

# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

fname = 'hightemp.txt'
col1f = open('col1.txt', 'w')
col2f = open('col2.txt', 'w')

with open(fname) as f:
	lines = f.readlines()
	col1 = list(map(lambda line: line.split()[0] + '\n', lines))
	col2 = list(map(lambda line: line.split()[1] + '\n', lines))
	col1f.writelines(col1)
	col2f.writelines(col2)

col1f.close()
col2f.close()


# $ cut -f1 hightemp.txt
# 高知県
# 埼玉県
# 岐阜県
# 山形県
# 山梨県
# 和歌山県
# 静岡県
# 山梨県
# 埼玉県
# 群馬県
# 群馬県
# 愛知県
# 千葉県
# 静岡県
# 愛媛県
# 山形県
# 岐阜県
# 群馬県
# 千葉県
# 埼玉県
# 大阪府
# 山梨県
# 山形県
# 愛知県
# $ cut -f2 hightemp.txt
# 江川崎
# 熊谷
# 多治見
# 山形
# 甲府
# かつらぎ
# 天竜
# 勝沼
# 越谷
# 館林
# 上里見
# 愛西
# 牛久
# 佐久間
# 宇和島
# 酒田
# 美濃
# 前橋
# 茂原
# 鳩山
# 豊中
# 大月
# 鶴岡
# 名古屋
