from lesson17.step1n2_auto.const import E_INCORRECT, E_OK

class InitLoginState():

    def update(self, req):

        # 入力
        msg = req.pull_trigger()

        # 分岐
        if msg == E_OK:
            return ['Lobby']
        elif msg == E_INCORRECT:
            return ['Init']
        else:
            raise ValueError("Unexpected condition")

