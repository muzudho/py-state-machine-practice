# lesson11

状態を持つサーバーの練習用のサンプルです  

## Explain

```plain
                +--------------+
                |              |
                |              |
                |   MyRoom     |
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

最初 外（Out）に居て、 次に 階段（Stairs）のある部屋に居て、 最後に 自分の部屋（My room）に居るとします。  
外では ドアを開く `Open` というメッセージを送信し、  
階段のある部屋では 階段を昇る `Up` というメッセージを送信し、  
自分の部屋では 椅子に座る `Sit down` というメッセージを送信すれば クリア―です。  

異なるメッセージを送ると 外（Out） に戻されます。  

## Run

Server start:  

```shell
python.exe -m lesson11.main
```

Client start:  

```shell
python.exe -m lesson09.main
```

Input:  

```plain
Open
Up
Sit down
q
```
