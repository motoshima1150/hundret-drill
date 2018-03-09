# coding: utf-8

# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

fname = 'hightemp.txt'
with open(fname) as f:
	print(len(f.readlines()))


# By UNIX commands
# $ wc -l hightemp.txt 
#       24 hightemp.txt
