from lesson17.code_gen.const_file_gen import gen_const_file_v17
from lesson20.transition_json_reader import TransitionJsonReader

def gen_const_py(input_path, output_path):
    """定数を定義したJSONファイルを元に、Pythonスクリプトを出力"""

    # JSON構造（順序付きDict）に変換 --> 出力
    transition_json_obj = TransitionJsonReader.read_file(input_path)
    gen_const_file_v17(output_path, transition_json_obj)
    