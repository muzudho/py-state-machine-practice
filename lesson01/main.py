from lesson01.juice_v01 import JuiceV01
from lesson01.fruit.apple_v01 import AppleV01
from lesson01.fruit.banana_v01 import BananaV01
from lesson01.fruit.cherry_v01 import CherryV01


if __name__ == "__main__":
    juice = JuiceV01(AppleV01())
    juice.print()

    juice = JuiceV01(BananaV01())
    juice.print()

    juice = JuiceV01(CherryV01())
    juice.print()
