# lesson01-2

Lesson01 で `🍎 Refreshing!` のように表示しましたが、このメッセージの部分を後から変えれるように **変数** を使う事を覚えてください

## Run

```shell
python.exe -m lesson01n2.main
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

fruit/apple_v01n2.py:  

```python
class AppleV01n2:
    def __init__(self, message):
        self._message = message

    def print(self):
        print(f"🍎 {self._message}")
```

👆 上記のように書くと  

main.py:  

```python
from lesson01.juice_v01 import JuiceV01
from lesson01n2.fruit.apple_v01n2 import AppleV01n2
from lesson01n2.fruit.banana_v01n2 import BananaV01n2
from lesson01n2.fruit.cherry_v01n2 import CherryV01n2


if __name__ == "__main__":
    juice = JuiceV01(AppleV01n2("My name is Apple!"))
    juice.print()
    juice = JuiceV01(AppleV01n2("Refreshing!"))
    juice.print()

    juice = JuiceV01(BananaV01n2("My name is Banana!"))
    juice.print()
    juice = JuiceV01(BananaV01n2("Very sweet!"))
    juice.print()

    juice = JuiceV01(CherryV01n2("My name is Cherry!"))
    juice.print()
    juice = JuiceV01(CherryV01n2("Sour!"))
    juice.print()
```

👆 コンストラクタの引数で 本文を渡せるようになります  
