import os
from lesson16.code_gen.file_io import FileIo
from lesson18.code_gen.state_file_gen import StateFileGen
from lesson18.const_conf import ConstConf
from lesson18_data.step1_const_dict_pen import const_pen_py_dict
from lesson16n3.transition_conf_v1n3 import TransitionConfV1n3
from lesson14_data.step2_transition_pen import transition_pen_py_dict


def gen_state_files(dir_path):
    const_conf = ConstConf(const_pen_py_dict)
    transition_conf = TransitionConfV1n3(transition_pen_py_dict)

    # エッジの一覧
    edge_list = transition_conf.create_edge_list()
    for edge in edge_list:
        print(f"[Render] edge={edge}")

    # フォルダーが無ければ作る
    FileIo.makedirs(dir_path)

    # ノードの一覧
    node_path_set = TransitionConfV1n3.extract_node_path_set(edge_list)
    for node_path in node_path_set:
        if node_path is None:
            continue

        StateFileGen().generate(dir_path, const_conf, transition_conf, node_path)
