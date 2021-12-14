from lesson15.const_conf import (
    A,
    E_A,
    E_AN,
    E_IS,
    E_OVER,
    E_PEN,
    E_PIN,
    E_THAT,
    E_THIS,
    E_WAS,
    INIT,
    IS,
    PEN,
    THIS,
)


class TransitionConf:
    def __init__(self):
        self._title = "This is a pen"
        self._entry_node = INIT
        self._data = {
            INIT: {
                E_OVER: [INIT],
                E_THAT: [INIT],
                E_THIS: [INIT, THIS],
                THIS: {
                    E_OVER: [INIT],
                    E_WAS: [INIT],
                    E_IS: [INIT, THIS, IS],
                    IS: {
                        E_OVER: [INIT],
                        E_AN: [INIT],
                        E_A: [INIT, THIS, IS, A],
                        A: {
                            E_OVER: [INIT],
                            E_PIN: [INIT],
                            E_PEN: [PEN],
                        },
                    },
                },
            },
            PEN: {
                E_OVER: None,
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
