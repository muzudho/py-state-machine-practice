from lesson17.step2_auto.const import E_LOGOUT, E_GAME_SUMMARY


class LobbyState:
    def update(self, req):

        # TODO 入力
        msg = ""

        # 分岐
        if msg == E_GAME_SUMMARY:
            return ["Reply"]
        elif msg == E_LOGOUT:
            return ["Lobby", "Logout"]
        else:
            raise ValueError("Unexpected condition")
