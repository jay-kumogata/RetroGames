## Octo記法によるゲーム開発記(2022年編)

### はじめに

2022年編としてスピンオフしました．

### 2022-01-16

twitter界隈でwordleというゲームが流行しているみたいです．以前chip8向けで紹介したmanstermindとルールが似ています．こちらの方は，単語を当てるので，比較的難易度が低いかもしれません．単語を知っている方が有利なので，教育的な効果も高そうです．cf. https://www.famitsu.com/news/202201/07247076.html

### 2022-01-21

David Winter氏によるBreakout (Brix hack / 1997年)も復刻させました．逆コンパイルで作ったソースリストに，ラベルとコメントを追記していく方法を使っています．A/Dキーか，←/→キーで，パドルが左/右に移動します．全てのブロックを崩してください．#chip8 #octo cf. https://johnearnest.github.io/Octo/index.html?key=0mk82EeX

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/breakout05.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/breakout06.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/breakout07.png)

### 2022-01-23

昨年末にしかかりになってた，breakoutのocto化を終わらせました．
ゲーム作りはしばらくお休み予定です（そもそもはじめてもないかもしれませんが）．

### 2022-01-31

[Mastering CHIP-8](https://github.com/mattmikolay/chip-8/wiki/Mastering-CHIP%E2%80%908)という比較的新しい文書を見つけました．
Google翻訳かけてみると，[案外読める](https://github-com.translate.goog/mattmikolay/chip-8/wiki/Mastering-CHIP%E2%80%908?_x_tr_sl=en&_x_tr_tl=ja)かもしれません．

### 2022-02-03

Octo/Chip8には，XO-Chipという独自拡張があります．4色スプライトが利用できるようになるので，過去に開発したゼビウス風ゲームのキャラクタを4色に変更してみます．

### 2022-02-04

Octojam8でサンプルゲームとして紹介されているDodgeのキャラクタを4色に変更してみました．ナムコの名作ゼビウスを意識しました．ソルバルウを操作して，ドームとピラミッドをひたすら避けてください．A/Dキーか，←/→キーで操作できます．#Chip8 #Octo cf. https://johnearnest.github.io/Octo/index.html?key=td25F1pa

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/dodge22.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/dodge23.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/dodge24.png)

### 2022-02-07

もうすぐ桃の節句(ひな祭り)ということで，chip8(xo-chip)でお内裏様とお雛様を描いてみました．世界初かも．次は，三人官女に挑戦するかも．「貝覆い」というゲームを作る準備も兼ねてます．#Chip8 #Octo cf. https://johnearnest.github.io/Octo/index.html?key=RaScBoUk

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/ohinasama01.png)

### 2022-02-08

chip8(xo-chip)でお雛様を描いていくシリーズ第2弾です．雪洞と台座を描いてみました．雛人形っぽくなってきました．「貝覆い」というのは，はまぐりの中に絵を描いて，神経衰弱のようにあわせていく遊びです．平安時代には遊んでいた記録があります．#Chip8 #Octo cf. https://johnearnest.github.io/Octo/index.html?key=paS5Dd9g

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/ohinasama11.png)

### 2022-02-09

chip8(xo-chip)でお雛様を描いていくシリーズ第3弾です．三人官女を描いてみました．ドット絵は，illustAC( https://ac-illust.com )というサイトを参考に(マルパク)しています．xo-chipではサウンド機能も拡張されているので，BGMにも挑戦していきます．#Chip8 #Octo cf. https://johnearnest.github.io/Octo/index.html?key=AkMBvOSt

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/ohinasama21.png)

### 2022-02-10

chip8(xo-chip)でお雛様を描いていくシリーズ第4弾です．菱餅を描いてみました．音程が若干微妙ですが，「うれしいひなまつり」も演奏してみました．音色は変更できるのですが，あえて矩形波を使って，チップチューンっぽい仕上がりにしてみました．#Chip8 #Octo cf. https://johnearnest.github.io/Octo/index.html?key=qBcaW6kf

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/ohinasama31.png)

### 2022-02-25

Chip8(xo-chip)でお雛様を描いていくシリーズ第5弾です．ドット絵風の色使いに変えてみました．雛祭りは女の子のお祭りなので，桃色をメイン使っています．初代ゲームボーイ風の緑色がメインでは，感じがでませんでした．雛祭りデモは完成に近づいています．#Chip8 #Octo cf. https://johnearnest.github.io/Octo/index.html?key=k3SV71pE

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/ohinasama41.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/ohinasama42.png)

### 2022-02-26

Octojam8のサンプルゲームDodgeのキャラクタもドット絵風の配色に変更してみました．ナムコの名作ゼビウスの音楽を演奏させてみました．権利的にはグレーかもしれませんが，オマージュ作品ということでご勘弁ください．ソルバルウを操作して，ドームとピラミッドをひたすら避けてください．A/Dキーか，←/→キーで操作できます．#Chip8 #Octo cf. https://johnearnest.github.io/Octo/index.html?key=dyTBtStv

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/dodge34.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/dodge31.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/dodge32.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/dodge33.png)

### 2022-03-06

ピクセルアート(16x16x4色)の練習として，ゼビウスのアンドアジェネシスを描きました．せっかく描いたので，Dodgeの敵キャラクタに登場させてみました．ソルバルウを操作して，敵キャラクタをひたすら避けてください．A/Dキーか，←/→キーで操作できます．#Chip8 #Octo cf. https://johnearnest.github.io/Octo/index.html?key=mo04OUlO

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/dodge42.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/dodge41.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/dodge43.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/dodge44.png)

### 2022-03-21

Octo/Chip8を使って，ここ1年間で復刻したビデオゲームです．その1です．

- 遊びで復刻してみたビデオゲーム(その1)
  - 写真1: PONG(1972年 / Atari社が販売)
  - 写真2: Breakout(1976年 / Atari社が販売) 
  - 写真3: Lunar Lander(1979年 / Atari社が販売)
  - 写真4: Hustle(1977年 / Gremlin社が販売)

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/pong04.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/breakout07.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/lander13.png)
![](https://github.com/jay-kumogata/Nostalgia/blob/main/octo/screenshots/snake09.png)

### 2022-03-22

Octo/Chip8を使って，ここ1年間で復刻したビデオゲームです．その2です．

- 遊びで復刻してみたビデオゲーム(その2)
  - 写真1: Mastermind(1978年 / Robert Lindley氏が開発) 
  - 写真2: VBrix(1996年 / Paul Robson氏が開発)
  - 写真3: Amabie(2021年 / OctoサンプルDeepのキャラクタを変更)
  - 写真4: Dodge(2021年 / Octojam8サンプルDodgeのキャラクタを変更)

そして，最後にスクリーンショットです．

![](https://github.com/jay-kumogata/RetroGames/blob/main/octo/screenshots/mastermind114.png)
![](https://github.com/jay-kumogata/RetroGames/blob/main/octo/screenshots/vbrix03.png)
![](https://github.com/jay-kumogata/RetroGames/blob/main/octo/screenshots/amabie15.png)
![](https://github.com/jay-kumogata/RetroGames/blob/main/octo/screenshots/dodge44.png)

### 2022-04-11

これまでは，Wikiに書いていた文章をMarkdown化して，GitHubリポジトリに移動しました．
記載した内容は特に変更していません．
cf. https://github.com/jay-kumogata/RetroGames/tree/main/doc

### 2022-04-23

昨年作っていたmastermind(簡易版/本格版)のソースコードをGitHubに上げ忘れていました．
GitHubに上げましたので，そのお知らせです．
Pyxelに移植を検討していますが，少し逡巡しています．
cf. https://github.com/jay-kumogata/RetroGames/tree/main/octo/

### 2022-06-08

COSMAC VIPとCHIP-8の設計者Joseph Weisbecker氏の娘さんJoyce Weisbecker氏が，世界最初の女性ゲームデザイナーに認定されているそうです．
日本人最初の女性ゲームデザイナーは，高橋はるみちゃんでしょうか．
cf. https://www.fastcompany.com/90147592/rediscovering-historys-lost-first-female-video-game-designer

以上
