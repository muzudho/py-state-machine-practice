from lesson16.code_gen.file_io import FileIo
from lesson16n3.code_gen.state_file_gen import gen_state_file_v16n3
from lesson16n3.code_gen.transition_conf_v16n3 import TransitionConfV16n3
from lesson15_projects.wcsc.data.transition import wcsc_transition_py_dict


def gen_state_files_v16n3(dir_path, output_dir):
    """
    Parameters
    ----------
    output_dir : str
        例えば 'lesson16n3_projects/example/auto_gen'
    """
    transition_conf = TransitionConfV16n3(wcsc_transition_py_dict)

    # エッジの一覧
    edge_list = transition_conf.create_edge_list()
    for edge in edge_list:
        print(f"[Render] edge={edge}")

    # フォルダーが無ければ作る
    FileIo.makedirs(dir_path)

    # ノードの一覧
    node_path_set = TransitionConfV16n3.extract_node_path_set(edge_list)
    for node_path in node_path_set:
        gen_state_file_v16n3(transition_conf, node_path, output_dir)
