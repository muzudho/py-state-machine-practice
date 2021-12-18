# Lesson 21-2

トランジション設定ファイル（JSON形式）と 定数設定ファイル（Python形式）から、 `transition_conf.py` ファイルを逆生成してみましょう  

## やりたいこと

```plain
    "entry_node": "Init",
```

👆 値が文字列の所を、  

```plain
    "entry_node": INIT,
```

👆 定数に置き換えたいです。そのためには、  

```python
from lesson18.step1n2_auto_const.pen import INIT
```

👆 import 文も合わせて書くことが必要です  

## やりかた

文字列を定数に置き換える方法は Lesson 17 を参照してください  

## Run

```shell
python.exe -m lesson21n2.main
```
