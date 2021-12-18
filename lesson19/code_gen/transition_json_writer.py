import os
from lesson16.code_gen.file_io import FileIo
from lesson19.code_gen.transition_json_stringification import (
    TransitionJsonStringification,
)


class TransitionJsonWriter:
    @classmethod
    def write(clazz, file_path, transition_conf):
        text = TransitionJsonStringification.stringify(
            title=transition_conf.title,
            entry_node=transition_conf.entry_node,
            data=transition_conf.data,
        )
        FileIo.makedirs(os.path.dirname(file_path))
        FileIo.write(file_path, text)
