from lesson18.step2_auto.const import E_OVER, E_IS, E_WAS

class InitThisState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_OVER:
            return ['Init']
        elif msg == E_WAS:
            return ['Init']
        elif msg == E_IS:
            return ['Init', 'This', 'Is']
        else:
            raise ValueError("Unexpected condition")

