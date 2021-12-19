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

👆 前レッスンでは ドアは 開く（Open）で開けました。  
しかし、ドアは ノブを回す（TurnKnob）、ノブを引く（PullKnob）、入る（Enter）の３ステップで開くものかもしれません。  

```plain
                     +--------------+
                     |              |
                     |              |
                     |   My room    |
                     |              |
                     |              |
+ . Out . . . . +    +---------     +
.               .    |   Stairs     |
.               .    |              |
.               .    |         +----+
.               .    |         |    |
.               .         +----+    |
.               .  Door   |         |
+ . . . . . . . +----+----+---------+
```

👆 そこでまず `Out` ステートは いったん本書では `Out` セット（Set;集合）と呼び方を変えます。  

```plain
                     +--------------+
                     |              |
                     |              |
                     |   My room    |
                     |              |
                     |              |
+ . Out . . . . +    +---------     +
.               .    |   Stairs     |
.               .    |              |
.               .    |         +----+
.     CloseKnob .    |         |    |
.     CloseDoor .         +----+    |
.     OpenDoor  .         |         |
+ . . . . . . . +----+----+---------+
```

👆 そして `Out` セットの中に ノブが閉じている（CloseKnob）、ドアが閉じている（CloseDoor）、  
ドアが開いている（OpenDoor）の３状態があるとします  

```plain
                     +--------------+
                     |              |
                     |              |
                     |   My room    |
                     |              |
                     |              |
+ . . . . . . . +    +---------     +
.               .    |   Stairs     |
.               .    |              |
.               .    |         +----+
. Out/CloseKnob .    |         |    |
. Out/CloseDoor .         +----+    |
. Out/OpenDoor  .         |         |
+ . . . . . . . +----+----+---------+
```

👆 `Out` は便宜上の分類名に変わったと考えれば、フラットに考えることができ、  
実質的な状態は５つあることになります  

では、 `Out` に技術的な意味は無くなったのでしょうか？  

```plain
                             +--------------+
                             |              |
                             |              |
                             |   My room    |
                             |              |
                             |              |
+ . . . . . . . . . . . +    +---------     +
.                       .    |   Stairs     |
.                       .    |              |
.                       .    |         +----+
. Out (Out/CloseKnob)   .    |         |    |
. Out/CloseDoor         .         +----+    |
. Out/OpenDoor          .         |         |
+ . . . . . . . . . . . +----+----+---------+
```

👆 強いて言えば `Out` は `Out/CloseKnob` の略称だ、ぐらいの働きを持てるかもしれません。  
ドアが必ず閉まってノブが元の回転位置に自動で戻ればですが  

## Run

Server start:  

```shell
python.exe -m lesson12.main
```

Client start:  

```shell
python.exe -m lesson09.main
```

Input:  

```plain
Turn knob
Pull knob
Enter
Up
Sit down
q
```
