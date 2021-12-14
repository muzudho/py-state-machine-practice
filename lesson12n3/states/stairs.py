from lesson12n3.const_conf import MSG_UP, E_FAILED, E_UP


class StairsState:
    def __init__(self):
        pass

    def update(self, req):
        req.c_sock.send("You can see the stairs.".encode())

        # 入力
        message = req.pull_trigger()

        # `Up` とメッセージを送ってくるのが正解です
        if message == MSG_UP:
            return E_UP

        else:
            return E_FAILED
