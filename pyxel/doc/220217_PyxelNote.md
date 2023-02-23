## Pyxelによるゲーム開発記

### はじめに

レトロゲームエンジン[Pyxel](https://github.com/kitao/pyxel)によるゲーム開発の記録です．

### 2022-02-17

お夜寝から目が覚めたので，pyxel環境を整えました．

 - python: 3.8.9
 - pip: 22.0.3
 - pyxel: 1.6.9

pyLodeRunnerを動かそうとしたら，すでに消えていました．
権利的にNGだったのかもしれません．
シューティングゲームのサンプルは無事に動きました．

### 2022-02-18

octo/chip8から，pyxelへの変換系を書く夢を見ました．
その変換系でpyxelコードを生成して，キャラクタを高精細化して，着色していくと，古いゲームがpyxelでも復刻できるかもしれません．
これが本当のピクセルリマスタかもしれません．

### 2022-02-19

ブックオフから帰宅して，もろもろ掃除とかして，この前に動かしたシューティングのサンプルソースコードを読みました．
pythonと2Dゲームの知識があれば，比較的すらすらと読めるかもしれません．
350行位だったので，そんなに苦労せずに理解できました．
ただ普通に何か作ってもつまらないので，少し考えます．

### 2022-02-20

pyxel 1.6.9だと若干構文が変わっています．

	% pyxel edit *.pyxres
	% pyxel copy_examples

[Asteroids](https://github.com/timbledum/asteroids)の実装がGitにあったので，動かしてみました．
ロジックをpythonで書く必要があるので，Pyxelでの開発はあまり気分が盛り上がらないです．

### 2022-04-03

Pyxelを少し練習しました．pngファイルが読み込めるみたいです．なにか作ってみようかなと考えています．

### 2022-04-24

昨年Chip8で作成していたマスターマインド(簡易版/本格版)をPyxelに移植しようかなと考えています．
午前中に，マスターマインド(簡易版)の方から作業開始しました．
Chip8版のキャラクタ(数字等)が，6x6ピクセルなので3倍弱に拡大して，Pyxel版のキャラクタ(数字)は16x16ピクセルで描くことにしました．
Chip8の画面(64x32ピクセル)は，3倍に拡大して，192x96ピクセルで初期化しました．
画面設計は完了です．

### 2022-06-10

他の方が筐体を組み立てる様子にあこがれて，ドット絵で筐体を描きはじめました．
外枠はできあがりました．
pyxelで表示させているのは，最後にpyxelchip8と組み合わせて，筐体の中でchip8を動かすためです．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/chip8mini/screenshots/Amabie01.gif)

筐体のデザインは，どうしよう．タイトルは，Amabieにしよう．右にイラストを書こうかな．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/chip8mini/screenshots/Amabie02.gif)

### 2022-06-11

ウォーキング(散歩)を2時間位してきました．
その後に，少しPyxelをいじったら，筐体の中でChip8が動くようになりました．
他のゲームも動くことを考えたら，Chip8 Mini等の汎用的なタイトルの方がいいのかもしれません．
今日はここまでで，ゲーム漁りにいきます．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/chip8mini/screenshots/Amabie06.gif)

### 2022-06-12

今日も，ウォーキング(散歩)を2時間位してきました(昨日と同じルートです)．
その後に，筐体のデザインを改造してみました．
ゲーム毎に筐体デザインを変えることにしました．
これは，アマビエ専用です．アマビエイラストと青海波(波模様)を描き加えてみました．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/chip8mini/screenshots/Amabie08.gif)

### 2022-06-17

Chip8Miniの第2弾として，今週はBreakoutを動かす筐体デザインを考えていました．
Atari製の筐体を参考にしているつもりですが，少し派手すぎかもしれません．
David Winter氏のBreakoutをChip8で動かしています．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/chip8mini/screenshots/Breakout01.gif)

### 2022-06-18

一応，[ソースコード](https://github.com/jay-kumogata/RetroGames/tree/main/pyxel/chip8mini)を公開しました．

### 2022-06-22

Chip8Miniの第3弾として，今週はSnakeを動かす筐体デザインを考えていました．
肝心のSnakeが動かなかったので，少し調べると，「0x8XY5 : VX = VX - VY, VF = Not Borrow」命令に実装誤りがあり，15年越しに修正しました．
画面はアンバーディスプレイ風にしてみました．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/chip8mini/screenshots/Snake01.gif)

0x8XY5命令を，

	  VX = VX - VY
	  if VX < 0 then
	    VF=0
	    VX=VX+0x100
	  else
	    VF=1

と実装していました．VX≡VF<0の場合，VF=0x100になってしまいます．

	  VX = VX - VY
	  if VX < 0 then
	    VX=VX+0x100
	    VF=0
	  else
	    VF=1

と実装すると，VF=0になり，正しく動作します．

### 2022-06-25

[GitHub](https://github.com/jay-kumogata/RetroGames/tree/main/pyxel/chip8mini)の方にソースコードを上げました．
「0xFX55 : Save V0..VX in memory starting at M(I)」命令と「0xFX65 : Load V0..VX from memory starting at M(I)」命令の実装誤りも修正しました．
仕様からは読み取れませんが，副作用として，Iレジスタがインクリメントされるようです．
Mastermind(4row)は，そのように実装されていました．

### 2022-07-01

Chip8Miniの第4弾として，今週はMasterMindを動かす筐体デザインを考えていました．
先日の[ZUNTATA NIGHTスペシャル『ZUNTATA35周年記念祭』](https://www.youtube.com/watch?v=u9inj3uCxOQ)に出演していた海野和子氏へのオマージュとして，バブルンとボブルンがマスターマインドで遊んでいるイラストを描いてみました．
タイトー社の著作権を侵害する意図は全くありません．問題あるようでしたら，ご連絡下さい．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/chip8mini/screenshots/Mastermind01.gif)

Chip8Miniの第3弾として，先週デザインしたSnake筐体に，蛇のイラストを描き加えてみました．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/chip8mini/screenshots/Snake02.gif)

### 2022-07-20

Pyxelで，ニキシー管時計を作りはじめました．
まず，ニキシー管のドット絵を描いてみましたが，少しおもちゃっぽい感じの仕上がりです．
電源をOFF/ONすると，LEDチェック（カウントアップ）が走るLED電卓を持っていたのですが，そのことを思い出しました．
この続きを作るかは微妙です．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/nixie/screenshots/Nixie01.gif)

### 2022-08-07

Chip8Miniの第5弾として，今週はネオン管を使った筐体デザインを考えてみました．
80年代後半のビアバーに飾ってあったようなネオンサインをイメージしています．
この物質的な発展が無限に続くような，そんな楽観的な空気感が伝わるように描きました．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/chip8mini/screenshots/Neon01.gif)

### 2023-02-18

模擬器作り依存症かもしれないです．
模擬器を作っていないと落ち着かないみたいです．
これまでは，PyxelChip8を作っていたのですが，完成に近づいてしまい，DCPU16模擬器を作りはじめました．
実は，20年位前に，Chip8の次は，DCPU16かなと考えてはいたのですが，本業が忙しくできませんでした．

### 2023-02-19

PythonでDCPU16模擬器を書いていたのですが，Rustの[実装](https://github.com/gustavla/dcpu16)を読んでいると，これは型がないとだめかなと感じました．
次のテーマにいくことにします．やはり，模擬器は，C++か，Rustか，で書くべきでしょう．
Chip8位であれば，Pythonで書けますが．

### 2023-02-20

Pythonでも，Ctypesライブラリで，c_uint16が使えるみたいのです．
明示的に型指定しない言語は，型推論があるので，複雑なことは避けた方がよさそうです．
そう考えると，Pythonのintだけで動作しているPyxelChip8は，結構奇跡かも知れません．
昨日悩んでたDCPU16模擬器ですが，下記の[実装](https://github.com/daniel-lundin/dcpu-16-python)が動き出したので，少し改造するかもしれません．
結局Python 3.0で型チェックが厳格化されてエラーになっていました．リファクタリングが必要です．
ただ，中途半端な実装で正確に動作させるには，結構時間が必要な模様です．

以上
