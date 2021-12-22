import sys

from lesson07n2.main_finally import MainFinally
from lesson17.code_gen.const_file_gen import gen_const_file_v17
from lesson17_data.step1_pen_const_dict import pen_const_py_dict

OUTPUT_FILE_PATH = "lesson17_data/step1n2_auto_const/pen_const.py"


class Main:
    def on_main(self):
        # 定数は transition_conf.py を作るために必要なので、先に作っておいてほしい
        gen_const_file_v17(OUTPUT_FILE_PATH, pen_const_py_dict)
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
