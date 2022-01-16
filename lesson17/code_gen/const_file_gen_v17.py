import os
from lesson11n80.code_gen.file_io import FileIo
from lesson17.code_gen.const_stringification_v17 import ConstStringificationV17


def gen_const_file_v17(output_file_path, const_doc):
    """Pythonスクリプトファイルを生成します"""

    text = ConstStringificationV17.stringify(const_doc)

    # 出力
    FileIo.makedirs(os.path.dirname(output_file_path))
    FileIo.write(output_file_path, text)
