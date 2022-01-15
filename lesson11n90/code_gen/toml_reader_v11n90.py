from tomlkit import parse

from lesson11n80.code_gen.file_io import FileIo


class TomlReaderV11n90:
    @classmethod
    def read_file(clazz, file_path):

        # テキストファイルを読込みます
        text = FileIo.read(file_path)

        # TOML形式のテキストをパースします
        return parse(text)
