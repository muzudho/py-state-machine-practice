from graphviz import Digraph
from lesson15.directive_edge import DirectiveEdge
from lesson15.clustered_directive_edge import ClusteredDirectiveEdge

# from lesson15.transition_conf_data import TransitionConf
from lesson15.transition_conf import TransitionConf
from lesson15.step2_transition_conf_wcsc import transition_conf_data


def create_edge_list(curr_dict, parent_state_node_path, node_name, result_edge_list):
    """辺の一覧を作成"""
    state_node_path = list(parent_state_node_path)
    if not (node_name is None) and not (node_name is ""):
        state_node_path.append(node_name)
        pass

    for child_key in curr_dict.keys():

        if Render.is_verbose():
            print(f"[render] child_key={child_key}")

        child = curr_dict[child_key]

        if isinstance(child, dict):
            create_edge_list(child, state_node_path, child_key, result_edge_list)
        else:
            edge = DirectiveEdge(
                src=state_node_path,
                dst=child,
                name=child_key,
            )
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

        transition_conf = TransitionConf(transition_conf_data)

        # エッジの一覧を作成
        create_edge_list(transition_conf.data, [], None, edge_list)

        # クラスター 'cluster_' から名前を始める必要あり
        with self._g.subgraph(name="cluster_root") as c:
            # 一番外側のクラスターのラベルは図のタイトルのように見える
            c.attr(color="white", label=transition_conf.title)
            # 始端記号
            c.node("(Start)", shape="circle", color="gray")
            # 始端と開始ノードのエッジ
            c.edge("(Start)", transition_conf.entry_node, label="start")
            # 終端記号
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
