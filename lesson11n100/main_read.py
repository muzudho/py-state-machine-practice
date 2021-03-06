import sys
import json
import argparse
import traceback

from lesson07n2.main_finally import MainFinally
from lesson11n100.code_gen.json_reader_v11n100 import JsonReaderV11n100


class Main:
    def on_main(self):
        parser = argparse.ArgumentParser(description='JSONファイルを読み込みます')
        parser.add_argument('input', help='JSONファイルへのパス')
        args = parser.parse_args()

        # Example: "lesson11n100_projects/example-v11n100/example.json"
        print(f'args.input  : {args.input}')

        # JSONファイルを読込みます
        doc = JsonReaderV11n100.read_file(args.input)
        # その内容を表示します
        jso_text = json.dumps(doc, indent=4, ensure_ascii=False)
        print(f"Java Script Object (Text)={jso_text}")
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
