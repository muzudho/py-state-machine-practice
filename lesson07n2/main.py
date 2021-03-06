import sys
import time
import traceback
from multiprocessing.sharedctypes import Value

from lesson07n2.main_finally import MainFinally


class Main:
    def on_main(self):
        """ここに処理を書いてください"""

        # print("0除算")
        # print(7/0)

        # [Ctrl] + [C]

        print("7秒待つので好きな強制終了をしろだぜ")
        for i in range(0, 6):
            time.sleep(1)
            print(6 - i)

        time.sleep(1)

        # 例外のテスト: raise ValueError("☆（＾～＾）")

        return 0

    def on_except(self, e):
        # ここで例外キャッチ
        traceback.print_exc()

    def on_finally(self):
        """終了時にやりたい処理をここに書いてください"""
        print("★これで終わり")

        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
