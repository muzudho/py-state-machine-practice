
from lesson01.state_machine import StateMachine
from lesson01.apple_state import AppleState
from lesson01.banana_state import BananaState


if __name__ == "__main__":
    state_machine = StateMachine(AppleState())
    state_machine.print()

    state_machine = StateMachine(BananaState())
    state_machine.print()
