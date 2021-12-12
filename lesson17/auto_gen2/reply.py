from lesson17.auto_gen1.const import E_AGREE, E_REJECT

class ReplyState():

    def update(self, req):

        # TODO 入力
        msg = ""

        # 分岐
        if msg == E_AGREE:
            return ['Reply', 'Agree']
        elif msg == E_REJECT:
            return ['Reply', 'Reject']
        else:
            raise ValueError("Unexpected condition")

