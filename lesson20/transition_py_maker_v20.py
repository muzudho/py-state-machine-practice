import sys
import json
import os
import argparse

from lesson07n2.main_finally import MainFinally
from lesson11n100.code_gen.json_reader import JsonReaderV11n100
from lesson16.code_gen.file_io import FileIo
from lesson10019.code_gen.transition_json_writer import TransitionJsonWriter


class Main:
    def on_main(self):
        parser = argparse.ArgumentParser(
            description='状態遷移を定義した .jsonファイルを元に、状態遷移を定義した .pyファイルを作成します')
        parser.add_argument('input', help='状態遷移を定義した入力ファイル(.json)')
        parser.add_argument('output', help='状態遷移を定義した出力ファイル(.py)')
        parser.add_argument('--output_default_format',
                            help='状態遷移を定義した出力ファイル(.py)デフォルトのフォーマットの確認用')
        args = parser.parse_args()

        # Example: "lesson10019_projects/house3n2/data/auto_gen/transition2.json"
        print(f'args.input  : {args.input}')
        # Example: "lesson20_projects/house3n2/data/auto_gen/transition3.json"
        print(f'args.output : {args.output}')
        # Example: "lesson20_projects/house3n2/data/auto_gen/transition3-default-fomat.json"
        print(f'args.output_default_format : {args.output_default_format}')

        # JSONファイルを読込みます
        transition_doc = JsonReaderV11n100.read_file(args.input)
        # print(f"transition_doc={transition_doc}")

        # デフォルトのフォーマッティングで出力するなら
        out_text = json.dumps(transition_doc, indent=4, ensure_ascii=False)
        FileIo.makedirs(os.path.dirname(args.output_default_format))
        print(f"[L20] write {args.output_default_format}")
        FileIo.write(args.output_default_format, out_text)

        # フォーマッティングするなら
        print(f"[L20] write {args.output}")
        TransitionJsonWriter.write(
            file_path=args.output,
            title=transition_doc["title"],
            entry_state=transition_doc["entry_state"],
            data=transition_doc["data"],
        )

        return 0

    def on_except(self, e):
        """ここで例外キャッチ"""
        print(e)

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
