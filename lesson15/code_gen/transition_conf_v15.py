class TransitionConfV15:
    def __init__(self, doc):
        self._doc = doc

    @property
    def doc(self):
        """ドキュメント構造のルート"""
        return self._doc
