import sys
import argparse
import traceback

from lesson07n2.main_finally import MainFinally
from lesson11n90.code_gen.toml_reader_v11n90 import TomlReaderV11n90
from lesson11n100.code_gen.json_reader_v11n100 import JsonReaderV11n100
from lesson18.code_gen.state_files_gen_v18 import gen_state_files_v18
from lesson18_projects.pen.data.const import pen_const_doc
from lesson18.code_gen.const_v18 import ConstV18
from lesson16n3.conf_obj.transition_v16n3 import TransitionV16n3


class Main:
    def on_main(self):
        parser = argparse.ArgumentParser(description='設定ファイルを読み込みます')
        parser.add_argument('conf', help='設定ファイルへのパス')
        args = parser.parse_args()

        # 設定ファイル（.toml）読取
        toml_doc = TomlReaderV11n90.read_file(args.conf)

        # TOMLの内容を読み取ります
        transition_file_path = toml_doc['transition_file']
        output_states_dir = toml_doc['output_states_dir']
        import_const_module = toml_doc['import_const_module']

        # JSONファイルを読込みます
        transition_doc = JsonReaderV11n100.read_file(
            transition_file_path)

        const = ConstV18(pen_const_doc)
        transition = TransitionV16n3(transition_doc)

        # ファイル生成
        gen_state_files_v18(
            const=const,
            transition=transition,
            import_module_path=import_const_module,
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
