import os
from lesson17.code_gen.py_gen import CodeGen
from lesson17.step1_const_conf import ConstConf
from lesson17.step2_transition_conf_wcsc import TransitionConf


def state_files_gen(dir_path):
    transition_conf = TransitionConf()
    const_conf = ConstConf()

    # エッジの一覧
    edge_list = transition_conf.create_edge_list()
    for edge in edge_list:
        print(f"[Render] edge={edge}")

    try:
        # フォルダーが無ければ作る
        os.makedirs(dir_path)
    except FileExistsError:
        # 既存なら無視
        pass

    # ノードの一覧
    node_path_set = TransitionConf.extract_node_path_set(edge_list)
    for node_path in node_path_set:
        if node_path is None:
            continue

        file_stem = node_path.replace("/", "_").lower()
        class_name = node_path.replace("/", "")
        # print(f"[Render] node_path={node_path} ----> {file_stem}")

        # `init.py` ファイルを作成します
        # 'x' - ファイルが存在しない場合のみの上書き
        path = f"{dir_path}/{file_stem}.py"
        try:
            with open(path, "x", encoding="UTF-8") as f:
                text = f"""class {class_name}State():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
"""

                # エッジの分岐部分
                directed_edge_list = TransitionConf.create_edge_list_by_node_path(
                    transition_conf.data, node_path.split("/")
                )

                # line_list = []
                # for edge in directed_edge_list:
                #    line_list.append(f"# {{edge.name}}")
                #
                # text += CodeGen.create_comment_block("        ", line_list)
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

                text += CodeGen.create_switch_block("        ", block_list)

                # 定数をインポートします
                if 0 < len(used_const):
                    pre_text = "from lesson17.step1n2_auto.const import "
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

        except FileExistsError as e:
            print(f"[Ignore] {e}")
