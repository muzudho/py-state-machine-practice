from lesson11n80.code_gen.file_io import FileIo
from lesson16n3.code_gen.py_syntax.switch_gen import SwitchGen
from lesson16n3.conf_obj.transition_v16n3 import TransitionV16n3


def gen_state_file_v17(
        dir_path,
        node_path,
        const,
        transition,
        import_module_path):

    file_stem = node_path.replace("/", "_").lower()
    class_name = node_path.replace("/", "")
    # print(f"[gen_state_file_v17] node_path={node_path} ----> {file_stem}")

    # ステート Python スクリプトファイルを作成します
    file_path = f"{dir_path}/{file_stem}.py"
    text = f"""class {class_name}State():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
"""

    # エッジの分岐部分
    directed_edge_list = TransitionV16n3.create_edge_list_by_node_path(
        transition.doc['data'], node_path.split("/")
    )

    used_const = set()
    if_elif_list = []
    for edge in directed_edge_list:

        if edge.name == "":
            cond = "True"  # 恒真式
            body_sequence = [f"return {edge.dst}"]  # TODO 遷移先の名前を定数で書きたい
            if_elif_list.append([cond, body_sequence])

        else:
            operand = const.stringify(
                edge.name, "'")  # できれば定数に変換します。でなければ文字列
            if operand[0] != "'":
                # 定数を使った
                used_const.add(operand)

            cond = f"msg == {operand}"  # 条件式。operandは文字列または定数

            # 遷移先ノードパス（リスト）
            # TODO ノードの文字列のうち、定数にできるところは定数にしたい
            text_list = []
            for item in edge.dst:
                s1 = const.stringify(item, "'")
                if s1[0] != "'":
                    # 定数を使った
                    used_const.add(s1)
                text_list.append(s1)

            return_statement = "return [" + ", ".join(text_list) + "]"
            body_sequence = [return_statement]

            if_elif_list.append([cond, body_sequence])

    # else文
    else_sequence = ['raise ValueError(f"Unexpected msg:{msg}")']

    switch_model = [if_elif_list, else_sequence]
    text += SwitchGen.generate_switch("        ", switch_model)

    # 定数をインポートします
    if 0 < len(used_const):
        pre_text = f"from {import_module_path} import "
        is_skip_first = True

        used_const_list = list(used_const)
        used_const_list.sort()

        for const in used_const_list:
            if is_skip_first:
                is_skip_first = False
            else:
                pre_text += ", "

            pre_text += const

        text = f"""{pre_text}

{text}
"""

    FileIo.write(file_path, text)
