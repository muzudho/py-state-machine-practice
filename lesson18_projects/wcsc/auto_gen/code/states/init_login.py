from lesson17_projects.wcsc.auto_gen.data.const import E_INCORRECT, E_OK, INIT, LOBBY

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

