from lesson17.auto_gen1.const import E_GAME_SUMMARY, E_LOGOUT

class LobbyState():

    def update(self, req):

        # TODO 入力
        msg = ""

        # 分岐
        if msg == E_GAME_SUMMARY:
            return ['Reply']
        elif msg == E_LOGOUT:
            return ['Lobby', 'Logout']
        else:
            raise ValueError("Unexpected condition")

