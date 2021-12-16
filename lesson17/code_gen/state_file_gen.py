from lesson16n3.code_gen.py_syntax.switch_gen import SwitchGen
from lesson16n3.transition_conf_v1n3 import TransitionConfV1n3


def gen_state_file(dir_path, node_path, const_conf, transition_conf):
    file_stem = node_path.replace("/", "_").lower()
    class_name = node_path.replace("/", "")
    # print(f"[Render] node_path={node_path} ----> {file_stem}")

    # `init.py` ファイルを作成します
    path = f"{dir_path}/{file_stem}.py"
    with open(path, "w", encoding="UTF-8") as f:
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
        block_list = []
        for edge in directed_edge_list:
            block = []

            if edge.name == "":
                block.append(f"True")  # 恒真式
                block.append(f"return {edge.dst}")  # TODO 遷移先の名前を定数で書きたい
                block_list.append(block)

            else:
                edge_const = const_conf.rev_data[edge.name]
                used_const.add(edge_const)

                block.append(f"msg == {edge_const}")  # 条件式。定数で書きます
                block.append(f"return {edge.dst}")  # TODO 遷移先の名前を定数で書きたい
                block_list.append(block)

        text += SwitchGen.generate("        ", block_list)

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

        f.write(text)
