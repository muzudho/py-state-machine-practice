import sys
import json
import os
import argparse
import traceback

from lesson07n2.main_finally import MainFinally
from lesson11n100.code_gen.json_reader_v11n100 import JsonReaderV11n100
from lesson11n80.code_gen.file_io import FileIo


class Main:
    def on_main(self):
        parser = argparse.ArgumentParser(
            description='状態遷移を定義した .jsonファイルを元に、状態遷移を定義した .pyファイルを作成します')
        parser.add_argument('input', help='状態遷移を定義した入力ファイル(.json)')
        parser.add_argument('output', help='状態遷移を定義した出力ファイル(.py)')
        args = parser.parse_args()

        # Example: "lesson17n2_projects/example-v17n2/example.json"
        print(f'args.input  : {args.input}')
        # Example: "lesson17n2_projects/example-v17n2/auto_gen/example.json"
        print(f'args.output : {args.output}')

        # JSONファイルを読込みます
        transition_doc = JsonReaderV11n100.read_file(args.input)
        # print(f"transition_doc={transition_doc}")

        # JSONファイルを出力します
        out_text = json.dumps(transition_doc, indent=4, ensure_ascii=False)
        FileIo.makedirs(os.path.dirname(args.output))
        print(f"[L20] write {args.output}")
        FileIo.write(args.output, out_text)

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
