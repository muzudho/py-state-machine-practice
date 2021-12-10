import sys
import signal


class MainAndFinally():
    def __init__(self, on_main, on_finally):
        self.on_main = on_main
        self.on_finally = on_finally

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
            self.on_finally()

            # 強制終了のシグナルを有効に戻します
            signal.signal(signal.SIGTERM, signal.SIG_DFL)
            signal.signal(signal.SIGINT, signal.SIG_DFL)

    def on_main(self):
        pass

    def on_finally(self):
        pass
