# coding: utf-8

# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#     英小文字ならば(219 - 文字コード)の文字に置換
#     その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ


plaintext = "Hello cipher"

def cipher(s):
	return "".join(map(lambda c: chr(219 - ord(c)) if c.islower() else c, s))

result = cipher(plaintext)
print(result)
# Hvool xrksvi

print(cipher(result))
# Hello cipher

print(plaintext == cipher(result))
# True

