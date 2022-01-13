# lesson11-203

前レッスン（Lesson11-2）では 状態（State）が 次のStateの名前 を返していました。  
これを 辺（Edge） の名前を返すように変更し、 transition.json ファイルの中で  
どの状態のどの辺は 次にどの状態につながるかを編集できるように変更します。  

## Run

Server start:  

```shell
python.exe -m lesson11n203.main "lesson11n203_projects/house2/conf.toml"
#                               ----------------------------------------
#                               設定ファイル
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
