import sys

from lesson07n2.main_finally import MainFinally
from lesson18.code_gen.state_files_gen import gen_state_files_v18
from lesson20.transition_json_reader import TransitionJsonReader

INPUT_CONST_JSON_FILE_PATH = "lesson22_data/step1-pen-const.json"
INPUT_TRANSITION_JSON_FILE_PATH = "lesson20_data/step2n2_auto/pen-transition.json"
OUTPUT_STEP2_AUTO_DIR = "lesson23/pen_step2n2_auto_state"


class Main:
    def on_main(self):
        # JSONファイルから、定数と遷移の設定を読込みます
        const_json_obj = TransitionJsonReader.read_file(INPUT_CONST_JSON_FILE_PATH)
        transition_json_obj = TransitionJsonReader.read_file(
            INPUT_TRANSITION_JSON_FILE_PATH
        )

        # 状態の .py スクリプトを出力します
        gen_state_files_v18(
            dir_path=OUTPUT_STEP2_AUTO_DIR,
            const_py_dict=const_json_obj,
            transition_py_dict=transition_json_obj,
        )
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
