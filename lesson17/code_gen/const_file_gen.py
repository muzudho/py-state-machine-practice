import os
from lesson16.code_gen.file_io import FileIo
from lesson17.code_gen.const_stringification import ConstStringification


def gen_const_file(file_path, const_conf_data):
    text = ConstStringification.stringify(const_conf_data)

    # フォルダーが無ければ作る
    FileIo.makedirs(os.path.dirname(file_path))

    FileIo.write(file_path, text)
