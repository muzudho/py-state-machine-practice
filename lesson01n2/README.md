# lesson01-2

Lesson01 ใง `๐ Refreshing!` ใฎใใใซ่กจ็คบใใพใใใใใใฎใกใใปใผใธใฎ้จๅใๅพใใๅคใใใใใใซ **ๅคๆฐ** ใไฝฟใไบใ่ฆใใฆใใ ใใ

## Run

```shell
python.exe -m lesson01n2.main
```

Output:  

```plain
๐ My name is Apple!
๐ Refreshing!
๐ My name is Banana!
๐ Very sweet!
๐ My name is Cherry!
๐ Sour!
```

## ่งฃ่ชฌ

fruit/apple_v01n2.py:  

```python
class AppleV01n2:
    def __init__(self, message):
        self._message = message

    def print(self):
        print(f"๐ {self._message}")
```

๐ ไธ่จใฎใใใซๆธใใจ  

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

๐ ใณใณในใใฉใฏใฟใฎๅผๆฐใง ๆฌๆใๆธกใใใใใซใชใใพใ  
