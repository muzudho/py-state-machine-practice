# lesson02

果物（State）オブジェクトを予めディクショナリーに追加しておき、使う時にキー（Key）を指定することで  
差し替えることができる理屈を習得してください

## Run

```shell
python.exe -m lesson02.main
```

## 解説

fruits_v02.py:  

```python
from lesson01.fruit.apple import AppleV1
from lesson01.fruit.banana import BananaV1
from lesson01.fruit.cherry import CherryV1


fruits_v02 = {
    "Apple": AppleV1(),
    "Banana": BananaV1(),
    "Cherry": CherryV1(),
}
```

👆 `fruits_v02` という名前のディクショナリーに Appleクラスのインスタンス、  
Bananaクラスのインスタンス、Cherryクラスのインスタンスを登録しています  

main.py:  

```python
from lesson02.fruits_v02 import fruits_v02


if __name__ == "__main__":
    juice = fruits_v02["Apple"]
    juice.print()

    juice = fruits_v02["Banana"]
    juice.print()

    juice = fruits_v02["Cherry"]
    juice.print()
```

👆 これによって、 Lesson01 では `juice = Juice(AppleV1())` と書いていたコードが、  
`juice = fruits_v02["Apple"]` と書くように変わりました  

`AppleV1()` とハードコーディングしていたところを `"Apple"` のように文字列指定に変わったのが大きいです。  
これにより外部ファイルを読込むことでプログラムの動きを変える、といったことが可能になりそうです  
