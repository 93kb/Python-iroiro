#制御構文
#if文　単純分岐
i = 10
if i == 10:
    print("変数iは10です")
else:
    print("変数iは10ではありません")
print("...END...")

#if文　多岐分岐
#複数の条件に合致しても実行されるブロックは最初に合致した一つだけ
i = 100
if i > 50:
    print("変数iは50より大きいです。")
elif i > 30:
    print("変数iは30より大きいです。")
else:
    print("変数iは30以下です。")

#この場合はi > 30の結果が出る
i = 100
if i > 30:
    print("変数iは30より大きいです。")

elif i > 50:
    print("変数iは50より大きいです。")

else:
    print("変数iは30以下です。")

#switch文
#Pythonではif...elifで代替出来るからswitch文はないらしい

rank = "甲"

if rank == "甲":
    print("大変良いです")
elif rank == "乙":
    print("よいです")
elif rank == "丙":
    print("がんばりましょう")
else:
    print("？？？")

#辞書型
rank = "あ"
msg = {
    "甲":"大変良いです。",
    "乙":"良いです。",
    "丙":"頑張りましょう。",
}
#キーの有無を確認
if rank in msg:
    print(msg[rank])
else:
    print("？？？")

#if文入れ子
i = 1
j = 0

if i == 1:
    if j == 1:
        print("変数はi、jは1です。")
    else:
        print("変数iは1ですが、jは1ではありません。")
else:
    print("変数iは1ではありません。")

#問題

score = 75

if score >= 90:
    print("優")
elif 90 > score >= 70:
    print("良") 
elif 70 > score >= 50:
    print("可") 
else:
    print("不可")

#繰り返し処理
#while文

i = 1
while i < 6:
    print(i,"番目のループです")
    i += 1

#for文
#リストの内容を順に表示
data = ["うめ","さくら","もも"]
for value in data:
    print(value)

#文字列は1文字ずつ出力
data = "こんにちは、山田さん"
for value in data:
    print(value)

for i in range(1,6):
    print(i,"番目のループです。")

#リストから新たなリストを作成
data = [15, 43, 7, 59, 98]
data2 = [i * 2 for i in data]
print(data2)

data = [15, 43, 7, 59, 98]
data2 = [str(i) for i in data]
for i in data:
    data2.append(i * 2)
    print(data2)

#特定の値だけ取得(合計値)
data = [15, 43, 7, 59, 98]
data2 = sum([i for i in data if i < 50])
print(data2)

#問題
for i in range(1,10):
    for j in range(1,10):
        result = i * j
        print(result,end=' ')
    print()

#ループの中断
sum = 0
for i in range(1,101):
    sum += i
    if sum > 1000:
        break
print("合計が1000を超えるのは、1～", i,"を加算した時です")

#周回をスキップ
sum = 0
for i in range(1, 101):
    if i % 2 != 0:
        continue
    sum += i
print("合計値は", sum, "です。")

#ループでの終了処理
data = ["さくら","うめ","x","くちなし","ぼたん"]
for name in data:
    #要素が「x」の場合にループ終了
    if name == "x":
        break
    print(name)
else:
    print("正常終了しました。")

#入れ子ループ中断50超の値は表示しない
for i in range(1,10):
    for j in range(1,10):
        result = i * j
        if result > 50:
            break
        print(result, end=' ')
    print()

#積が1回でも50を超えたら出力を中断させる
for i in range(1,10):
    for j in range(1,10):
        result = i * j
        if result > 50:
            break
        print(result, end=' ')
    #内側のループを正常終了したら次の周回へ
    else:
        print()
        continue
    #内側のループをbreakしたら外側もbreak
    break

#問題
i = 0
sum = 0
while i <= 100:
    i += 1
    if i % 2 != 0:
        continue
    sum += i
print("合計値は", sum, "です。")

#例外処理
num = input("数字を入力してください：")
print("2倍すると…", float(num) * 2)

#try処理
#発生するかもしれないエラーを想定しておき、実行を継続できるように処理する
try:
    num = input("数字を入力してください：")
    print("2倍すると…", float(num) * 2)
except ValueError as ex:
    print("エラー発生：", ex)

while True:
    try:
        num = input("数字を入力してください：")
        print("2倍すると…", float(num) * 2)
    except ValueError:
        print("入力値エラーです。")
    else:
        break

#問題
#１
#for item in data:
#    print(item)

#２
#for i in range(1,101):
#    print(i)

#３
#data2 = [i * 10 for i in data]

#４
#result = sum([i for i in data if i >= 0])

#５
#if 10 <= num < 50:
#    print(num)

#100~200の範囲になる奇数値の合計
sum = 0
for i in range(100,201):
    if i % 2 == 0:
        continue
    sum+= i
print("合計値は", sum, "です。")
