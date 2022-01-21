# Lesson02-2

Lesson02 で、後から変えられなかった本文を、後から変えられるようにしてみましょう。 **ラムダ式** を使えばできます  

## Run

```shell
python.exe -m lesson02n2.main
```

Output:  

```plain
🍎 My name is Apple!
🍎 Refreshing!
🍌 My name is Banana!
🍌 Very sweet!
🍒 My name is Cherry!
🍒 Sour!
```

## 解説

fruits_v02n2.py:  

```python
from lesson01n2.fruit.apple_v01n2 import AppleV01n2
from lesson01n2.fruit.banana_v01n2 import BananaV01n2
from lesson01n2.fruit.cherry_v01n2 import CherryV01n2


fruits_v02n2 = {
    "Apple": lambda msg: AppleV01n2(msg),
    "Banana": lambda msg: BananaV01n2(msg),
    "Cherry": lambda msg: CherryV01n2(msg),
}
```

👆 `lambda 引数: 式` という書き方を使ってみましょう。  
ラムダ式は 書いても（**ラムダ抽象(Abstraction)**と呼ぶ）その場では実行されず、  
あとで引数が渡されたとき（**適用(Application)** と呼ぶ）に実行されるという 振る舞いをします。  

main.py:  

```python
from lesson02n2.fruits_v02n2 import fruits_v02n2


if __name__ == "__main__":
    juice = fruits_v02n2["Apple"]("My name is Apple!")
    juice.print()
    juice = fruits_v02n2["Apple"]("Refreshing!")
    juice.print()

    juice = fruits_v02n2["Banana"]("My name is Banana!")
    juice.print()
    juice = fruits_v02n2["Banana"]("Very sweet!")
    juice.print()

    juice = fruits_v02n2["Cherry"]("My name is Cherry!")
    juice.print()
    juice = fruits_v02n2["Cherry"]("Sour!")
    juice.print()
```

👆 上記が **適用** をしたものです。  
これで、後から引数も渡せることを習得しました  
