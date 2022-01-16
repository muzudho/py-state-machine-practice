from lesson11n100.code_gen.json_reader_v11n100 import JsonReaderV11n100
from lesson17.code_gen.const_file_gen_v17 import gen_const_file_v17


def gen_const_py_v18n2(input_path, output_path):
    """定数を定義したJSONファイルを元に、Pythonスクリプトを出力"""

    # JSON構造（順序付きDict）に変換 --> 出力
    transition_doc = JsonReaderV11n100.read_file(input_path)
    gen_const_file_v17(output_path, transition_doc)
