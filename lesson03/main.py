from lesson02.fruits import fruits_v02


if __name__ == "__main__":
    program = [
        "Apple",  # プログラムは縦に並べると見やすいです
        "Banana",
        "Banana",
        "Cherry",
        "Cherry",
        "Cherry",
        "Apple",
    ]

    # プログラムを先頭から順に実行していきます
    for key in program:
        state = fruits_v02[key]
        state.print()
