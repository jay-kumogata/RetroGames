# 01_ゲーム製作: 01_ローグライク開発記

##  ローグライク開発記（2021年編）

つぶやきながら，ローグライクを開発する日記です．
現時点で，まだ何もできていません．

_(2025-04-13) 2021年編は，アマビエを主役にしてローグライクを開発しようと試みて，断念するまでの話です．_

### 2021-04-23

シューティングは，これまで何度か作ったことがあります．
ローグライクは，作ったことがないので，作ってみることにしました．
主人公は，アマビエです．
舞台は，海の中です．
世界中のマーマンやマーメイドに出会うストーリーにします．
アリエルとかも登場させるかもしれません．

### 2021-05-08

- プロジェクト案
  - ローグライク開発(チョコダン2で盛り上がる / pythonで実装した書籍あり / 興味を失ったので放置)
  - チョコダン2 → ローグライク
- 参考
  - [ローグライクを作ったので開発手順をまとめてみた](https://qiita.com/2dgames_jp/items/1730e7c4822091c3c320)
  - [インディーズゲームの小部屋：Room＃48「Elona」](https://www.4gamer.net/games/040/G004096/20080627031/)
  - [ローグ型RPGを作る「デバッグではじめるCプログラミング」](http://blog.lv99.com/?eid=799310)

### 2021-05-13

ビデオゲームには，神話がモチーフになるものことを多いです．
ヤマタノオロチも時々登場します．
そう考えると，我々が作っているビデオゲームは，先人達の知恵や文化的な背景に影響を受けるのかなと思います．
アマビエを主人公にしたRPGを構想していて，世界中の人魚が登場するストーリーはどうかなと思います．

### 2021-05-19

図書館で人魚の文化史の本を借りてきました．
2冊です．
少し読み始めたのですが，マーメイド(女性)，マーマン(男性)だけでなく，トリトンも人魚の仲間と知りました．
人魚が出てきたゲームを調べることから始めようかなと思いついたのですが，作業はできていないです．
チョコダン2にも，3種類(色違い)がでてきます．

### 2021-05-20

お散歩中に考えたことのメモです．
まず，ゲームを作りはじめるまえにストーリー(お話)を組み立てみることにしました．
xeviousもシューティングを開発する前に，ストーリーを考えています．

- タイトル: アマビエ2 
  - 前作アマビエは，疫病退散させるシューティングアクション
  - Octo環境で開発
- ジャンル: ローグライク
  - 純粋なローグライクではなく，セーブありのRGB風ローグライク
  - チョコダン2と同じ想定
- ストーリー:
  - 主題は，アマビエの自分探しの旅．最後には，自分は人魚の仲間ということを知る
  - アマビエは，疫病退散のヒーローになり，日本中でちやほやされる
  - 自分が何者なのかを知りたくなり，世界中を旅することにした
  - 5大陸で，それぞれ人魚の友達に出会い，彼らの課題を解決して，成長していく
  - 5大陸にどんな人魚がいるのかは，これから調べる
  - 課題は適当に考える
  - 水戸黄門みたいに，悪い敵が出てきて，それをダンジョンでやっつけていくというのが，典型的な流れだろう
  - どんな悪い奴が出てくるのか，友達がどう困っているのかを考える

### 2021-05-21

明日からは，それそれの大陸でのストーリーを考えます．

- 大陸:
- 人魚:
- エピソード:

### 2021-05-23

- 大陸: アジア
- 人魚: メカアマビエ
- エピソード: 
  - ウィルスを生物兵器として世界中に広めようとしている悪の組織がいる
  - アマビエが悪霊退散でウィルスを退治していくのが目障りとなる
  - アマビエを倒すために，メカアマビエを作り，アマビエをダンジョンにおびき寄せる
  - ダンジョンクリアして，最後のボス(メカアマビエ)を倒すまでのストーリー
  - それでも，アマビエと悪の組織との闘いは続く

(参考文献)

- [1] ヴォーンス・クリブナー(川副智子, 肱岡千泰訳): 人魚の文化史 神話・科学・マーメイド伝説, 原書房 (2021-2).
- [2] 篠田知和基: 世界魚類神話, 八坂書房 (2019-6). 

### 2021-06-07

- 大陸:アメリカ
- 人魚:歌姫2匹(arena and selena)
- エピソード:
  - arenaは恋人に捨てられて自殺未遂をする．
  - selenaは男を利用してどんどん有名になる．
  - アマビエはarenaの手助けをして，彼女がまた歌姫として活躍できるのを支援する．
  - selenaをダンジョンに追い詰めて，ダンジョン最後にselenaを倒すまでのストーリー．
- 余談:
  - 雲型計算研究所のプロジェクトペーパーを作る
  - これまでの資料を流し込んで，当時の資料風のものを作ってみる(レトロ偽装)

### 2021-06-08

- エピソード:
  - 昨日案だと，単にarenaがselenaに逆恨みになるので，少し手直し
  - arenaとselenaは幼馴染で仲が良かった
  - selenaがarenaの歌の才能に嫉妬して，arenaの恋人をそそのかして，arenaを再起不能に
  - selenaは，歌姫の座をほしいままに
  - アマビエは，arenaの手助けをして，彼女がまた歌姫として活躍できるのを支援する．
  - selenaをダンジョンに追い詰めて，ダンジョン最後にselenaを倒すまでのストーリー．

### 2022-01-07

ゲーム製作で，GitHubの方に上がっていないのは，これだけになってしまいました．
完成するあては，ほぼほぼないのですが，未完成でもGitHubに上げて終わりにしてしまうのがよいかなと思います．

### 2022-01-08

この時期，コロナ自粛ということで家にこもることが多かったです．
チョコボの不思議のダンジョン2を家でプレイしていたこともあり，ローグライクを作ってみたくなったのだと思います．
同じ時期に，アステロイドを作っており，そちらは見事に完成しています．
が，こちらはストーリーすら完成できずに終わってしまっています．

- 大陸:ヨーロッパ
- 人魚:
- エピソード:

### 2022-02-02

今週先週はゲームを作ることよりも，ゲームを買うことに興味が湧いていました．
ローグライクを作ろうと思ったのですが，やる気出ず，2度目の断念です．
ローグライクを作ることは，案外労働集約的な作業であることを知りました．
システム全体のデータ構造定義，自動生成ロジック，主人公の移動とアクション，敵のAI設計，色々あります．
とりあえず，理解したことにして，先に進みます．

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
