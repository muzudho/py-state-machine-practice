class StateMachine():
    def __init__(self, state):
        self._state = state

    def print(self):
        self._state.print()
