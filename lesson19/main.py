import sys

from lesson07n2.main_finally import MainFinally
from lesson19.transition_json_writer import TransitionJsonWriter
from lesson16n3.transition_conf_v1n3 import TransitionConfV1n3
from lesson19.step2_transition_conf_pen import (
    transition_conf_data as transition_conf_pen,
)


class Main:
    def on_main(self):
        transition_conf = TransitionConfV1n3(transition_conf_pen)
        TransitionJsonWriter.write(
            "lesson19/auto/transition_pen.json", transition_conf.data
        )
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
