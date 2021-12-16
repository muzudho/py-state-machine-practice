import sys

from lesson07n2.main_finally import MainFinally
from lesson16n2.code_gen.state_file_gen import gen_state_file


class Main:
    def on_main(self):
        gen_state_file()
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
