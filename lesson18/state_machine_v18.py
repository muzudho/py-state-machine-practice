from lesson13.state_machine_helper_v13 import StateMachineHelperV13
from lesson16n3.code_gen.transition_conf_v16n3 import TransitionConfV16n3


class StateMachineV18:
    def __init__(self, state_gen, transition_doc, entry_state_path):
        self._is_verbose = False
        self._state_gen = state_gen
        self._transition_doc = transition_doc
        self._transition_conf = TransitionConfV16n3(self._transition_doc)
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

    def start(self):
        """ステートマシーンを開始します"""
        # 最初
        state_path = self.state_path
        # state_gen_conf.py を見て state_path から state を生成します
        state = StateMachineHelperV13.create_state_v13(
            self.state_gen, state_path)

        while True:
            req = self.create_request()

            # メッセージに応じたアクションを行ったあと、Edge名を返します。
            # Edge名は空でない文字列です。 None や list であってはいけません
            edge_name = state.update(req)

            if self._is_verbose:
                print(
                    f"[state_machine] transition_conf.title={self.transition_conf.title}"
                )
                print(
                    f"[state_machine] transition_conf.entry_state={self.transition_conf.entry_state}"
                )
                print(
                    f"[state_machine] transition_conf.data={self.transition_conf.data}"
                )
                print(f"[state_machine] state_path={state_path}")
                print(f"[state_machine] edge_name={edge_name}")

            # transition_conf.py を見て、edge_nameから、state_path を得ます
            state_path = StateMachineHelperV13.lookup_next_state_path_v13(
                self.transition_conf.data, state_path, edge_name
            )

            if self._is_verbose:
                print(f"[state_machine] state_path={state_path}")

            if state_path is None:
                # 次のステートがナンだったので、ステートマシンは終了しました
                self.on_terminated()
                break

            # state_gen_conf.py を見て state_path から state を生成します
            state = StateMachineHelperV13.create_state_v13(
                self.state_gen, state_path)

    def create_request(self):
        """Request変数を返す関数です"""
        return None

    def on_terminated(self):
        """ステートマシーン終了時に呼び出されます"""
        pass
