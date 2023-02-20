___

## アステロイド開発記

つぶやきながら，アステロイドを開発する記録です．

### 2021-04-27

数式でゲームが作れるのか，という不思議な問いを思いつきました．そういえば，過去にアステロイドという古いゲームのhaskell実装を調査したことがありました．隕石の形を少し改良して，そのまま放置しています．今週は，この話題を，privateではやろうかなと考えています．そして，また飽きたら放置します．

### 2021-04-28

自機が円だったので三角形に変更しました．ミサイル発射と同時に向きを変えるように改造しました．prelude.atan2を使うとなぜかうまくいきました．点数はダミーで表示しています．monadchip8と違いmonadを使わないpureなasteroid実装です．数式というか，経過時間に応じて状態が変化するシミュレータという感じでしょうか．

![](https://github.com/jay-kumogata/RetroGames/blob/main/haskell/asteroids/screenshots/asteroids01.png)

### 2021-04-29

emacs環境を整えて，haskell modeを最新化しました．.emacs.d/init.elにいろいろ書いて使いやすくしました．これで結構時間を使ったので，続きはまた明日かなと考えています．

ダミー表示だった点数はちゃんと表示するようにしました．ただ，ミサイルを撃つ度に点数が増えるロジックにしたので，どんどん点数が増える変なゲームになりました．

![](https://github.com/jay-kumogata/RetroGames/blob/main/haskell/asteroids/screenshots/asteroids02.png)

### 2021-04-30

Atari社Asteroidsのhaskell実装の続きです．点数ロジックを追加，隕石を分裂させたら100点，消滅させたら500点にしてみました．何もないよりも，点数が増える方がやる気が出ることが分かりました．IOモナドを使わなと副作用が書けなくて，結局同じことを2度も3度も書くことになります．haskellには，IOモナドが必須かなと考えています．

### 2021-05-01

純粋関数型で状態遷移を記載しようとすると，

	next_state1,...,n = now_state1,...,n
	where
	  next_state1 = update_state1 ( now_state1 )
	  ...
	  next_staten = update_staten ( now_staten )

みたいになって，同じよう更新処理(update_state1,...,n)を何度も書かないといけません．

具体的には，

- 次の状態での隕石を計算するロジック
- 次の状態での点数を計算するロジック

が，ほぼ同じなのですが，一緒には記載できませんでした．計算を
- ラムダ計算と捉えるか，
- チューリング機械と捉えるかで，

直感的な記述が違うのだろうなといつも思うわけです．数式で考える人にいいのかなと考えています．

【参考】Atari Asteroids 関連情報
- [Golden age of arcade video games](https://en.wikipedia.org/wiki/Golden_age_of_arcade_video_games)
- [Atari Asteroids](https://t-lcarchive.org/atari-asteroids/)
- [Atari Asteroids: Creating a Vector Arcade Classic](https://arcadeblogger.com/2018/10/24/atari-asteroids-creating-a-vector-arcade-classic/)

### 2021-05-02

真夜中に目が覚めてしまったので，少しウォーキングをしました．9月まではコードを書くのをやめることにしました（禁コーディングです）．ということで，ここまでの[成果](https://github.com/jay-kumogata/RetroGames/tree/main/haskell/asteroids)をgithubに上げました．[アステロイド開発記](https://github.com/jay-kumogata/RetroGames/blob/main/doc/210427_AsteroidsNote.md)もwikiに上げました．そして，ステイホーム連休もDAY2になりました．

### 2021-05-03

ステイホーム連休DAY3です．昨日は1日中寝てしまいました．1990年代後半に，NY観光したことがあり，1日だけ大雪が嵐のようになって，仕方ないのでホテルで1日寝てたことを思い出しました．1泊200ドルぐらいだったから，もったいなかったけど，いい思い出かもしれません．その時も疲れたんだけど，1日寝たら元気になりました．

### 2021-05-04

ステイホーム連休DAY4です．動かし方を書いておきますね．

	> (gitの方から適当にdownload / cloneします)
	> stack install gloss
	> stack ghc Asteroids.hs
	> ./Asteroids.exe

左クリックで弾を撃って，隕石を分裂させていきましょう．小さな隕石は消滅させられます．隕石にあたるとゲームオーバー．右クリックでリプレイです．

### 2021-05-08

プロジェクト案
- Asteroids開発: 無事に公開できたので，プロジェクトとしては成就です

### 2021-05-20

日本語を少し直しました．ですます調に統一しました．

### 2021-08-28

アステロイド（アタリ社 / 1979年）のHaskell実装を少し改良しました．ゲーム黎明期の全方位シューティングです．クリックした方向にミサイルを発射して，隕石を分裂・消滅させていきます．隕石を分裂させたら100点，消滅させたら500点です．#アタリ #アステロイド #Haskell cf. https://github.com/jay-kumogata/RetroGames/tree/main/haskell/asteroids

![](https://github.com/jay-kumogata/RetroGames/blob/main/haskell/asteroids/screenshots/asteroids00.png)

___
Copyright (c) 2021 Kumogata Jay. All Rights Reserved.
