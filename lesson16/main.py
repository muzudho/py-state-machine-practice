import sys

from lesson07n2.main_finally import MainFinally
from lesson16.code_gen.init_file_gen import gen_init_file

render = None


class Main:
    def on_main(self):
        gen_init_file()
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
