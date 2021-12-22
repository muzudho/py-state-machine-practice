class LobbyLogoutState():

    def update(self, req):

        # TODO 入力
        msg = ""

        # 分岐
        if msg == 'completed':
            return ['Init']

        else:
            raise ValueError("Unexpected condition")
