import sys

from lesson07n2.main_finally import MainFinally
from lesson17.code_gen.state_files_gen import gen_state_files
from lesson17_data.step1_const_dict_wcsc import const_wcsc_py_dict
from lesson15_data.step2_transition_wcsc import transition_wcsc_py_dict


class Main:
    def on_main(self):
        gen_state_files(
            const_conf_py_dict=const_wcsc_py_dict,
            transition_conf_data=transition_wcsc_py_dict,
            output_dir_path="lesson17/step2n2_auto_state",
        )
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
