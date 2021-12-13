import os
from lesson16n3.code_gen import CodeGen
from lesson16n3.transition_conf_wcsc import TransitionConf


class Render:
    @classmethod
    def is_verbose(clazz):
        return True

    def __init__(self):
        pass

    def run(self):
        transition_conf = TransitionConf()

        # エッジの一覧
        edge_list = transition_conf.create_edge_list()
        for edge in edge_list:
            print(f"[Render] edge={edge}")

        try:
            # `auto_gen` フォルダーが無ければ作る
            os.makedirs("lesson16n3/auto_gen")
        except FileExistsError:
            # 既存なら無視
            pass

        # ノードの一覧
        node_path_set = TransitionConf.extract_node_path_set(edge_list)
        for node_path in node_path_set:
            file_stem = node_path.replace("/", "_").lower()
            class_name = node_path.replace("/", "")
            # print(f"[Render] node_path={node_path} ----> {file_stem}")

            # `init.py` ファイルを作成します
            # 'x' - ファイルが存在しない場合のみの上書き
            path = f"lesson16n3/auto_gen/{file_stem}.py"
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

    def clean_up(self):
        pass
