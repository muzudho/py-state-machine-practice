import sys

from lesson07.main_and_finally import MainAndFinally
from lesson09.client import Client

client = None


def __on_main():
    client = Client(server_host="127.0.0.1", server_port=5002)
    client.run()


def __on_finally():
    if client:
        client.clean_up()

    print("★しっかり終わった")


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainAndFinally(on_main=__on_main, on_finally=__on_finally).run())
