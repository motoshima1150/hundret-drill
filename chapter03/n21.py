# coding: utf-8

# Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
#     1行に1記事の情報がJSON形式で格納される
#     各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
#     ファイル全体はgzipで圧縮される
# 以下の処理を行うプログラムを作成せよ．

# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import re
import n20 as n

article_text = n.get_country_text('イギリス')

print(article_text)
category_regex = r'\[\[Category:.*\]\]'
pattern = re.compile(category_regex)
	
lines = article_text.split('\n')
categorys = [line for line in lines if pattern.match(line) is not None]

for category in categorys:
	print(category)

# ans
# [[Category:イギリス|*]]
# [[Category:英連邦王国|*]]
# [[Category:G8加盟国]]
# [[Category:欧州連合加盟国]]
# [[Category:海洋国家]]
# [[Category:君主国]]
# [[Category:島国|くれいとふりてん]]
# [[Category:1801年に設立された州・地域]]
