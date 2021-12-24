import sys


from lesson07n2.main_finally import MainFinally
from lesson18.server_v18 import ServerV18
from lesson18.state_machine_v18 import StateMachineV18
from lesson20.transition_json_reader import TransitionJsonReader

# Lesson 23
from lesson23_data.step1n2_auto_const.wcsc_const import INIT
from lesson23_data.wcsc_step4_state_gen_v23 import wcsc_state_gen_v23

INPUT_TRANSITION_JSON_FILE_PATH = "lesson20_data/step2n2_auto/wcsc-transition.json"
server = None


class Main:
    def on_main(self):
        transition_json_obj = TransitionJsonReader.read_file(
            INPUT_TRANSITION_JSON_FILE_PATH
        )

        # 状態遷移マシン
        state_machine = StateMachineV18(
            state_gen=wcsc_state_gen_v23,
            transition_py_dict=transition_json_obj,
            entry_state_path=[INIT],
        )

        # サーバー
        server = ServerV18(
            host="0.0.0.0",
            port=5002,
            state_machine=state_machine,
        )
        server.run()
        return 0

    def on_finally(self):
        # [Ctrl] + [C] を受け付けないから、ここにくるのは難しい
        if server:
            server.clean_up()

        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
