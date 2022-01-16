from tomlkit import parse

from lesson11n80.code_gen.file_io_v11n80 import FileIoV11n80


class TomlReaderV11n90:
    @classmethod
    def read_file(clazz, file_path):

        # テキストファイルを読込みます
        text = FileIoV11n80.read(file_path)

        # TOML形式のテキストをパースします
        return parse(text)
