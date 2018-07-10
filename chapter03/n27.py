# coding: utf-8

# Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
#     1行に1記事の情報がJSON形式で格納される
#     各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
#     ファイル全体はgzipで圧縮される
# 以下の処理を行うプログラムを作成せよ．

# 27. 内部リンクの除去
# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．

import re
import n20 as n20
import n25 as n25
import n26 as n26

article_text = n20.get_country_text('イギリス')
basic_information_lines = n25.get_basic_information(article_text).split('\n')

def remove_inner_link_markup(text):
	return re.sub(r'\[\[([^|\]]+?\|)*(.+?)\]\]', r'\2', text)

if __name__ == '__main__':
	# Prameter extraction
	param_regex = r'^\|(.*?) = (.*)'
	param_pattern = re.compile(param_regex)

	params = {}
	for info_line in basic_information_lines:
		info = param_pattern.match(info_line)
		if info is not None:
			value = n26.remove_emp_markup(info.group(2))
			params[info.group(1)] = remove_inner_link_markup(value)
			pass

	# Show answer
	for key in params.keys():
		print(key, params[key])

# ans
# 略名 イギリス
# 日本語国名 グレートブリテン及び北アイルランド連合王国
# 公式国名 {{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>
# 国旗画像 Flag of the United Kingdom.svg
# 国章画像 イギリスの国章
# 国章リンク （国章）
# 標語 {{lang|fr|Dieu et mon droit}}<br/>（フランス語:神と私の権利）
# 国歌 神よ女王陛下を守り給え
# 位置画像 Location_UK_EU_Europe_001.svg
# 公用語 英語（事実上）
# 首都 ロンドン
# 最大都市 ロンドン
# 元首等肩書 女王
# 元首等氏名 エリザベス2世
# 首相等肩書 首相
# 首相等氏名 デーヴィッド・キャメロン
# 面積順位 76
# 面積大きさ 1 E11
# 面積値 244,820
# 水面積率 1.3%
# 人口統計年 2011
# 人口順位 22
# 人口大きさ 1 E7
# 人口値 63,181,775<ref>[http://esa.un.org/unpd/wpp/Excel-Data/population.htm United Nations Department of Economic and Social Affairs>Population Division>Data>Population>Total Population]</ref>
# 人口密度値 246
# GDP統計年元 2012
# GDP値元 1兆5478億<ref name="imf-statistics-gdp">[http://www.imf.org/external/pubs/ft/weo/2012/02/weodata/weorept.aspx?pr.x=70&pr.y=13&sy=2010&ey=2012&scsm=1&ssd=1&sort=country&ds=.&br=1&c=112&s=NGDP%2CNGDPD%2CPPPGDP%2CPPPPC&grp=0&a= IMF>Data and Statistics>World Economic Outlook Databases>By Countrise>United Kingdom]</ref>
# GDP統計年MER 2012
# GDP順位MER 5
# GDP値MER 2兆4337億<ref name="imf-statistics-gdp" />
# GDP統計年 2012
# GDP順位 6
# GDP値 2兆3162億<ref name="imf-statistics-gdp" />
# GDP/人 36,727<ref name="imf-statistics-gdp" />
# 建国形態 建国
# 確立形態1 イングランド王国／スコットランド王国<br />（両国とも1707年連合法まで）
# 確立年月日1 927年／843年
# 確立形態2 グレートブリテン王国建国<br />（1707年連合法）
# 確立年月日2 1707年
# 確立形態3 グレートブリテン及びアイルランド連合王国建国<br />（1800年連合法）
# 確立年月日3 1801年
# 確立形態4 現在の国号「グレートブリテン及び北アイルランド連合王国」に変更
# 確立年月日4 1927年
# 通貨 UKポンド (&pound;)
# 通貨コード GBP
# 時間帯 ±0
# 夏時間 +1
# ISO 3166-1 GB / GBR
# ccTLD .uk / .gb<ref>使用は.ukに比べ圧倒的少数。</ref>
# 国際電話番号 44
# 注記 <references />
