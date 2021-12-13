import os
from lesson18.code_gen.state_file_gen import StateFileGen
from lesson18.step1_const_conf import ConstConf
from lesson18.step2_transition_conf import TransitionConf


def state_files_gen(dir_path):
    const_conf = ConstConf()
    transition_conf = TransitionConf()

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

        StateFileGen().generate(dir_path, const_conf, transition_conf, node_path)
