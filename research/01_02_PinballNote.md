# 01_ゲーム製作: 02_ピンボール開発記

つぶやきながら，ピンボールを開発する日記です．

##  ピンボール開発記

### 2022-08-07

最近，ピンボールを作りたくなっているけど，いまさらなので，やめようかなと考えています．
ただ，「車輪の再発見」という言葉あるけど，「再発見」しないと本当には理解できないと思います．
モノ作りってそういうものです．これは，ビジネススクールでは教えてくれないことです．

### 2023-04-28

年初から，ピンボールを作りたいと思い，数日前から作りはじめました．
PICO-8実装を写経するという手法です．
Isidor氏の [Pinball Pong](https://www.lexaloffle.com/bbs/?tid=28488) を写経しました．
ピンボールというか，ピンボールとブロック崩しが融合したゲームです．
オリジナルはランダム要素が強かったので，シミュレーション要素を強めに変更しています．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pinball/screenshots/Pinball01.gif)

### 2023-04-30

画面上部の障害物，画面左右のバー（5点），ゲームオーバー処理を追加しました．
キャラクタも立体感が出るように描き直しました．
[コード](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pinball) は，多少リファクタリングしました．
小学生の時に，PC-8001mkIIで作ったブロック崩しを思い出します．
あれから40年位経過したけど，やっていることに進歩がないですね．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pinball/screenshots/Pinball02.gif)

### 2023-07-16

昔は，ピンボールとブロック崩しが合体したゲームが結構あったらしいです．
ナムコのボムビーとか，キューティーキューとかです．
結構作ってみると，フリッパーの処理が難しくて，パドルだと簡単に作れることがわかります．

### 2023-07-17

Isidor氏の [Pinball Pong](https://www.lexaloffle.com/bbs/?tid=28488)をPyxel に移植してみました．
ピンボールとポンを組み合わせたようなゲームです．
春頃に作って公開するのを忘れていました．
任天堂ピンボールのツイートを見て，思い出しました．
#Pyxel #Pinball

### 2023-07-18

Pyxelで動作するPinball Pong🕹️の [ソースリスト](https://github.com/jay-kumogata/RetroGames/tree/main/pyxel/pinball) 📁を公開しました．
#Pyxel #Pinball 

### 2023-10-23

週末に，春頃に作ってたPinball Pongを少し直しました．
Pongということで，パドルでボールを跳ね返すゲームだったのを，Pinballらしく，フリッパーを付けました．
しかも，デザインの都合で，ダブルフリッパーです．
各アイテムの位置決めが結構大変で，いい感じにするのに時間がかかりました．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pinball/screenshots/Pinball03.gif)

### 2023-11-09

Pyxelで動作するPinball🕹️の [ソースリスト](https://github.com/jay-kumogata/RetroGames/tree/main/pyxel/pinball) 📁を公開しました．
#Pyxel #Pinball 

### 2023-11-17

Pinballの続きです．フリッパーを追加したのはよかったのですが，ボールの動きが不自然なままでした．
そこで，重力加速度を大きめにして，フリッパーの速度に応じて，ボールが上がるように修正しました．
物理シミュレーションっぽい感じにはなりましたが，ビデオゲームとして面白いかは不明です．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pinball/screenshots/Pinball04.gif)

### 2023-11-18

小学生の頃に，コリントゲームをヒントに木製のピンボールを作ったことがあります．
その時は，全然完成しませんでした．
約45年の時を超えて，ようやくピンボールが完成しました．

以上
