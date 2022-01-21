# lesson02

果物（State）オブジェクトを予めディクショナリーに追加しておき、使う時にキー（Key）を指定することで  
差し替えることができる理屈を習得してください

## Run

```shell
python.exe -m lesson02.main
```

Output:  

```shell
🍎 Refreshing!
🍌 Very sweet!
🍒 Sour!
```

## 解説

fruits_v02.py:  

```python
from lesson01n2.fruit.apple_v01n2 import AppleV01n2
from lesson01n2.fruit.banana_v01n2 import BananaV01n2
from lesson01n2.fruit.cherry_v01n2 import CherryV01n2


fruits_v02 = {
    "Apple": AppleV01n2("Refreshing!"),
    "Banana": BananaV01n2("Very sweet!"),
    "Cherry": CherryV01n2("Sour!"),
}
```

👆 `fruits_v02` という名前のディクショナリーに Appleクラスのインスタンス、  
Bananaクラスのインスタンス、Cherryクラスのインスタンスを登録しています  

main.py:  

```python
from lesson01.juice_v01 import JuiceV01
from lesson02.fruits_v02 import fruits_v02


if __name__ == "__main__":
    juice = JuiceV01(fruits_v02["Apple"])
    juice.print()

    juice = JuiceV01(fruits_v02["Banana"])
    juice.print()

    juice = JuiceV01(fruits_v02["Cherry"])
    juice.print()
```

👆 これによって、 Lesson01 では `juice = JuiceV01(AppleV1())` と書いていたコードが、  
`juice = JuiceV01(fruits_v02["Apple"])` と書くように変わりました  

`AppleV1()` とハードコーディングしていたところを `"Apple"` のように文字列指定に変わったのが大きいです。  
これにより外部ファイルを読込むことでプログラムの動きを変える、といったことが可能になりそうです  

ただし、この方法だと　果物の本文を後から変えることができないため、不便に感じるかもしれません  
