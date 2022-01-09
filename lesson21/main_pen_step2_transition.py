import sys
import os

from lesson07n2.main_finally import MainFinally
from lesson16.code_gen.file_io import FileIo
from lesson20.json_reader_v20 import JsonReaderV20
from lesson21.code_gen.transition_conf_py_stringification import (
    TransitionConfPyStringification,
)
from lesson18_data.pen_step1_const_dict import pen_const_py_dict

INPUT_TRANSITION_JSON_FILE_PATH = "lesson19_data/step2_auto/pen-transition.json"
OUTPUT_AUTO_TRANSITION_FILE_PATH = "lesson21_data/step2n2_auto/step2_pen_transition.py"
OUTPUT_TRANSITION_VARIABLE_NAME = "pen_transition_py_dict"


class Main:
    def on_main(self):
        data = JsonReaderV20.read_file(INPUT_TRANSITION_JSON_FILE_PATH)

        transition_conf_py_stringification = TransitionConfPyStringification(
            const_py_dict=pen_const_py_dict,
            import_from_path="lesson18_data.step1n2_auto_const.pen_const",
        )
        out_text = transition_conf_py_stringification.stringify(
            variable_name=OUTPUT_TRANSITION_VARIABLE_NAME, ordered_dict_data=data
        )

        FileIo.makedirs(os.path.dirname(OUTPUT_AUTO_TRANSITION_FILE_PATH))
        print(f"[L21] write {OUTPUT_AUTO_TRANSITION_FILE_PATH}")
        FileIo.write(OUTPUT_AUTO_TRANSITION_FILE_PATH, out_text)

        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
