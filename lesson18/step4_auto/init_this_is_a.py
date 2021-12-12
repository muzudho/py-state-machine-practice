from lesson18.step2_auto.const import E_OVER, E_PIN, E_PEN

class InitThisIsAState():

    def update(self, req):

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
