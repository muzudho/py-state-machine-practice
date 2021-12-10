import sys
import time

from lesson07.main_and_exit import MainAndExit


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":

    def __on_main():
        """ここに処理を書いてください"""

        # print("0除算")
        # print(7/0)

        # [Ctrl] + [C]

        print("7秒待つので好きな強制終了をしろだぜ")
        for i in range(0, 6):
            time.sleep(1)
            print(6-i)

        time.sleep(1)

    def __on_exit():
        """終了時にやりたい処理をここに書いてください"""
        print("★しっかり終わった")

    sys.exit(MainAndExit(on_main=__on_main, on_exit=__on_exit).run())
