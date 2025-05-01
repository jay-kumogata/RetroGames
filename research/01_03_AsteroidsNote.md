# 01_ゲーム製作: 03_アステロイド開発記

つぶやきながら，アステロイドを開発する記録です．

## アステロイド開発記(2024年編)

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

### 2024-09-02

Asteroids開発の続報です．本日の進捗は，以下の通りです．

- コメントを修正
- Asteroidsクラスを修正
  - 弾を撃ったら，自機も動くように変更(作用反作用の法則)

### 2024-09-23

Asteroids開発の続報です．ビデオゲームとしては，一旦完成です．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/asteroids/screenshots/asteroids01.gif" width=320 />

### 2024-12-25

秋頃に，Haskellで書いたAsteroidsを，Pyxel/Pythonに移植しました．
Githubの方には，[ソースコード](https://github.com/jay-kumogata/RetroGames/tree/main/pyxel/asteroids)を公開しましたが，Xには投稿していませんでした．
Haskellでは関数適用を繰り返す処理も，Pythonだと逐次的な処理になり，楽しい移植作業でした．

<img src="https://github.com/jay-kumogata/RetroGames/blob/main/pyxel/asteroids/screenshots/asteroids01.gif" width=320 />

以上
