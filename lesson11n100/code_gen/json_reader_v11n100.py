import json
from collections import OrderedDict
from msilib.schema import File

from lesson11n80.code_gen.file_io import FileIo


class JsonReaderV11n100:
    @classmethod
    def read_file(clazz, file_path):

        # JSON形式のファイルを読込みます
        itext = FileIo.read(file_path)

        doc = json.loads(itext, object_pairs_hook=OrderedDict)
        # print(f"doc={doc}")

        return doc
