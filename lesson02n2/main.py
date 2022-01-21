from lesson02n2.fruits_v02n2 import fruits_v02n2


if __name__ == "__main__":
    juice = fruits_v02n2["Apple"]("My name is Apple!")
    juice.print()
    juice = fruits_v02n2["Apple"]("Refreshing!")
    juice.print()

    juice = fruits_v02n2["Banana"]("My name is Banana!")
    juice.print()
    juice = fruits_v02n2["Banana"]("Very sweet!")
    juice.print()

    juice = fruits_v02n2["Cherry"]("My name is Cherry!")
    juice.print()
    juice = fruits_v02n2["Cherry"]("Sour!")
    juice.print()
