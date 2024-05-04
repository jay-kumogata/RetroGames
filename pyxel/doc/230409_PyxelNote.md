## Pyxelによるゲーム開発記（2023年編）

### はじめに

レトロゲームエンジン [Pyxel](https://github.com/kitao/pyxel) によるゲーム開発の記録です．

### 2023-04-09

数式でアートが作れるなら，数式で遊びが作れるのだろうか．と考えながら散歩しました．多分できないです．
数式でできるのは，シミュレーションまでです．それを遊びにするのは，ホモ・ルーデンスである我々ということになります．

例えば，月面着陸船の挙動を数式で表して，それを月面着陸シミュレーションにすることはできます．
でも，それを訓練と思うか，遊びと思うかは，あくまで我々ということです．
そもそも，数式でアートが作れるというのも，数式でシミュレーション（もしくは単なる模様）が作れるだけです．
それを美しいと思うのは我々なんだなと思います．
何を芸術と思うか，何を遊びと考えるか，ということを，他の人と共有できれば，それらは芸術や遊びとして成立するのでしょう．
数式で遊びが作れるか，という問いについて，少し考えてみました．

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

### 2023-09-11

昔ベーマガに載ったゲームがありましたが，持っていない機種のゲームだったので，遊ぶことができませんでした．
どんなゲームだろうと思っていたので，40年の時を超えて，Pyxelで作り直しています．
異常に難しいゲームでした．
ある程度まとまった時点で，リリースしようかと考えています．

### 2023-09-12

当時のBASICで書かれたゲームは，なんか偶然で動いてるというか，設計しないで思いつきで作っているようです．
なので，Pyxel化しつつ，リファクタリングしないと意味不明なコードになります．
ただ，ビデオゲームを買っても，遊ぶわけでもないですし，まして，自分で作ったゲームなど，遊ぶわけないですね．
できたら，おしまいです．

### 2023-09-18

ウィングマン氏の [ACLM](https://archive.org/details/micom-basic-magazine-issue-16-october-1983/page/n92/mode/1up) をPyxelに移植しました．
オリジナルは，「マイコン BASIC Magazine（1983年10月号）」に掲載されています．
自機（赤）を操作して，敵機（青）を上下左右にぶつけて倒すゲームです．
異常に難しいので，自機と敵機が衝突した場合は，「負け」ではなく，「引分け」にルール変更しました．
また，オリジナルには，その後に，都市を攻撃するシーン（2面）があるようです．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/aclm/screenshots/aclm01.gif)
![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/aclm/screenshots/aclm02.gif)
![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/aclm/screenshots/aclm03.gif)

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

### 2023-11-26

夏頃に花札を作ろうと思い，ドットを置きました．
完成が遠いので，とりあえず，48枚の花札を表示するデモを作ってみました．
matt氏作の [Hanafuda Koi-Koi (Japanese card game)](https://www.lexaloffle.com/bbs/?tid=2421) を参考にしています．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/hanafuda/screenshots/hanafuda01.png)

以上
