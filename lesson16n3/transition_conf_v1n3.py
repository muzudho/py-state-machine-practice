from lesson16n2.transition_conf_v1n2 import TransitionConfV1n2
from lesson15n2.directive_edge import DirectiveEdge


class TransitionConfV1n3(TransitionConfV1n2):
    @classmethod
    def create_edge_list_by_node_path(clazz, curr_dict, node_path):
        """ノードパスを指定して、辺（DirectiveEdgeクラス）の一覧を作成"""
        # print(f"[128] node_path={node_path}")

        def __create_edge_list(curr_dict, result_edge_list, node_path, depth):
            # print(f"[131] node_path={node_path} len={len(node_path)} depth={depth}")

            if depth < len(node_path) and isinstance(curr_dict, dict):
                node_name = node_path[depth]
                # print(f"[135] node_name={node_name}")

                # 下りる
                __create_edge_list(
                    curr_dict[node_name],
                    result_edge_list,
                    node_path,
                    depth + 1,
                )

            else:
                # ノードパスのリスト
                edge_name = node_path[depth - 1]
                # print(
                #    f"[149] node_path={node_path} edge_name={edge_name} curr_dict={curr_dict}"
                # )

                # 空文字、または先頭が小文字ならエッジ名
                for key, destination_node_path in curr_dict.items():
                    if key == "" or key[0].islower():
                        edge_name = key
                        # print(
                        #    f"[157] edge_name={edge_name} destination_node_path={destination_node_path}"
                        # )
                        edge = DirectiveEdge(
                            src=node_path,
                            dst=destination_node_path,
                            name=edge_name,
                        )
                        result_edge_list.append(edge)

        result_edge_list = []

        __create_edge_list(curr_dict, result_edge_list, node_path, 0)

        return result_edge_list
