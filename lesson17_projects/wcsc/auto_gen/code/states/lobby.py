from lesson17_projects.wcsc.data.auto_gen.const import LOGOUT, E_GAME_SUMMARY, REPLY, LOBBY, E_LOGOUT

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

