# lesson01

果物（状態, State）を差し替えることで、せりふ（振る舞い, Behavior）が変わる理屈を習得してください  

## Run

```shell
python.exe -m lesson01.main
```

Output:  

```plain
🍎 Refreshing!
🍌 Very sweet!
🍒 Sour!
```

## 解説

juice_v01.py:  

```python
class JuiceV01:
    def __init__(self, fruit):
        self._fruit = fruit

    def print(self):
        self._fruit.print()
```

👆 Juice クラスの `.print()` メソッドは、  
JuiceV01 クラスが持っている fruit オブジェクトの `.print()` を代わりに呼んでいるだけ、  
ということに注目してください

fruit/apple_v01.py:  

```python
class AppleV01:
    def print(self):
        print("🍎 Refreshing!")
```

fruit/banana_v01.py:  

```python
class BananaV01:
    def print(self):
        print("🍌 Very sweet!")
```

fruit/cherry_v01.py:

```python
class CherryV01:
    def print(self):
        print("🍒 Sour!")
```

👆 fruit オブジェクトには、例えば AppleV01 クラスのインスタンスだったり、  
BananaV01 クラスのインスタンスだったり、 CherryV01 クラスのインスタンスが代入されているとします

main.py:  

```python
from lesson01.juice import JuiceV01
from lesson01.fruit.apple import AppleV01
from lesson01.fruit.banana import BananaV01
from lesson01.fruit.cherry import CherryV01


if __name__ == "__main__":
    juice = JuiceV01(AppleV01())
    juice.print()

    juice = JuiceV01(BananaV01())
    juice.print()

    juice = JuiceV01(CherryV01())
    juice.print()
```

👆 コードで書くと上記の通りです。  
これで、 JuiceV01 クラスの `.print()` メソッドは **振る舞い** を変えています。  

このように、振る舞いを変えるコードの書き方のパターンを 覚えてください。  
