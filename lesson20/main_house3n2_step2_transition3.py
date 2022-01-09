import sys
import json
import os

from lesson07n2.main_finally import MainFinally
from lesson16.code_gen.file_io import FileIo
from lesson19.code_gen.transition_json_writer import TransitionJsonWriter
from lesson20.code_gen.json_reader_v20 import JsonReaderV20

INPUT_JSON_FILE_PATH = "lesson19_data/step2_auto/house3n2-transition2.json"
OUTPUT_JSON_FILE_PATH_1 = (
    "lesson20_data/step2n2_auto/house3n2-transition3-default-fomat.json"
)
OUTPUT_JSON_FILE_PATH_2 = "lesson20_data/step2n2_auto/house3n2-transition3.json"


class Main:
    def on_main(self):
        # JSONファイルを読込みます
        transition_json_obj = JsonReaderV20.read_file(INPUT_JSON_FILE_PATH)
        # print(f"transition_json_obj={transition_json_obj}")

        # フォーマッティング無しで出力するなら
        out_text = json.dumps(transition_json_obj, indent=4, ensure_ascii=False)
        FileIo.makedirs(os.path.dirname(OUTPUT_JSON_FILE_PATH_1))
        print(f"[L20] write {OUTPUT_JSON_FILE_PATH_1}")
        FileIo.write(OUTPUT_JSON_FILE_PATH_1, out_text)

        # フォーマッティングするなら
        print(f"[L20] write {OUTPUT_JSON_FILE_PATH_2}")
        TransitionJsonWriter.write(
            file_path=OUTPUT_JSON_FILE_PATH_2,
            title=transition_json_obj["title"],
            entry_state=transition_json_obj["entry_state"],
            data=transition_json_obj["data"],
        )

        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
