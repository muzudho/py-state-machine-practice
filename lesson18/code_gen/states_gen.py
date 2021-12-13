import os
from lesson18.code_gen.state_file_gen import StateFileGen
from lesson18.step1_const_conf import ConstConf
from lesson18.step2_transition_conf import Transition


def state_files_gen(dir_path):
    const_conf = ConstConf()
    transition = Transition()

    # エッジの一覧
    edge_list = transition.create_edge_list()
    for edge in edge_list:
        print(f"[Render] edge={edge}")

    try:
        # フォルダーが無ければ作る
        os.makedirs(dir_path)
    except FileExistsError:
        # 既存なら無視
        pass

    # ノードの一覧
    node_path_set = Transition.extract_node_path_set(edge_list)
    for node_path in node_path_set:
        if node_path is None:
            continue

        StateFileGen().generate(dir_path, const_conf, transition, node_path)
