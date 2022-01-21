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
