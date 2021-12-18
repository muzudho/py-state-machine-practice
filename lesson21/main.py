import sys
import json

from lesson07n2.main_finally import MainFinally
from lesson16.code_gen.file_io import FileIo
from lesson20.transition_json_reader import TransitionJsonReader
from lesson21.code_gen.transition_conf_py_stringification import (
    TransitionConfPyStringification,
)

INPUT_JSON_FILE_PATH = "lesson19/auto/transition-pen.json"
OUTPUT_AUTO_DIR_PATH = "lesson21/auto"
OUTPUT_AUTO_FILE_PATH = "lesson21/auto/transition_conf.py"


class Main:
    def on_main(self):
        data = TransitionJsonReader.read_file(INPUT_JSON_FILE_PATH)

        # TODO Stringify
        out_text = TransitionConfPyStringification.stringify(data)

        FileIo.makedirs(OUTPUT_AUTO_DIR_PATH)
        print(f"[L21] write {OUTPUT_AUTO_FILE_PATH}")
        FileIo.write(OUTPUT_AUTO_FILE_PATH, out_text)

        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
