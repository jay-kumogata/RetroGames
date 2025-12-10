# 01_ゲーム製作: 01_ローグライク開発記

##  ローグライク開発記（2024年編）

_(2025-04-13) 2024年編は，ローグライクチュートリアルをPyxelに移植した話です．_

### 2024-05-07

コロナ前にチョコボの不思議なダンジョン2をクリアしてから，何度かローグライクを作ろうとしましたが，その都度，挫折しました． 
TCODライブラリを使った[ローグライクチュートリアル](https://rogueliketutorials.com/tutorials/tcod/v2/)を発見したので，
Pyxelライブラリに移植しながら，勉強してみようかな．

### 2024-05-08

ローグライクチュートリアルの[Part0](https://rogueliketutorials.com/tutorials/tcod/v2/part-0/)と[Part1](https://rogueliketutorials.com/tutorials/tcod/v2/part-1/)をPyxelへ移植しました．
画面上でプレイヤーを動かせるようになりました．画面表示とキー入力以外は，TCOD版のコードを流用することにしました． TCOD版では，キャラクタ('@')が表示されますが，Pyxel版では，暫定的にピクセルを表示しています．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelrogue/screenshots/pyxelrogue01.gif" width="360">

### 2024-05-12

ローグライクチュートリアルの[Part2](https://rogueliketutorials.com/tutorials/tcod/v2/part-2/)をPyxelへ移植しました．壁と床を使って，マップを実装しました．プレイヤー(白色)は，床(水色)の上は歩けるのですが，壁(青色)にぶつかると先に進めません．次は，ダンジョンを自動生成していきます．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelrogue/screenshots/pyxelrogue02.gif" width="360">

### 2024-05-17

ローグライクチュートリアルの[Part3](https://rogueliketutorials.com/tutorials/tcod/v2/part-3/)をPyxelへ移植しました．ダンジョンが自動生成されるようになりました．TCODライブラリに含まれるブレゼンハムのアルゴリズム(近似的に直線を引くアルゴリズム)を使って，部屋間の通路を描いています．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelrogue/screenshots/pyxelrogue03.gif" width="360">

### 2024-05-18

ローグライクチュートリアルの[Part4](https://rogueliketutorials.com/tutorials/tcod/v2/part-4/)をPyxelへ移植しました．自分の周辺だけが明るくなり，よく見えるという演出を追加しました． この演出も，TCODライブラリに含まれている機能を使っています． TCODライブラリには，ローグライクを作る上で便利な機能が揃っているようです．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelrogue/screenshots/pyxelrogue04.gif" width="360">

### 2024-05-24

ローグライクチュートリアルの[Part5](https://rogueliketutorials.com/tutorials/tcod/v2/part-5/)をPyxelへ移植しました．オークとトロールが，敵として登場するようになりました．ただ，今の時点では，登場するだけで，まだ動きません．次は，敵の移動と近接攻撃について，実装していきます．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelrogue/screenshots/pyxelrogue05.gif" width="360">

### 2024-05-25

ローグライクチュートリアルの[Part6](https://rogueliketutorials.com/tutorials/tcod/v2/part-6/)をPyxelへ移植しました．オークやトロール等の敵が，移動するようになりました．敵に近接攻撃すると，敵が死ぬ(紫色に変化する)ようになりました．ピクセルでの表示が限界を迎えたので，次は，キャラクタ(4x5ピクセル)での表示を実装していきます．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelrogue/screenshots/pyxelrogue06.gif" width="360">

### 2024-05-26

ローグライクチュートリアルの[Part7](https://rogueliketutorials.com/tutorials/tcod/v2/part-7/)をPyxelへ移植しました．ピクセル表示から，キャラクタ表示(4x5ピクセル)に変更しました．下の方に，HPとメッセージが表示されるようになりました．また，メッセージログの窓を開くことで，過去のメッセージも確認できます．今週はここまでです．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelrogue/screenshots/pyxelrogue07.gif" width="360">

### 2024-05-31

ローグライクチュートリアルの[Part8](https://rogueliketutorials.com/tutorials/tcod/v2/part-8/)をPyxelへ移植しました．ダンジョンにアイテムが配置されるようになりました．プレイヤ('@')は，アイテムを拾ったり，捨てたり，アイテムの窓を開いて，使ったりできます．例えば，ポーション('!')を拾って，使うとHPが回復します．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelrogue/screenshots/pyxelrogue08.gif" width="360">

### 2024-06-01

ローグライクチュートリアルの[Part9](https://rogueliketutorials.com/tutorials/tcod/v2/part-9/)をPyxelへ移植しました．アイテムとして，巻物('~')が使えるようになりました．混乱の巻物，光の巻物，火の玉の巻物が追加されました．火の玉の巻物を使うと，指定した範囲内の敵にダメージを与えることができます．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelrogue/screenshots/pyxelrogue09.gif" width="360">

### 2024-06-02

ローグライクチュートリアルの[Part10](https://rogueliketutorials.com/tutorials/tcod/v2/part-10/)をPyxelへ移植しました．セーブ機能とロード機能を実装しました．ゲームを途中で終了させると，自動的にセーブされます．タイトル画面で，「続きから」を選択すると，ゲームがロードされて，続きから遊べます．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelrogue/screenshots/pyxelrogue10.gif" width="360">

### 2024-06-03

最近ローグライクのソースリストを読んでますが，何度も設計を繰り返したんだろうなという感じがします．
欧州の古い建造物を見たような，なんか尊さすら感じるレベルです．
おそらく，最初のローグの設計が良かったんだろうなとも考えています．
月まで言っていたのですから，70年代の米国のレベルは高かったんでしょう．

私は学校には通ったのですが，プログラミングはほぼ独学でした．
プログラミングの学習で，最も役立ったのは，他の人が書いたソースを読むことでした．
フレンチのシェフが，皿に残ったソースを舐めて，味を学ぶという話がありますが，
プログラミングでも，そういうことがあるかもしれません．
ただ，今は，正しく教育がされているのでしょう．
当時は，Turbo Pascalでした．

### 2024-06-07

ローグライクチュートリアルの[Part11](https://rogueliketutorials.com/tutorials/tcod/v2/part-11/)をPyxelへ移植しました．ダンジョンに階段（'>'）を追加しました． 階段を降りると，新しいダンジョンが現れます．この仕掛けで，無限に遊べるゲームの完成です．なお，タイトルは，PyxelRogueに変更しました．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelrogue/screenshots/pyxelrogue11.gif" width="360">

### 2024-06-08

ローグライクチュートリアルの[Part12](https://rogueliketutorials.com/tutorials/tcod/v2/part-12/)をPyxelへ移植しました．
ダンジョンの下の階に行くほど，難しくなるように調整しました．
具体的には，アイテムが少なくなり，敵がたくさん出てきます．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelrogue/screenshots/pyxelrogue12.gif" width="360">

### 2024-06-09

ローグライクチュートリアルの[Part13](https://rogueliketutorials.com/tutorials/tcod/v2/part-13/)をPyxelへ移植しました．
ダンジョンに剣と鎧が配置されるようになりました．
剣と鎧を装備すると，攻撃と防御が上昇するようになりました．
チュートリアルもこれで完了ですが，引き続き改造していく予定です．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/pyxelrogue/screenshots/pyxelrogue13.gif" width="360">

### 2024-06-10

RoguelikeからPyxelRogueにタイトルを変更しました．
[リポジトリ名](https://github.com/jay-kumogata/RetroGames/tree/main/pyxel/pyxelrogue)にも反映しました．
元々の計画では，キャラクタのサイズや色を変更していく予定でした．
が，少し飽きたので，別プロジェクトをはじめたいと考えています．
___
