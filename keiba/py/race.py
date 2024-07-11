#どこの競馬場が主宰する何レースでいくらお金が動くか計算するソフト
#膨大なデータベースから競争馬名がわかるシステム
#和名と英名の関係がわからない外国人でも操作可能にするため
#数字とRnterキーしか用いない　選択肢から数字で好きなのを選ぶ操作系
#それしかない（限定・平準化・簡単にリファクト）
#膨大な競走馬データを簡単に扱う処理をしたソフトです。
#レースに出る馬の名前を調べるソフトで数字とエンターキーだけで操作します。
#レイース開催日程の10分前までオッズなどはリアルタイムに変化します。
#Pythonベースのスクレイピングという技法を用いています。
#競馬は毎年開催される感じの行動日程です。時計優先で進行します。
#天皇賞は年に2回の周期で開催されます。（毎年できるお仕事です　再現性　お金）
#見ればわかるように設計してある　エンタープライズ（Windows）は右クリックすると
#できることのメニューが出るから好きなのを選択する仕組みになってる（基本設計）
#学生時代にこれを教えてもらえなかった人には難しいかもしれませんが
#規則があります。うちの会社のシステムは右クリックでできること全部出しておいてとか
#ミスしないように見ればわかるように工夫してと注文が入ったからそうなってます。
#GUI前提の画面遷移の仕組み　右クリックで選ぶと目的の画面が出るようにつながってます。
#目的の機能を呼び出すと記載します。Windowsはダブルクリックで全部できるような設計も流行しました。
#Windowsはキーボードだけでも操作ができるように工夫されてるとか
#マウスをカチカチするだけで処理が進む仕組みになってるとか
#マウスで選ぶと仕事が進む感じに計画してという依頼でそうなりました。
#1990年代のPC競馬ブームがあったのは事実です。
#これはテンキーだけで競馬情報を調べるソフトです。
#高額配当の馬券が買いたい人　馬主で賞金が出る人などいろいろ立場があります。
#趣味娯楽の世界で獲得賞金2億円のダービー馬が牧場でのんびりしている様子を眺めて楽しむなど
#厩舎で働くことを決めるのもいいでしょう。やろうと思えば毎年開催できるビジネスだからです。
#外れ馬券を買って大損しなさいというソフトではありません。
#まだ若くて育成中の3勝目の3歳馬を応援するとお金も結構動きます。
#馬って3歳ぐらいで1300万円ぐらい稼ぐんですよ。オープン戦勝利時の賞金は1000万円
#運による資金の増え方の変動を確率で計算して　期待値　回収率などと記載しています。
#馬向けの日程はレースに出るのは3ヶ月に1回ぐらいです。3歳馬ぐらいの子はあんまり難しい走り方できないですが
#重賞の国際戦は国家が仕掛ける戦略で大金が動きます。コンピュータで自動計算しています。
#農林水産省管轄分野で農林水産大臣賞賞金を出すのは国です。
#8頭立て牝馬未勝利レースとか言うのは必ず1等賞の賞金を受け取る子が出るレースです。
#当たる馬券を教えてくださいって感じで情報料がほしい企業も多々あります。
#どういう馬だか全く知らない状況ではなかなか馬券も当たりませんし面白いとも思えないかと思います。
#コンピュータで数字だけで調べきれることをお知らせしたくて開発しました。
#競馬クラブ所属の馬が重賞で勝利して、牧場にお金がいっぱい来たから記念の宴会とかもあるんです。
#3歳馬未勝利とか馬なりに頑張って逃げ切りなレースとかも多いですが統計できます。
#馬主が預けた厩舎で走り方を教えてもらった子が3着以内に入る確率も高いです。馬券に関与した馬と表記します。
#毎年開催される競馬のレースの賞金の計算する計算機を受注していましたが、競馬場が破産しない程度に
#賞金出せる経営上の都合があります。中央競馬と地方競馬と大きく資本が分かれており、農林水産大臣賞は
#国が一回お金を出してくれるため存続できます。天皇賞が年に2回予定されており、やってくることが戦略的で
#難しい走り方を見せてくるので面白いです。子馬は教育で着順に差が出ていきます。馬主が注いだ愛情の分だけ
#賞金が上がるところも見受けられます。この重賞狙って好条件重ねた子が勝つところもあります。
import datetime
import subprocess
t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
import re
command = 'clear'
ret = subprocess.run(command, shell=True)
#print(ret)
#日付
y = now.strftime('%Y')
d = now.strftime('%m%d')
print(d)
print("これは生涯競馬を楽しむ目的のあるシステムです。")
print("1/2 競馬場コード2桁を入れてください。")
print("金沢：46 笠松：47 園田：50 名古屋：48")
code= input("")

print("2/2 レース番号2桁を入れてください。")
RNO= input("")

#print("race_idを入力してください")
#race_id = input("")
race_id=y+code+d+RNO
print(race_id)
#race_id = "202254110511"
#race_id  = "20240625431"
url = f"https://nar.netkeiba.com/odds/index.html?type=b1&race_id={race_id}"
import requests
from bs4 import BeautifulSoup
print("////////////////////////////////////////////////////////////")

response = requests.get(url)
#soup = BeautifulSoup(response.content)
soup = BeautifulSoup(response.content,'html5lib')
title = soup.find('div', attrs={'class': 'RaceName'})
#print(title)
p = re.compile("<[^>]*?>")
tag_str = str(title)
s=p.sub("", tag_str)
print(s.replace('\n',''))
#result = re.sub(r'[ \t]*<.+?>', "", title)
#print(result)
#print(title.replace('<div',''))
#print(title.replace('\n', ''))
data = soup.find('div', attrs={'class': 'RaceData01'})

#p = re.compile(r"<[^>]*?>")
#tag_str = data
#p.sub("", tag_str)
#print(data)
p = re.compile("<[^>]*?>")
tag_str = str(data)
s=p.sub("", tag_str)
#print(s)
s=s.replace('?','')
print(s.replace('\n',''))

odds_tan_block = soup.find('div', attrs={'id': 'odds_tan_block'})
trs = odds_tan_block.find_all('tr')
arr=[]
arr1={}
arr2={}
#print(arr)
try:
    for n, tr in enumerate(trs):
        if n == 0:
            continue
        horse_name = tr.find("td", attrs={"class": "Horse_Name"}).text
        odds = float(tr.find("td", attrs={"class": "Odds"}).text)
        #    print( horse_name , odds)
        #print(n,"\t" , horse_name,"\t\t" ,odds)
        arr.append(horse_name)
        arr1[n]=horse_name
        arr2[n]=odds

except AttributeError:
     print("データを取得できませんでした。")

#print(arr1)
#print(arr2)
"""
student_name_list = ["山田　一郎", "鈴木　次郎", "佐藤　ゴンザレスモリモリマッスル花子"]
"""

name_len_max = 10 # プリントできる最大の文字列
i=1
f = open('query/'+race_id+'.txt', 'w')
f.write("NO" +","+"os"+","+"name"+"\n")

syouryaku_str = "..."
for student_name in arr:
    if len(student_name) > name_len_max:
        name_print = student_name[:name_len_max-len(syouryaku_str)] + syouryaku_str
    else:
        name_print = student_name
    print(i,"\t",arr2[i],"\t",name_print)
    f.write(str(i) +","+str(arr2[i])+","+name_print+"\n")
    i=i+1
f.close()
print("//////////////////////(C)JFLABO/////////////////////////////")

print('年度:',race_id[0:4],'\t競馬場：',race_id[4:6],'\t日付',race_id[6:10],'\tR:',race_id[10:12])
print("////////////////////////////////////////////////////////////")
command = 'python3 sort.py ~/query/'+race_id+".txt"
ret = subprocess.run(command, shell=True)
