import os
from lesson17.code_gen.state_file_gen import gen_state_file
from lesson17.const_conf import ConstConf
from lesson17.step1_const_conf_wcsc_v2 import const_conf_data
from lesson16n3.transition_conf_v1n3 import TransitionConfV1n3
from lesson17.step2_transition_conf_wcsc import transition_conf_data


def gen_state_files(dir_path):
    transition_conf = TransitionConfV1n3(transition_conf_data)
    const_conf = ConstConf(const_conf_data)

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
    node_path_set = TransitionConfV1n3.extract_node_path_set(edge_list)
    for node_path in node_path_set:
        if node_path is None:
            continue

        gen_state_file(dir_path, node_path, const_conf, transition_conf)
