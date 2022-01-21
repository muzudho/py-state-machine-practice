# lesson03

キー（Key）をリストで並べると、まるでプログラムのシーケンス実行になるという理屈を習得してください

```shell
python.exe -m lesson03.main
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

main:  

```python
from lesson02n2.fruits_v02n2 import fruits_v02n2


if __name__ == "__main__":
    program = [
        ("Apple", "My name is Apple!"),  # プログラムは縦に並べると見やすいです
        ("Apple", "Refreshing!"),
        ("Banana", "My name is Banana!"),
        ("Banana", "Very sweet!"),
        ("Cherry", "My name is Cherry!"),
        ("Cherry", "Sour!"),
    ]

    # プログラムを先頭から順に実行していきます
    for line in program:
        state = fruits_v02n2[line[0]](line[1])
        state.print()
```

👆 まるで、 果物の名前が プログラムのコマンドのように振る舞い、  
本文が その引数として 振る舞っています  
