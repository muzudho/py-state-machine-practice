import os
from lesson16n2.transition_conf_v1n2 import TransitionConfV1n2
from lesson16n2.step2_transition_conf_wcsc import transition_conf_data


class Render:
    @classmethod
    def is_verbose(clazz):
        return True

    def __init__(self):
        pass

    def run(self):
        transition_conf = TransitionConfV1n2(transition_conf_data)

        # エッジの一覧
        edge_list = transition_conf.create_edge_list()
        for edge in edge_list:
            print(f"[Render] edge={edge}")

        try:
            # `step2n2_auto` フォルダーが無ければ作る
            os.makedirs("lesson16n2/step2n2_auto")
        except FileExistsError:
            # 既存なら無視
            pass

        # ノードの一覧
        node_path_set = TransitionConfV1n2.extract_node_path_set(edge_list)
        for node_path in node_path_set:
            file_stem = node_path.replace("/", "_").lower()
            class_name = node_path.replace("/", "")
            print(f"[Render] node_path={node_path} ----> {file_stem}")

            # `init.py` ファイルを作成します
            # 'x' - ファイルが存在しない場合のみの上書き
            path = f"lesson16n2/step2n2_auto/{file_stem}.py"
            with open(path, "w", encoding="UTF-8") as f:
                f.write(
                    f"""from lesson15.step1_const_conf_wcsc_v1 import E_OVER

class {class_name}State():

    def update(self, req):
        # 何もせず終わります
        return E_OVER

"""
                )

    def clean_up(self):
        pass
