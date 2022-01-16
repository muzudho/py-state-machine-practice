import sys
import traceback

from lesson07n2.main_finally import MainFinally
from lesson11.server_v11 import ServerV11

server = None


class Main:
    def on_main(self):
        server = ServerV11(host="0.0.0.0", port=5002)
        server.run()
        return 0

    def on_except(self, e):
        """ここで例外キャッチ"""
        traceback.print_exc()

    def on_finally(self):
        # [Ctrl] + [C] を受け付けないから、ここにくるのは難しい
        if server:
            server.clean_up()

        print("★これで終わり")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
