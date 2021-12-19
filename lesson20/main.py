import sys
import json
import os

from lesson07n2.main_finally import MainFinally
from lesson16.code_gen.file_io import FileIo
from lesson19.code_gen.transition_json_writer import TransitionJsonWriter
from lesson20.transition_json_reader import TransitionJsonReader

INPUT_JSON_FILE_PATH = "lesson19_data/step2_auto/transition-pen.json"
OUTPUT_JSON_FILE_PATH_1 = "lesson20_data/auto/transition-pen-default-fomat.json"
OUTPUT_JSON_FILE_PATH_2 = "lesson20_data/auto/transition-pen.json"


class Main:
    def on_main(self):
        transition_conf_data = TransitionJsonReader.read_file(INPUT_JSON_FILE_PATH)
        # print(f"transition_conf_data={transition_conf_data}")

        out_text = json.dumps(transition_conf_data, indent=4, ensure_ascii=False)
        FileIo.makedirs(os.path.dirname(OUTPUT_JSON_FILE_PATH_1))
        print(f"[L20] write {OUTPUT_JSON_FILE_PATH_1}")
        FileIo.write(OUTPUT_JSON_FILE_PATH_1, out_text)

        print(f"[L20] write {OUTPUT_JSON_FILE_PATH_2}")
        TransitionJsonWriter.write(
            file_path=OUTPUT_JSON_FILE_PATH_2,
            title=transition_conf_data["title"],
            entry_node=transition_conf_data["entry_node"],
            data=transition_conf_data["data"],
        )

        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
