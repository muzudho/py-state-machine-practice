import sys

from lesson07n2.main_finally import MainFinally
from lesson17.code_gen.const_file_gen import gen_const_file_v17
from lesson20.code_gen.json_reader import JsonReaderV20

INPUT_CONST_JSON_FILE_PATH = "lesson22_data/step1-house3-const.json"
OUTPUT_CONST_PY_FILE_PATH = "lesson23_data/step1n2_auto_const/house3n2_const.py"


class Main:
    def on_main(self):
        transition_json_obj = JsonReaderV20.read_file(INPUT_CONST_JSON_FILE_PATH)

        # 定数は transition_conf.py を作るために必要なので、先に作っておいてほしい
        gen_const_file_v17(OUTPUT_CONST_PY_FILE_PATH, transition_json_obj)
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
