import sys
import argparse

from lesson07n2.main_finally import MainFinally
from lesson18.code_gen.state_files_gen import gen_state_files_v18
from lesson20.code_gen.json_reader import JsonReaderV20

class Main:
    def on_main(self):
        parser = argparse.ArgumentParser(description='ステートを定義した .pyファイルを作成します')
        parser.add_argument('input_const', help='定数を定義した入力ファイル(.json)')
        parser.add_argument('input_transition', help='状態遷移を定義した入力ファイル(.json)')
        parser.add_argument('import_module', help='import文に書く文字列')
        parser.add_argument('output', help='状態を定義したファイルを出力するディレクトリ')
        args = parser.parse_args()

        print(f'args.input_const : {args.input_const}') # Example: "lesson22_data/step1-house3-const.json"
        print(f'args.input_transition : {args.input_transition}') # Example: "lesson20_data/auto_gen/house3n2-transition3.json"
        print(f'args.import_module : {args.import_module}') # Example: "lesson23_data.auto_gen.house3n2_const"
        print(f'args.output : {args.output}') # Example: "lesson23/house3n2_step2n2_auto_state"


        # JSONファイルから、定数と遷移の設定を読込みます
        const_json_obj = JsonReaderV20.read_file(args.input_const)
        transition_json_obj = JsonReaderV20.read_file(args.input_transition)

        # 状態の .py スクリプトを出力します
        gen_state_files_v18(
            dir_path=args.output,
            const_py_dict=const_json_obj,
            transition_py_dict=transition_json_obj,
            import_from_path=args.import_module,
        )
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
