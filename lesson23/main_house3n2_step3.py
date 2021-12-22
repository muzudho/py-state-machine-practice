import sys


from lesson07n2.main_finally import MainFinally
from lesson18.server import Server
from lesson19_data.step2_house3n2_transition3 import house3n2_transition3_py_dict

# Lesson 23
from lesson23_data.step1n2_auto_const.house3n2_const import OUT
from lesson23_data.house3n2_step4_state_gen import house3n2_state_gen

server = None


class Main:
    def on_main(self):
        server = Server(
            state_gen=house3n2_state_gen,
            transition_py_dict=house3n2_transition3_py_dict,
            host="0.0.0.0",
            port=5002,
            entry_state=OUT,
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
