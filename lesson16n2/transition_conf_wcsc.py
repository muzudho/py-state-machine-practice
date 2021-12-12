# States
# ------
#
# ディクショナリーのキーとして Edge と被らないように PascalCase にします

from lesson15n2.directive_edge import DirectiveEdge


INIT = "Init"
if INIT:  # インデントしてるだけ
    LOGIN = "Login"

LOBBY = "Lobby"
if LOBBY:
    LOGOUT = "Logout"

REPLY = "Reply"
if REPLY:
    AGREE = "Agree"
    REJECT = "Reject"

GAME = "Game"
if GAME:
    pass

# Edges
# -----
#
# ディクショナリーのキーとして State と被らないように頭に snake_case にします

E_OK = "ok"
E_INCORRECT = "incorrect"
E_LOGOUT = "logout"
E_COMPLETED = "completed"
E_GAME_SUMMARY = "game_summary"
E_AGREE = "agree"
E_REJECT = "reject"
E_START = "start"
E_MOVE = "move"
E_MOVE_ECHO = "move_echo"
E_GAME_OVER_FLOODGATE = "game_over_floodgate"
E_GAME_OVER_WCSC = "game_over_wcsc"

E_OVER = "over"  # 練習プログラム用

# Transition
# ----------


class Transition:
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
                    edge = DirectiveEdge(child_key, state_node_path, child)
                    result_edge_list.append(edge)

        result_edge_list = []

        __create_edge_list(self._data, [], "", result_edge_list)

        return result_edge_list

    @classmethod
    def extract_node_path_set(clazz, edge_list):
        """エッジにノードパスが含まれているので、エッジを元にノードパス文字列のセットを作成します"""
        node_path_set = set()

        for edge in edge_list:
            node_path_set.add(edge.to_src_str())
            node_path_set.add(edge.to_dst_str())

        return node_path_set
