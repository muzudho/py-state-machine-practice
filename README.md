# py-state-machine-practice

状態遷移マシンの練習（＾～＾）

* 📖 [Lesson01](./lesson01) - ステートを差し替えることで、振る舞いが変わる理屈を習得してください
* 📖 [Lesson02](./lesson02) - ステート（State）オブジェクトを先に生成しておき、キー（Key）を指定することで 差し替えることができる理屈を習得してください
* 📖 [Lesson03](./lesson03) - キー（Key）をリストで並べると、まるでプログラムのシーケンス実行になるという理屈を習得してください
* 📖 [Lesson04](./lesson04) - ノード（Node）をつなげるとグラフ（Graph）になるという理屈を習得してください
* 📖 [Lesson05](./lesson05) - 振る舞い（Behavior）を持たせるという感覚を習得してください
* 📖 [Lesson06](./lesson06) - １つ前のノードの振る舞い（Behavior）によって、その後ろのノードが振る舞いを 変える（非マルコフ連鎖）という感覚を習得してください
* 📖 [Lesson07](./lesson07) - なぜか Python で標準で用意されていない「終了処理を必ずやる」コードの書き方のサンプルです
* 📖 [Lesson08](./lesson08) - これから練習でよく使うことになるサーバーを作るための練習用のサンプルです
* 📖 [Lesson09](./lesson09) - サーバーに文字列を送るアプリケーションのサンプルです
* 📖 [Lesson10](./lesson10) - 数字を受け取ると、大きいと `Too Big`、小さいと `Too Small`、 ちょうどいいなら `Just Right` を返してくるサーバーです
* 📖 [Lesson11](./lesson11) - 状態を持つサーバーの練習用のサンプルです
* 📖 [Lesson11-2](./lesson11n2) - 状態の数だけ if 文を書いていたところを、 ステート（State）デザインパターンで書き直す練習用のサンプルです
* 📖 [Lesson11-3](./lesson11n3) - 前レッスンでは 状態（State）が 次の State の名前 を返していました。  
  これを 辺（Edge） の名前を返すように変更し、 transition_conf.py ファイルの中で  
  どの状態のどの辺は 次にどの状態につながるかを編集できるように変更します
* 📖 [Lesson12](./lesson12) - サブ状態（Sub-state）を持つサーバーの練習用のサンプルです
* 📖 [Lesson12-2](./lesson12n2) - update() のメソッドの中で `c_sock.recv()` を呼び出すタイミングをプログラマーが毎回指定する手間の方が、コードが散らばる手間よりメンテナンスしやすいでしょう
