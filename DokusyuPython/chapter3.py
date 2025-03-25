#四則演算
import decimal

#文字列(数)の連結
print("10"+"3")

#普通の文字列の連結
print("こんにちは、"+"〇さん")

#文字列をn回繰り返す
print("こんにちは" * 3)

#これはエラー
#print(15 + "30")

#int/strで型を変換して演算させる
print(15 + int("30"))
print(str(15)+"30")

#浮動小数点が入る場合
print(5 / 3)

#整数部の結果だけ知りたいときは//
print(5 // 3)

#余りが知りたいときはdivmodを使う
print(divmod(8,3))

#これだと0.6にはならない　※2進数で演算しているので誤差が出る
print(0.2 * 3)

#decimal型に変換させて10進数に直させる
d1 = decimal.Decimal("0.2")
d2 = decimal.Decimal("3")
d3 = decimal.Decimal("0.6")

print(d1 * d2)#0.6
print(d1 * d2 == d3)#True

#問題
#１　'4' + '5'　⇒　45
#２　2 ** 4　⇒　16
#３　10 // 6　⇒　1
#４　2.0 / 0　⇒　エラー
#５　10 % 4　⇒　2

#リストを分解して個々の変数に分解する
data = [1,2,3,4,5]
a,b,c,d,e = data
print(a)
print(b)
print(c)
print(d)
print(e)

#一部の要素がいらない場合は、_を利用する
#_に複数回値を代入しているので、最終的な値は4になる
data = [1,2,3,4,5]
a, _, b, _, c = data
print(a)
print(b)
print(c)
print(_)

#入れ子のリストでも出来る
data = [1,2,[31,32,33]]
a, b, c = data
print(a)
print(b)
print(c)

#入れ子のリストも1つずつ展開したいなら()で括って指定する
x, y, (z1, z2, z3) = data
print(x)
print(y)
print(z1)
print(z2)
print(z3)

#変数の値を入れ替える
x = 15
y = 38
x, y = y, x
print(x, y)

#リストの比較
#先頭から要素を比較、最初に異なる要素が見つかった場合にその大小でリスト全体の大小を決定
data1 = [1, 2, 3]
data2 = [1, 5]
data3 = [1, 2]
print(data1 < data2)#data1が2、data2が5で比較される、5のほうが大きいのでTrue
print(data1 < data3)#data3が2要素しかないのでdata3が小さいとみなされる、False

#問題
#１　i -= 2
#２　d = decimal.Decimal('0.5')
#３　x, y, *z = [2, 4, 6, 8, 10]
#４　n, m = m, n
#５　10 <= x < 50