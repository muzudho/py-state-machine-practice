from lesson17.step2_auto.const import E_COMPLETED


class LobbyLogoutState:
    def update(self, req):

        # TODO 入力
        msg = ""

        # 分岐
        if msg == E_COMPLETED:
            return ["Init"]
        else:
            raise ValueError("Unexpected condition")
