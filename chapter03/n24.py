# coding: utf-8

# Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
#     1行に1記事の情報がJSON形式で格納される
#     各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
#     ファイル全体はgzipで圧縮される
# 以下の処理を行うプログラムを作成せよ．

# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．

import re
import n20 as n

article_text = n.get_country_text('イギリス')

print(article_text)
category_regex = r'\[\[(File|ファイル):(.*?)(\|.*)?\]\]'
pattern = re.compile(category_regex)
	
lines = article_text.split('\n')
file_names = []
for line in lines:
	result = pattern.search(line)
	if result is not None:
		file_names.append(result.group(2).strip())

for file_name in file_names:
	print(file_name)

# ans
# Royal Coat of Arms of the United Kingdom.svg
# Battle of Waterloo 1815.PNG
# The British Empire.png
# Uk topo en.jpg
# BenNevis2005.jpg
# Elizabeth II greets NASA GSFC employees, May 8, 2007 edit.jpg
# Palace of Westminster, London - Feb 2007.jpg
# David Cameron and Barack Obama at the G20 Summit in Toronto.jpg
# Soldiers Trooping the Colour, 16th June 2007.jpg
# Scotland Parliament Holyrood.jpg
# London.bankofengland.arp.jpg
# City of London skyline from London City Hall - Oct 2008.jpg
# Oil platform in the North SeaPros.jpg
# Eurostar at St Pancras Jan 2008.jpg
# Heathrow T5.jpg
# Anglospeak.svg
# CHANDOS3.jpg
# The Fabs.JPG
# Wembley Stadium, illuminated.jpg
