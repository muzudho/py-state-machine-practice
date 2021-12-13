# States
# ------
#
# ディクショナリーのキーとして Edge と被らないように PascalCase にします

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
