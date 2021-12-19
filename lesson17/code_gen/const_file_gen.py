import os
from lesson16.code_gen.file_io import FileIo
from lesson17.code_gen.const_stringification import ConstStringification


def gen_const_file(output_file_path, const_conf_py_dict):
    """Pythonスクリプトファイルを生成します"""

    text = ConstStringification.stringify(const_conf_py_dict)

    # フォルダーが無ければ作る
    FileIo.makedirs(os.path.dirname(output_file_path))

    FileIo.write(output_file_path, text)
