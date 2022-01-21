from lesson01.juice_v01 import JuiceV01
from lesson02.fruits_v02 import fruits_v02


if __name__ == "__main__":
    juice = JuiceV01(fruits_v02["Apple"])
    juice.print()

    juice = JuiceV01(fruits_v02["Banana"])
    juice.print()

    juice = JuiceV01(fruits_v02["Cherry"])
    juice.print()
