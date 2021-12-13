from lesson17.step1n2_auto.const import E_LOGOUT, E_GAME_SUMMARY

class LobbyState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_GAME_SUMMARY:
            return ['Reply']
        elif msg == E_LOGOUT:
            return ['Lobby', 'Logout']
        else:
            raise ValueError("Unexpected condition")

