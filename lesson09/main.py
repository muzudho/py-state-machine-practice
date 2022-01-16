import sys
import traceback

from lesson07n2.main_finally import MainFinally
from lesson09.client import Client

client = None


class Main:
    def on_main(self):
        client = Client(server_host="127.0.0.1", server_port=5002)
        client.run()
        return 0

    def on_except(self, e):
        """ここで例外キャッチ"""
        traceback.print_exc()

    def on_finally(self):
        if client:
            client.clean_up()

        print("★これで終わり")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
