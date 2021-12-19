from lesson16.code_gen.file_io import FileIo
from lesson16n3.code_gen.state_file_gen import gen_state_file
from lesson16n3.transition_conf_v1n3 import TransitionConfV1n3
from lesson15_data.step2_transition_wcsc import transition_wcsc_py_dict


def gen_state_files():
    transition_conf = TransitionConfV1n3(transition_wcsc_py_dict)

    # エッジの一覧
    edge_list = transition_conf.create_edge_list()
    for edge in edge_list:
        print(f"[Render] edge={edge}")

    # `step2n2_auto` フォルダーが無ければ作る
    dir_path = "lesson16n3/step2n2_auto"
    FileIo.makedirs(dir_path)

    # ノードの一覧
    node_path_set = TransitionConfV1n3.extract_node_path_set(edge_list)
    for node_path in node_path_set:
        gen_state_file(transition_conf, node_path)
