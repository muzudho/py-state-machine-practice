import sys
import argparse


from lesson07n2.main_finally import MainFinally
from lesson11n90.code_gen.toml_reader import TomlReaderV11n90
from lesson11n100.code_gen.json_reader import JsonReaderV11n100
from lesson18.server_v18 import ServerV18
from lesson18.state_machine_v18 import StateMachineV18
from lesson18_projects.pen.auto_gen.data.const import INIT
from lesson18_projects.pen.data.state_gen import pen_state_gen_v18

server = None


class Main:
    def on_main(self):
        parser = argparse.ArgumentParser(description='設定ファイルを読み込みます')
        parser.add_argument('conf', help='設定ファイルへのパス')
        args = parser.parse_args()

        # 設定ファイル（.toml）読取
        toml_doc = TomlReaderV11n90.read_file(args.conf)

        # TOMLの内容を読み取ります
        transition_file_path = toml_doc['transition_file']

        # JSONファイルを読込みます
        transition_doc = JsonReaderV11n100.read_file(
            transition_file_path)

        # 状態遷移マシン
        state_machine = StateMachineV18(
            state_gen=pen_state_gen_v18,
            transition_py_dict=transition_doc,
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
