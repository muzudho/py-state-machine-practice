class ReplyAgreeState():

    def update(self, req):

        # TODO 入力
        msg = ""

        # 分岐
        if msg == 'start':
            return ['Game']

        else:
            raise ValueError("Unexpected condition")
