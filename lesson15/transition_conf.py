# States
# ------
#
# ディクショナリーのキーとして Edge と被らないように PascalCase にします

INIT = "Init"
if INIT:
    THIS = "This"
    if THIS:  # インデントを付けてるだけ
        IS = "Is"
        if IS:
            A = "A"

PEN = "Pen"

# Actions
# -------

MSG_THAT = "That"
MSG_THIS = "This"
MSG_WAS = "was"
MSG_IS = "is"
MSG_AN = "an"
MSG_A = "a"
MSG_PIN = "pin"
MSG_PEN = "pen"

# Edges
# -----
#
# ディクショナリーのキーとして State と被らないように頭に snake_case にします

E_THAT = "that"
E_THIS = "this"
E_WAS = "was"
E_IS = "is"
E_AN = "an"
E_A = "a"
E_PIN = "pin"
E_PEN = "pen"
E_OVER = "over"  # 以上

# Transition
# ----------


class Transition:
    def __init__(self, title, entry_node):
        self._title = title
        self._entry_node = entry_node
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

        pass

    @property
    def title(self):
        return self._title

    @property
    def data(self):
        return self._data

    @property
    def entry_node(self):
        """開始ノードの名前"""
        return self._entry_node
