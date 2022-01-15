import sys

from lesson07n2.main_finally import MainFinally
from lesson08.echo_server import EchoServer

echo_server = None


class Main:
    def on_main(self):
        echo_server = EchoServer(host="0.0.0.0", port=5002)
        echo_server.run()
        return 0

    def on_except(self, e):
        """ここで例外キャッチ"""
        print(e)

    def on_finally(self):
        # [Ctrl] + [C] を受け付けないから、ここにくるのは難しい
        if echo_server:
            echo_server.clean_up()

        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
