from lesson11n3.keywords import MSG_OPEN
from lesson11n3.keywords import E_FAILED, E_OPENED


class OutState():
    def __init__(self):
        pass

    def react(self, message, c_sock):
        # 外に居ます。 'Open' とメッセージを送ってくるのが正解です
        if message == MSG_OPEN:
            c_sock.send("You can see the stairs.".encode())
            return E_OPENED

        else:
            c_sock.send("You can see the house.".encode())
            return E_FAILED