import sys


from lesson07n2.main_finally import MainFinally
from lesson24.server_v24 import ServerV24
from lesson20.transition_json_reader import TransitionJsonReader

# Lesson 23
from lesson23_data.step1n2_auto_const.pen_const import INIT
from lesson24.state_machine_v24 import StateMachineV24
from lesson24_data.pen_step4_state_gen_v24 import pen_state_gen_v24

INPUT_TRANSITION_JSON_FILE_PATH = "lesson20_data/step2n2_auto/pen-transition.json"
server = None


class Main:
    def on_main(self):
        transition_json_obj = TransitionJsonReader.read_file(
            INPUT_TRANSITION_JSON_FILE_PATH
        )

        # 状態遷移マシン
        state_machine = StateMachineV24(
            state_gen=pen_state_gen_v24,
            transition_py_dict=transition_json_obj,
            entry_state_path=[INIT],
        )

        # サーバー
        server = ServerV24(
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
