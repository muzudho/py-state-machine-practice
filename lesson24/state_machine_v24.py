from lesson13.state_machine_helper_v13 import StateMachineHelperV13
from lesson16n3.transition_conf_v1n3 import TransitionConfV1n3


class StateMachineV24:
    def __init__(self, state_gen, transition_py_dict, entry_state_path):
        """ステートマシン

        Parameters
        ----------
        state_gen : dict
            状態オブジェクトを生成するのに使います
        entry_state_path : list
            開始状態
        """

        self._is_verbose = False
        self._state_gen = state_gen
        self._transition_py_dict = transition_py_dict
        self._transition_conf = TransitionConfV1n3(self._transition_py_dict)
        self._state_path = entry_state_path

        # state_gen_conf.py を見て state_path から state を生成します
        self._state = StateMachineHelperV13.create_state_v13(
            self._state_gen, self._state_path
        )

        self._edge = None

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

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, val):
        self._state = val

    @property
    def edge_name(self):
        return self._edge_name

    @edge_name.setter
    def edge_name(self, val):
        self._edge_name = val

    def start(self):
        """ステートマシーンを開始します"""
        # このループも ステートマシーンに入れたら？
        while True:
            req = self.create_request()

            self.update_state_path(req)

            if self.state_path is None:
                # 次のステートがナンだったので、ステートマシンは終了しました
                self.on_terminated()
                break  # ループから抜けます

            self.move_to_next_state()

    def update_state_path(self, req):
        """メッセージに応じたアクションを行ったあと、Edge名を返します。
        Edge名は空でない文字列です。 None や list であってはいけません

        Parameters
        ----------
        req : RequestV24
            状態に渡される引数
        """
        self._edge_name = self.state.update(req)

        if self._is_verbose:
            print(
                f"[state_machine] transition_conf.title={self._transition_conf.title}"
            )
            print(
                f"[state_machine] transition_conf.entry_state={self._transition_conf.entry_state}"
            )
            print(f"[state_machine] transition_conf.data={self._transition_conf.data}")
            print(f"[state_machine] state_path={self.state_path}")
            print(f"[state_machine] edge_name={self.edge_name}")

        # transition_conf.py を見て state_path を得ます
        self.state_path = StateMachineHelperV13.lookup_next_state_path_v13(
            self.transition_conf.data,
            self.state_path,
            self.edge_name,
        )

        if self._is_verbose:
            print(f"[state_machine] state_path={self.state_path}")

    def move_to_next_state(self):
        # state_gen_conf.py を見て state_path から state を生成します
        self.state = StateMachineHelperV13.create_state_v13(
            self._state_gen, self.state_path
        )

    def create_request(self):
        """Request変数を返す関数です"""
        return None

    def on_terminated(self):
        """ステートマシーン終了時に呼び出されます"""
        pass
