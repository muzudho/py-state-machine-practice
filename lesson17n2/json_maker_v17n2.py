import sys
import json
import os
import argparse

from lesson07n2.main_finally import MainFinally
from lesson16.code_gen.file_io import FileIo
from lesson17n2.code_gen.json_reader import JsonReaderV17n2


class Main:
    def on_main(self):
        parser = argparse.ArgumentParser(description='状態遷移を定義した .jsonファイルを元に、状態遷移を定義した .pyファイルを作成します')
        parser.add_argument('input', help='状態遷移を定義した入力ファイル(.json)')
        parser.add_argument('output', help='状態遷移を定義した出力ファイル(.py)')
        args = parser.parse_args()

        print(f'args.input  : {args.input}') # Example: "lesson17n2_data/example-v17n2.json"
        print(f'args.output : {args.output}') # Example: "lesson17n2_data/auto_gen/example-v17n2.json"

        # JSONファイルを読込みます
        transition_json_obj = JsonReaderV17n2.read_file(args.input)
        # print(f"transition_json_obj={transition_json_obj}")

        # JSONファイルを出力します
        out_text = json.dumps(transition_json_obj, indent=4, ensure_ascii=False)
        FileIo.makedirs(os.path.dirname(args.output))
        print(f"[L20] write {args.output}")
        FileIo.write(args.output, out_text)

        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
