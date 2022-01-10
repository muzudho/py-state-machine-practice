import sys

from lesson07n2.main_finally import MainFinally
from lesson16n3.code_gen.state_files_gen import gen_state_files_v16n3

OUTPUT_DIR_PATH = "lesson16n3_projects/wcsc/auto_gen/code/states"


class Main:
    def on_main(self):
        gen_state_files_v16n3(OUTPUT_DIR_PATH)
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
