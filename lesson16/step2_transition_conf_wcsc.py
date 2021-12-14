from lesson16.step1_const_conf_wcsc import (
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
