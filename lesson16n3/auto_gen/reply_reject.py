class ReplyRejectState():

    def update(self, req):

        # TODO 入力
        msg = ""

        # 分岐
        if msg == 'reject':
            return ['Lobby']

        else:
            raise ValueError("Unexpected condition")
