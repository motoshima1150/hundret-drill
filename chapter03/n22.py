# coding: utf-8

# Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
#     1行に1記事の情報がJSON形式で格納される
#     各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
#     ファイル全体はgzipで圧縮される
# 以下の処理を行うプログラムを作成せよ．

# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import re
import n20 as n

article_text = n.get_country_text('イギリス')

category_regex = r'\[\[Category:(.*?)(\|.*)?\]\]'
pattern = re.compile(category_regex)
	
lines = article_text.split('\n')

category_titles = []
for line in lines:
	category_result = pattern.findall(line)
	if category_result is not None:
		category_titles.append(category_result.group(1))


for category in category_titles:
	print(category)

# ans
# イギリス
# 英連邦王国
# G8加盟国
# 欧州連合加盟国
# 海洋国家
# 君主国
# 島国
# 1801年に設立された州・地域