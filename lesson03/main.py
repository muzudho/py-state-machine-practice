
from lesson03.states import states


if __name__ == "__main__":
    program = ["Apple",
               "Banana",
               "Banana",
               "Cherry",
               "Cherry",
               "Cherry",
               "Apple"]

    for key in program:
        state = states[key]
        state.print()
