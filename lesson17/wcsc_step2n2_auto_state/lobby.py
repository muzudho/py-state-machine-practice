from lesson17_data.step1n2_auto_const.wcsc_const import E_LOGOUT, E_GAME_SUMMARY, LOGOUT, REPLY, LOBBY

class LobbyState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_GAME_SUMMARY:
            return [REPLY]

        elif msg == E_LOGOUT:
            return [LOBBY, LOGOUT]

        else:
            raise ValueError(f"Unexpected msg:{msg}")

