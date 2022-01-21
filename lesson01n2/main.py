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
