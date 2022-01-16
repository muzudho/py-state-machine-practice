from lesson17_projects.wcsc.data.auto_gen.const import E_REJECT, LOBBY

class ReplyRejectState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_REJECT:
            return [LOBBY]

        else:
            raise ValueError(f"Unexpected msg:{msg}")

