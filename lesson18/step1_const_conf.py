class ConstConf:
    def __init__(self):
        # 全単射にしてください
        self._data = {
            # States
            # ------
            #
            # ディクショナリーのキーとして Edge と被らないように PascalCase にします
            "INIT": "Init",
            "THIS": "This",
            "IS": "Is",
            "A": "A",
            "PEN": "Pen",
            # Actions
            # -------
            #
            # 競合しないので、任意の文字列です
            "MSG_THAT": "That",
            "MSG_THIS": "This",
            "MSG_WAS": "was",
            "MSG_IS": "is",
            "MSG_AN": "an",
            "MSG_A": "a",
            "MSG_PIN": "pin",
            "MSG_PEN": "pen",
            # Edges
            # -----
            #
            # ディクショナリーのキーとして State と被らないように頭に snake_case にします
            "E_THAT": "that",
            "E_THIS": "this",
            "E_WAS": "was",
            "E_IS": "is",
            "E_AN": "an",
            "E_A": "a",
            "E_PIN": "pin",
            "E_PEN": "pen",
            "E_OVER": "over",  # 以上
        }

        # 逆向きは自動生成します
        self._rev_data = {}

        for key, value in self._data.items():
            self._rev_data[value] = key

    @property
    def data(self):
        return self._data

    @property
    def rev_data(self):
        return self._rev_data
