# coding: utf-8

# 07. テンプレートによる文生成
# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．

x_val = 12
y_val = "気温"
z_val = 22.4

def template(x, y, z):
	return str(x) + "時の" + y + "は" + str(z)

print(template(x_val, y_val, z_val))
# 12時の気温は22.4