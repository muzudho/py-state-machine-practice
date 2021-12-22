import sys

from lesson07n2.main_finally import MainFinally
from lesson18.code_gen.state_files_gen import gen_state_files

OUTPUT_DIR = "lesson18/pen_step2n2_auto_state"


class Main:
    def on_main(self):
        gen_state_files(OUTPUT_DIR)
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
