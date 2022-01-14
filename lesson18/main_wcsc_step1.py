import sys

from lesson07n2.main_finally import MainFinally
from lesson17.code_gen.const_file_gen import gen_const_file_v17
from lesson18_projects.wcsc.data.const import wcsc_const_doc

OUTPUT_CONST_FILE_PATH = "lesson18_projects/wcsc/auto_gen/data/const.py"


class Main:
    def on_main(self):
        # 定数は transition_conf.py を作るために必要なので、先に作っておいてほしい
        gen_const_file_v17(OUTPUT_CONST_FILE_PATH, wcsc_const_doc)
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
