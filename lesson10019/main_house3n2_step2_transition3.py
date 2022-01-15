import sys

from lesson07n2.main_finally import MainFinally
from lesson10019.code_gen.transition_json_writer import TransitionJsonWriter
from lesson16n3.conf_obj.transition_v16n3 import TransitionV16n3
from lesson10019_projects.house3n2.data.transition3 import house3n2_transition3_doc_v14


OUTPUT_FILE_PATH = "lesson10019_projects/house3n2/auto_gen/data/transition2.json"


class Main:
    def on_main(self):
        transition = TransitionV16n3(house3n2_transition3_doc_v14)
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
