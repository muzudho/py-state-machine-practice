from lesson18.step2_auto.const import E_AN, E_OVER, E_A

class InitThisIsState():

    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_OVER:
            return ['Init']
        elif msg == E_AN:
            return ['Init']
        elif msg == E_A:
            return ['Init', 'This', 'Is', 'A']
        else:
            raise ValueError("Unexpected condition")


    def on_entry(self, req):
        pass
