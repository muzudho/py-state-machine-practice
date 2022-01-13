import sys

from lesson07n2.main_finally import MainFinally
from lesson17.code_gen.state_files_gen import gen_state_files_v17
from lesson17_projects.wcsc.data.const_dict import wcsc_const_py_dict
from lesson14_projects.wcsc.data.transition import wcsc_transition_doc_v14

STEP2_AUTO_STATE_DIR_PATH = "lesson17_projects/wcsc/auto_gen/code/states"


class Main:
    def on_main(self):
        gen_state_files_v17(
            const_conf_py_dict=wcsc_const_py_dict,
            transition_conf_data=wcsc_transition_doc_v14,
            output_dir_path=STEP2_AUTO_STATE_DIR_PATH,
        )
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
