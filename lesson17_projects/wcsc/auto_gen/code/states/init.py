from lesson17_projects.wcsc.data.auto_gen.const import E_LOGIN, INIT, LOGIN

class InitState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_LOGIN:
            return [INIT, LOGIN]

        else:
            raise ValueError(f"Unexpected msg:{msg}")

