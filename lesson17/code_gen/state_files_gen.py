from lesson16.code_gen.file_io import FileIo
from lesson17.code_gen.state_file_gen import gen_state_file
from lesson17.code_gen.const_conf import ConstConfV17
from lesson16n3.code_gen.transition_conf_v16n3 import TransitionConfV16n3


def gen_state_files_v17(const_conf_doc, transition_conf_data, output_dir_path):
    transition_conf = TransitionConfV16n3(transition_conf_data)
    const_conf = ConstConfV17(const_conf_doc)

    # エッジの一覧
    edge_list = transition_conf.create_edge_list()
    for edge in edge_list:
        print(f"[Render] edge={edge}")

    # フォルダーが無ければ作る
    FileIo.makedirs(output_dir_path)

    # ノードの一覧
    node_path_set = TransitionConfV16n3.extract_node_path_set(edge_list)
    for node_path in node_path_set:
        if node_path is None:
            continue

        gen_state_file(output_dir_path, node_path, const_conf, transition_conf)
