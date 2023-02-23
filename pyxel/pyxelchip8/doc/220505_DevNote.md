## PyxelによるChip8エミュレータ開発記

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

### 2023-02-13

年末年始に，Pyxel版Chip8エミュレータ（PyxelChip8） を少し改良しました．週末にソースコードを少し整理しました．
後楽園球場の電光掲示版を意識したテーマを追加しています．David Winter氏の有名なINVADERS.ch8を動かしてみました．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelchip8/screenshots/INVADERS01.gif)

### 2023-02-17

桃の節句に因んで，緑と桃色のテーマも追加してみました．いわゆるブロック崩し（BRIX.ch8）を動かしてみました．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelchip8/screenshots/BRIX01.gif)

### 2023-02-21

桃色とグレーのテーマも追加してみました．Chip8のテストコード（test_opcode.ch8）を動かしてみました．
無事全ての命令で合格となりました．
Chip8miniで修正した不具合も同時に直しました．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelchip8/screenshots/test_opcode.gif)

### 2023-02-23

Chip8の多種多様な拡張で，最も有名なのが，SuperChipです．PyxelChip8にも，SuperChipの命令を追加していきます．

- CPU
  - 00FE: Disable high-resolution mode 命令
  - 00FF: Enable high-resolution mode 命令
  - DXY0: Draw 16 x 16 sprite命令

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelchip8/screenshots/amabie03.gif)

以上