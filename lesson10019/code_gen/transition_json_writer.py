import os
from lesson11n300.code_gen.file_io import FileIo
from lesson10019.code_gen.transition_json_stringification import (
    TransitionJsonStringification,
)


class TransitionJsonWriter:
    @classmethod
    def write(clazz, file_path, title, entry_state, data):
        text = TransitionJsonStringification.stringify(
            title=title,
            entry_state=entry_state,
            data=data,
        )
        FileIo.makedirs(os.path.dirname(file_path))
        FileIo.write(file_path, text)
