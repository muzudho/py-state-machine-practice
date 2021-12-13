from lesson17.step1n2_auto.const import E_START

class ReplyAgreeState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_START:
            return ['Game']
        else:
            raise ValueError("Unexpected condition")

