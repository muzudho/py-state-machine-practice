from lesson17_data.auto_gen.wcsc_const import E_INCORRECT, INIT, E_OK, LOBBY

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

