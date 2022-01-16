class InitLoginState():

    def update(self, req):

        # TODO 入力
        msg = ""

        # 分岐
        if msg == 'ok':
            return ['Lobby']

        elif msg == 'incorrect':
            return ['Init']

        else:
            raise ValueError("Unexpected condition")
