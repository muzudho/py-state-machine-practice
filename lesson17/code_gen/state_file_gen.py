from lesson16.code_gen.file_io import FileIo
from lesson16n3.code_gen.py_syntax.switch_gen import SwitchGen
from lesson16n3.transition_conf_v1n3 import TransitionConfV1n3


def gen_state_file(dir_path, node_path, const_conf, transition_conf):
    file_stem = node_path.replace("/", "_").lower()
    class_name = node_path.replace("/", "")
    # print(f"[Render] node_path={node_path} ----> {file_stem}")

    # ステート Python スクリプトファイルを作成します
    file_path = f"{dir_path}/{file_stem}.py"
    text = f"""class {class_name}State():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
"""

    # エッジの分岐部分
    directed_edge_list = TransitionConfV1n3.create_edge_list_by_node_path(
        transition_conf.data, node_path.split("/")
    )

    # line_list = []
    # for edge in directed_edge_list:
    #    line_list.append(f"# {{edge.name}}")
    #
    # text += CommentGen.generate("        ", line_list)
    #                    text += """
    #        # 何もせず終わります
    #        return E_OVER
    # """

    used_const = set()
    if_elif_list = []
    for edge in directed_edge_list:

        if edge.name == "":
            cond = "True"  # 恒真式
            body_sequence = [f"return {edge.dst}"]  # TODO 遷移先の名前を定数で書きたい
            if_elif_list.append([cond, body_sequence])

        else:
            operand = const_conf.stringify(edge.name, '"')  # できれば定数に変換します。でなければ文字列
            if operand[0] != '"':
                # 定数に変換した
                used_const.add(operand)

            cond = f"msg == {operand}"  # 条件式。operandは文字列または定数

            # 遷移先ノードパス（リスト）
            # TODO ノードの文字列のうち、定数にできるところは定数にしたい
            destination_list = edge.dst
            print(f"[Lesson17] destination_list={destination_list}")

            body_sequence = [f"return {edge.dst}"]  # TODO 遷移先の名前を定数で書きたい

            if_elif_list.append([cond, body_sequence])

    # else文
    else_sequence = ['raise ValueError(f"Unexpected msg:{msg}")']

    switch_model = [if_elif_list, else_sequence]
    text += SwitchGen.generate("        ", switch_model)

    # 定数をインポートします
    if 0 < len(used_const):
        pre_text = "from lesson17.step1n2_auto_const.pen import "
        is_skip_first = True

        for const in used_const:
            if is_skip_first:
                is_skip_first = False
            else:
                pre_text += ", "

            pre_text += const

        text = f"""{pre_text}

{text}
"""

    FileIo.write(file_path, text)
