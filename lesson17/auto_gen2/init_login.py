from lesson17.auto_gen1.const import E_OK, E_INCORRECT

class InitLoginState():

    def update(self, req):

        # TODO 入力
        msg = ""

        # 分岐
        if msg == E_OK:
            return ['Lobby']
        elif msg == E_INCORRECT:
            return ['Init']
        else:
            raise ValueError("Unexpected condition")

