from lesson13.state_machine_helper_v13 import StateMachineHelperV13


class StateMachineV24:
    def __init__(self, state_gen, entry_state_path):
        """ステートマシン

        Parameters
        ----------
        state_gen : dict
            状態オブジェクトを生成するのに使います
        entry_state_path : list
            開始状態
        """

        self._state_gen = state_gen
        self._state_path = entry_state_path
        # state_gen_conf.py を見て state_path から state を生成します
        self._state = StateMachineHelperV13.create_state_v13(
            self._state_gen, self._state_path
        )

    @property
    def state_path(self):
        return self._state_path

    @state_path.setter
    def state_path(self, val):
        self._state_path = val

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, val):
        self._state = val
