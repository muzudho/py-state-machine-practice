import sys

from lesson07.main_and_finally import MainAndFinally
from lesson08.echo_server import EchoServer

echo_server = None


def __on_main():
    echo_server = EchoServer(host="0.0.0.0", port=5002)
    echo_server.run()


def __on_finally():
    # [Ctrl] + [C] を受け付けないから、ここにくるのは難しい
    echo_server.clean_up()
    print("★しっかり終わった")


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainAndFinally(on_main=__on_main, on_finally=__on_finally).run())
