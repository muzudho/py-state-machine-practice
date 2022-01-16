import sys
import argparse
import traceback

from lesson07n2.main_finally import MainFinally
from lesson11n100.code_gen.json_reader_v11n100 import JsonReaderV11n100
from lesson18.code_gen.state_files_gen import gen_state_files_v18


class Main:
    """状態を定義した .pyファイルを作成します

    Examples
    --------
    # Windows
    python.exe -m lesson23.state_py_maker "example-const.json" "example-transition.json" "lesson23_projects.house3n2.data.auto_gen.const" "lesson23/house3n2/auto_gen/states"
    #                                     -------------------- ------------------------- ------------------------------------------------ -----------------------------------
    #                                     定数定義ファイル       状態遷移定義ファイル        import文に書く文字列                              出力ディレクトリ
    """

    def on_main(self):
        parser = argparse.ArgumentParser(description='ステートを定義した .pyファイルを作成します')
        parser.add_argument('input_const', help='定数を定義した入力ファイル(.json)')
        parser.add_argument('input_transition', help='状態遷移を定義した入力ファイル(.json)')
        parser.add_argument('import_module', help='import文に書く文字列')
        parser.add_argument('output', help='状態を定義したファイルを出力するディレクトリ')
        args = parser.parse_args()

        # Example: "lesson18n2_projects/house3/data/const.json"
        print(f'args.input_const : {args.input_const}')
        # Example: "lesson20_projects/house3n2/data/auto_gen/transition3.json"
        print(f'args.input_transition : {args.input_transition}')
        # Example: "lesson23_projects.house3n2.data.auto_gen.const"
        print(f'args.import_module : {args.import_module}')
        # Example: "lesson23/house3n2/auto_gen/states"
        print(f'args.output : {args.output}')

        # JSONファイルから、定数と遷移の設定を読込みます
        const_json_obj = JsonReaderV11n100.read_file(args.input_const)
        transition_doc = JsonReaderV11n100.read_file(args.input_transition)

        # 状態の .py スクリプトを出力します
        gen_state_files_v18(
            dir_path=args.output,
            const_doc=const_json_obj,
            transition_doc=transition_doc,
            import_from_path=args.import_module,
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
