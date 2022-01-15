import os
from lesson11n80.code_gen.file_io import FileIo
from lesson16n3.code_gen.py_syntax.switch_gen import SwitchGen
from lesson16n3.conf_obj.transition_v16n3 import TransitionV16n3


def gen_state_file_v16n3(transition, node_path, output_dir):
    file_stem = node_path.replace("/", "_").lower()
    class_name = node_path.replace("/", "")
    # print(f"[gen_state_file_v16n3] node_path={node_path} ----> {file_stem}")

    # `init.py` ファイルを作成します
    # 'x' - ファイルが存在しない場合のみの上書き
    file_path = os.path.join(output_dir, f"{file_stem}.py")
    text = f"""class {class_name}State():

    def update(self, req):

        # TODO 入力
        msg = ""

        # 分岐
"""

    # エッジの分岐部分
    directed_edge_list = TransitionV16n3.create_edge_list_by_node_path(
        transition.doc['data'], node_path.split("/")
    )

    switch_model = __edge_switch_model(directed_edge_list)

    text += SwitchGen.generate_switch("        ", switch_model)

    FileIo.write(file_path, text)


def __edge_switch_model(directed_edge_list):
    if_elif_list = []
    for edge in directed_edge_list:
        # 条件式
        cond = f"msg == '{edge.name}'"  # TODO 条件式。定数で書きたい

        # 本文シーケンス
        body_sequence = []
        body_sequence.append(f"return {edge.dst}")  # TODO 遷移先の名前を定数で書きたい

        if_elif_list.append([cond, body_sequence])

    else_sequence = ['raise ValueError("Unexpected condition")']

    return [if_elif_list, else_sequence]
