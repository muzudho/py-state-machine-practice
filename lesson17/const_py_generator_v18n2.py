import sys
import argparse
import traceback

from lesson07n2.main_finally import MainFinally
from lesson17.code_gen.const_py_gen_v18n2 import gen_const_py_v18n2


class Main:
    """定数を定義した .pyファイルを作成します

    Examples
    --------
    # Windows
    python.exe -m lesson18n2.const_py_maker "example-const.json" "example_const.py"
    #                                       -------------------- ------------------
    #                                       入力ファイル           出力ファイル

    # example-const.json
    {
        "CLOSE_DOOR": "CloseDoor",
        "OPEN_DOOR": "OpenDoor",
        "E_TURNED_KNOB": "turned_knob",
        "E_PULLED_KNOB": "pulled_knob",
        "MSG_TURN_KNOB": "Turn knob",
        "MSG_PULL_KNOB": "Pull knob",
    }

    # example_const.py
    CLOSE_DOOR = 'CloseDoor'
    OPEN_DOOR = 'OpenDoor'
    E_TURNED_KNOB = 'turned_knob'
    E_PULLED_KNOB = 'pulled_knob'
    MSG_TURN_KNOB = 'Turn knob'
    MSG_PULL_KNOB = 'Pull knob'
    """

    def on_main(self):
        parser = argparse.ArgumentParser(description='定数を定義した .pyファイルを作成します')
        parser.add_argument('input', help='定数を定義した入力ファイル(.json)')
        parser.add_argument('output', help='定数を定義した出力ファイル(.py)')
        args = parser.parse_args()

        # Example: "lesson18n2_projects/house3/data/const.json"
        print(f'args.input : {args.input}')
        # Example: "lesson18n2_projects/house3/data/auto_gen/const.py"
        print(f'args.output: {args.output}')

        gen_const_py_v18n2(args.input, args.output)
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