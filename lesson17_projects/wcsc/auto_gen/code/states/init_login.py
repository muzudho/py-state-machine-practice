from lesson17_projects.wcsc.data.auto_gen.const import E_OK, INIT, LOBBY, E_INCORRECT

class InitLoginState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_OK:
            return [LOBBY]

        elif msg == E_INCORRECT:
            return [INIT]

        else:
            raise ValueError(f"Unexpected msg:{msg}")

