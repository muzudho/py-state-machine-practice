from lesson17_projects.wcsc.data.auto_gen.const import INIT, E_COMPLETED

class LobbyLogoutState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_COMPLETED:
            return [INIT]

        else:
            raise ValueError(f"Unexpected msg:{msg}")
