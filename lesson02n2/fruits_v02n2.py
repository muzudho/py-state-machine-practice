from lesson01n2.fruit.apple_v01n2 import AppleV01n2
from lesson01n2.fruit.banana_v01n2 import BananaV01n2
from lesson01n2.fruit.cherry_v01n2 import CherryV01n2


fruits_v02n2 = {
    "Apple": lambda msg: AppleV01n2(msg),
    "Banana": lambda msg: BananaV01n2(msg),
    "Cherry": lambda msg: CherryV01n2(msg),
}
