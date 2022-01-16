class RequestV23:
    def __init__(self, state_path, context=None):
        self._state_path = state_path
        self._context = context

    @property
    def state_path(self):
        """list"""
        return self._state_path

    @property
    def context(self):
        """システムの外部から与えるオブジェクト"""
        return self._context
