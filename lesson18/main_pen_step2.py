import sys
import argparse

from lesson07n2.main_finally import MainFinally
from lesson11n90.code_gen.toml_reader import TomlReaderV11n90
from lesson11n100.code_gen.json_reader import JsonReaderV11n100
from lesson18.code_gen.state_files_gen import gen_state_files_v18
from lesson18_projects.pen.data.const_dict import pen_const_py_dict

OUTPUT_STEP2_AUTO_STATE_DIR = "lesson18_projects/pen/auto_gen/code/states"
IMPORT_FROM_PATH = "lesson18_projects.pen.auto_gen.data.const"


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

        # ファイル生成
        gen_state_files_v18(
            dir_path=OUTPUT_STEP2_AUTO_STATE_DIR,
            const_py_dict=pen_const_py_dict,
            transition_py_dict=transition_doc,
            import_from_path=IMPORT_FROM_PATH,
        )
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
