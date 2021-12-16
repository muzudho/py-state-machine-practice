from graphviz import Digraph
from lesson15n2.directive_edge import DirectiveEdge
from lesson15n2.clustered_directive_edge import ClusteredDirectiveEdge

from lesson15.transition_conf_v1 import TransitionConfV1
from lesson15n2.step2_transition_conf_pen import transition_conf_data

# from lesson15n2.transition_conf_wcsc import transition_conf_data


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
            edge = DirectiveEdge(src=state_node_path, dst=child, name=child_key)
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

        transition_conf = TransitionConfV1(transition_conf_data)

        # エッジの一覧を作成
        create_edge_list(transition_conf.data, [], None, edge_list)

        # ノードパスによってクラスタリング
        clustered_edge_in_list = clustering(edge_list)
        # Debug
        for clustering_edge in clustered_edge_in_list:
            print(f"clustering_edge={clustering_edge}")

        # ツリー構造に再配置
        tree = rearrenge_in_tree(clustered_edge_in_list)
        # Debug
        def __show_tree(curr_dict, indent, cluster_name):
            # エッジを先に検出
            if "__edge__" in curr_dict:
                edge_list = curr_dict["__edge__"]
                for edge in edge_list:
                    print(f"[Tree] {indent}{cluster_name} value={edge}")

            for key, value in curr_dict.items():
                if key == "__edge__":
                    pass  # 検出済み
                else:
                    __show_tree(value, f"{indent}  ", f"cluster_{key}")

        __show_tree(tree, "", "cluster_root")

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

            # Debug
            def __create_cluster(curr_dict, indent, cluster_key):
                with self._g.subgraph(name=f"cluster_{cluster_key}") as c2:
                    c2.attr(color="pink", label=cluster_key)

                    # エッジを先に検出
                    if "__edge__" in curr_dict:
                        edge_list = curr_dict["__edge__"]
                        for edge in edge_list:
                            src_node = edge.to_src_str()
                            dst_node = edge.to_dst_str()
                            if dst_node is None:
                                dst_node = "(Terminal)"
                            # ノード
                            c2.node(src_node, shape="circle", color="pink")
                            # エッジ
                            c2.edge(src_node, dst_node, label=edge.name)

                    for key, value in curr_dict.items():
                        if key == "__edge__":
                            pass  # 検出済み
                        else:
                            __create_cluster(value, f"{indent}  ", key)

            __create_cluster(tree, "", "root")

        # 描画
        self._g.render("lesson15n2-graphs")

    def clean_up(self):
        pass
