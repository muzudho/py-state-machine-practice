from lesson01.juice_v1 import Juice
from lesson01.fruit.apple_v1 import AppleV1
from lesson01.fruit.banana_v1 import BananaV1
from lesson01.fruit.cherry_v1 import CherryV1


if __name__ == "__main__":
    juice = Juice(AppleV1())
    juice.print()

    juice = Juice(BananaV1())
    juice.print()

    juice = Juice(CherryV1())
    juice.print()
