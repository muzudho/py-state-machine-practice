class ConstConf:
    def __init__(self):
        # (1) キーと値は 全単射にしてください
        # (2) 大文字と小文字は区別します
        self._data = {
            # States
            # ------
            #
            # "ステート定数": "ステートマシン図のノード名"
            # 本レッスンではノード名を PascalCase にします（エッジと被らないように）
            "INIT": "Init",
            "THIS": "This",
            "IS": "Is",
            "A": "A",
            "PEN": "Pen",
            # Edges
            # -----
            #
            # "エッジ定数": "ステートマシン図のエッジ名"
            # 本レッスンではエッジ名を snake_case にします（ノード名と被らないように）
            # ディクショナリーのキーとして State と被らないように頭に E_ を付けます
            "E_THAT": "that",
            "E_THIS": "this",
            "E_WAS": "was",
            "E_IS": "is",
            "E_AN": "an",
            "E_A": "a",
            "E_PIN": "pin",
            "E_PEN": "pen",
            "E_OVER": "over",  # 以上
            # Actions
            # -------
            #
            # 任意の文字列ですが、値が State や Edge と突合するなら、それを使い回してください
            "MSG_THAT": "That",
            # "MSG_THIS": "This", # 被るので THIS を使い回してください
            # "MSG_WAS": "was",  # 被るので E_WAS を使い回してください
            # "MSG_IS": "is", # 以下略
            # "MSG_AN": "an",
            # "MSG_A": "a",
            # "MSG_PIN": "pin",
            # "MSG_PEN": "pen",
            # "MSG_OVER": "over",
        }

        # 逆向きは自動生成します
        self._rev_data = {}

        init_size = len(self._data)

        for key, value in self._data.items():
            if value in self._rev_data:
                raise ValueError("value:{value} が重複しました。全単射にしてください")

            self._rev_data[value] = key

        if init_size != len(self._rev_data):
            raise ValueError("定数のキーとバリューは全単射にしてください")

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

    def pickup_from_item(self, item, used_const_set):
        """item が定数なら used_const_set へ追加します"""
        if item in self._data:
            used_const_set.add(item)

    def pickup_from_list(self, list_obj, used_const_set):
        """list_obj の中で使われている定数を used_const_set へ追加します"""
        for item in list_obj:
            if item in self._data:
                used_const_set.add(item)
