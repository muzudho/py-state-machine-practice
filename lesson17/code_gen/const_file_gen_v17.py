import os
from lesson11n80.code_gen.file_io_v11n80 import FileIoV11n80
from lesson17.code_gen.const_stringification_v17 import ConstStringificationV17


def gen_const_file_v17(const_doc, output_file_path):
    """Pythonスクリプトファイルを生成します"""

    text = ConstStringificationV17.stringify(const_doc)

    # 出力
    FileIoV11n80.makedirs(os.path.dirname(output_file_path))
    FileIoV11n80.write(output_file_path, text)
