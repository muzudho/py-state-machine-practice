import json
from collections import OrderedDict
from msilib.schema import File

from lesson11n80.code_gen.file_io_v11n80 import FileIoV11n80


class JsonReaderV11n100:
    @classmethod
    def read_file(clazz, file_path):

        # JSON形式のファイルを読込みます
        itext = FileIoV11n80.read(file_path)

        doc = json.loads(itext, object_pairs_hook=OrderedDict)
        # print(f"doc={doc}")

        return doc
