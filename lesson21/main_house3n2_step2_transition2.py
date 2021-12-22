import sys
import os

from lesson07n2.main_finally import MainFinally
from lesson16.code_gen.file_io import FileIo
from lesson20.transition_json_reader import TransitionJsonReader
from lesson21.code_gen.transition_conf_py_stringification import (
    TransitionConfPyStringification,
)

from lesson18_data.house3_step1_const_dict import house3_const_py_dict

INPUT_JSON_FILE_PATH = "lesson19_data/step2_auto/house3n2-transition2.json"
OUTPUT_AUTO_FILE_PATH = "lesson21_data/step2n2_auto/step2_house3n2_transition2.py"
OUTPUT_VARIABLE_NAME = "house3n2_transition2_py_dict"


class Main:
    def on_main(self):
        data = TransitionJsonReader.read_file(INPUT_JSON_FILE_PATH)

        transition_conf_py_stringification = TransitionConfPyStringification(
            house3_const_py_dict
        )
        out_text = transition_conf_py_stringification.stringify(
            variable_name=OUTPUT_VARIABLE_NAME, ordered_dict_data=data
        )

        FileIo.makedirs(os.path.dirname(OUTPUT_AUTO_FILE_PATH))
        print(f"[L21] write {OUTPUT_AUTO_FILE_PATH}")
        FileIo.write(OUTPUT_AUTO_FILE_PATH, out_text)

        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
