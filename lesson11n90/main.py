import sys
import argparse
from tomlkit import dumps

from lesson07n2.main_finally import MainFinally
from lesson11n90.code_gen.toml_reader import TomlReaderV11n90


class Main:
    def on_main(self):
        parser = argparse.ArgumentParser(description='TOMLファイルを読み込みます')
        parser.add_argument('input', help='TOMLファイルへのパス')
        args = parser.parse_args()

        print(f'args.input  : {args.input}') # Example: "lesson11n90_projects/example/data/example.toml"

        # TOMLファイルを読込みます
        toml_doc = TomlReaderV11n90.read_file(args.input)
        # その内容を表示します
        toml_text = dumps(toml_doc)
        print(f"toml_text={toml_text}")
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
