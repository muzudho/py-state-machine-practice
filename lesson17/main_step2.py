import sys

from lesson07n2.main_finally import MainFinally
from lesson17.code_gen.state_files_gen import gen_state_files
from lesson17.step1_const_conf_wcsc_v2 import const_conf_py_dict
from lesson15.step2_transition_conf_wcsc import transition_conf_data


class Main:
    def on_main(self):
        gen_state_files(
            const_conf_py_dict=const_conf_py_dict,
            transition_conf_data=transition_conf_data,
            output_dir_path="lesson17/step2n2_auto_state",
        )
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
