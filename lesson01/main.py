from lesson01.juice import Juice
from lesson01.fruit.apple import Apple
from lesson01.fruit.banana import Banana
from lesson01.fruit.cherry import Cherry


if __name__ == "__main__":
    juice = Juice(Apple())
    juice.print()

    juice = Juice(Banana())
    juice.print()

    juice = Juice(Cherry())
    juice.print()
