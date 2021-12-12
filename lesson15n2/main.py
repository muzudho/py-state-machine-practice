import sys

from lesson07.main_and_finally import MainAndFinally
from lesson15n2.render import Render

server = None


def __on_main():
    server = Render()
    server.run()


def __on_finally():
    # [Ctrl] + [C] を受け付けないから、ここにくるのは難しい
    if server:
        server.clean_up()

    print("★しっかり終わった")


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainAndFinally(on_main=__on_main, on_finally=__on_finally).run())
