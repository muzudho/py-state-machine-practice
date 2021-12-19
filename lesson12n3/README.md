# Lesson12-3

前回の Lesson12-2 のサンプルでは、  

```python
    def update(self, c_sock, pull_trigger):
        pass
```

👆 `update()` メソッドの引数が `c_sock` と `pull_trigger` でした。  
開発が進むと update() の引数が増えたり、 ほとんどのステートにとって要らない引数を沢山指定するといった、  
手間が増えるでしょう  

```python
    def update(self, req):
        # rec.c_sock
        # rec.pull_trigger()
        pass
```

👆 そこで `update()` の引数は `req` 変数 と決めつけてしまい、その下に変数をぶら下げることにしましょう。  
`req` 変数（Requestクラス変数）は 様々な変数をぶら下げる巨大なオブジェクトになるでしょう  

## Run

Server start:  

```shell
python.exe -m lesson12n3.main
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
