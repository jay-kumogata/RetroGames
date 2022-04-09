___

## Octoで学ぶChip8アセンブリ言語

### はじめに

小学生向けにアセンブラを教えていく企画です．
Z80を題材にしてもよいのですが，結構複雑なので，超簡単なアセンブリ言語を題材にしましょう．
世界中で何人このチュートリアルを必要としているかは不明ですが，もしいるとしたら将来はIT長者かもしれません．

### Chip8とは

1977年に設計された仮想マシンです．
ゲームを作るのに適しており，現在でもマニアがゲームを作り続けられています．
Octoは，Chip8を開発するための環境で，エディタやアセンブラなどが一緒になっています．
だから，とても簡単にゲームが作れます．

#### Chip8入門

まず，Chip8について理解しましょう．
さまざまな言語で開発されたChip8エミュレータの記事
[[1]](https://qiita.com/yukinarit/items/4bdc821f1e46b0688d0d)
[[2]](https://qiita.com/whisper0077/items/b87f9a346fdf522a40fa)
があります．
これらの記事を読めば，概ねChip8の仕様が理解できると思います．
特に，命令セットの説明があるので，どんな命令があるかは理解しておいてください．

#### Chip8の歴史

筆者は，20年くらい前からChip8について調べてきました．
当時は，英語の文書をそのまま読んでいたのですが，先日日本語に翻訳された仕様[[3]](https://yukinarit.github.io/cowgod-chip8-tech-reference-ja/)を発見しました．
折角ですので，Chip8の歴史についてお話していきます．

Chip8というのは仕様ですので，Chip8というビデオゲーム機(ハードウェア)が存在したわけではありません．
こんな感じの解釈系を作ると，ビデオゲームが簡単に作れるかもという目的で考案された仕様です．
その意味だと，basicなどに近い概念です．ですので，Chip8エミュレータではなくて，Chip8インタープリタという呼び方の方が正確です．
エミュレータを書いていると，ビデオゲーム機の理解不能な動きに困惑することがままありますが，Chip8はある程度決定論的な動きをしてくれます．
そういう意味でも，エミュレータ(インタープリタ)を書きやすい利点があります．

Chip8の歴史には，何回か盛り上がり(ムーブメント)がありました．
まず最初は，70年代後半の発表時です．
非力なPC上で実装されて，いくつかのビデオゲームが作られました．
当時は紙に命令を直接書いていました．
機能を追加するには，jump命令で別の場所に飛んでから，コードを追加することが繰り返されました．
いわゆる「スパゲッティコード」です．
筆者も教科書では習いましたが，初めて見たのはChip8上でした．
Chip8はこのまま役割を終えるはずでしたが，90年代にHP製電卓上で復活します．
同時に動作させるマシン性能も向上しており，schip等の機能拡張がおこなわれました．
schipでは，画面の解像度が4倍になりました．
2000年代に入ると，ビデオゲームで遊びたいというよりも，プログラマの習作として，自分の環境で動作するChip8エミュレータが盛んに書かれるようになります．
筆者も最初はC++で，次はpythonで，そしてhaskellというように，3回書いています．
当然のように，javascriptで書く方もいて，webブラウザ上でもChip8が動くようになります．
そんな流れの中で，ニーモニックを古臭いアセンブラではなくて，少しC風の記法に変えて，ブラウザ上で動かせるOctoという実装[[4]](https://johnearnest.github.io/Octo/)が現れました．
筆者は，コロナ禍になり，偶然それを発見しました．
少し遊んでみると，とてもビデオゲームが作りやすく，はまっています．
また，Octoは，xo-chipという独自の拡張もしています．

最近の若い方は，こういった低レベルの技術に興味を持ちません．
スペインの大学は，Octoを使い低レベルに興味を持ってもらう取り組み[[5]](https://www.researchgate.net/publication/334415595_APPLICATIONS_OF_CHIP-8_A_VIRTUAL_MACHINE_FROM_THE_LATE_SEVENTIES_IN_CURRENT_DEGREES_IN_COMPUTER_ENGINEERING)を考案しているようです．
筆者が子供の頃は，ビデオゲームで遊びたい一心で，計算機のことを自然に学べてました．
が，最近の子供は，なかなか学ぶ機会がないのかもしれません．

### Octoとは

Chip8は非常に古いので，昔のアセンブリ言語の記法を使ってプログラミングされています．
OctoはAlgol系の記法を用いて，アセンブリ言語を記述しやすくしています．

#### Octo入門

それでは，簡単な例を見ながら，Octoについて説明していきます．

まず，pongのサンプルを動かしてみましょう．
右のURLを押してみてください．
cf. https://johnearnest.github.io/Octo/index.html?key=oHPV39w-

![](https://github.com/jay-kumogata/RetroGames/blob/main/octo/screenshots/pong04.png)

pongという古いゲームが動きます．
ボールが動き出しますね．
[1][Q]キーで左のパドルを動かします．
[4][R]キーで右のパドルを動かします．
パドルでボールを跳ね返します．
跳ね返せないと相手に点数が入ります．
左上と右上の数字が点数です．

左上の×を押してください．
謎のカラフルなコードが表示されましたか．
そして，左上の×を押すと，元の画面に戻ります．
はい．それだけのコードです．

コードの中身は説明せずに，もう一度動かしてみましょう．
左上にRunというボタンがありますので，それをクリックしてみてください．
そして，もう一度，左上の×を押すとコードに戻ります．

次に，コードを説明していきます．

	61 : main
	62   va := 2  # Set left player X coord.
	63   vb := 12 # Set left player Y coord.
	64   vc := 63 # Set right player X coord.
	65   vd := 12 # Set right player Y coord.

Octoでは，`: name`は，ラベルを意味します．
ラベルは，最終的には番地に変換されます．
Octoでは，`: main`は特別なラベルです．
コードは，ここを起点にして動作します．
Octoでは，`:=`はレジスタへの代入です．
Octoでは，`#`から改行までは，コメントです．

すなわち，このコードでは，
`va`レジスタに，左のプレイヤのX座標(初期値)を代入します．
`vb`レジスタに，左のプレイヤのY座標(初期値)を代入します．
`vc`レジスタに，右のプレイヤのX座標(初期値)を代入します．
`vd`レジスタに，右のプレイヤのY座標(初期値)を代入します．

	67   i := paddle    # Get address of paddle sprite
	68   sprite va vb 6 # Draw left paddle
	69   sprite vc vd 6 # Draw right paddle

次のコードをみてみましょう．
`i`レジスタは，16ビッドレジスタです．
Chip8のメモリ空間を全て指し示すことができます．
`i`レジスタに，パドルのスプライト(1x6ピクセル)の先頭アドレスを代入します．

Octoでは，Chip8のdraw命令を`sprite`と記述します．
`va`レジスタ,`vb`の位置に縦6ピクセル分(左パドル)を表示します．
`vc`レジスタ,`vd`の位置に縦6ピクセル分(右パドル)を表示します．

	71  ve := 0    # Set score to 00
	72  draw_score # Draw score

レジスタveに，初期スコア(00)をセットして，表示します．
左のプレイヤが1の位で，右のプレイヤが10の位に保存されます．
Octoでは，ラベルを直接書いた場合は，サブルーチンコールとなります．
ですので，`draw_score`と書くと，サブルーチン`draw_score`が呼び出されます．

	74   v6 := 3 # Set X coord. of ball to 3
	75   v8 := 2 # Set ball X direction to right

`v6`レジスタに，ボールのX座標(3)をセットします．
`v8`レジスタに，ボールのX方向(右)をセットします．

	77 : big_loop
	78   v0 := 0x60  # Set V0=delay before ball launch
	79   delay := v0 # Set delay timer to V0

`big_loop`は，このゲームのメインループです．
レジスタ`v0`に，ボール発射までの待ち時間(60)をセットします．
ディレイタイマーに，`v0`の値(60)をセットします．
ディレイタイマーは，1/60秒毎に1減じられます．

	81 : dt_loop
	82   v0 := delay                  # Read delay timer into V0
	83   if v0 != 0 then jump dt_loop # Read again delay timer if not 0

次に，レジスタ`v0`にディレイタイマーの値を代入します．
レジスタ`v0`が0でなければ，dt_loopに戻ります．
したがって，ディレイタイマーが0になるまで，待ちを発生されることができます．
ちなみに，1/60秒 x 60回 = 1秒間の待ちが発生します．
このような待ち方のことを，ビジーウェイト(busy wait)と呼びます．
何度もチェックするので，忙しい(busy)という意味です．

	85  v7 := random 23 # Set Y coord. to rand # AND 23 (0...23)
	86  v7 += 8         # And adjust it to is 8...31

`v7`レジスタには，ボールのY座標が代入されます．
`random`は，乱数を発生する命令に変換されます．
0から23までの乱数を発生させた上で，8を足すので，8から31までの乱数が発生します．

	88  v9 := 0xff      # Set ball Y direction to up
	89  i := ball       # Get address of ball sprite
	90  sprite v6 v7 1  # Draw ball

`v9`レジスタに，ボールのY軸方向の速度を代入します．
-1(0xff)なので，上方向に移動します．
`i`レジスタに，ボールのスプライトの先頭アドレスが代入します．
`v6`レジスタがX座標で，`v7`レジスタがY座標の位置に，ボールのスプライトを表示します．

	92 : padl_loop
	93   i := paddle    # Get address of paddle sprite
	94   sprite va vb 6 # Draw left paddle
	95   sprite vc vd 6 # Draw right paddle

`padl_loop`は，このゲームのサブループです．
`i`レジスタに，パドルのスプライトの先頭アドレスを代入します．
`va`レジスタがX座標で，`vb`レジスタがY座標の位置に，左パドルのスプライトを表示します．
`vc`レジスタがX座標で，`vd`レジスタがY座標の位置に，右パドルのスプライトを表示します．

	97   # Set V0 to KEY 1 and Subtract 2 from Y coord. of left paddle if KEY in 1 is pressed
	98   v0 := OCTO_KEY_1 if v0 key then vb += 0xfe 

`OCTO_KEY_1`は，あらかじめ定義された定数です．
`1`のキーコードが定義されています．
したがって，`v0`レジスタに`OCTO_KEY_1`が代入されます．
`v0 key`は，`v0`に代入されたキーコードのキー(ここでは，`1`キー)が押された場合は真(TRUE)で，押されていない場合は偽(FALSE)になります．
真の場合には，`vb`レジスタ(左パドルのY座標)が-2(0xfe)されます(2だけ減ります)．
結果として，左パドルの位置が，上に2ピクセル移動します．

	99   # Set V0 to KEY 4 and Add 2 to Y coord. of left paddle if KEY in 4 is pressed
	100   v0 := OCTO_KEY_Q if v0 key then vb += 2

このコードは前と同じです．
`Q`キーが押された場合には，左パドルの位置が，下に2ピクセル移動します．

	102   v0 := 31       # Set V0 to max Y coord.  | These three lines are here to
	103   vb &= v0       # AND VB with V0          | adjust the paddle position if
	104   sprite va vb 6 # Draw left paddle        | it is out of the screen

`v0`レジスタに，Y座標の最大値(31)を代入します．
`vb`レジスタ(左パドルのY座標)と論理積(AND)をとることで，左パドルが画面外に出た時の位置を補正します．
`vb`レジスタが32まで増加した時には，31と論理積(AND)をとることで，0に戻ります．

	106   # Set V0 to KEY C and Subtract 2 from Y coord. of right paddle if KEY in C is pressed
	107   v0 := OCTO_KEY_4 if v0 key then vd += 0xfe
	108   # Set V0 to KEY D and Add 2 to Y coord. of right paddle  if KEY in D is pressed 
	109   v0 := OCTO_KEY_R if v0 key then vd += 2

このコードも前と同じです．
`4`キーが押された場合には，右パドルの位置が，上に2ピクセル移動します．
`R`キーが押された場合には，右パドルの位置が，下に2ピクセル移動します．

	111   v0 := 31       # Set V0 to max Y coord.  | These three lines are here to
	112   vd &= v0       # AND VD with V0          | adjust the paddle position if
	113   sprite vc vd 6 # Draw right paddle       | it is out of the screen

このコードも前と同じです．
右パドルが画面外に出た時の位置を補正します．

	115   i := ball      # Get address of ball sprite
	116   sprite v6 v7 1 # Draw ball

ここからは，ボールの移動処理です．
`i`レジスタのボールのスプライトの先頭アドレスを代入します．
`v6`,`v7`レジスタの位置に，ボールを再表示します．
Chip8では，スプライトは排他的論理和(XOR)で表示されるため，再表示すると消去となります．

	118   v6 += v8  # Compute next X coord of the ball
	119   v7 += v9  # Compute next Y coord of the ball

`v6`レジスタ(ボールのX座標)に，`v8`レジスタ(ボールのX方向の速度)を足します．
`v7`レジスタ(ボールのY座標)に，`v9`レジスタ(ボールのY方向の速度)を足します．

	121   v0 := 63  # Set V0 to max X location
	122   v6 &= v0  # AND V6 with V0

`v0`レジスタに，X座標の最大値(63)を代入します．
`v6`レジスタ(ボールのX座標)と論理積(AND)をとることで，ボールが画面外(X座標)に出た時の位置を補正します．
`v6`レジスタが64まで増加した時には，63と論理積(AND)をとることで，0に戻ります．

	124   v1 := 31  # Set V1 to max Y location
	125   v7 &= v1  # AND V7 with V1

このコードは前と同じです．
ボールが画面外(Y座標)に出た時の位置を補正します．

	127   if v6 == 2  then jump left_side  # if ball at left
	128   if v6 == 63 then jump right_side # if ball at right

ボールがX座標の左端に到着した場合，`left_side`ラベルに移動します．
ボールがX座標の右端に到着した場合，`right_side`ラベルに移動します．

	130  : ball_loop
	131   if v7 == 31 then v9 := 0xff  #  Set Y direction to up if ball at bottom 
	132   if v7 == 0  then v9 := 1     # Set Y direction to down if ball at top
	133   sprite v6 v7 1               # Draw ball
	134   jump padl_loop               #

ボールがY座標の下端に到着した場合，`v9`レジスタ(ボールのY方向の速度)に-1(0xff)を代入します．
ボールがY座標の上端に到着した場合，`v9`レジスタ(ボールのY方向の速度)に+1を代入します．
新しい位置にボールを表示して，`padl_loop`ラベルに移動します．
	

#### 練習問題

ここまでの知識を使って，続きのコードを理解しましょう．

	136  : left_side
	137   v8 := 2       # Set X direction to right
	138   v3 := 1       # Set V3 to 1 in case left player misses ball
	139   v0 := v7      # Set V0 to V7 Y coord. of ball
	140   v0 -= vb      # Subtract position of paddle from ball
	141   jump pad_coll # Check for collision
	
	143  : right_side
	144   v8 := 254  # Set X direction to left
	145   v3 := 10   # Set V3 to 10 in case right player misses ball
	146   v0 := v7   # Set V0 to V7 Y coord. of ball
	147   v0 -= vd   # Subtract position of paddle from ball
	
	148  : pad_coll
	149   if vf != 1 then jump ball_lost # if ball above paddle
	 
	151   v1 := 2                       # Set V1 to 02
	152   v0 -= v1                      # Subtract V1 from V0
	153   if vf != 1 then jump ball_top # Ball at top of paddle if ball at top of paddle
	 
	155   v0 -= v1                      # Subtract another 2 from V0
	156   if vf != 1 then jump pad_hit  # Ball in middle of paddle if ball at middle of paddle
	 
	158   v0 -= v1                      # Subtract another 2 from V0
	159   if vf != 1 then jump ball_bot # Ball at bottom of paddle if ball at bottom of paddle
	
	161  : ball_lost
	162   v0 := 32      # Set lost ball beep delay
	163   buzzer := v0  # Beep for lost ball
	 
	164   draw_score # Erase previous score
	165   ve += v3   # Add 1 or 10 to score depending on V3
	166   draw_score # Write new score
	 
	168   v6 := 62                # Set ball X coord. to right side
	169   if v3 != 1 then v6 := 3 # Set ball X coord. to left side if left player got point
	170   v8 := 0xfe              # Set direction to left
	171   if v3 != 1 then v8 := 2 # Set direction to right  if left player got point
	172   jump big_loop           #
	 
	174  : ball_top
	175   v9 += 0xff                    # Subtract 1 from V9, ball Y direction 
	176   if v9 == 0xfe then v9 := 0xff # Set V9=FF (-1)  if V9 == FE (-2)
	177   jump pad_hit                  #

	179  : ball_bot
	180   v9 += 1                   # Add 1 to V9, ball Y direction
	181   if v9 == 2 then v9 := 1   # Set V9=01  if V9 == 02
	
	183  : pad_hit
	184   v0 := 4        # Set beep for paddle hit
	185   buzzer := v0   # Sound beep
	 
	187   v6 += 1                    #
	188   if v6 == 64 then v6 += 254 #
	189   jump ball_loop             #
	 
	191  : draw_score
	192   i := score     # Get address of Score
	193   bcd ve         # Stores in memory BCD representation of VE
	194   load v2        # Reads V0...V2 in memory, so the score
	195   i := hex v1    # I points to hex char in V1, so the 1st score char
	196   v4 := 0x14     # Set V4 to the X coord. to draw 1st score char
	197   v5 := 0        # Set V5 to the Y coord. to draw 1st score char
	198   sprite v4 v5 5 # Draw 8*5 sprite at (V4,V5) from M[I], so char V1
	199   v4 += 0x15     # Set X to the X coord. of 2nd score char
	200   i := hex v2    # I points to hex char in V2, so 2nd score char
	201   sprite v4 v5 5 # Draw 8*5 sprite at (V4,V5) from M[I], so char V2
	202   return         # Return

	204  : paddle
  	205   0x80 0x80 0x80 0x80 0x80 0x80
	
	207  : ball
	208   0x80 0x80
	
	210  : score
	211   0x00 0x00 0x00 0x00

### おわりに

この文書では，Octoという環境でChip8向けゲームを作る方法を説明しました．
この文章は，書きかけです．
今後加筆される可能性が高いです．

___

Copyright (c) 2021, 2022 Kumogata Jay. All Rights Reserved.