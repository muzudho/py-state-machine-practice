import sys
import argparse
import traceback

from lesson07n2.main_finally import MainFinally
from lesson11n90.code_gen.toml_reader_v11n90 import TomlReaderV11n90
from lesson11n100.code_gen.json_reader_v11n100 import JsonReaderV11n100
from lesson15.conf_obj.transition_v15 import TransitionV15
from lesson15n2.graph_gen.render_v15n2 import GraphRenderV15n2


class Main:
    """設定ファイル（.toml）を指定することで、状態遷移図を出力します。

    # コマンド
    python.exe -m this.is.a.module.graph_generator "this/is/a/path/conf.toml" "transition_file" "output_graph_text_file"

    上記のコマンドのケースでは、設定ファイルに必要な内容は以下の通りです。

    # 状態遷移図
    transition_file = "This/is/a/path/transition.json"

    # 状態遷移図の出力先
    output_graph_text_file = "This/is/a/path/transigion_graph.txt"
    """

    def __init__(self):
        self._graph_render = None

    def on_main(self):
        parser = argparse.ArgumentParser(description='設定ファイルを読み込みます')
        parser.add_argument('conf', help='設定ファイル（TOML形式）へのパス')
        parser.add_argument(
            'input_property', help='読込ファイル（JSON形式）へのパスが書いてあるプロパティのキー')
        parser.add_argument(
            'output_property', help='書込ファイル（テキストファイル形式）へのパスが書いてあるプロパティのキー')
        args = parser.parse_args()

        # 設定ファイル（.toml）読取
        toml_doc = TomlReaderV11n90.read_file(args.conf)

        # TOMLの内容を読み取ります
        transition_file_path = toml_doc[args.input_property]
        output_graph_text_file = toml_doc[args.output_property]

        # JSONファイルを読込みます
        transition_doc = JsonReaderV11n100.read_file(
            transition_file_path)

        # オブジェクト作成
        transition = TransitionV15(transition_doc)

        # グラフ描画
        self._graph_render = GraphRenderV15n2()
        self._graph_render.write(
            transition=transition,
            output_text_file=output_graph_text_file)
        return 0

    def on_except(self, e):
        """ここで例外キャッチ"""
        traceback.print_exc()

    def on_finally(self):
        # [Ctrl] + [C] を受け付けないから、ここにくるのは難しい
        if self._graph_render:
            self._graph_render.clean_up()

        print("★これで終わり")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
