import sys
import json
import os

from lesson07n2.main_finally import MainFinally
from lesson17.code_gen.const_file_gen import gen_const_file_v17
from lesson20.transition_json_reader import TransitionJsonReader
from lesson16.code_gen.file_io import FileIo

INPUT_JSON_FILE_PATH = "lesson22_data/step1_house3_const.json"
OUTPUT_JSON_FILE_PATH = "lesson22_data/step1n2_auto_const/house3_const.json"
OUTPUT_FILE_PATH = "lesson22_data/step1n2_auto_const/house3_const.py"


class Main:
    def on_main(self):
        transition_json_obj = TransitionJsonReader.read_file(INPUT_JSON_FILE_PATH)

        # フォーマッティング無しで出力するなら
        out_text = json.dumps(transition_json_obj, indent=4, ensure_ascii=False)
        FileIo.makedirs(os.path.dirname(OUTPUT_JSON_FILE_PATH))
        print(f"[L20] write {OUTPUT_JSON_FILE_PATH}")
        FileIo.write(OUTPUT_JSON_FILE_PATH, out_text)

        # TODO json_obj(JSON) を dict等 に変換したい。 OrderedDict は dict というより tupleのlistに近い
        print(f"[L20] transition_json_obj {transition_json_obj}")

        # dict等 に変換できれば、既存コードに引き渡せます
        # gen_const_file_v17(OUTPUT_FILE_PATH, house3_const_py_dict)
        gen_const_file_v17(OUTPUT_FILE_PATH, transition_json_obj)
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
