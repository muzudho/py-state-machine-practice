import json
from collections import OrderedDict


class TransitionJsonReader:
    @classmethod
    def read_file(clazz, file_path):

        # Pivotファイル（JSON形式）を読込みます
        with open(file_path, encoding="utf-8") as f:
            in_text = f.read()

        data = json.loads(in_text, object_pairs_hook=OrderedDict)

        out_text = json.dumps(data, indent=4, ensure_ascii=False)
        print(f"out_text={out_text}")
