import sys
import argparse

from lesson07n2.main_finally import MainFinally
from lesson11n80.code_gen.file_io import FileIo


class Main:
    def on_main(self):
        parser = argparse.ArgumentParser(description='設定ファイルを読み込みます')
        parser.add_argument('conf', help='設定ファイルへのパス')
        args = parser.parse_args()

        # 設定ファイル（.toml）読取
        text = FileIo.read(args.conf)

        # 表示
        print(f"text\n----\n{text}")
        return 0

    def on_except(self, e):
        """ここで例外キャッチ"""
        print(e)

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
