import sys
import os
import argparse

from lesson07n2.main_finally import MainFinally
from lesson16.code_gen.file_io import FileIo
from lesson17n2.code_gen.json_reader import JsonReaderV17n2
from lesson21.code_gen.transition_conf_py_stringification import (
    TransitionConfPyStringification,
)

from lesson18_projects.house3.data.const_dict import house3_const_py_dict

class Main:
    def on_main(self):
        parser = argparse.ArgumentParser(description='状態遷移を定義した .jsonファイルを元に、状態遷移を定義した .pyファイルを作成します')
        parser.add_argument('input', help='状態遷移を定義した入力ファイル(.json)')
        parser.add_argument('output', help='状態遷移を定義した出力ファイル(.py)')
        parser.add_argument('import_module', help='import文に書く文字列')
        parser.add_argument('var_name', help='状態遷移ディクショナリーの変数名')
        args = parser.parse_args()

        print(f'args.input  : {args.input}') # Example: "lesson19_projects/house3n2/data/auto_gen/transition2.json"
        print(f'args.output : {args.output}') # Example: "lesson21_projects/house3n2/data/auto_gen/transition2.py"
        print(f'args.import_module : {args.import_module}') # Example: "lesson18_projects.house3n2.data.auto_gen.const"
        print(f'args.var_name : {args.var_name}') # Example: "house3n2_transition2_py_dict"

        data = JsonReaderV17n2.read_file(args.input)

        transition_conf_py_stringification = TransitionConfPyStringification(
            const_py_dict=house3_const_py_dict,
            import_from_path=args.import_module,
        )
        out_text = transition_conf_py_stringification.stringify(
            variable_name=args.var_name, ordered_dict_data=data
        )

        FileIo.makedirs(os.path.dirname(args.output))
        print(f"[L21] write {args.output}")
        FileIo.write(args.output, out_text)

        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
