from lesson17.auto_gen1.const import E_REJECT

class ReplyRejectState():

    def update(self, req):

        # TODO 入力
        msg = ""

        # 分岐
        if msg == E_REJECT:
            return ['Lobby']
        else:
            raise ValueError("Unexpected condition")

