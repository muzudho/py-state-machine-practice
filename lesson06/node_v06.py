from lesson04.node_v04 import NodeV04


class NodeV06(NodeV04):
    def __init__(self, name, next_name_list, behavior):
        """ノードです

        Parameters
        ----------
        name : str
            このノードの名前です

        next_name_list : list
            このノードから行ける隣のノードの名前のリストです

        behavior : object
            振る舞いです
        """
        super().__init__(name, next_name_list)
        self._behavior = behavior

    def create_message_v06(self, message):
        return self._behavior.create_message_v06(message)
