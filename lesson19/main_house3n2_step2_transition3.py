import sys
import argparse

from lesson07n2.main_finally import MainFinally
from lesson11n90.code_gen.toml_reader import TomlReaderV11n90
from lesson11n100.code_gen.json_reader import JsonReaderV11n100
from lesson19.code_gen.transition_json_writer import TransitionJsonWriter
from lesson16n3.code_gen.transition_conf_v16n3 import TransitionConfV16n3


OUTPUT_FILE_PATH = "lesson19_projects/house3n2/auto_gen/data/transition2.json"


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
        transition_doc = JsonReaderV11n100.read_file(transition_file_path)

        transition_doc = TransitionConfV16n3(transition_doc)
        TransitionJsonWriter.write(
            file_path=OUTPUT_FILE_PATH,
            title=transition_doc.title,
            entry_state=transition_doc.entry_state,
            data=transition_doc.data,
        )
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
