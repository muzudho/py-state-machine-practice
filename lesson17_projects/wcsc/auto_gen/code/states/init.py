from lesson17_projects.wcsc.auto_gen.data.const import INIT, LOGIN

class InitState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == 'login':
            return [INIT, LOGIN]

        else:
            raise ValueError(f"Unexpected msg:{msg}")

