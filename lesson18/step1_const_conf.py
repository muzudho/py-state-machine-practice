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

    def replace_item(self, item, quote):
        """文字列に対して、定数に書きかえられるなら定数に書きかえて返します"""
        if item in self.rev_data:
            return self.rev_data[item]  # 定数
        else:
            return f"{quote}{item}{quote}"  # 文字列

    def replace_list(self, old_list, quote):
        """リストに対して、定数に書きかえられる要素は定数に書きかえた新しいリストを返します"""
        new_list = []
        for item in old_list:
            if item in self._rev_data:
                new_list.append(self._rev_data[item])  # 定数
            else:
                new_list.append(f"{quote}{item}{quote}")  # 文字列

        return new_list
