import sys

from lesson07n2.main_finally import MainFinally
from lesson17.render_step1 import Render

render = None


class Main:
    def on_main(self):
        render = Render()
        render.run()
        return 0

    def on_finally(self):
        if render:
            render.clean_up()

        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
