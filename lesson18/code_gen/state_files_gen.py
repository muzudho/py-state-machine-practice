from lesson16.code_gen.file_io import FileIo
from lesson18.code_gen.state_file_gen import StateFileGen
from lesson18.code_gen.const_conf import ConstConfV18
from lesson16n3.code_gen.transition_conf_v16n3 import TransitionConfV16n3


def gen_state_files_v18(dir_path, const_py_dict, transition_py_dict, import_from_path):
    const_conf = ConstConfV18(const_py_dict)
    transition_conf = TransitionConfV16n3(transition_py_dict)

    # エッジの一覧
    edge_list = transition_conf.create_edge_list()
    for edge in edge_list:
        print(f"[Render] edge={edge}")

    # フォルダーが無ければ作る
    FileIo.makedirs(dir_path)

    # ノードの一覧
    node_path_set = TransitionConfV16n3.extract_node_path_set(edge_list)
    for node_path in node_path_set:
        if node_path is None:
            continue

        StateFileGen().generate_state_file(
            dir_path,
            const_conf,
            transition_conf,
            node_path,
            import_from_path,
        )
