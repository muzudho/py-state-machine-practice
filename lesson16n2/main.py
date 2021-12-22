import sys

from lesson07n2.main_finally import MainFinally
from lesson16n2.code_gen.state_files_gen import gen_state_files_v16n2

STEP2_AUTO_DIR_PATH = "lesson16n2/step2n2_auto"


class Main:
    def on_main(self):
        gen_state_files_v16n2(STEP2_AUTO_DIR_PATH)
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
