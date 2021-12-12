import os
from lesson16n2.transition_conf_wcsc import Transition


class Render:
    @classmethod
    def is_verbose(clazz):
        return True

    def __init__(self):
        pass

    def run(self):
        transition = Transition()
        edge_list = transition.create_edge_list()
        for edge in edge_list:
            print(f"[Render] edge={edge}")

        node_path_set = Transition.extract_node_path_set(edge_list)
        for node_path in node_path_set:
            print(f"[Render] node_path={node_path}")

        try:
            # `auto_gen` フォルダーが無ければ作る
            os.makedirs("lesson16n2/auto_gen")
        except FileExistsError:
            # 既存なら無視
            pass

        # `init.py` ファイルを作成します
        # 'x' - ファイルが存在しない場合のみの上書き
        path = "lesson16n2/auto_gen/init.py"
        try:
            with open(path, "x") as f:
                f.write(
                    """from lesson16n2.transition_conf_wcsc import E_OVER

    class InitState():

        def update(self, req):
            # 何もせず終わります
            return E_OVER

    """
                )
        except FileExistsError as e:
            print(f"[Ignore] {e}")

    def clean_up(self):
        pass
