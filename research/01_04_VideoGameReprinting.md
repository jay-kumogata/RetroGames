# 01_ゲーム製作: 04_ビデオゲーム復刻記

## はじめに

ビデオゲームを復刻した記録です．
元々のタイトルは，「ビデオゲーム復刻論」でしたが，「復刻論」を論じるつもりも，能力もありません．

### 2021-11-09

当初はゲーム製作という課題でしたが，古いゲームを復刻するという課題に移行していくことになりました．

_(2025-05-02) ゲーム研究は，製作/歴史/収集というテーマを掲げて，開始されたのです．が，実態は，製作より復刻が中心になりつつあります．_

### 2023-11-29

すでに2023年も終わりに近づいています．2023年の主な成果としては，

- (1) PyxelChip8改造(SuperChip対応)
- (2) PyGmc4作成
- (3) Pinball作成(pico8より移植)
- (4) ACLM作成(ベーマガより移植)

等です．2024年は，少し大きな復刻に着手しようかと考えています．

## BasicからPyxelへの移植

### 2023-09-11

昔ベーマガに載ったゲームがありましたが，持っていない機種のゲームだったので，遊ぶことができませんでした．
どんなゲームだろうと思っていたので，40年の時を超えて，Pyxelで作り直しています．
異常に難しいゲームでした．
ある程度まとまった時点で，リリースしようかと考えています．

_(2025-04-29) Chip8と同時にBASIC言語のソースを復刻することも試行していました．_

### 2023-09-12

当時のBASICで書かれたゲームは，なんか偶然で動いてるというか，設計しないで思いつきで作っているようです．
なので，Pyxel化しつつ，リファクタリングしないと意味不明なコードになります．
ただ，ビデオゲームを買っても，遊ぶわけでもないですし，まして，自分で作ったゲームなど，遊ぶわけないですね．
できたら，おしまいです．

### 2023-09-15

BASICマガジン1983年10月号に掲載の「ASLM」というゲームをPyxel化しました．
本日は大雨でした．

### 2023-09-18

ウィングマン氏の [ACLM](https://archive.org/details/micom-basic-magazine-issue-16-october-1983/page/n92/mode/1up) をPyxelに移植しました．
オリジナルは，「マイコン BASIC Magazine（1983年10月号）」に掲載されています．
自機（赤）を操作して，敵機（青）を上下左右にぶつけて倒すゲームです．
異常に難しいので，自機と敵機が衝突した場合は，「負け」ではなく，「引分け」にルール変更しました．
また，オリジナルには，その後に，都市を攻撃するシーン（2面）があるようです．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/aclm/screenshots/aclm01.gif)
![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/aclm/screenshots/aclm02.gif)
![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/aclm/screenshots/aclm03.gif)

### 2024-06-14

[オートレース(1画面ソフト)](https://github.com/jay-kumogata/RetroGames/tree/main/pyxel/autorace)を公開しました．
昔懐かしい[はるみのゲームライブラリ](https://archive.org/details/Fm-7Fm-8/page/n173/mode/2up)からの移植です．
PyxelRogueを開発(移植)する過程で蓄積された「キャラクタ画面の扱い方のノウハウ」を再利用してみました．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/autorace/screenshots/autorace01.gif)

### 2025-03-13

2021年頃から，昔のBASICのゲームを復刻していくと楽しいかなと思い，2023年頃にPyxelをはじめて，少し復刻しました．
[ACLM](https://github.com/jay-kumogata/RetroGames/tree/main/pyxel/aclm)とか，
[Autorace](https://github.com/jay-kumogata/RetroGames/tree/main/pyxel/autorace)とかです．
でも，手動での変換は面倒なので，すぐに飽きてしまい中断してしまいました．

## JavaScriptからPyxelへの移植

### 2025-05-21

Chip8からPyxelへの変換は，限界が見えてきたので，視点を変えることにしました．
今度は，古いBASICをターゲットにして，Pyxelへ変換していくことにしました．
色々と検索する中で，古いゲームをJavaScriptで実装している
[サイト](https://gist.github.com/straker/)
を発見しました．
ただ，このサイトのゲームは，JavaScriptで書かれており，基本的な構造のみ(Basic)という意味でした．

そこで，Grok3で
[Frogger](https://gist.github.com/straker/82a4368849cbd441b05bd6a044f2b2d3)
をPyxelに変換してみました．
また，ほぼ修正なく，動いてしまいました．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/frogger/screenshots/frogger01.gif" width="208">

### 2025-05-22

色を修正してみました．本物の色に近づけました．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/frogger/screenshots/frogger02.gif" width="208">

### 2025-09-02

ビデオゲームを作る技法で，すでに化石になってしまった「疑似3D」に興味を持ちました．
「[疑似3Dでかんたんアウトラン](https://zenn.dev/sdkfz181tiger/articles/5b96fc307510a3)」
という記事を見つけたので，Grok4でJavascriptからPyxelに変換してみました．
Grok4は，Grok3よりも変換に時間を要しますが，正確なコードを出力します．
我々が数十年歩んできた「コードを書く楽しい時代」が，ほぼ正確に終わろうとしています．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/outrun/screenshots/outrun01.gif" width="240">

### 2025-09-05

背景を黒から青に変えました．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/outrun/screenshots/outrun02.gif" width="240">

### 2025-09-07

お盆前に，ビデオゲームを作る技法で，すでに化石となってしまった「疑似3D」に興味を持ちました．「疑似3Dでかんたんアウトラン」 という記事を見つけたので，Grok4でPyxelに変換してみました． Grok4は，Grok3よりも正確なコードを出力するようです．

## ProcessingからPyxelへの移植

### 2025-06-14

世界初のビデオゲーム(*1)である[Tennis for Two](https://ja.wikipedia.org/wiki/Tennis_for_Two)をPyxel/Pythonに
[移植](https://github.com/jay-kumogata/RetroGames/tree/main/pyxel/tennis)
しました．
Processingの[ソース](https://openprocessing.org/sketch/9892/)を，Grok3で変換しました．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/tennis/screenshots/tennis01.gif" width="256">

_(2025-06-14) (*1) 諸説あります．_

### 2025-06-20

Xに投稿しました．ビデオゲームの歴史を逆にたどる旅もいよいよ終着です．
[#pyxel](https://x.com/hashtag/pyxel?src=hashtag_click) 
[#pixelart](https://x.com/hashtag/pixelart?src=hashtag_click)

### 2025-07-29

Tea for TwoからのTennis for Twoへのコンボです．
「Tennis for Two（二人でテニスを）」のタイトルは，アメリカの楽曲および映画「二人でお茶を」に由来すると思われます
（なお『～大全』及び『～時代』では名前はなかったとしています）．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/tennis/screenshots/tennis01.gif" width="256">

## まとめ

### 2025-04-28

ビデオゲームの復刻については，
1996年頃に住んでいた駅前のレンタルビデオ店で，映画「ローマの休日」を借りたところから話がはじまります．
そのレンタルビデオ店に，映画「ローマの休日」を返却する時に，「昔の映画は簡単に観れるのに，
昔のビデオゲームは簡単には遊べないのは，なぜだろう．」という疑問を持ったのです．
その疑問を解決する技術として，模擬器(Emulator)があることを知り，1998年頃の模擬器開発につながっていくわけです．

_(2025-04-29) 模擬器の開発経緯については，それぞれのリポジトリの開発記を参照ください．_

その流れがあり，いくつかのビデオゲームは手動で復刻してみました．
昔のBASICで書かれたコードも，Pyxelに移してみました．

### 2025-05-01

X(Twitter)にも投稿しました．
また，蛇足ではあるのですが，産業的には，CobolからJavaへの変換は重要です．
最近は，生成AIを使っているみたいなのですが，CobolからJavaへ直接変換すると，CobolっぽいJava(=Jabol)になってしまうそうです．
そこで，Cobolから仕様，仕様からJavaに変換するといい感じになるらしいです．
一度仕様にすることで，意味が蒸留されるのでしょう．

_(2025-05-04) ビデオゲームの復刻については，一旦完了で，新しいテーマに移ることにします．_

以上
