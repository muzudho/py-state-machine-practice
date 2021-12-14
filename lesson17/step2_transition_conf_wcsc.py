from lesson15n2.directive_edge import DirectiveEdge
from lesson17.step1n2_auto_const.pen import (
    AGREE,
    E_AGREE,
    E_COMPLETED,
    E_GAME_OVER_FLOODGATE,
    E_GAME_OVER_WCSC,
    E_GAME_SUMMARY,
    E_INCORRECT,
    E_LOGOUT,
    E_MOVE,
    E_MOVE_ECHO,
    E_OK,
    E_REJECT,
    E_START,
    GAME,
    INIT,
    LOBBY,
    LOGIN,
    LOGOUT,
    REJECT,
    REPLY,
)


class TransitionConf:
    def __init__(self):
        self._title = "CSA Server protocol 1.2.1"
        self._entry_node = INIT
        self._data = {
            INIT: {
                "": [INIT, LOGIN],
                LOGIN: {E_OK: [LOBBY], E_INCORRECT: [INIT]},
            },
            LOBBY: {
                E_GAME_SUMMARY: [REPLY],
                E_LOGOUT: [LOBBY, LOGOUT],
                LOGOUT: {E_COMPLETED: [INIT]},
            },
            REPLY: {
                E_AGREE: [REPLY, AGREE],
                E_REJECT: [REPLY, REJECT],
                AGREE: {E_START: [GAME]},
                REJECT: {E_REJECT: [LOBBY]},
            },
            GAME: {
                E_MOVE: [GAME],
                E_MOVE_ECHO: [GAME],
                E_GAME_OVER_FLOODGATE: [INIT],
                E_GAME_OVER_WCSC: [LOBBY],
            },
        }

    @property
    def title(self):
        """図のタイトル"""
        return self._title

    @property
    def data(self):
        """ツリー構造のエッジ"""
        return self._data

    @property
    def entry_node(self):
        """開始ノードの名前"""
        return self._entry_node

    def create_edge_list(self):
        """辺（DirectiveEdgeクラス）の一覧を作成"""

        def __create_edge_list(
            curr_dict, parent_state_node_path, node_name, result_edge_list
        ):
            state_node_path = list(parent_state_node_path)
            if not (node_name is None) and not (node_name is ""):
                state_node_path.append(node_name)

            print(
                f"parent_state_node_path={parent_state_node_path} node_name={node_name} state_node_path={state_node_path}"
            )

            for child_key in curr_dict.keys():

                child = curr_dict[child_key]

                if isinstance(child, dict):
                    __create_edge_list(
                        child, state_node_path, child_key, result_edge_list
                    )
                else:
                    edge = DirectiveEdge(src=state_node_path, dst=child, name=child_key)
                    result_edge_list.append(edge)

        result_edge_list = []

        __create_edge_list(self._data, [], "", result_edge_list)

        return result_edge_list

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

    @classmethod
    def extract_node_path_set(clazz, edge_list):
        """エッジにノードパスが含まれているので、エッジを元にノードパス文字列のセットを作成します"""
        node_path_set = set()

        for edge in edge_list:
            node_path_set.add(edge.to_src_str())
            node_path_set.add(edge.to_dst_str())

        return node_path_set
