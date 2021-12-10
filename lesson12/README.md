# lesson12

サブ状態（Sub-state）を持つサーバーの練習用のサンプルです

## Explain

```plain
                +--------------+
                |              |
                |              |
                |   My room    |
                |              |
                |              |
+ . . . . . . . +---------     +
.               |   Stairs     |
.               |              |
.               |         +----+
.     Out       |         |    |
.                    +----+    |
.             Door   |         |
+---------------+----+---------+
```

前レッスンでは ドアは 開く（Open）で開けました。  
しかし、ドアは ノブを回す（Turn）、引く（Pull）、閉じる（Close）の３ステップで開くものかもしれません。  

```plain
                +--------------+
                |              |
                |              |
                |   My room    |
                |              |
                |              |
+ . . . . . . . +---------     +
.               |   Stairs     |
.               |              |
.               |         +----+
.         Out.Turn        |    |
.         Out.Pull   +----+    |
.         Out.Close  |         |
+---------------+----+---------+
```

これは Out 状態（State）には例えば OpenDoor という名前でサブステートマシン（Sub-state machine）を持っており、  
OpenDoorサブステートマシンには Turn, Pull, Close のサブ状態（Sub-state）があると言えます。  

これをどう考えるかというと、 Out 状態は また Out 状態に **戻ってくる**（Loopback）という足踏みを３回すると考えます。  

## Run

Server start:  

```shell
python.exe -m lesson12.main
```

Client start:  

```shell
python.exe -m lesson12.main
```
