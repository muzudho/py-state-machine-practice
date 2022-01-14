from lesson17_projects.wcsc.data.auto_gen.const import AGREE, E_AGREE, REPLY, E_REJECT, REJECT

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

