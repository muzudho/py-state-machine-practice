# lesson01

果物（状態, State）を差し替えることで、せりふ（振る舞い, Behavior）が変わる理屈を習得してください  

## Run

```shell
python.exe -m lesson01.main
```

## 解説

juice_v1.py:  

```python
class Juice:
    def __init__(self, fruit):
        self._fruit = fruit

    def print(self):
        self._fruit.print()
```

👆　Juice クラスの `.print()` メソッドは、  
Juice クラスが持っている fruit オブジェクトの `.print()` を代わりに呼んでいるだけ、  
ということに注目してください

fruit/apple_v1.py:  

```python
class AppleV1:
    def print(self):
        print("Refreshing!")
```

fruit/banana_v1.py:  

```python
class BananaV1:
    def print(self):
        print("Very sweet!")
```

fruit/cherry_v1.py:

```python
class CherryV1:
    def print(self):
        print("Sour!")
```

👆 fruit オブジェクトには、例えば AppleV1 クラスのインスタンスだったり、  
BananaV1 クラスのインスタンスだったり、 CherryV1 クラスのインスタンスが代入されているとします

main.py:  

```python
from lesson01.juice import Juice
from lesson01.fruit.apple import AppleV1
from lesson01.fruit.banana import BananaV1
from lesson01.fruit.cherry import CherryV1


if __name__ == "__main__":
    juice = Juice(AppleV1())
    juice.print()

    juice = Juice(BananaV1())
    juice.print()

    juice = Juice(CherryV1())
    juice.print()
```

👆 コードで書くと上記の通りです。  
これで、 Juice クラスの `.print()` メソッドは **振る舞い** を変えています。  

このように、振る舞いを変えるコードの書き方のパターンを 覚えてください。  
