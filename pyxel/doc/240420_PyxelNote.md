## Pyxelによるゲーム開発記（2024年編）

### はじめに

レトロゲームエンジン [Pyxel](https://github.com/kitao/pyxel) によるゲーム開発の記録です．

### 2024-04-20

過去のゲーム開発記は，以下にあります．
- [アステロイド開発記（2021年編）](https://github.com/jay-kumogata/RetroGames/blob/main/haskell/doc/210427_AsteroidsNote.md)
- [Octo記法によるゲーム開発記（2021年編）](https://github.com/jay-kumogata/PyxelChip8/blob/main/games/doc/210307_OctoNote.md)
- [Octo記法によるゲーム開発記（2022年編）](https://github.com/jay-kumogata/PyxelChip8/blob/main/games/doc/220116_OctoNote.md)
- [Pyxelによるゲーム開発記（2022年編）](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/doc/220217_PyxelNote.md)
- [Pyxelによるゲーム開発記（2023年編）](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/doc/230409_PyxelNote.md)

### 2024-06-12

PyxelRogueの開発記を，[01_ゲーム製作: 01_ローグライク開発記](https://github.com/jay-kumogata/RetroGames/blob/main/research/01_01_RoguelikeNote.md)にまとめました．前半は，詩創作的なので，読み飛ばしてください．

### 2024-06-14

[オートレース(1画面ソフト)](https://github.com/jay-kumogata/RetroGames/tree/main/pyxel/autorace)を公開しました．
昔懐かしい[はるみのゲームライブラリ](https://archive.org/details/Fm-7Fm-8/page/n173/mode/2up)からの移植です．
PyxelRogueを開発(移植)する過程で蓄積された「キャラクタ画面の扱い方のノウハウ」を再利用してみました．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/autorace/screenshots/autorace01.gif)

### 2024-06-15

「40年前は，プログラミングしてる小中学生は，頭がおかしい子扱いされた」というが，正しいです．

### 2024-06-28

今週なぜか話題になっていた「メキシカンハット」を，Pyxelにも移植してみました．
おまけで，SuperChip8（128x64ピクセル，単色）だと，どんな感じになるかも，表示させてみました．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/sombrero/screenshots/sombrero01.png" width=320 />
<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/sombrero/screenshots/sombrero02.png" width=160 />
<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/sombrero/screenshots/sombrero03.png" width=128 />

[ソースコード](https://github.com/jay-kumogata/RetroGames/tree/main/pyxel/sombrero)も公開しています．

### 2024-06-29

「どんなに恐ろしい武器を持っても，たくさんの可哀想なロボットを操っても，Numpyから離れては生きられないのよ．」

### 2024-06-30

今週も雑務が多く，コードしたのは，メキシカンハットだけでした．来週も，BASICをPythonに移植します．

### 2024-07-07

フォルダをあさると，「なんでこんなもの作ったんだろう．」と思うものが，結構あります．
需要云々ではなく，「成仏」という意味で，GitHubにあげるのはよいことかもしれません．
牧草を食べる羊のプログラムの時は，シムアントに対抗して，シムタンポポというタンポポ畑育成ゲームを作ろうとしてたのでした．
綿毛が風に乗って，こう広まる感じです．
でも，なんかつまらないから，頓挫しました．

### 2024-07-08

図書館で「[Pythonではじめる数学の冒険―プログラミングで図解する代数，幾何学，三角関数](https://www.oreilly.co.jp/books/9784873119304/)」という本を借りてきました．
9章に掲載されていた「食事する羊のプログラム」を，Pyxelに移植してみました．
羊が牧草を食べながら移動するシミュレーションです．
食べる牧草がなくなると，天国へ召されてしまいます．
書籍の方では，子孫を残すロジックも紹介されていますが，興味を失ったので実装していません．

![](https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/sheep/screenshots/sheep01.gif)

### 2024-07-12

過去に開発した
[Asteroids in Haskell](https://github.com/jay-kumogata/RetroGames/tree/main/haskell/asteroids)
を，Pyxel/Pythonに移植してみることにしました．

<img src="https://github.com/jay-kumogata/RetroGames/raw/main/haskell/asteroids/screenshots/asteroids02.png" width="300" />

### 2024-07-13

Asteroids開発の続報です．本日の進捗は，以下の通りです．

- Vecクラス(旧PointInSpaceクラス)を実装
- Rockクラスを実装

### 2024-07-14

Asteroids開発の続報です．本日の進捗は，以下の通りです．

- Shipクラスを実装
- Bulletクラスを実装
- Asteroidsクラスを実装(未完了)

### 2024-07-20

Asteroids開発の続報です．本日の進捗は，以下の通りです．

- Asteroidsクラスを実装(未完了)
  - 弾発射処理
  - 岩分裂処理

### 2024-07-21

Asteroids開発の続報です．本日の進捗は，以下の通りです．

- Asteroidsクラスを実装(未完了)
  - 自機当り判定処理
  - ゲームオーバー処理

### 2024-07-25


Haskellみたいな関数型は，関数適用が多く，コードが横長になり，Pythonみたいな逐次型は，コードが縦長になる傾向があります．

### 2024-07-27

Asteroids開発の続報です．本日の進捗は，以下の通りです．

- Asteroidsクラスを実装
  - 点数表示処理

### 2024-08-27

PyxelでPyxapp形式に固めて実行する方法は分かりました．
けど，Numpyとか使ってると実行時エラーになります．NumpyもWebAssemblyで与えないと駄目なのですが，やり方がわからないから諦めます．

### 2024-08-31

試行錯誤の結果，5タイトルはブラウザ内で遊べるようになりました．

- [Pinball](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.RetroGames.pyxel.pinball.Pinball)
- [ACLM](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.RetroGames.pyxel.aclm.aclm)
- [Nixie](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.RetroGames.pyxel.nixie.Nixie)
- [Hanafuda](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.RetroGames.pyxel.hanafuda.hanafuda)
- [Sombrero](https://kitao.github.io/pyxel/wasm/launcher/?run=jay-kumogata.RetroGames.pyxel.sombrero.sombrero&packages=numpy)

Numplyについては，ランチャーのURLにパラメータで与えられることが分かりました．
ただ，Pyodideに含まれたパッケージに限ります．

### 2024-09-01

Pyxapp形式に固めて，Numpyを使う方法が分かりました．マニュアルに書いてありました．ただ，Pyodideに含まれてるライブラリだけみたいです．
当然といえば当然です．ただ，ソースリストが，複数ファイルにまたがってると，うまくいきません．今日は諦めることにしました．

### 2024-09-02

Asteroids開発の続報です．本日の進捗は，以下の通りです．

- コメントを修正
- Asteroidsクラスを修正
  - 弾を撃ったら，自機も動くように変更(作用反作用の法則)

### 2024-09-23

Asteroids開発の続報です．ビデオゲームとしては，一旦完成です．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/asteroids/screenshots/asteroids01.gif" width=320 />

### 2024-09-28

Pinballの開発記を，[01_ゲーム製作: 02_ピンボール開発記](https://github.com/jay-kumogata/RetroGames/blob/main/research/01_02_PinballNote.md)にまとめました．

### 2024-09-29

今年は，子供の頃から作りたかったピンボールとローグライクを作ったので，残りは縦シューティングかなと考えています．
作り方は大体わかってるのですが，気分が上がらずに作れていません．

### 2024-11-07

子供向けに，Pyxel はいいと思います．Python の勉強できますし，AI戦士を育てる意味でも.

### 2024-12-24

PyxelもNintendo Switchで動くといいのかもしれません．

### 2024-12-25

秋頃に，Haskellで書いたAsteroidsを，Pyxel/Pythonに移植しました．
Githubの方には，[ソースコード](https://github.com/jay-kumogata/RetroGames/tree/main/pyxel/asteroids)を公開しましたが，Xには投稿していませんでした．
Haskellでは関数適用を繰り返す処理も，Pythonだと逐次的な処理になり，楽しい移植作業でした．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/asteroids/screenshots/asteroids01.gif" width=320 />

以上
