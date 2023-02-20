## Octo記法によるゲーム開発記

### はじめに

ファミコン向けに[雪合戦ゲーム](https://twitter.com/in_mot_komani/status/1368227394385977347)を作っている人がいたので，僕もchip8向けに新作ゲームを作ってみることにしました．

### 2021-03-07

100周遅れぐらいかもしれませんが，私もchip8で新作ゲーム作りをはじめています．
octoというchip8開発環境を発見したので，最近遊んでいます．まず，pongを移植(記法変換)しているところです．
cf. https://johnearnest.github.io/Octo/

### 2021-03-08

pongの移植(記法変換)ができました．アセンブリ言語をocto記法に変更しただけです．リファクタリングすると見通しがよくなると想像するのですが，疲れたので，ここまでにします．octo記法にも習熟してきたので，オリジナルゲームを検討することにします．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/pong02.png)

このurlでつながるみたいです．
cf. https://johnearnest.github.io/Octo/index.html?key=jI2EPcN9

### 2021-03-12

Octoアセンブリ言語のサンプルゲームDeep8のキャラクタとタイトルを変更した新作ゲームが完成しました．アマビエがお札を投げて疫病を退散させるゲームです．疫病の日本上陸を阻止してください．A/S/Dキーか，←/↓/→キーで操作できます．#chip8 #octo #アマビエ 
cf. https://johnearnest.github.io/Octo/index.html?key=yGBhxexA

### 2021-03-13

キャラクタ変更だけでゲームを作るのは結構簡単でした．ゲームロジックとキャラクタを組み合わせることで，新作ゲームは完成しました．

### 2021-03-14

なんか外国の方にcodeというリストに加えていただきました．おそらくcodeを書く人というリストなんでしょうけど．しかし，最近書いてるのは，謎のoctoアセンブリ言語ですし，アマビエゲーム作ってるだけですし．

### 2021-03-15

A new game has been completed by changing characters  of a sample game of the Octo language. It is a game in which Amabie throws Ofuda to disperse the plagues. Stop them from landing in Japan. It can be operated with the A / S / D keys. #chip8 #octo 
cf. https://johnearnest.github.io/Octo/index.html?key=rW3O5zrM

Please refer to the following URLs for Amabie(*1) and Ofuda(*2). Now in Japan, Amabie has been a character to overcome the COVID-19. I hope it will subside and the Tokyo Olympics will be held.
- (*1) https://en.wikipedia.org/wiki/Amabie
- (*2) https://en.wikipedia.org/wiki/Ofuda

### 2021-03-16

ドット絵を描いたのいつぶりでしょうか．アマビエのお墓は結構うまく描けたでしょうか．1984年頃に，SHARP PC-1245でマンホールライクなゲームを作った時以来です．

### 2021-03-17

The pong was ported (notation conversion). I just changed the assembly language to octo notation. Refactoring will improve the readability, but I'm tired, so that's it. I'm also familiar with octo notation, so I will consider an original game. #chip8 
cf. https://johnearnest.github.io/Octo/index.html?key=973uE4zV

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/pong03.png)

### 2021-03-20

タイトルは80年代ナムコ風に，波キャラは伝統的な青海波模様風に，煙幕キャラはアニメーション風に，それぞれ修正しました．「はじめてでも上手に描ける 入門！ドット絵道場」（2021年・ナツメ社刊）という本を参考にしました．#アマビエ #amabie #chip8 #octo cf. https://johnearnest.github.io/Octo/index.html?key=cXOhX6AA

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/amabie11.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/amabie15.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/amabie14.png)

### 2021-03-21

新しいものを作ると学ぶことが多いです．35年ぶりにドット絵を作ってみましたが，以前よりはうまくなりました．
昔懐かしいゲームのキャラクタだけ，作ってみました．8ピクセル×8ピクセル×2色で，どこまでできるでしょう．

### 2021-03-22

【まとめ】
- キャラクタ変更を使うと簡単に新しいゲームができあがります(いわゆるリノベーションに近いです)
- キャラクタの出来具合でゲームの印象が変わります(日本のゲームの優位性は，現時点でもここにあると推認されます)
- ナムコのキャラデザインへのこだわりはぜくう氏論文(cf. ゲームラボ2021年1月号)でも指摘されています
- キャラクタ変更の繰り返しは，新しいゲーム(いわゆるイノベーション)を生みづらくなります
- テトリスやマイクラのような新ジャンルを開拓するゲームは海外発が多いです(日本ゲーム界の課題で，漫画やアニメを超越できない理由です)
- 漫画には少年ジャンプといったシリコンバレーモデル(イノベーション生産工場)が存在します
- アニメやゲームには存在しないため，将来的にゲームは漫画の下流工程になる可能性があります(鬼滅の刃ゲームが早晩ローンチされるでしょう)

### 2021-04-04

chip8向けの垂直型ブロック崩し
[vbirx](https://github.com/badlogic/chip8/blob/master/roms/sources/VBRIX.SRC)
をoctoに移植(記法変換)しはじめました．
chip8のアセンブリ言語とocto言語の対応(一部)は，次の通りです．

| アセンブリ言語 | octo言語 |
|---------------|----------|
| mov v0, v1 | v0 := v1 |
| add v2, v3 | v2 += v3 |
| skne v4, v5 | if v4 == v5 then |
| skeq v6,v7 | if v6 != v7 then |
| jmp label | jump label |
| jsr label | label |

chip8のアセンブリ言語も複数の記法あるようで，ソースコードで微妙に異なります．

### 2021-04-07

octo版vbrixが完成しました．
cf. https://johnearnest.github.io/Octo/index.html?key=drtrCk7o

特に，下記の処理は興味深いです．
- ボールとブロックの衝突を検知すると，どのブロックに衝突したかをXY座標を3で割り論理的な座標を求めます（192行から199行まで）
- さらに論理的な座標を3倍して物理的な座標を求めて，その座標のブロックを消しています（200行から209行まで）

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/vbrix01.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/vbrix04.png)

### 2021-04-09

SuperChip8って，よくわかってなかったのですが，hires命令で，高解像度(128x64)に切り替わって，16x16スプライトが使えるみたいです．
なんかShootingとか作れるのでしょうか．

### 2021-05-05

Octo環境でのChip8向けゲームとか，Atari社アステロイドのHaskell実装とか，いろいろつぶやきましたが，tweetの方は消して，wikiにまとめました．

- cf. https://github.com/jay-kumogata/Nostalgia/wiki/210307_OctoNote
- cf. https://github.com/jay-kumogata/Nostalgia/wiki/210427_AsteroidsNote

未公開写真も載せておきました．ゲーム作りは運動不足になるので，しばらくお休みです．

### 2021-05-20

日本語を少し直しました．ですます調に統一しました．

### 2021-07-04

昨日位から，またocto環境をいじりたくなりました．
[ufo](https://github.com/badlogic/chip8/blob/master/roms/sources/UFO.SRC) という古いゲームをoctoアセンブリ言語に変換してみました．

### 2021-07-05

[ufo](https://github.com/badlogic/chip8/blob/master/roms/sources/UFO.SRC) をoctoアセンブリ言語に写経してみました．
4(Qキー)と5(Wキー)，6(Eキー)で右/上/左にミサイルを発射，2種類のUFOを撃墜します．
15発で何回UFOを撃墜できるかを競います．
オリジナルでは，ラベル名がアドレス表記でしたが，意味が分かるラベル名に変更した結果，ソースリストの可読性は格段に向上しました．#chip8 #octo cf. https://johnearnest.github.io/Octo/index.html?key=RoehWpc2

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/ufo04.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/ufo02.png)

### 2021-08-09

2021年7月に作成してたufoのソースリストとスクリーンショットを [GitHub](https://github.com/jay-kumogata/Nostalgia/tree/main/octo/) に上げました．[Wiki](https://github.com/jay-kumogata/Nostalgia/wiki/210307_OctoNote) にも追記しました．

### 2021-08-14

[snake](https://github.com/massung/CHIP-8/blob/master/games/sources/snake.c8)もoctoアセンブリ言語に写経してみました．
蛇を操作して餌を食べる有名なゲームです．
餌を食べるたびに蛇が長く成長します．
W/S/A/Dキーで，上/下/左/右に移動します．
ハッスル（1977年 / グレムリン）がオリジナルでしょうか．
当時日電製PC-8001には，移植版が存在しました．#chip8 #octo cf. https://johnearnest.github.io/Octo/index.html?key=s9lZRK2j

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/snake04.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/snake09.png)

### 2021-08-29

[clock](https://github.com/massung/CHIP-8/blob/master/games/sources/clock.c8)もoctoアセンブリ言語に写経してみました．
オーソドックスなデジタル時計デモです．
CHIP8には，1/60秒毎にカウントアップするディレイタイマが内蔵されています．
それを計数して，数字を表示しています．
時計や迷路は，当時デモプログラムの定番でした．#Chip8 #Octo cf. https://johnearnest.github.io/Octo/index.html?key=vYOgYUe-

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/clock03.png)

### 2021-09-01

[maze](https://github.com/badlogic/chip8/blob/master/roms/sources/MAZE.SRC)もoctoアセンブリ言語に写経してみました．
少し変わった迷路デモです．
ビットマップで右向きと左向きの対角線を作成します．
右向きの対角線には接続点が追加します．
いずれかを乱数でタイル状に表示していくアルゴリズムです．
時計や迷路は，当時デモプログラムの定番でした．#Chip8 #Octo cf. https://johnearnest.github.io/Octo/index.html?key=2h3CGRrv

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/maze02.png)

### 2021-09-12

[Octojam8](https://itch.io/jam/octojam-8)で，サンプルゲームとして紹介されているDodgeのキャラクタを変更してみました．
テーカン（現コーエーテクモゲームス）の名作スターフォースを意識しました．
落下する隕石をひたすら避けてください．
A/Dキーか，←/→キーで操作できます．
#Chip8 #Octo cf. https://johnearnest.github.io/Octo/index.html?key=qRs0BFdX

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/dodge04.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/dodge03.png)

### 2021-09-25

[Octojam8](https://itch.io/jam/octojam-8)というのは，octo/chip8のプログラムコンテストのようなものらしいです．
これは，その[参加作品](https://twitter.com/TomRintjema/status/1441408350122483723)です．
[2ツイート目](https://twitter.com/TomRintjema/status/1441408713558945799)に記述がありますが，ボールの動きが4方向だけでなく，8方向あり，リアルな表現がされているみたいです．
Pong時代の伝統的なテクニックです．

[Octojam8](https://itch.io/jam/octojam-8)の[参加作品](https://twitter.com/TomRintjema/status/1441392001727959048)です．
3D迷路です．
迷路データを最初に作成しておき，現在位置と進行方向で，壁を表示するアルゴリズムだと推測します．
但し，実装はしたことがないので，適当なコメントです．
この画面を見ていると，名作ブラックオニキスを思い出します．
ブラックオニキスの販売元BSPの社長は，その後に任天堂の支援を受けて，テトリスの版権を取得して，富豪になりました．

### 2021-09-29

[boot](https://github.com/massung/CHIP-8/blob/master/games/sources/boot.c8)もoctoアセンブリ言語に写経してみました．
元々はChip8エミュレータでイメージを指定しない時に表示されるデモです．
オリジナルのロゴは「CHIP-8」だったのですが，3x4ピクセルのアルファベットで名前を描いてみました．
mの文字は，3x4ピクセルでは表現できずに若干苦労しました．#Chip8 #Octo cf. https://johnearnest.github.io/Octo/index.html?key=cYnRGjHz

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/boot02.png)

### 2021-10-02

[Octojam8](https://itch.io/jam/octojam-8)でサンプルゲームとして紹介されているDodgeのキャラクタを変更してみました．
ナムコ（現バンダイナムコ）の名作ゼビウスを意識しました．
ソルバルウを操作して，ドームとピラミッドをひたすら避けてください．
A/Dキーか，←/→キーで操作できます．#Chip8 #Octo cf. https://johnearnest.github.io/Octo/index.html?key=RjDV5jpJ

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/dodge15.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/dodge16.png)

### 2021-10-03

3x4ピクセルで[アルファベット](https://twitter.com/ajbkr/status/1312839042933850112)を表現しています．
参考になります．

### 2021-10-06

- 7月頃からマイブーム（死語）になっていたOcto/Chip8で作ったゲームとスクリーンショットを[Github](https://github.com/jay-kumogata/Nostalgia/tree/main/octo)の方に上げました
- [Wiki](https://github.com/jay-kumogata/Nostalgia/wiki/210307_OctoNote)も加筆しました

### 2021-11-10

mastermindをoctoアセンブリ言語で復刻しました．mastermindは，過去に本格版と簡易版の2種類が開発されています．ここでは，簡易版バイナリを逆コンパイルして，Viperという雑誌(1巻7号, pp.22-26)に掲載された本格版のコメントを転記しています．#Chip8 #Octo cf. https://johnearnest.github.io/Octo/index.html?key=ZcpKkcEl

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/mastermind102.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/mastermind103.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/mastermind104.png)

### 2021-11-12

簡易版mastermindは，1から6までの数字を4個当てるゲームです．10回試行できます．1/2/3/Q/W/Eキーで数字を入力します．Vキーで入力をキャンセルできます．数字の値と位置が両方一致した場合は「点線」が，値のみ一致した場合は「白線」が表示されます．そのヒントを参考に数字を当てていきます．

### 2021-11-13

本格版mastermindもoctoアセンブリ言語で復刻してみました．Viperという雑誌(1巻7号, pp.22-26)に掲載された本格版ソースを手作業で打ち込みました．ゲームとしては動作しているみたいですが，低解像度モード(64x32)ではピクセル不足で画面が崩れました．#Chip8 #Octo  cf. https://johnearnest.github.io/Octo/index.html?key=IadqXvZS

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/mastermind203.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/mastermind204.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/mastermind205.png)

### 2021-11-14

高解像度モード(128x64)で動作させてみると，画面崩れは発生しませんでした．本格版では，行数が4行から5行に，数字も6個(1から6まで)から8個(0から7まで)に増えています．数字は，X/1/2/3/Q/W/E/Aキーで入力していきます．それ以外は，簡易版と同じです．#Chip8 #Octo cf. https://johnearnest.github.io/Octo/index.html?key=rp9zbF4S

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/mastermind213.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/mastermind214.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/mastermind215.png)

### 2021-11-16

簡易版mastermindの数字フォントを少しおしゃれに変更してみました．サイコロや麻雀牌バージョンも作ってみましたが，4x5ピクセルでは上手に表現できませんでした．やはりMr.ドットマンは偉大です．次は，少し和風な「花札」バージョンを作ってみます．#Chip8 #Octo cf. https://johnearnest.github.io/Octo/index.html?key=pBwOheiC

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/mastermind113.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/mastermind114.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/mastermind115.png)

### 2021-11-17

簡易版mastermindの数字フォントを変更してみました．「麻雀牌(筒子)」をモチーフにして作りはじめましたが，矢追純一氏のUFO特集で，謎の金属に刻まれている「宇宙語」みたいになってしまいました．4x5ピクセルでは，「花札」は難しくて断念しました．#Chip8 #Octo cf. https://johnearnest.github.io/Octo/index.html?key=zv6u4yUz

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/mastermind123.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/mastermind124.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/mastermind126.png)

### 2021-11-19

本格版mastermindの数字フォントも少しおしゃれに変更してみました．フォントを変更するだけで，外観の印象（ルック・アンド・フィール）が若干改善することが分かります．ビデオゲームが進化する方向性としては，やはり重要な要素なのでしょう．#Chip8 #Octo cf. https://johnearnest.github.io/Octo/index.html?key=Lx6kulFm

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/mastermind223.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/mastermind224.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/mastermind225.png)

### 2021-11-20

mastermindシリーズには，下記のバージョンがあります．

- 簡易版(4行): クラシック数字 / デザイン数字 / 麻雀数字
- 本格版(5行): クラシック数字 / デザイン数字

また，mastermindのアルゴリズムは，下記の通りです．

- (1) 初期画面表示
- (2) 解答(ANS)作成　乱数(0から7まで:5行バージョンの場合 ⇒ 1から6まで: 4行バージョンの場合)
  - ⇒数字の種類を8種類から6種類にすることで簡単にしている(5行⇒4行)
- (3) キー(IN)入力(1から6まで)　F→キャンセルロジック
- (4) バー表示
  - (4-1) ドットバー
    - 場所と数字が一致した場合に表示　一致数+1
    - COPY(=ANS)　⇔　IN を比較
    - 4個とも一致したら、あたり　⇒　(5) 解答表示へ
  - (4-2) 白いバー
    - ドットバーは除いて、数字が一致した時に表示
    - COPY(=ANS) × INで総当たり(ドットバーを表示したところは除外しておく)で比較
- ステップ(3)から(4)までを10回繰り返す
- (5) 解答表示(ANS)　⇒　点滅

### 2021-11-21

[5x7ピクセル](https://twitter.com/fontdasu/status/1461881782161182725)あると，結構いろいろとできるのでしょう．4x5ピクセルだと結構つらいです．

### 2021-11-26

[snake](https://johnearnest.github.io/Octo/index.html?key=s9lZRK2j)の実装法は，

- (1) 蛇の胴体の座標を事前に保存(同時に画面表示)
- (2) キー操作で蛇の向き(上/下/左/右)を変更
- (3) 蛇の先頭の座標を蛇の向きに1ピクセル更新(同時に画面表示)
- (4) 当り判定
  - 餌: 点数と胴体の長さを増やす
  - 胴体と外枠: ゲームオーバー
- (5) (2)から(4)を繰り返す

が一般的です．

### 2021-12-01

[mastermind](https://johnearnest.github.io/Octo/index.html?key=Lx6kulFm)という遊技(*1)について，少し調査してみました．
任天堂スイッチの[世界のアソビ大全51](https://www.nintendo.co.jp/switch/as7ta/)だと，「ヒットアンドブロー」というタイトルで収録されています．
これ以外にも，ルールは同じで内容が異なる亜種が多数存在します．
日本では，野村トーイが，[おむすび探偵団](https://mouneru.com/toys-omusubi-tanteidan/)という亜種を販売しています．
おむすびの具を当てる遊技で，具の中身があうと「お茶」，中身と場所があうと「おしんこ」が出されるという内容です．

(*1) あえて「遊技」という用語を使う場合は，ボードゲーム等のビデオゲーム以外を意味します．

### 2021-12-05

[Lunar Lander](https://github.com/massung/CHIP-8/blob/master/games/sources/lander.c8)もoctoアセンブリ言語で復刻させてみました．月着陸船を操作して，月面に着陸するゲームです．W/A/Dキーで，上/左/右に移動します．Lunar Lander(1979年/アタリ)が有名な実装ですが，アポロ計画の月着離船シミュレータがオリジナルのようです．#chip8 #octo cf. https://johnearnest.github.io/Octo/index.html?key=jQyyYdGT

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/lander02.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/lander12.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/lander13.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/lander05.png)

### 2021-12-07

1点訂正です．正しくは「W/A/Dキーか，↑/←/→キーで，上/左/右に移動します．」でした．蛇足ですが，歴史を総括した記事を見つけました．最初の実装は，Moonlander (1973年/DEC GT-40)で，その後も，さまざまなプラットフォームで実装されているようです．cf. https://www.pcmag.com/news/50-years-on-the-moon-the-evolution-of-lunar-lander-games

### 2021-12-08

本作品のオリジナルは，[Jeffrey Massung氏による実装](https://github.com/massung/CHIP-8/blob/master/games/sources/lander.c8)です．Chip8アセンブラで記載されていたソースをOcto記法に変換しています．ですので，ロジックは変更していません．時々難易度が高い地形が現れますが，これもバグではなくて仕様なのだと想像します．#chip8 #octo

### 2021-12-11

時々難易度が高い地形も現れます．レベルとは関係なく，ランダムに現れます．難易度が十分に調整がされていないのかもしれません．また，Lunar Landerには，[1979年のUdo Pernisz氏による実装](https://github.com/yupferris/Uno8/blob/master/GamesPreprocessor/Games/Lunar%20Lander%20\(Udo%20Pernisz,%201979\).ch8)も存在します．現在，復刻の作業中ですので，近日中に公開します．#chip8 #octo cf. https://johnearnest.github.io/Octo/index.html?key=jQyyYdGT

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/lander06.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/lander03.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/lander04.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/lander07.png)

### 2021-12-12

[Lunar Lander(Udo Pernisz氏 / 1979年)](https://github.com/yupferris/Uno8/blob/master/GamesPreprocessor/Games/Lunar%20Lander%20\(Udo%20Pernisz,%201979\).ch8)もoctoアセンブリ言語で復刻させてみました．逆コンパイルで生成したソースリストを大幅に変更しています．1/2/3キーでレベル選択後に，月着離船を月面に着陸させてください．2/Q/Eキーで，上/左/右に移動します．#chip8 #octo cf. https://johnearnest.github.io/Octo/index.html?key=7BbFr8Es

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/lander202.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/lander207.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/lander203.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/lander205.png)

以上
