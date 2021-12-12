from lesson18.step2_auto.const import E_THAT, E_OVER, E_THIS

class InitState():

    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_OVER:
            return ['Init']
        elif msg == E_THAT:
            return ['Init']
        elif msg == E_THIS:
            return ['Init', 'This']
        else:
            raise ValueError("Unexpected condition")


    def on_entry(self, req):
        pass
