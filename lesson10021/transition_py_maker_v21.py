import sys
import os
import argparse
import traceback

from lesson07n2.main_finally import MainFinally
from lesson11n100.code_gen.json_reader_v11n100 import JsonReaderV11n100
from lesson11n80.code_gen.file_io_v11n80 import FileIoV11n80
from lesson10021.code_gen.transition_stringification import (
    TransitionConfPyStringification,
)
from lesson18.conf_obj.const_v18 import ConstV18


class Main:
    def on_main(self):
        parser = argparse.ArgumentParser(
            description='状態遷移を定義した .jsonファイルを元に、状態遷移を定義した .pyファイルを作成します')
        parser.add_argument('input_const', help='定数を定義した入力ファイル(.json)')
        parser.add_argument('input_transition', help='状態遷移を定義した入力ファイル(.json)')
        parser.add_argument('output', help='状態遷移を定義した出力ファイル(.py)')
        parser.add_argument('import_module', help='import文に書く文字列')
        parser.add_argument('var_name', help='状態遷移ディクショナリーの変数名')
        args = parser.parse_args()

        const_doc = JsonReaderV11n100.read_file(args.input_const)
        transition_data = JsonReaderV11n100.read_file(args.input_transition)

        const = ConstV18(const_doc)

        transition_stringification = TransitionConfPyStringification(
            const=const,
            import_from_path=args.import_module,
        )
        out_text = transition_stringification.stringify(
            variable_name=args.var_name, ordered_dict_data=transition_data
        )

        FileIoV11n80.makedirs(os.path.dirname(args.output))
        print(f"[L21] write {args.output}")
        FileIoV11n80.write(args.output, out_text)

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
