import sys

from lesson07n2.main_finally import MainFinally
from lesson19.code_gen.transition_json_writer import TransitionJsonWriter
from lesson16n3.code_gen.transition_conf_v16n3 import TransitionConfV16n3
from lesson19_projects.house3n2.data.transition3 import house3n2_transition3_py_dict


OUTPUT_FILE_PATH = "lesson19_projects/house3n2/auto_gen/data/transition2.json"


class Main:
    def on_main(self):
        transition_conf_obj = TransitionConfV16n3(house3n2_transition3_py_dict)
        TransitionJsonWriter.write(
            file_path=OUTPUT_FILE_PATH,
            title=transition_conf_obj.title,
            entry_state=transition_conf_obj.entry_state,
            data=transition_conf_obj.data,
        )
        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
