from lesson17_data.step1n2_auto_const.wcsc_const import E_REJECT, LOBBY

class ReplyRejectState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_REJECT:
            return [LOBBY]

        else:
            raise ValueError(f"Unexpected msg:{msg}")

