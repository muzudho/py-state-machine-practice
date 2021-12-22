from lesson17_data.step1n2_auto_const.wcsc_const import GAME, E_START

class ReplyAgreeState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_START:
            return [GAME]

        else:
            raise ValueError(f"Unexpected msg:{msg}")

