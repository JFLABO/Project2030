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
#賞金が上がるところも見受けられます。この重賞狙って好条件重ねて育てた子が勝つところもあります。
#うちで育てた子が重賞で1位になったのとか言うドラマもあるんです。どの子も1勝ぐらいはできるように配慮していたりもするのです。
#この子は馬主がお金をかけてなくて、騎手がもっと早くとやっても応じないのとか言うのもわかります。
#兵庫で育成中の勝てる子とかにお金かけてる（教えるのが上手な調教師にお金を払って調教中とか）
#あがり3ハロンの走り方を最近教えた子が勝ったとか　馬主が同じ騎手を指名して育てている真っ最中な馬とか情報があるんです。
#オッズの計算式も売り上げに応じて競馬場が破産しないギリギリまで賞金に割り当てているとか差が出ます。
#レース映像の中継とか見るとイギリス製とかドイツ製とかいろいろ入れ替わっています。主宰する何レースかで違うんです。
#競馬はブラッドレースで競走馬の子に生まれないとレースに出れないとかいろいろ条件もあるんです。
#私はこの世に生まれて2年目です。ってこは教育次第で重賞1着で1400万円ぐらい稼ぐんです。
#馬に乗る職業に就職すると1200万円ぐらいは業界からもらえます。馬主同士の駆け引きもあります。
#名馬の子馬が生まれると、牧場に800万円ぐらいお金が入りますので、いろいろ計算するんです。
#天皇陛下も馬術部だったりして、農林水産大臣賞（地方競馬）の賞金増やそうとか言う話もあります。
#うちの牧場で競走馬の子馬が一頭誕生しましたとまだ名前がありませんと言う時点で情報が出始めます。その子をお金で売ってくださいという感じで
#馬主様が確定します。最近は日本の馬主も株式会社化しているようですね。競馬専用の株式会社というのがあります。
#リスク情報　病気　怪我　故障　アクシデントの算定もやらなくてはいけません。馬の日程は3ヶ月に1回ぐらいです。
#私たちは競馬新聞の読み方がまだわかりませんとか言う段階からでも学べます。競馬は教養で稼げるようになるものです。
#人気度通りに行かない方が配当額がおっきい点も知っておきましょう。
#なんか事情があっても時計優先でレースが開催されるところも知っておきましょう。
#さえない牧場が名馬の手配でリッチで豪華に変貌する様子もありました。うま娘が製造されたことでいろいろ変化がありました。
#競馬で個人的に10万円ぐらい負けている状況では面白くはないでしょう。馬券買っていないと面白くない人も出るでしょう。
#勤務地が牧場で重賞で勝てる名馬を生産すると獲得賞金が通常5億円ぐらい行きます。過去そういう数字が秒速で動いている業界です。
#レースに出れる競走馬は管理下にあります。全部数字で特定できます。株式会社として名馬の生産手がけている企業と記載できる企業があります。
#勝てる子は　勝ち馬と記します。優駿と記載することがあります。農林水産大臣賞が設定されています。スポンサーは国です。
#いまはここの厩舎が勝てる子育成できるとかいう情報もあります。レース名工夫します。とかいろいろ変化がありました。2024
#仕事で競馬をやっていると持ち時間は5分ぐらいしかないという感じで忙しいです。所属が新聞社で予想売ってるとかで差が出ます。
#こういうシステム開発するのも時間は時計屋が測定しているとか、計算が多いとか事情があります。
#名馬の育成に成功すると牧場に入るお金は通常5億円になるお仕事です。馬に関わるお仕事で若手の育成も熱心です。
#競馬新聞専門家は予想が外れたときのクレームがすごいとか言う悩みもあったりします。
#主力事業が名馬の生産という感じの牧場は名馬の生産に成功すると5億円ぐらいもらえてきています。
#映像と音声を用いた放送はみんなの印象に残るという特性もあるのです。調教がいまいちで打つ手なしだとなかなか勝てません。情報が左右します。
#人気がすごくてお金も豪快に循環していますというのも情報です。外資系ハイブランドで中古で高値がつくところとかは中世頃馬具の製造で有名だった企業です。
#競馬の5世代血統データはよく知る日本国だけで閉じているのではなく地球共通言語として設計されているので教えておきますね。和名に対して英名が必ずあります。
#競馬は勉強するとそこそこお金が入ります。何この馬初めて見たと言う情報料では稼げません。お給料が安定してもらえる厩舎勤務や警備の受注とかをやるでしょう。
#牧場とかも設営するために5億円ぐらいかかっていましたがその数字を払った人が事業主です。専門誌の編集と売買で通信料または情報料が毎週入る企業も存在します。
#結構当たる競馬新聞などのことです。かなりの的中率の高度な競馬新聞の情報料が550円とか言うビジネスです。
#学校とかの競馬クラブとか行くとうちはこの子の馬主ですって企業の子も混ざっているのが実情です。この子はうちの厩舎の管理場ですよって人もいます。
#文章書いてて忙しい人とか　券を買うだけの人とかもいますが、この子が勝つと賞金が会社に入るのという位置取りが面白いでしょう。
#まだ若い馬を集めたレースで真ん中辺で動かない子はこのレースで1等賞とりたいと思えない感じの子だったりします。
#名馬を預かる環境がいい牧場向けのシステムをやっています。きれいな馬は環境がいいところでのびのび育つ、戦略も差が出る。
#馬って必死に走ってて大変そう　と言うシーンばかり出でなく　寝てたり　のんびりしている様子もあります。
#セリの数字も紹介しておきます。
#1位	デルフィニアIIの2023	牡	6億4900万円　馬一頭の生産でこのくらいの大金が動きます。
#予想についてはあんまり駆け引きがない馬なりに走るレースは人気通りでローマやアラブ、フランスが戦略的に仕掛けてるくると変動します。
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
