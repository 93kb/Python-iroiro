
#標準ライブラリ
import datetime

today = datetime.date(2020, 11, 10)
#2020/11/10を表すdatetime.date型のインスタンスを生成したことになる

data = [25 , 3 , 49, 67 , 14]
data.sort(reverse=True)
print(data)

today = datetime.date(2020, 11, 10)
print(today.year)

#todayメソッドで今日の日付を求める
current = datetime.date.today()
print(current)

#数学演算のmathモジュール、floor関数は小数点部分を切り捨てる関数
import math
print(math.floor(1.34))

#文字列の長さを取得
#日本語を1文字として数えたいならlen関数を使う
title = "WINGSプロジェクト"
print(len(title))

#半角を1文字、全角を2文字として数えたいならunicodedata
#戻り値の指定　F：全角英数　W：漢字や全角かな　A：特殊文字
import unicodedata

data = "WINGSプロジェクト２０２０"
count = 0
for ch in data:
    if unicodedata.east_asian_width(ch) in "FWA":
        count += 2
    else:
        count += 1
print(count)


#文字列を大文字⇔小文字で変換する
data1 = "Wings Project"
data2 = "self learn python"
data3 = "Fuβball"

print(data1.lower())
print(data1.upper())
print(data1.swapcase())
print(data2.capitalize())
print(data2.title())
print(data3.lower())
print(data3.casefold())

#部分文字列を取得する
title = "あいうえおかきくけこ"
print(title[2])
print(title[2:5])
print(title[2:])
print(title[:5])
print(title[:])
print(title[-7:])
print(title[-7:-5])
print(title[::2])
print(title[1::2])
print(title[::-1])

#文字の種類を判定
print("abc123".isalnum())
print("abc++".isalnum())
print("abcde".isalpha())
print("abc123".isalpha())
print("abc".isascii())
print("あいう".isascii())
print("100".isdecimal())
print("0x64".isdecimal())
print("1234".isdigit())
print("1234.56".isdigit())
print("百万".isnumeric())
print("million".isnumeric())
print("abc_123".isidentifier())
print("abc-123".isidentifier())
print("wings".islower())
print("Wings".islower())
print("WINGS".isupper())
print("Wings".isupper())
print("Wings Project".istitle())
print("WINGS Project".istitle())
print("Hello World".isprintable())
print("Hello\nWorld".isprintable())
print("   ".isspace())
print("***".isspace())
#isdecimalはアラビア数字だけ認める
#isdigitはさらに上付き数字のような文字も認める(2乗とかのやつ)
#isnumericはさらに漢数字・ローマ字を含める

#文字列を数値に変換
#数値文字を数値(int/float)に変換ならunicodedataモジュールのdigit/numeric関数を使用
import unicodedata
print(unicodedata.digit("5"))
print(unicodedata.numeric("参"))
print(unicodedata.numeric("Ⅷ"))

#予約済みの識別子を確認
#isidentifierメソッド
#与えられた文字列が識別子として認められている文字のみで構成されるかを判定
#keywordモジュールのiskeyword関数を使用
import keyword
id1 = "tiff"
id2 = "if"
print(id1.isidentifier())
print(id2.isidentifier())
print(keyword.iskeyword(id1))
print(keyword.iskeyword(id2))

#文字列を検索
#文字列を戦闘から純に検索して、見つかった場合委には文字位置を返す
#見つからなかった場合は-1を返す
msg = "にわにはにわにわとりがいる"
#にわにはにわにわとりがいる
#０１２３４５６７８９101112
print(msg.find("にわ"))
print(msg.find("にも"))
print(msg.rfind("にわ"))
#最後に「にわ」が合まれるのが6文字目のため返ってくるのが「6」になる
print(msg.find("にわ", 3))
print(msg.find("にわ", 3, 5))
print(msg.find("にわ", -7, -1))

#部分文字列の登場回数をカウント
#countメソッドを使用する
msg = "にわにはにわにわとりがいる"
print(msg.count("にわ"))
print(msg.count("にわ", 3))
print(msg.count("にわ", 3, 6))

msg = "いちいちいちばにいち"
print(msg.count("いちいち"))
#countメソッドは重複のない出現数をカウントする。
#0~3文字目で1つカウント、次は4文字目から検索される

#文字列の前後から空白を削除する
msg = " 　こんにちは \t\n\r"
print('「' + msg.strip() + '」')
print('「' + msg.lstrip() + '」')
print('「' + msg.rstrip() + '」')

msg2 = "!=====[独習Python]=====!"
print('「' + msg2.strip("!= []") + '」')

msg = "WINGSプロジェクト"

print("プロ" in msg)
print("プロ" not in msg)
print(msg.startswith("WINGS"))
print(msg.endswith("WINGS"))
print(not msg.startswith("WINGS"))
print(msg.startswith("WINGS", 1))
print("プロ" in msg[6:])
print("wings" in msg)
print("wings" in msg.casefold)