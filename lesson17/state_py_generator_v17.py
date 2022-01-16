import sys
import argparse
import traceback

from lesson07n2.main_finally import MainFinally
from lesson11n90.code_gen.toml_reader_v11n90 import TomlReaderV11n90
from lesson11n100.code_gen.json_reader_v11n100 import JsonReaderV11n100
from lesson17.code_gen.state_files_gen import gen_state_files_v17
from lesson17_projects.wcsc.data.const import wcsc_const_doc


class Main:
    def on_main(self):
        parser = argparse.ArgumentParser(description='設定ファイルを読み込みます')
        parser.add_argument('conf', help='設定ファイルへのパス')
        parser.add_argument(
            'input_property', help='読込ファイル（JSON形式）へのパスが書いてあるプロパティのキー')
        parser.add_argument(
            'output_property', help='書込先ディレクトリーへのパスが書いてあるプロパティのキー')
        args = parser.parse_args()

        # 設定ファイル（.toml）読取
        toml_doc = TomlReaderV11n90.read_file(args.conf)

        # TOMLの内容を読み取ります
        transition_file_path = toml_doc[args.input_property]
        output_states_dir = toml_doc[args.output_property]

        # JSONファイルを読込みます
        transition_doc = JsonReaderV11n100.read_file(
            transition_file_path)

        # ファイル生成
        gen_state_files_v17(
            const_doc=wcsc_const_doc,
            transition_doc=transition_doc,
            output_dir_path=output_states_dir,
        )
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
