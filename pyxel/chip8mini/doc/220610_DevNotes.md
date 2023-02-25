## Chip8 Mini開発記

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

### 2022-08-07

Chip8Miniの第5弾として，今週はネオン管を使った筐体デザインを考えてみました．
80年代後半のビアバーに飾ってあったようなネオンサインをイメージしています．
この物質的な発展が無限に続くような，そんな楽観的な空気感が伝わるように描きました．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/chip8mini/screenshots/Neon01.gif)

以上