import os
from lesson11n80.code_gen.file_io import FileIo
from lesson16n2.conf_obj.transition_v16n2 import TransitionV16n2


def gen_state_files_v16n2(transition_doc, output_dir_path):
    transition = TransitionV16n2(transition_doc)

    # エッジの一覧
    edge_list = transition.create_edge_list_v16n2()
    for edge in edge_list:
        print(f"[gen_state_files_v16n2] edge={edge}")

    # フォルダーが無ければ作る
    FileIo.makedirs(output_dir_path)

    # ノードの一覧
    node_path_set = TransitionV16n2.extract_node_path_set(edge_list)
    for node_path in node_path_set:
        file_stem = node_path.replace("/", "_").lower()
        class_name = node_path.replace("/", "")
        print(
            f"[gen_state_files_v16n2] node_path={node_path} ----> {file_stem}")

        # `init.py` ファイルを作成します
        # TODO import文を変数にしたい
        file_path = os.path.join(output_dir_path, f"{file_stem}.py")
        text = f"""from lesson15_projects.wcsc.data.const import E_OVER

class {class_name}State():

    def update(self, req):
        # 何もせず終わります
        return E_OVER

"""

        FileIo.write(file_path, text)
