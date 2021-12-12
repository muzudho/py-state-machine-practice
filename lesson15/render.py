import collections
from graphviz import Digraph
from lesson15.directive_edge import DirectiveEdge
from lesson15.clustered_directive_edge import ClusteredDirectiveEdge

# from lesson15.transition_conf import Transition
from lesson15.transition_conf_wcsc import Transition


def create_edge_list(curr_dict, parent_state_node_path, node_name, result_edge_list):
    """辺の一覧を作成"""
    state_node_path = list(parent_state_node_path)
    if not (node_name is None):
        state_node_path.append(node_name)
        pass

    for child_key in curr_dict.keys():

        if Render.is_verbose():
            print(f"[render] child_key={child_key}")

        child = curr_dict[child_key]

        if isinstance(child, dict):
            create_edge_list(child, state_node_path, child_key, result_edge_list)
        else:
            edge = DirectiveEdge(child_key, state_node_path, child)
            result_edge_list.append(edge)


def clustering(edge_list):
    """ノードパスによってクラスタリング"""
    clustered_edge_in_list = []

    for edge in edge_list:
        clustering_edge = ClusteredDirectiveEdge.clustering(edge)
        clustered_edge_in_list.append(clustering_edge)

    return clustered_edge_in_list


def rearrenge_in_tree(clustered_edge_in_list):
    """ツリー構造に再配置"""
    tree = {}

    for clustering_edge in clustered_edge_in_list:
        print("----")
        print(f"clustering_edge.directive_edge={clustering_edge.directive_edge}")

        print(f"clustering_edge.to_cluster_str()={clustering_edge.to_cluster_str()}")

        curr_dict = tree

        if len(clustering_edge.cluster) < 1:
            print(f"len(clustering_edge.cluster)={len(clustering_edge.cluster)}")
            pass
        else:

            for cluster_node in clustering_edge.cluster:
                print(f"  cluster_node={cluster_node}")

                if not (cluster_node in curr_dict):
                    curr_dict[cluster_node] = {}

                curr_dict = curr_dict[cluster_node]

        if "__edge__" in curr_dict:
            curr_dict["__edge__"].append(clustering_edge.directive_edge)
        else:
            curr_dict["__edge__"] = [clustering_edge.directive_edge]

    print("----")
    return tree


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

        transition = Transition()

        # エッジの一覧を作成
        create_edge_list(transition.data, [], None, edge_list)

        # ノードパスによってクラスタリング
        clustered_edge_in_list = clustering(edge_list)
        # Debug
        for clustering_edge in clustered_edge_in_list:
            print(f"clustering_edge={clustering_edge}")

        # ツリー構造に再配置
        tree = rearrenge_in_tree(clustered_edge_in_list)
        # Debug
        def __show_tree(curr_dict, indent):
            # エッジを先に検出
            if "__edge__" in curr_dict:
                edge_list = curr_dict["__edge__"]
                for edge in edge_list:
                    print(f"[Tree] __edge__ {indent}value={edge}")

            for key, value in curr_dict.items():
                if key == "__edge__":
                    pass  # 検出済み
                else:
                    __show_tree(value, f"{indent}  ")

        __show_tree(tree, "")

        # クラスター 'cluster_' から名前を始める必要あり
        with self._g.subgraph(name="cluster_root") as c:
            # 一番外側のクラスターのラベルは図のタイトルのように見える
            c.attr(color="white", label=transition.title)
            # 始端記号
            c.node("(Start)", shape="circle", color="gray")
            # 始端と開始ノードのエッジ
            c.edge("(Start)", transition.entry_node, label="start")
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
