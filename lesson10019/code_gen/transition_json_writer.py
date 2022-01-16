import os
from lesson11n80.code_gen.file_io_v11n80 import FileIoV11n80
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
        FileIoV11n80.makedirs(os.path.dirname(file_path))
        FileIoV11n80.write(file_path, text)
