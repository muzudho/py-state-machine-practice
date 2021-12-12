import os
from lesson17.code_gen.py_gen import CodeGen
from lesson17.transition_conf_wcsc import Transition


def state_files_gen(dir_path):
    transition = Transition()

    # エッジの一覧
    edge_list = transition.create_edge_list()
    for edge in edge_list:
        print(f"[Render] edge={edge}")

    try:
        # `auto_gen` フォルダーが無ければ作る
        os.makedirs(dir_path)
    except FileExistsError:
        # 既存なら無視
        pass

    # ノードの一覧
    node_path_set = Transition.extract_node_path_set(edge_list)
    for node_path in node_path_set:
        file_stem = node_path.replace("/", "_").lower()
        class_name = node_path.replace("/", "")
        # print(f"[Render] node_path={node_path} ----> {file_stem}")

        # `init.py` ファイルを作成します
        # 'x' - ファイルが存在しない場合のみの上書き
        path = f"{dir_path}/{file_stem}.py"
        try:
            with open(path, "x", encoding="UTF-8") as f:
                # from lesson16n3.transition_conf_wcsc import E_OVER
                text = f"""class {class_name}State():

def update(self, req):

    # TODO 入力
    msg = ""

    # 分岐
"""

                # エッジの分岐部分
                directed_edge_list = Transition.create_edge_list_by_node_path(
                    transition.data, node_path.split("/")
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
                block_list = []
                for edge in directed_edge_list:
                    block = []
                    block.append(f"msg == '{edge.name}'")  # TODO 条件式。定数で書きたい
                    block.append(f"return {edge.dst}")  # TODO 遷移先の名前を定数で書きたい
                    block_list.append(block)

                text += CodeGen.create_switch_block("        ", block_list)

                f.write(text)

        except FileExistsError as e:
            print(f"[Ignore] {e}")
