import os
from lesson11n300.code_gen.file_io import FileIo
from lesson17.code_gen.const_stringification import ConstStringification


def gen_const_file_v17(output_file_path, const_conf_doc):
    """Pythonスクリプトファイルを生成します"""

    text = ConstStringification.stringify(const_conf_doc)

    # 出力
    FileIo.makedirs(os.path.dirname(output_file_path))
    FileIo.write(output_file_path, text)
