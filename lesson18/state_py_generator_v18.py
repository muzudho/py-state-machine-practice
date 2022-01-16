import sys
import argparse
import traceback

from lesson07n2.main_finally import MainFinally
from lesson11n90.code_gen.toml_reader_v11n90 import TomlReaderV11n90
from lesson11n100.code_gen.json_reader_v11n100 import JsonReaderV11n100
from lesson18.code_gen.state_files_gen_v18 import gen_state_files_v18
from lesson18.conf_obj.const_v18 import ConstV18
from lesson16n3.conf_obj.transition_v16n3 import TransitionV16n3


class Main:
    def on_main(self):
        parser = argparse.ArgumentParser(description='設定ファイルを読み込みます')
        parser.add_argument('conf',
                            help='設定ファイルへのパス')
        parser.add_argument('const_input_property',
                            help='定数の読込ファイル（JSON形式）へのパスが書いてあるプロパティのキー')
        parser.add_argument('transition_input_property',
                            help='状態遷移の読込ファイル（JSON形式）へのパスが書いてあるプロパティのキー')
        parser.add_argument('output_property',
                            help='書込先ディレクトリーへのパスが書いてあるプロパティのキー')
        parser.add_argument('import_module',
                            help='[import_module]テーブル下の、import文のモジュールへのパスが入ったプロパティの名前')
        args = parser.parse_args()

        # 設定ファイル（.toml）読取
        toml_doc = TomlReaderV11n90.read_file(args.conf)

        # TOMLの内容を読み取ります
        const_file_path = toml_doc[args.const_input_property]
        transition_file_path = toml_doc[args.transition_input_property]
        output_states_dir = toml_doc[args.output_property]
        import_module_const = toml_doc['import_module'][args.import_module]

        # JSONファイルを読込みます
        const_doc = JsonReaderV11n100.read_file(
            const_file_path)
        transition_doc = JsonReaderV11n100.read_file(
            transition_file_path)

        const = ConstV18(const_doc)
        transition = TransitionV16n3(doc=transition_doc)

        # ファイル生成
        gen_state_files_v18(
            const=const,
            transition=transition,
            import_module_path=import_module_const,
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
