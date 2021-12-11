# Lesson12-2

前回の Lesson12 のサンプルでは、  

```plain
You can see the house.
You can see the close knob.
```

のメッセージがとらばっており、面倒でした。  
これは `c_sock.recv()` の前と後ろを挟むように ステートの update() メソッドができていないことから  
起こることでした。  

かといって、 `c_sock.recv()` の前後に react_before_input() や react_after_input() といった２つのメソッドを置くのもまた面倒です。  

update() のメソッドの中で `c_sock.recv()` を呼び出すタイミングをプログラマーが毎回指定する手間の方が、コードが散らばる手間よりメンテナンスしやすいでしょう。  

## Run

Server start:  

```shell
python.exe -m lesson12n2.main
```

Client start:  

```shell
python.exe -m lesson09.main
```
