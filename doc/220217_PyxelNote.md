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

### 2022-05-01

Alan Turingという数学者がいます．
彼の大きな業績としては，Turing Machine(計算モデル)，Turing Test(人工知能)，Turing Bombe(暗号解読)が有名です．
そして，晩年のあまり知られていない業績として，Turing Pattern(セルオートマトン)もあります．
とある偏微分方程式を数値的に解くと，自然界で見られる模様が現れるというものです(産業的な応用は現時点では不明です)．
[Python実装](https://ipython-books.github.io/124-simulating-a-partial-differential-equation-reaction-diffusion-systems-and-turing-patterns/)があるので，練習も兼ねて，Pyxelで表示させてみました．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/turing/screenshots/turing01.gif)

最初はランダムな状態から開始されています．
時間が経過していくと，島ができてくるのが分かります．
Pyxelでは，パレットが固定されているので，ヒートマップのような表示はできません．
ここでは，負の値は暗い色で，正の値は明るい色で表示されるように工夫しました．
しかしながら，計算機が遅い時代に手で計算してたAlan Turingは，やはり天才です．

Turing Patternsを表示するには，いろいろなモデルがあるようです．
ここでは，元東京大学教授の南雲仁一氏が考案した「FitzHugh–Nagumoモデル」を利用しています．
他にも，「Gray-Scottモデル」等があるようですが，Pyxelの練習ですでので，これ以上は深入りしないことにします．

### 2022-05-02

[Github Wiki](https://github.com/jay-kumogata/RetroGames/wiki/220217_PyxelNote)の方にも転載しました．
また，[ソースコード](https://github.com/jay-kumogata/RetroGames/tree/main/pyxel/turing)も上げました．
一連のtweetsは，絵的には美しくないので，しばらくしたら削除すると思います(ナウシカのセリフではありませんが)．

### 2022-05-05

15年以上前に書いたPython版Chip8エミュレータ([PyChip8](https://github.com/jay-kumogata/PyChip8))をPyxelで書き直しました．
Pyxelの場合には，1画面を処理する毎に，ロジック更新(update())と画面更新(draw())が実行されます．
そのため，Chip8エミュレータのようなプログラムは，比較的書きやすいです．
おまけ機能として，Chip8の1ドットをPyxelの4x4x16色ピクセルで表現してみました．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelchip8/screenshots/PONG01.gif)

### 2022-05-06

3月頃に、Chip8アセンブリ言語(Octo)をPyxelに変換する夢をみました．
OctoからPyxelに変換する変換系を書く方が楽しそうですが，まずはお手軽に模擬系を書くことにしました．
昔書いたコードがほぼ流用できました．
VBRIXが動作しない等，若干精度が悪いみたいですが，そこは放置かなと考えています．
3DNesの技術を使うと，キャラクターをグレードアップできるかもしれません．

Chip8の場合には，DrawSprite命令の前に，iレジスタにスプライトの先頭番地を保存します．
そのアドレス毎に，属性情報を事前に準備しておけば，キャラクタに色(16色)を塗ることができそうです．
ちなみに，3DNesの場合には，3次元ピクセルを事前に用意しておいて，3次元表示を実現しているのではないかと想像しています．

### 2022-05-07

Pyxel版Chip8エミュレータ(PyxelChip8)の進捗です．
VBRIXが動作しない不具合は，エミュレーションのスレッドを分離することで直りました．
その結果，動きが速くなってしまったので，適当にスリープ処理を入れています．
vsyncタイミングも超適当な実装なので，明日修正するかもしれません．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelchip8/screenshots/VBRIX02.gif)

Chip8命令でキー入力を待つ命令を実装するコードで，単純にウェイト処理(busy wait)していると，キー入力を監視するスレッドにCPU時間が割り当てられず，永遠にウェイトしてしまう不具合がありました．
前回Pygameを利用した時に修正していた不具合でしたが，同じ間違いをしてしまいました．
Pygameを利用した前回のコードを見て，「なぜスレッドを起動しているのだろうか」と素朴に考えてしまいました．

ソースコードを綺麗にして，[GitHub](https://github.com/jay-kumogata/RetroGames/tree/main/pyxel/pyxelchip8)の方に上げておきました．
Readmeも適当な英語で書いておきました(スペルも結構忘れてますね)．
vsyncタイミング修正も未着手なので，そこも適当実装です(そもそも実機は存在しないので，多少適当でも許されるでしょう)．
Pythonの練習もできたので，次はオリジナルのゲームを作りたいです． 

### 2022-05-10

お誘いいただきまして，ありがとうございます．
簡単ではありますが，[投稿](https://github.com/kitao/pyxel/issues/378#issuecomment-1121612076)させていただきました．
いかがでしょうか．

### 2022-05-12

Pyxel版Chip8エミュレータ(PyxelChip8)の進捗です．
昨晩，拙作[amabie](https://github.com/jay-kumogata/RetroGames/tree/main/octo/amabie)を動作させてみました．
修正は不要で特に問題なく動作しました．
妖怪アマビエが活躍して，このまま疫病が終息することを期待します．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelchip8/screenshots/amabie02.gif)

なお，拙作[amabie](https://github.com/jay-kumogata/RetroGames/tree/main/octo/amabie)の方では，バイナリ(amabie.ch8)とカートリッジ画像(amabie.gif)も追加で配布しています．

### 2022-05-15

前回のGIFアニメでは，妖怪アマビエが疫病に感染してしまう場面が繰り返し表示されます．
若干縁起が悪い印象です．
本来は，妖怪アマビエが疫病に御札を投げて，疫病を退治することが主題のゲームです．
GIFアニメを再度録画しました．
また，前回より，PyxelChip8の色味を桃色系に変更しています．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelchip8/screenshots/amabie01.gif)

### 2022-05-22

PyxelChip8のコードの大半は、15年前に書いたものです．
エミュレーションロジックとゲームエンジンを繋ぐコードは，あらかじめ分離した設計にしておくと，今回のようにゲームエンジンの変更も簡単に実現できます．
模擬系ではなくて，変換系も設計中ではあるのですが，少しペンディングです．
プライベートでは，コーディングではなくて，なるべくウォーキングすることにします．
Pyxelの宣伝に少しは役立てたでしょうか．

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

### 2022-08-16

2022年5月頃に，Pyxelの練習を兼ねて，Turingパターンデモを作りました．
その時には，「FitzHugh-Nagumoモデル」を利用したのですが，「Gray-Scottモデル」という方程式系のデモも作ってみました．
デモの途中で，「ミャクミャク様」のようなパターンも現れます．少し気持ちが悪いです．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/grayscott/screenshots/grayscott_spots01.gif" width="256">

なお，書籍「作って動かすALife - 実装を通した人工生命モデル理論入門」の[サンプルコード](https://github.com/alifelab/alife_book_src/tree/master/chap02)を参考にさせていただきました．


以上
