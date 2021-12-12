from lesson18.step2_auto.const import E_OVER

class PenState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_OVER:
            return None
        else:
            raise ValueError("Unexpected condition")

