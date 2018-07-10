# coding: utf-8

# Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
#     1行に1記事の情報がJSON形式で格納される
#     各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
#     ファイル全体はgzipで圧縮される
# 以下の処理を行うプログラムを作成せよ．

# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

import re
import n20 as n

article_text = n.get_country_text('イギリス')
print(article_text)
section_regex = r'^(=+)(.*?)(=+)$'
pattern = re.compile(section_regex)
	
lines = article_text.split('\n')

titles = []
for line in lines:
	result = pattern.search(line)
	if result is not None:
		titles.append((result.group(2).strip(), (len(result.group(1)) - 1)))

for title in titles:
	print(title)

# ans
# ('国名', 1)
# ('歴史', 1)
# ('地理', 1)
# ('気候', 2)
# ('政治', 1)
# ('外交と軍事', 1)
# ('地方行政区分', 1)
# ('主要都市', 2)
# ('科学技術', 1)
# ('経済', 1)
# ('鉱業', 2)
# ('農業', 2)
# ('貿易', 2)
# ('通貨', 2)
# ('企業', 2)
# ('交通', 1)
# ('道路', 2)
# ('鉄道', 2)
# ('海運', 2)
# ('航空', 2)
# ('通信', 1)
# ('国民', 1)
# ('言語', 2)
# ('宗教', 2)
# ('婚姻', 2)
# ('教育', 2)
# ('文化', 1)
# ('食文化', 2)
# ('文学', 2)
# ('哲学', 2)
# ('音楽', 2)
# ('イギリスのポピュラー音楽', 3)
# ('映画', 2)
# ('コメディ', 2)
# ('国花', 2)
# ('世界遺産', 2)
# ('祝祭日', 2)
# ('スポーツ', 1)
# ('サッカー', 2)
# ('競馬', 2)
# ('モータースポーツ', 2)
# ('脚注', 1)
# ('関連項目', 1)
# ('外部リンク', 1)
