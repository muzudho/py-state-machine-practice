import sys
import signal
import time


class MainAndExit():
    def __init__(self):
        pass

    def run(self):

        def sigterm_handler(_signum, _frame) -> None:
            sys.exit(1)

        # 強制終了のシグナルを受け取ったら、強制終了するようにします
        signal.signal(signal.SIGTERM, sigterm_handler)

        try:
            # ここで何か処理
            self.on_main()
        finally:
            # 強制終了のシグナルを無視するようにしてから、クリーンアップ処理へ進みます
            signal.signal(signal.SIGTERM, signal.SIG_IGN)
            signal.signal(signal.SIGINT, signal.SIG_IGN)

            # ここで終了処理
            self.on_exit()

            # 強制終了のシグナルを有効に戻します
            signal.signal(signal.SIGTERM, signal.SIG_DFL)
            signal.signal(signal.SIGINT, signal.SIG_DFL)

    def on_main(self):
        pass

    def on_exit(self):
        pass


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    main_and_exit = MainAndExit()

    def __on_main():
        """ここに処理を書いてください"""

        # print("0除算")
        # print(7/0)

        # [Ctrl] + [C]

        print("7秒待つので好きな強制終了をしろだぜ")
        for i in range(0, 7):
            time.sleep(1)
            print(6-i)

    main_and_exit.on_main = __on_main

    def __on_exit():
        """終了時にやりたい処理をここに書いてください"""
        print("★終わった")

    main_and_exit.on_exit = __on_exit

    sys.exit(main_and_exit.run())
