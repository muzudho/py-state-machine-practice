from lesson17_data.auto_gen.wcsc_const import REJECT, E_REJECT, E_AGREE, REPLY, AGREE

class ReplyState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_AGREE:
            return [REPLY, AGREE]

        elif msg == E_REJECT:
            return [REPLY, REJECT]

        else:
            raise ValueError(f"Unexpected msg:{msg}")

