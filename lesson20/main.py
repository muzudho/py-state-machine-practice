import sys

from lesson07n2.main_finally import MainFinally
from lesson20.transition_json_reader import TransitionJsonReader

JSON_FILE_PATH = "lesson19/auto/transition_pen.json"


class Main:
    def on_main(self):
        TransitionJsonReader.read_file(JSON_FILE_PATH)
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
