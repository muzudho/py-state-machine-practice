import sys
import argparse

from lesson07n2.main_finally import MainFinally
from lesson11n90.code_gen.toml_reader import TomlReaderV11n90
from lesson11n100.code_gen.json_reader import JsonReaderV11n100
from lesson15.conf_obj.transition_v15 import TransitionV15
from lesson15n2.graph_gen.render_v15n2 import GraphRenderV15n2


class Main:
    def __init__(self):
        self._graph_render = None

    def on_main(self):
        parser = argparse.ArgumentParser(description='設定ファイルを読み込みます')
        parser.add_argument('conf', help='設定ファイルへのパス')
        args = parser.parse_args()

        # 設定ファイル（.toml）読取
        toml_doc = TomlReaderV11n90.read_file(args.conf)

        # TOMLの内容を読み取ります
        transition_file_path = toml_doc['transition_file']

        # JSONファイルを読込みます
        transition_doc = JsonReaderV11n100.read_file(
            transition_file_path)

        # オブジェクト作成
        transition = TransitionV15(transition_doc)

        # グラフ描画
        self._graph_render = GraphRenderV15n2(transition=transition)
        self._graph_render.run()
        return 0

    def on_except(self, e):
        """ここで例外キャッチ"""
        print(e)

    def on_finally(self):
        # [Ctrl] + [C] を受け付けないから、ここにくるのは難しい
        if self._graph_render:
            self._graph_render.clean_up()

        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
