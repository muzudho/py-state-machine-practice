import sys

from lesson07n2.main_finally import MainFinally
from lesson17.code_gen.const_file_gen import gen_const_file
from lesson17.step1_const_conf_wcsc_v2 import const_conf_py_dict


class Main:
    def on_main(self):
        # 定数は transition_conf.py を作るために必要なので、先に作っておいてほしい
        output_file_path = "lesson17/step1n2_auto_const/pen.py"
        gen_const_file(output_file_path, const_conf_py_dict)
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
