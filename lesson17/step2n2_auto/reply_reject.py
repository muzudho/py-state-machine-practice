from lesson17.step1n2_auto.const import E_REJECT

class ReplyRejectState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_REJECT:
            return ['Lobby']
        else:
            raise ValueError("Unexpected condition")

