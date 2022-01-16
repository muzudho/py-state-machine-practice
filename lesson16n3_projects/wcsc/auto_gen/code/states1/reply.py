class ReplyState():

    def update(self, req):

        # TODO 入力
        msg = ""

        # 分岐
        if msg == 'agree':
            return ['Reply', 'Agree']

        elif msg == 'reject':
            return ['Reply', 'Reject']

        else:
            raise ValueError("Unexpected condition")
