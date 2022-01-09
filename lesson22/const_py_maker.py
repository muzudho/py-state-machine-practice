import sys
import argparse

from lesson07n2.main_finally import MainFinally
from lesson17.code_gen.const_file_gen import gen_const_file_v17
from lesson20.transition_json_reader import TransitionJsonReader

class Main:
    def on_main(self):
        parser = argparse.ArgumentParser(description='(定数).pyファイルを作成します')
        parser.add_argument('input', help='定数を定義した入力ファイル(.json)')
        parser.add_argument('output', help='出力ファイル(.py)')
        args = parser.parse_args()

        print(f'args.input : {args.input}') # Example: "lesson22_data/step1-house3-const.json"
        print(f'args.output: {args.output}') # Example: "lesson22_data/step1n2_auto_const/house3_const.py"

        # JSON構造（順序付きDict）に変換 --> 出力
        transition_json_obj = TransitionJsonReader.read_file(args.input)
        gen_const_file_v17(args.output, transition_json_obj)
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
