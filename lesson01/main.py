from lesson01.juice_v01 import Juice01
from lesson01.fruit.apple_v01 import AppleV01
from lesson01.fruit.banana_v01 import BananaV01
from lesson01.fruit.cherry_v01 import CherryV01


if __name__ == "__main__":
    juice = Juice01(AppleV01())
    juice.print()

    juice = Juice01(BananaV01())
    juice.print()

    juice = Juice01(CherryV01())
    juice.print()
