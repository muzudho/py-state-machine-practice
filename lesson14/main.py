import sys
import argparse
import traceback

from lesson07n2.main_finally import MainFinally
from lesson11n90.code_gen.toml_reader_v11n90 import TomlReaderV11n90
from lesson11n100.code_gen.json_reader_v11n100 import JsonReaderV11n100
from lesson14.server_v14 import ServerV14

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

        # サーバー起動
        server = ServerV14(
            transition_doc=transition_doc, host="0.0.0.0", port=5002)
        server.run()
        return 0

    def on_except(self, e):
        """ここで例外キャッチ"""
        traceback.print_exc()

    def on_finally(self):
        # [Ctrl] + [C] を受け付けないから、ここにくるのは難しい
        if server:
            server.clean_up()

        print("★これで終わり")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
