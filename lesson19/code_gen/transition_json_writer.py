import os
from lesson16.code_gen.file_io import FileIo
from lesson19.code_gen.transition_json_stringification import (
    TransitionJsonStringification,
)


class TransitionJsonWriter:
    @classmethod
    def write(clazz, file_path, data):
        text = TransitionJsonStringification.stringify(data)
        FileIo.makedirs(os.path.dirname(file_path))
        FileIo.write(file_path, text)
