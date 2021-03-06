# py-state-machine-practice

状態遷移マシンの練習（＾～＾）

* 📖 [Lesson01](./lesson01) - 果物（状態, State）を差し替えることで、せりふ（振る舞い, Behavior）が変わる理屈を習得してください
* 📖 [Lesson01-2](./lesson01n2) - Lesson01 で `🍎 Refreshing!` のように表示しましたが、このメッセージの部分を後から変えれるように **変数** を使う事を覚えてください
* 📖 [Lesson02](./lesson02) - 果物（State）オブジェクトを予めディクショナリーに追加しておき、使う時にキー（Key）を指定することで差し替えることができる理屈を習得してください
* 📖 [Lesson02-2](./lesson02n2) - Lesson02 で、後から変えられなかった本文を、後から変えられるようにしてみましょう。 **ラムダ式** を使えばできます
* 📖 [Lesson03](./lesson03) - キー（Key）をリストで並べると、まるでプログラムのシーケンス実行になるという理屈を習得してください
* 📖 [Lesson04](./lesson04) - ノード（Node）をつなげるとグラフ（Graph）になるという理屈を習得してください
* 📖 [Lesson05](./lesson05) - 振る舞い（Behavior）を持たせるという感覚を習得してください
* 📖 [Lesson06](./lesson06) - １つ前のノードの振る舞い（Behavior）によって、その後ろのノードが振る舞いを 変える（非マルコフ連鎖）という感覚を習得してください
* 📖 Lesson07-1 - 削除
* 📖 [Lesson07-2](./lesson07n2) - 前回の lesson7-1 の改良版です
* 📖 [Lesson08](./lesson08) - これから練習でよく使うことになるサーバーを作るための練習用のサンプルです
* 📖 [Lesson09](./lesson09) - サーバーに文字列を送るアプリケーションのサンプルです
* 📖 [Lesson10](./lesson10) - 数字を受け取ると、大きいと `Too Big`、小さいと `Too Small`、 ちょうどいいなら `Just Right` を返してくるサーバーです
* 📖 [Lesson11](./lesson11) - 状態を持つサーバーの練習用のサンプルです
* 📖 [Lesson11-2](./lesson11n2) - 状態の数だけ if 文を書いていたところを、 ステート（State）デザインパターンで書き直す練習用のサンプルです
* 📖 [Lesson11-80](./lesson11n80) - テキストファイルを読込む練習をしよう
* 📖 [Lesson11-90](./lesson11n90) - TOMLファイルを読み取って見ましょう
* 📖 [Lesson11-100](./lesson11n100) - JSONファイルを読み取って見ましょう
* 📖 [Lesson11-203](./lesson11n203) - (Lesson11-3 から Lesson11-203 へリナンバリング) 前レッスン（Lesson11-2）では 状態（State）が 次のStateの名前 を返していました。  
これを 辺（Edge） の名前を返すように変更し、 transition.json ファイルの中で  
どの状態のどの辺は 次にどの状態につながるかを編集できるように変更します。  
* 📖 [Lesson11-300](./lesson11n300) - `auto_gen` フォルダーを自動生成し、その中に `init.py` （状態）ファイルの雛型を自動生成してみましょう
* 📖 [Lesson12](./lesson12) - サブ状態（Sub-state）を持つサーバーの練習用のサンプルです
* 📖 [Lesson12-2](./lesson12n2) - update() のメソッドの中で `c_sock.recv()` を呼び出すタイミングをプログラマーが毎回指定する手間の方が、コードが散らばる手間よりメンテナンスしやすいでしょう
* 📖 [Lesson12-3](./lesson12n3) - `update()` の引数は `req` 変数 と決めつけてしまい、その下に変数をぶら下げることにしましょう
* 📖 [Lesson13](./lesson13) - ステート（State）とサブステート（Sub-state）を分けて 大きな状態遷移、小さな状態遷移といった　強調を  
  付けた方が 人間の目の検索能力の負担を軽くできるかもしれません
* 📖 [Lesson13-2](./lesson13n2) - `transigion2.py` に、ステートマシンを終了させる出口を指定できるようにしましょう
* 📖 [Lesson14](./lesson14) - 状態遷移定義ファイルを作ってみましょう。サブサブサブステートマシンを作ってみましょう
* 📖 [Lesson15](./lesson15) - `transition.json` だけあれば、状態遷移がちゃんとつながっているか検証できるはずです。 graphviz を使って可視化しましょう
* 📖 [Lesson15-2](./lesson15n2) - サブステートを可視化できるように、 graphviz のクラスタリングを使いましょう
* 📖 Lesson16 - Lesson11-300に移動
* 📖 [Lesson16-2](./lesson16n2) - `pen_transition.py` からすべてのステートを読取り、ステートクラスを自動生成しましょう
* 📖 [Lesson16-3](./lesson16n3) - 次に、 エッジの分岐を自動生成しましょう
* 📖 [Lesson17](./lesson17) - doc構造でデータ化した定数（`const.py`）を元に、定数を定義したスクリプト（`const.py`）も自動生成するようにしましょう TODO (Lesson17 より先に Lesson22 を持ってこれないか？)
* 📖 Lesson17-2 - Lesson11-100 に移動
* 📖 [Lesson18](./lesson18) - Lesson17 で行ったコードの自動生成を発展させ、doc構造でデータ化した定数（`const.py`）を元に、Lesson14 と同等の Python スクリプトのルーチン（状態のスクリプト）を自動生成しましょう
* 📖 Lesson18-2 - Lesson17 へ統合
* 📖 Lesson18-3 - Lesson23 へ統合
* 📖 Lesson22 - Lesson18-2 へ移動
* 📖 [Lesson23](./lesson23) - Lesson18 をさらに発展させ、doc構造のデータを元に、Lesson14と同等のPythonスクリプトのルーチン（状態のスクリプト）を自動生成しましょう
* 📖 Lesson24 - **Lesson24の内容はLesson18に取り込みました**

## すぐには使わなさそうなものは 10000番台へ移動

* 📖 [Lesson10019](./lesson10019) - `transition.py` のデータ部を JSON へ書き出してみましょう (TODO 状態遷移ファイルは、最初からJSONで書けないか？)
* 📖 [Lesson10020](./lesson10020) - `transition.json` ファイルを読み取ってみましょう (Lesson17-2へ一部移動)
* 📖 [Lesson10021](./lesson10021) - 状態遷移定義ファイル（JSON形式）から、 `pen_transition.py` ファイルを逆生成してみましょう
