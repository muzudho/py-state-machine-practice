from lesson17_projects.wcsc.auto_gen.data.const import E_START, GAME

class ReplyAgreeState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_START:
            return [GAME]

        else:
            raise ValueError(f"Unexpected msg:{msg}")

