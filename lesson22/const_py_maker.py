import sys
import argparse

from lesson07n2.main_finally import MainFinally
from lesson22.code_gen.const_py_gen import gen_const_py

class Main:
    """定数を定義した .pyファイルを作成します

    Examples
    --------
    # Windows
    python.exe -m lesson22.const_py_maker "example-const.json" "example_const.py"
    #                                     -------------------- ------------------
    #                                     入力ファイル           出力ファイル

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

        print(f'args.input : {args.input}') # Example: "lesson22_data/step1-house3-const.json"
        print(f'args.output: {args.output}') # Example: "lesson22_data/step1n2_auto_const/house3_const.py"

        gen_const_py(args.input, args.output)
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
