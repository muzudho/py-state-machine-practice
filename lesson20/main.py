import sys
import json

from lesson07n2.main_finally import MainFinally
from lesson16.code_gen.file_io import FileIo
from lesson19.code_gen.transition_json_writer import TransitionJsonWriter
from lesson20.transition_json_reader import TransitionJsonReader

JSON_FILE_PATH = "lesson19/auto/transition_pen.json"


class Main:
    def on_main(self):
        data = TransitionJsonReader.read_file(JSON_FILE_PATH)

        dir_path = "lesson20/auto"
        file_path = "lesson20/auto/from_json_no_fomat.txt"
        out_text = json.dumps(data, indent=4, ensure_ascii=False)
        print(f"out_text={out_text}")
        FileIo.makedirs(dir_path)
        FileIo.write(file_path, out_text)

        file_path = "lesson20/auto/from_json.txt"
        TransitionJsonWriter.write(file_path, data)

        return 0

    def on_finally(self):
        print("★しっかり終わった")
        return 1


# このファイルを直接実行したときは、以下の関数を呼び出します
if __name__ == "__main__":
    sys.exit(MainFinally.run(Main()))
