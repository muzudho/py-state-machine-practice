import sys
import argparse
import traceback

from lesson07n2.main_finally import MainFinally
from lesson11n90.code_gen.toml_reader_v11n90 import TomlReaderV11n90
from lesson11n100.code_gen.json_reader_v11n100 import JsonReaderV11n100
from lesson17.code_gen.const_file_gen_v17 import gen_const_file_v17


class Main:
    """定数を定義した .pyファイルを作成します

    Examples
    --------
    # 入力ファイル example-const.json
    {
        "CLOSE_DOOR": "CloseDoor",
        "OPEN_DOOR": "OpenDoor",
        "E_TURNED_KNOB": "turned_knob",
        "E_PULLED_KNOB": "pulled_knob",
        "MSG_TURN_KNOB": "Turn knob",
        "MSG_PULL_KNOB": "Pull knob",
    }

    # 出力ファイル example_const.py
    CLOSE_DOOR = 'CloseDoor'
    OPEN_DOOR = 'OpenDoor'
    E_TURNED_KNOB = 'turned_knob'
    E_PULLED_KNOB = 'pulled_knob'
    MSG_TURN_KNOB = 'Turn knob'
    MSG_PULL_KNOB = 'Pull knob'
    """

    def on_main(self):
        parser = argparse.ArgumentParser(description='定数を定義した .pyファイルを作成します')
        parser.add_argument('conf', help='設定ファイルへのパス')
        parser.add_argument(
            'input_property', help='読込ファイル（JSON形式）へのパスが書いてあるプロパティのキー')
        parser.add_argument(
            'output_property', help='書込ファイル（Python形式）へのパスが書いてあるプロパティのキー')
        args = parser.parse_args()

        # 設定ファイル（.toml）読取
        toml_doc = TomlReaderV11n90.read_file(args.conf)

        # TOMLの内容を読み取ります
        input_const_file_path = toml_doc['input_const_file']
        output_const_file_path = toml_doc['output_const_file']

        # JSONファイルを読込みます
        const_doc = JsonReaderV11n100.read_file(
            input_const_file_path)

        # 定数ファイル生成
        gen_const_file_v17(const_doc, output_const_file_path)
        return 0

    def on_except(self, e):
        """ここで例外キャッチ"""
        traceback.print_exc()

    def on_finally(self):
        print("★これで終わり")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
