from lesson17.step1n2_auto.const import E_REJECT, E_AGREE

class ReplyState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_AGREE:
            return ['Reply', 'Agree']
        elif msg == E_REJECT:
            return ['Reply', 'Reject']
        else:
            raise ValueError("Unexpected condition")

