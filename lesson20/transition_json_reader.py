import json
from collections import OrderedDict


class TransitionJsonReader:
    @classmethod
    def read_file(clazz, file_path):

        # Pivotファイル（JSON形式）を読込みます
        with open(file_path, encoding="utf-8") as f:
            in_text = f.read()

        transition_conf_data = json.loads(in_text, object_pairs_hook=OrderedDict)
        return transition_conf_data
