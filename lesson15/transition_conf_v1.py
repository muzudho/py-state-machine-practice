class TransitionConfV1:
    def __init__(self, data):
        self._title = data["title"]
        self._entry_node = data["entry_node"]
        self._data = data["data"]

    @property
    def title(self):
        """図のタイトル"""
        return self._title

    @property
    def entry_node(self):
        """開始ノードの名前"""
        return self._entry_node

    @property
    def data(self):
        """ツリー構造のエッジ"""
        return self._data
