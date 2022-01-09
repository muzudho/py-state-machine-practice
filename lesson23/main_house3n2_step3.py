import sys


from lesson07n2.main_finally import MainFinally
from lesson18.server_v18 import ServerV18
from lesson18.state_machine_v18 import StateMachineV18
from lesson20.code_gen.json_reader_v20 import JsonReaderV20

# Lesson 23
from lesson23_data.step1n2_auto_const.house3n2_const import OUT
from lesson23_data.house3n2_step4_state_gen_v23 import house3n2_state_gen_v23

INPUT_TRANSITION_JSON_FILE_PATH = "lesson20_data/step2n2_auto/house3n2-transition3.json"
server = None


class Main:
    def on_main(self):
        transition_json_obj = JsonReaderV20.read_file(
            INPUT_TRANSITION_JSON_FILE_PATH
        )

        # 状態遷移マシン
        state_machine = StateMachineV18(
            state_gen=house3n2_state_gen_v23,
            transition_py_dict=transition_json_obj,
            entry_state_path=[OUT],
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
