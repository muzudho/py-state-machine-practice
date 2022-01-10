from lesson17_data.auto_gen.wcsc_const import E_LOGOUT, E_GAME_SUMMARY, LOGOUT, REPLY, LOBBY

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

