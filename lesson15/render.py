from graphviz import Digraph
from lesson15.directive_edge import DirectiveEdge
from lesson15.transition_conf import transition


def search(curr_dict, parent_state_node_path, node_name, result_edge_list):
    state_node_path = list(parent_state_node_path)
    if not (node_name is None):
        state_node_path.append(node_name)
        pass

    for child_key in curr_dict.keys():

        if Render.is_verbose():
            print(f"[render] child_key={child_key}")

        child = curr_dict[child_key]

        if isinstance(child, dict):
            search(child, state_node_path, child_key, result_edge_list)
        else:
            edge = DirectiveEdge(child_key, state_node_path, child)
            result_edge_list.append(edge)


class Render:
    @classmethod
    def is_verbose(clazz):
        return True

    def __init__(self):
        # グラフの設定
        self._g = Digraph(format="png")
        self._g.attr("node", shape="square", style="filled")

    def run(self):

        edge_list = []

        search(transition, [], None, edge_list)

        # クラスター 'cluster_' から名前を始める必要あり
        with self._g.subgraph(name="cluster_root") as c:
            # 一番外側のクラスターのラベルは図のタイトルのように見える
            c.attr(color="white", label="--Title--")
            # 始端ノード
            c.node("(Start)", shape="circle", color="gray")
            # TODO 最初のノード
            c.node("Init", shape="circle", color="pink")
            # 終端ノード
            c.node("(Terminal)", shape="circle", color="gray")

            for edge in edge_list:
                src_node = edge.to_src_str()
                dst_node = edge.to_dst_str()
                if dst_node is None:
                    dst_node = "(Terminal)"

                # ノード
                c.node(src_node, shape="circle", color="pink")
                # エッジ
                c.edge(src_node, dst_node, label=edge.name)

        # 描画
        self._g.render("lesson15-graphs")

    def clean_up(self):
        pass
