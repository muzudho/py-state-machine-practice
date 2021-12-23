import sys


from lesson07n2.main_finally import MainFinally
from lesson18.server import Server
from lesson18_data.step1n2_auto_const.pen_const import INIT
from lesson18_data.pen_step4_state_gen import pen_state_gen_v18
from lesson14_data.step2_pen_transition import pen_transition_py_dict

server = None


class Main:
    def on_main(self):
        server = Server(
            state_gen=pen_state_gen_v18,
            transition_py_dict=pen_transition_py_dict,
            host="0.0.0.0",
            port=5002,
            entry_state=INIT,
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
