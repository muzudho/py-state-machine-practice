# lesson01

果物（状態, State）を差し替えることで、せりふ（振る舞い, Behavior）が変わる理屈を習得してください  

```shell
python.exe -m lesson01.main
```

## 解説

juice.py:  

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

fruit/apple.py:  

```python
class Apple:
    def print(self):
        print("Refreshing!")
```

fruit/banana.py:  

```python
class Banana:
    def print(self):
        print("Very sweet!")
```

fruit/cherry.py:

```python
class Cherry:
    def print(self):
        print("Sour!")
```

👆 fruit オブジェクトには、例えば Apple クラスのインスタンスだったり、  
Banana クラスのインスタンスだったり、 Cherry クラスのインスタンスが代入されているとします

main.py:  

```python
from lesson01.juice import Juice
from lesson01.fruit.apple import Apple
from lesson01.fruit.banana import Banana
from lesson01.fruit.cherry import Cherry


if __name__ == "__main__":
    juice = Juice(Apple())
    juice.print()

    juice = Juice(Banana())
    juice.print()

    juice = Juice(Cherry())
    juice.print()
```

👆 コードで書くと上記の通りです。  
これで、 Juice クラスの `.print()` メソッドは **振る舞い** を変えています。  

このように、振る舞いを変えるコードの書き方のパターンを 覚えてください。  
