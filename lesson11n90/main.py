import sys
import argparse
from tomlkit import dumps

from lesson07n2.main_finally import MainFinally
from lesson11n90.code_gen.toml_reader_v11n90 import TomlReaderV11n90
import traceback


class Main:
    def on_main(self):
        parser = argparse.ArgumentParser(description='TOMLファイルを読み込みます')
        parser.add_argument('input', help='TOMLファイルへのパス')
        args = parser.parse_args()

        # Example: "lesson11n90_projects/example/data/example.toml"
        print(f'args.input  : {args.input}')

        # TOMLファイルを読込みます
        toml_doc = TomlReaderV11n90.read_file(args.input)
        # その内容を表示します
        toml_text = dumps(toml_doc)
        print(f"toml_text-->{toml_text}")

        # TOMLの内容を読み取ってみましょう
        print(f"toml_doc['file_path']-->{toml_doc['file_path']}")
        return 0

    def on_except(self, e):
        """ここで例外キャッチ"""
        traceback.print_exc()

    def on_finally(self):
        print("★これで終わり")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
