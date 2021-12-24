from lesson16n3.transition_conf_v1n3 import TransitionConfV1n3


class StateMachineV18:
    def __init__(self, state_gen, transition_py_dict, entry_state_path):
        self._is_verbose = False
        self._state_gen = state_gen
        self._transition_py_dict = transition_py_dict
        self._transition_conf = TransitionConfV1n3(self._transition_py_dict)
        self._state_path = entry_state_path

    @property
    def state_gen(self):
        return self._state_gen

    @property
    def transition_conf(self):
        return self._transition_conf

    @property
    def state_path(self):
        return self._state_path

    @state_path.setter
    def state_path(self, val):
        self._state_path = val

    def create_request(self):
        """Request変数を返す関数です"""
        return None

    def on_terminated(self):
        """ステートマシーン終了時に呼び出されます"""
        pass
