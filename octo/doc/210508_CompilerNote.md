## 関数型言語の翻訳系研究記

### 2021-05-08

プロジェクト案
- Octo記法への射影
  - 関数型言語の簡単な翻訳系が出力する中間コードをOcto記法に変換

### 2021-05-09

昨日の夜，昔読んだプログラミングHaskellという本の17章に説明されていた簡単な翻訳系を思い出しました．Githubに[コード片](https://github.com/singleheart/programming-in-haskell/blob/master/ch17/compiler.hs)があったので，動かしてみることにしました．

例えば，

	> stack ghci
	> :l compiler.hs
	> eval (Val 1)
	1

となります．evalは評価系なので，(Val 1) :: Exprを渡すと，1を返します．

	> eval (Add (Val 1) (Val 3))
	4

加算もできます．1+3=4を表しています．ここでは，Expr型の木構造から開始していますが，前処理として構文解析系が存在して，

	1 + 3

を

	(Add (Val 1) (Val 3)) :: Expr

には変換することを前提にしています（過去に読んだ東北大学住井先生の解説には，そのような記載がありました）．

いよいよ本題です．これを翻訳系に喰わせてみると，

	> comp  (Add (Val 1) (Val 3))
	PUSH 1 (PUSH 3 (ADD HALT))

という機械語が生成されます．PUSHはスタックに値を積む命令，ADDはスタックから2つ値をPOPして加算してスタックに積む命令，HALTは終了する命令です．

つまり，スタックは，

	[]	PUSH 1
	[1]	PUSH 3
	[3 1]	ADD
	[4]	HALT

というように変化する想定です(スタックの説明をするときに，必ずカフェテリアのトレイの話が使われていましたが，今でも同じ説明をしているのでしょうか)．

最後に実行系で機械語を動かしてみると，

	> exec (PUSH 1 (PUSH 3 (ADD HALT))) []
	[4]

となり，めでたしめでたしとなります．関数型言語を実用するかはともかく，仮想マシンを理解するサンプルとしては結構よい例題だと思います．実行系は，スタックマシンを想定していますが，レジスタマシンの場合は，後処理でスタックトップをレジスタに割り付ける最適化を施すと高速化できます．バローズB5000でも，同様の最適化が導入されています．

今日は眠いので休みます．

### 2021-05-10

夜になり，Chip8命令への変換系を書きました．コードはgithubの方に後日あげますが，宣言としては下記の通りです．

	code2chip' :: Code -> Int -> ChipCode

スタックマシン用コード(Code)と利用可能な先頭のレジスタno.を渡すと，Chip8命令のコードを出力します．例えば，

	> code2chip' (PUSH 1 (PUSH 3 (ADD HALT))) 0
	LDR (Reg 0) (Imm 1) (LDR (Reg 1) (Imm 3) (ADR (Reg 0) (Reg 1) (EXIT (Reg 0))))

というように変換されます．LDRはロード(レジスタ)命令，ADRは加算(レジスタ)命令．(Reg 0)は，レジスタv0，(Imm 1)は，直値(1)を表しています．

最終的には，Octo記法を出力するコードを書けば，

	v0 := 1
	v1 := 3
	v0 += v1
	exit (計算結果はv0に)

というOcto記法のコードを出力できます．

【補足】 Chip8にはスタックはあるのですが，リターンアドレスだけです(データスタックは存在しない)．ここでは，スタックをレジスタ(v0~ve)で代用しています．

### 2021-05-11

関数型言語の翻訳系と，Chip8命令への変換系について，いろいろつぶやきましたが，tweetの方は消して，[wiki](https://github.com/jay-kumogata/Nostalgia/wiki/210508_CompilerNote)にまとめました．

変換系コードも載せておきました．コーディングは運動不足になるので，しばらくお休みです．

【参考】変換系コード(compiler.hsに追記)

	-- Chip8命令への変換系
	  
	data Op
	  = Imm Int
	  | Reg Int
	  deriving (Show)
	
	data ChipCode
	  = EXIT Op
	  | LDR Op Op ChipCode
	  | ADR Op Op ChipCode
	  deriving (Show)

	code2chip' :: Code -> Int -> ChipCode
	code2chip' HALT r = EXIT (Reg (r-1))
	code2chip' (PUSH n c) r = (LDR (Reg r) (Imm n) (code2chip' c (r+1)))
	code2chip' (ADD c) r = (ADR (Reg (r-2)) (Reg (r-1)) (code2chip' c (r-1)))

### 2021-05-12

昨日の夜（今日の朝）に，Chip8命令のコードをOcto記法で出力する出力系を書きました．コードはgithubの方に後日あげますが，宣言としては下記の通りです．

	chip2octo :: ChipCode -> [String]

Chip8命令のコードを入力すると，Chip8命令(Octa記法)のコード(Stringリスト)を返却します．例えば，

	> chip2octo (LDR (Reg 0) (Imm 1) (LDR (Reg 1) (Imm 3) (ADR (Reg 0) (Reg 1) (EXIT (Reg 0)))))
	["v0 := 1","v1 := 3","v0 += v1","exit"]

というように変換されます．Octo記法では，":="は代入を，"+="は加算をそれぞれ表しています．そして，最後に，

	> mapM_ putStrLn ["v0 := 1","v1 := 3","v0 += v1","exit"]
	v0 := 1
	v1 := 3
	v0 += v1
	exit

というようにOcto記法のコードが出力されます．ちなみに，putStrLnの型は，

	> :t putStrLn
	putStrLn :: String -> IO ()

なので，mapではなくて，mapM_を使います（Haskellは難しい言語ですね）．

mapとmapM_の型を比較して，理解をすすめてください．
MapM_は，副作用(文字列印字等)だけに意味があり，結果には意味がありません（IO ()等が返却されるだけです）．

	> :t map
	map :: (a -> b) -> [a] -> [b]
	> :t mapM_
	mapM_ :: (Foldable t, Monad m) => (a -> m b) -> t a -> m ()

これまでの成果をまとめると，

	> mapM_ putStrLn (chip2octo (code2chip' (comp (Add (Val 3) (Val 1))) 0))
	v0 := 3
	v1 := 1
	v0 += v1
	exit

という翻訳系が作れます．ただ，code2chip'の宣言を，

	code2chip' ::  Int -> Code -> ChipCode

にすると，関数合成(.)でもう少しエレガントにかけるかもしれないです．

【参考】出力系コード(compiler.hsに追記)

	-- Octo記法の出力系
	
	tostr :: Op -> String
	tostr (Imm n) = show n
	tostr (Reg n) = "v" ++ (show n)
	
	chip2octo :: ChipCode -> [String]
	chip2octo (EXIT op) = [ "exit" ]
	chip2octo (LDR op1 op2 oc)
	  = [ (tostr op1) ++ " := " ++ (tostr op2) ] ++ (chip2octo oc)
	chip2octo (ADR op1 op2 oc)
	  = [ (tostr op1) ++ " += " ++ (tostr op2) ] ++ (chip2octo oc)

### 2021-05-13

昨日，関数合成(.)を使うとエレガントに書けるといいましたので，少しやってみました．まず，

	code2chip :: Code -> ChipCode
	code2chip c = code2chip' c 0

という関数を定義します．すると，

	> ((mapM_ putStrLn) . chip2octo . code2chip . comp) (Add (Val 3) (Val 1))
	v0 := 3
	v1 := 1
	v0 += v1
	exit

というような書き方ができます．UNIXのpipe(|)のように使えます．また，

	> mario = (mapM_ putStrLn) . chip2octo . code2chip . comp
	> mario (Add (Val 3) (Val 1))
	v0 := 3
	v1 := 1
	v0 += v1
	exit

というように，1関数（関数名に意味はありません）としても，定義できます．

Haskell言語のさして広くはない応用分野として，今回紹介した言語処理系があります．私が楽しみで書いているような仮想機械を書くのには，あまり適さないです．チューリング機械もラムダ代数も，計算できることに違いはなので，あとは書きやすい言語を選べばいいんでしょうけど(原理原則としては)．ただ，自然言語と同様にプログラミング言語にも習得コストがかかるので，既存の言語に似た記法で新しい概念を詰め込んで，生産性を高めることを，言語開発者の方々はされているのだろうと想像します．そういった意味では，言語開発者の方々を，とても尊敬します．

### 2021-05-19

[関数型言語の翻訳系研究記](https://github.com/jay-kumogata/Nostalgia/wiki/210508_CompilerNote)の日本語を少し直しました．ですます調に統一しました．mapとmapM_の型を追記しました．

### 2022-01-06

関数名を理解しやすいように変更しました．また，用語も統一しました．

以上