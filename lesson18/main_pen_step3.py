import sys


from lesson07n2.main_finally import MainFinally
from lesson18.server_v18 import ServerV18
from lesson18.state_machine_v18 import StateMachineV18
from lesson18_projects.pen.auto_gen.data.const import INIT
from lesson18_projects.pen.data.state_gen import pen_state_gen_v18
from lesson14_projects.pen.data.transition import pen_transition_obj_v14

server = None


class Main:
    def on_main(self):

        # 状態遷移マシン
        state_machine = StateMachineV18(
            state_gen=pen_state_gen_v18,
            transition_py_dict=pen_transition_obj_v14,
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
