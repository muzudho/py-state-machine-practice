from lesson18.step2_auto.const import E_PIN, E_OVER, E_PEN

class InitThisIsAState():

    def update(self, req):

        self.on_entry(req)

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_OVER:
            return ['Init']
        elif msg == E_PIN:
            return ['Init']
        elif msg == E_PEN:
            return ['Pen']
        else:
            raise ValueError("Unexpected condition")


    def on_entry(self, req):
        pass
