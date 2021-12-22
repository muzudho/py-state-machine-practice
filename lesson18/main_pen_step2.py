import sys

from lesson07n2.main_finally import MainFinally
from lesson18.code_gen.state_files_gen import gen_state_files_v18
from lesson18_data.pen_step1_const_dict import pen_const_py_dict
from lesson14_data.step2_pen_transition import pen_transition_py_dict

OUTPUT_STEP2_AUTO_STATE_DIR = "lesson18/pen_step2n2_auto_state"


class Main:
    def on_main(self):
        gen_state_files_v18(
            dir_path=OUTPUT_STEP2_AUTO_STATE_DIR,
            const_py_dict=pen_const_py_dict,
            transition_py_dict=pen_transition_py_dict,
        )
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
