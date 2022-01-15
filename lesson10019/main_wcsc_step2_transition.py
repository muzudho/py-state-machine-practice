import sys

from lesson07n2.main_finally import MainFinally
from lesson10019.code_gen.transition_json_writer import TransitionJsonWriter
from lesson16n3.code_gen.transition_conf_v16n3 import TransitionConfV16n3
from lesson10019_projects.wcsc.data.transition import wcsc_transition_doc_v19

OUTPUT_FILE_PATH = "lesson10019_projects/wcsc/auto_gen/data/transition.json"


class Main:
    def on_main(self):
        transition = TransitionConfV16n3(wcsc_transition_doc_v19)
        TransitionJsonWriter.write(
            file_path=OUTPUT_FILE_PATH,
            title=transition.doc['title'],
            entry_state=transition.doc['entry_state'],
            data=transition.doc['data'],
        )
        return 0

    def on_except(self, e):
        """ここで例外キャッチ"""
        print(e)

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
