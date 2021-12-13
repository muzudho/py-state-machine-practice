from lesson17.step1n2_auto.const import E_COMPLETED

class LobbyLogoutState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_COMPLETED:
            return ['Init']
        else:
            raise ValueError("Unexpected condition")

