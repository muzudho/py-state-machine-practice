from lesson12n2.keywords import MSG_UP
from lesson12n2.keywords import E_FAILED, E_UP


class StairsState():
    def __init__(self):
        pass

    def react(self, c_sock, pull_trigger):
        c_sock.send("You can see the stairs.".encode())

        # 入力
        message = pull_trigger()

        # `Up` とメッセージを送ってくるのが正解です
        if message == MSG_UP:
            return E_UP

        else:
            return E_FAILED