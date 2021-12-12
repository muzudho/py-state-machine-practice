from lesson17.step2_auto.const import E_START


class ReplyAgreeState:
    def update(self, req):

        # TODO 入力
        msg = ""

        # 分岐
        if msg == E_START:
            return ["Game"]
        else:
            raise ValueError("Unexpected condition")
