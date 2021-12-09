class Node():
    def __init__(self, name, next_name_list):
        """ノードです

        Parameters
        ----------
        name : str
            このノードの名前です

        next_name_list : list
            このノードから行ける隣のノードの名前のリストです
        """
        self._name = name
        self._next_name_list = next_name_list

    @property
    def name(self):
        return self._name

    @property
    def next_name_list(self):
        return self._next_name_list
