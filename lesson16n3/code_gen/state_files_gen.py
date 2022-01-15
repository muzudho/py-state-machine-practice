from lesson11n80.code_gen.file_io import FileIo
from lesson16n3.code_gen.state_file_gen import gen_state_file_v16n3
from lesson16n3.conf_obj.transition_v16n3 import TransitionV16n3


def gen_state_files_v16n3(transition_doc, output_dir_path):
    """
    Parameters
    ----------
    output_dir : str
        例えば 'lesson16n3_projects/wcsc/auto_gen/code/states'
    """
    transition = TransitionV16n3(transition_doc)

    # エッジの一覧
    edge_list = transition.create_edge_list_v16n2()
    for edge in edge_list:
        print(f"[gen_state_files_v16n3] edge={edge}")

    # フォルダーが無ければ作る
    FileIo.makedirs(output_dir_path)

    # ノードの一覧
    node_path_set = TransitionV16n3.extract_node_path_set(edge_list)
    for node_path in node_path_set:
        gen_state_file_v16n3(transition, node_path, output_dir_path)
